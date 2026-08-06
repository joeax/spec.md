---
name: specmd-plan-run
description: Execute and validate a plan document's task checklist — implementing its tasks in the codebase (Run) and auditing that implementation against the plan (Validate). Use when the user wants to run, implement, or execute a plan (e.g. from .specmd/), or wants to validate, verify, or audit a plan's status against the actual codebase. Operates on any document following the plan.yml schema, independent of whichever skill produced it.
metadata:
  author: joeax
  version: 2026-08-06
---

# SPEC.md Run Plan Skill

Use this skill to implement a plan document's task checklist in the codebase, and to validate that implementation against the plan. This is an extension skill, self-contained and independent of specmd and specmd-plan-create — it operates on any document that follows the plan schema bundled with this skill, regardless of which skill produced it.

## Core principles

- Prefer evidence from the repository over assumptions.
- Implement only what the plan's Tasks section describes. If a task is ambiguous or would require a decision the plan doesn't make, mark it `[C]` (clarification needed) rather than guessing.
- If work would materially expand scope beyond the plan (new tasks, different architecture, files outside what's implied), stop and ask the user for confirmation before proceeding.
- Never mark a task `[X]` to make the plan look complete when it isn't — status markers must reflect actual codebase state.

## Required reading order

Before running or validating, load the plan document:

1. Read the plan schema file (bundled with this skill) to understand frontmatter fields, section structure, and status marker vocabulary.
2. Follow Plan selection below to identify the target plan document, then read it in full: frontmatter, Summary of Changes, Tasks, Implementation Notes.
3. Inspect the current codebase for the scope described by the plan to ground status markers in actual state before making changes.

## Plan selection

Used by both Run and Validate when the user doesn't name a specific plan file:

1. Look in `.specmd/` for plan documents matching the plan schema.
2. If exactly one exists, or exactly one has `state: ready`, use it.
3. Otherwise, list the candidates and ask the user which to use.

## Run

Intent: Implement a plan document's tasks in the codebase, updating the plan to reflect real progress as work completes.

Use when the user asks to run, implement, execute, or build out a plan (or a specific task/subset of tasks within one).

Steps:
1. Follow Required reading order and Plan selection above.
2. Work through Tasks in order (or the user-specified subset), implementing each as described.
3. As each task completes, update its status marker in the plan document (`[ ]` → `[X]`/`[P]`/`[D]`/`[C]`) and add or adjust Implementation Notes when a status isn't self-explanatory (e.g. why something is `[P]` or `[D]`).
4. If a task can't be completed as written (missing dependency, contradictory instruction, needs a decision), mark it `[C]` and record why in Implementation Notes rather than guessing or skipping silently.
5. Leave the status of tasks outside the current request's scope untouched.
6. Once done with the requested scope, update the plan's frontmatter `state` field to reflect overall readiness (e.g. `completed`, `partial`, `blocked`).

Output: codebase changes implementing the requested tasks, plus an updated plan document whose statuses reflect actual progress.

## Validate

Intent: Audit a plan document against the current codebase to confirm tasks marked complete are actually done, and surface drift.

Use when the user asks to validate, verify, or audit a plan — independent of whether Run was just used, e.g. after manual edits, a different session, or before merging.

Steps:
1. Follow Required reading order and Plan selection above.
2. For each task, inspect the codebase to determine whether its actual state matches its recorded status marker.
3. Run existing automated checks relevant to the plan's scope (tests, build, lint) if the project has them, and note results.
4. Flag mismatches explicitly in either direction: tasks marked `[X]` that aren't actually done, or tasks marked `[ ]`/`[P]` that are now actually complete. Also revisit `[D]`/`[C]` items whose blocking condition may have been resolved.
5. Correct status markers to reflect ground truth and document findings in Implementation Notes. Never silently launder a mismatch by leaving it unflagged.

Output: an updated plan document whose task statuses are truthful, with mismatches documented in Implementation Notes, plus a chat-level summary of what was found and corrected. Validate doesn't produce a separate report file.

## Working guidelines

- Unlike `specmd` and `specmd-plan-create` skills, this skill is expected to edit the codebase — but only within the scope the plan describes.
- Prefer small, incremental changes per task over large batch rewrites, consistent with the plan's own task granularity.
- Keep the plan document's structure (frontmatter fields, section headings, status marker vocabulary) conformant to the plan schema at all times.
- Never edit the plan's frontmatter except the `state` field described in Run step 6 — all other progress and findings belong in task status markers and Implementation Notes.

## Additional resources

- [Plan schema file](./references/schemas/plan.yml): full schema for the plan document this skill executes and validates against. Bundled locally so this skill has no install-time dependency on specmd-plan-create.
- [Plan example](./references/examples/plan.md): example plan document showing status markers in a realistic state.
