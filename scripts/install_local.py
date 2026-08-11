#!/usr/bin/env python3
"""
Symlink SPEC.md skills into the local Claude skills directory.

For local development: lets you edit a skill in this repo and have Claude
Code pick up the changes immediately, without reinstalling via skills.sh.

NOTE: You may need admin rights to run this script on Windows, 
      or enable Developer Mode (Settings > Update & Security > For developers).
"""

import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

AGENT_ROOT = ".claude"
SKILLS = "skills"
SKILLS_SRC = REPO_ROOT / SKILLS
SKILLS_DEST = Path.home() / AGENT_ROOT / SKILLS


def find_skills(skills_dir: Path) -> list[Path]:
    """Return a list of skill directories in the given skills_dir."""
    return sorted(
        d for d in skills_dir.iterdir()
        if d.is_dir() and (d / "SKILL.md").is_file()
    )


def link_skill(source: Path, dest: Path) -> str:
    """Create/refresh the symlink for one skill. Returns "linked", "up_to_date", "skipped", or "failed"."""
    if dest.is_symlink():
        if dest.resolve() == source.resolve():
            print(f"  up to date: {dest.name}")
            return "up_to_date"
        print(f"  relinking {dest.name} (was -> {os.readlink(dest)})")
        dest.unlink()
    elif dest.exists():
        print(f"  skipping {dest.name}: a real file/folder already exists there, leaving it alone")
        return "skipped"

    try:
        os.symlink(source, dest, target_is_directory=True)
        print(f"  linked: {dest.name} -> {source}")
        return "linked"
    except OSError as e:
        print(f"  failed to link {dest.name}: {e}")
        if os.name == "nt":
            print(
                "    On Windows, creating symlinks requires Developer Mode "
                "(Settings > Update & Security > For developers) or running "
                "this script as Administrator."
            )
        return "failed"


def main() -> int:
    """Main entry point for the script."""
    if not SKILLS_SRC.is_dir():
        print(f"No skills/ folder found at {SKILLS_SRC}")
        return 1

    skills = find_skills(SKILLS_SRC)
    if not skills:
        print(f"No skills found in {SKILLS_SRC}")
        return 1

    SKILLS_DEST.mkdir(parents=True, exist_ok=True)
    print(f"Linking {len(skills)} skill(s) from {SKILLS_SRC} into {SKILLS_DEST}")

    results = [link_skill(skill_dir, SKILLS_DEST / skill_dir.name) for skill_dir in skills]

    linked = results.count("linked")
    up_to_date = results.count("up_to_date")
    skipped = results.count("skipped")
    failed = results.count("failed")
    print(f"\nDone: {linked} linked, {up_to_date} already up to date, {skipped} skipped, {failed} failed")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
