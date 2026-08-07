#!/usr/bin/env python3
"""
Validate a specmd plan document's structure before it is run.

Checks frontmatter fields, the document title, and the Tasks section's
bullet/ID format -- the mechanical parts of the plan document format
(see specmd-plan-create/references/schemas/plan.yml) that don't require
judgment. Contextual checks (scope, consistency, whether content
addresses the agent as instructions rather than describing work) are
the run skill's job, not this script's -- see the skill's Plan
integrity check section.

Exit code 0: the plan is structurally valid.
Exit code 1: one or more structural problems were found; each is
             printed, one per line.
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

VALID_STATES = {"ready", "partial", "completed", "blocked"}
KNOWN_FRONTMATTER_FIELDS = {"id", "description", "generated", "state", "spec", "metadata"}
KNOWN_METADATA_FIELDS = {"author", "updated"}
TASK_HEADINGS = {"## Tasks", "## Checklist"}
TITLE = "# Execution Plan"

TASK_LINE_RE = re.compile(r"^- \[( |X|P|D|C)\] \*\*T(\d{2,})\*\*:")
FRONTMATTER_LINE_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$")


def split_frontmatter(text: str) -> tuple[list[str], list[str], list[str]]:
    """Split a plan document into (frontmatter_lines, body_lines, errors)."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return [], lines, ["frontmatter: document must start with a '---' frontmatter fence"]
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i], lines[i + 1 :], []
    return [], lines, ["frontmatter: no closing '---' fence found"]


def parse_frontmatter(fm_lines: list[str]) -> tuple[dict[str, str], list[str]]:
    """Parse frontmatter lines into a flat field dict, flagging unknown fields."""
    fields: dict[str, str] = {}
    errors: list[str] = []
    i = 0
    while i < len(fm_lines):
        line = fm_lines[i]
        if not line.strip():
            i += 1
            continue
        match = FRONTMATTER_LINE_RE.match(line)
        if not match:
            errors.append(f"frontmatter: could not parse line: {line!r}")
            i += 1
            continue
        key, value = match.group(1), match.group(2)
        if key not in KNOWN_FRONTMATTER_FIELDS:
            errors.append(f"frontmatter: unknown field '{key}'")
        if key == "metadata":
            i += 1
            while i < len(fm_lines) and fm_lines[i].startswith((" ", "\t")):
                sub = FRONTMATTER_LINE_RE.match(fm_lines[i].strip())
                if sub and sub.group(1) not in KNOWN_METADATA_FIELDS:
                    errors.append(f"frontmatter: unknown metadata field '{sub.group(1)}'")
                i += 1
            continue
        fields[key] = value
        i += 1
    return fields, errors


def validate_state(raw_value: str) -> list[str]:
    """Validate the frontmatter state field, including its optional '# see log' comment."""
    errors: list[str] = []
    if "#" in raw_value:
        base, _, comment = raw_value.partition("#")
        base = base.strip()
        comment = comment.strip()
        if comment != "see log":
            errors.append(f"frontmatter: unexpected trailing comment on state: '# {comment}'")
        elif base != "completed":
            errors.append(
                f"frontmatter: '# see log' comment is only valid when state is 'completed', found state '{base}'"
            )
    else:
        base = raw_value.strip()
    if base not in VALID_STATES:
        errors.append(f"frontmatter: state '{base}' is not one of {sorted(VALID_STATES)}")
    return errors


def validate_title(body_lines: list[str]) -> list[str]:
    """Validate the document title is exactly '# Execution Plan'."""
    for line in body_lines:
        if not line.strip():
            continue
        if line.strip() != TITLE:
            return [f"title: expected '{TITLE}', found '{line.strip()}'"]
        return []
    return [f"title: document body is empty, expected '{TITLE}'"]


def find_section(body_lines: list[str], headings: set[str]) -> list[str] | None:
    """Return the lines belonging to the first matching '## ' section, or None if absent."""
    start = None
    for i, line in enumerate(body_lines):
        if line.strip() in headings:
            start = i + 1
            break
    if start is None:
        return None
    end = len(body_lines)
    for i in range(start, len(body_lines)):
        if body_lines[i].startswith("## "):
            end = i
            break
    return body_lines[start:end]


def validate_tasks(body_lines: list[str]) -> list[str]:
    """Validate the Tasks/Checklist section's bullet format and task ID sequence.

    Only top-level (zero-indent) '- ' bullets are checked against the task
    format; indented subsections/continuations under a task are left alone.
    """
    section = find_section(body_lines, TASK_HEADINGS)
    if section is None:
        return ["tasks: no '## Tasks' or '## Checklist' section found"]

    errors: list[str] = []
    ids: list[int] = []
    for line in section:
        if not line.startswith("- "):
            continue
        match = TASK_LINE_RE.match(line)
        if not match:
            errors.append(f"tasks: line does not match '- [ ] **T01**: ...' format: {line!r}")
            continue
        ids.append(int(match.group(2)))

    if not ids:
        errors.append("tasks: no task entries found in the Tasks section")
        return errors

    duplicates = sorted(n for n, count in Counter(ids).items() if count > 1)
    for n in duplicates:
        errors.append(f"tasks: duplicate task ID T{n:02d}")

    unique_ids = set(ids)
    missing = sorted(set(range(1, max(unique_ids) + 1)) - unique_ids)
    if missing:
        missing_str = ", ".join(f"T{n:02d}" for n in missing)
        errors.append(f"tasks: missing task ID(s) in sequence: {missing_str}")

    return errors


def validate_plan(path: Path) -> list[str]:
    """Run all structural checks on the plan document at `path`; return a list of errors."""
    text = path.read_text(encoding="utf-8")
    fm_lines, body_lines, errors = split_frontmatter(text)
    if errors:
        return errors  # can't safely parse further without a valid frontmatter fence

    fields, fm_errors = parse_frontmatter(fm_lines)
    errors.extend(fm_errors)

    if "state" not in fields:
        errors.append("frontmatter: missing required field 'state'")
    else:
        errors.extend(validate_state(fields["state"]))

    errors.extend(validate_title(body_lines))
    errors.extend(validate_tasks(body_lines))

    return errors


def main() -> int:
    """CLI entry point: validate a plan document and report errors."""
    parser = argparse.ArgumentParser(description="Validate a specmd plan document's structure.")
    parser.add_argument("plan_path", type=Path, help="path to the plan document (e.g. .specmd/plan-....md)")
    args = parser.parse_args()

    if not args.plan_path.is_file():
        print(f"error: no such file: {args.plan_path}")
        return 1

    errors = validate_plan(args.plan_path)
    if errors:
        print(f"Plan failed structural validation ({len(errors)} issue(s)):")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Plan is structurally valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
