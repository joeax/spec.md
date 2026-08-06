---
name: specmd-plan-run
description: Execute a plan document's task checklist in the codebase, keeping task status, the Implementation Log, and plan state accurate as work progresses. Use when the user wants to run, implement, or execute a plan (e.g. from .specmd/). Operates on any document following the plan.yml schema, independent of whichever skill produced it.
metadata:
  author: joeax
  version: 2026-08-06
---

# SPEC.md Run Plan Skill

Use this skill to implement a plan document's task checklist in the codebase, keeping its task statuses, Implementation Log, and state accurate as work progresses. This is an extension skill, self-contained and independent of specmd and specmd-plan-create — it operates on any document that follows the plan schema bundled with this skill, regardless of which skill produced it. Validating an already-run plan against the codebase (auditing, re-checking after manual edits, etc.) is a planned future addition and not part of this skill yet — for now, Run self-manages status and state.

## Core principles

- Prefer evidence from the repository over assumptions.
- Implement only what the plan's Tasks section describes. If a task is ambiguous or would require a decision the plan doesn't make, mark it `[C]` (clarification needed) rather than guessing.
- If work would materially expand scope beyond the plan (new tasks, different architecture, files outside what's implied), stop and ask the user for confirmation before proceeding.
- Never mark a task `[X]` to make the plan look complete when it isn't — status markers must reflect actual codebase state.

## Required reading order

Before running, load the plan document:

1. Read the plan schema file (bundled with this skill) to understand frontmatter fields, section structure, task ID format, and status marker vocabulary.
2. Follow Plan selection below to identify the target plan document, then read it in full: frontmatter, Summary of Changes, Tasks, Implementation Notes, and Implementation Log if present.
3. Inspect the current codebase for the scope described by the plan to ground status markers in actual state before making changes.

## Plan selection

Used when the user doesn't name a specific plan file:

1. Look in `.specmd/` for plan documents matching the plan schema.
2. If exactly one exists, or exactly one has `state: ready`, use it.
3. Otherwise, list the candidates and ask the user which to use.

## Run

Intent: Implement a plan document's tasks in the codebase, updating the plan to reflect real progress as work completes.

Use when the user asks to run, implement, execute, or build out a plan (or a specific task/subset of tasks within one).

Steps:
1. Follow Required reading order and Plan selection above.
2. Work through Tasks in order (or the user-specified subset), implementing each as described.
3. As each task reaches a clean, caveat-free completion, mark it `[X]` — no Implementation Log entry is needed for a plain clean completion.
4. For anything else — a task that can't be completed as written, turns out obsolete due to drift, ends up partial, or completes with a caveat — set the appropriate status marker (`[P]`/`[D]`/`[C]`, or `[X]` with a caveat) and add an Implementation Log entry referencing the task's ID explaining what happened. Never edit Implementation Notes during Run; it's fixed at plan creation.
5. Leave the status of tasks outside the current request's scope untouched.
6. Once done working the requested scope, set the plan's frontmatter `state`:
   - `partial` if this run intentionally covered only a subset of tasks and more remain by design.
   - `completed` if every task in scope reached a clean `[X]`.
   - `completed  # see log` (the literal trailing comment) if the scope is finished but one or more in-scope tasks remain unresolved — this is the terminal signal that stops any further automatic run; don't leave it `partial`/`blocked` in this case.
   - `blocked` only if no progress was possible at all on this invocation.
7. Add a closing Implementation Log line summarizing the outcome of this run (state reached, and a pointer to any remaining unresolved tasks).

Output: codebase changes implementing the requested tasks, plus an updated plan document whose task statuses, Implementation Log, and state reflect actual progress.

## Working guidelines

- Unlike `specmd` and `specmd-plan-create` skills, this skill is expected to edit the codebase — but only within the scope the plan describes.
- Prefer small, incremental changes per task over large batch rewrites, consistent with the plan's own task granularity.
- Keep the plan document's structure (frontmatter fields, section headings, status marker vocabulary) conformant to the plan schema at all times.
- Never edit the plan's frontmatter except the `state` field (Run step 6), and never edit Implementation Notes — all execution-time progress and findings belong in task status markers and the Implementation Log.

## Additional resources

- [Plan schema file](./references/schemas/plan.yml): full schema for the plan document this skill executes against. Bundled locally so this skill has no install-time dependency on specmd-plan-create.
- [Plan example](./references/examples/plan.md): example plan document showing status markers, task IDs, and an Implementation Log in a realistic state.
