---
name: specmd
description: Read, define, plan, and sync SPEC.md files — the agent-optimized spec format for a project's intent. Use whenever the user references a SPEC.md file, or asks to define/create a "spec" for a software project (e.g. "define a new spec for a car-photos website"), wants an implementation plan derived from spec requirements, or wants a spec reconciled with the codebase.
metadata:
  author: joeax
  version: 2026-08-04
---

# SPEC.md Skill

Use this skill to read, define, plan, and sync SPEC.md documents. Follow the instructions below carefully and prefer the most specific source of truth available.

## Core principles

- Treat the SPEC.md document as the primary source of intent for the project.
- Prefer evidence from the repository over assumptions.
- When information is missing or ambiguous, make the smallest reasonable assumption and state it clearly.
- If a change would materially affect scope, architecture, or implementation, ask the user for confirmation before proceeding.
- When frontmatter and the Requirements section conflict, the Requirements section takes precedence and the conflict should be called out explicitly.

## Required reading order

Whenever a function below needs to load an existing SPEC.md file (Read, Plan, Sync), follow this order:

1. Read the core schema file first to understand the rules of the SPEC.md framework.
2. Read the relevant SPEC.md file from the project root. Only read other SPEC.md files if they are clearly in scope.
3. Parse the frontmatter.
4. Resolve the schema. The default schema is the built-in `specmd` schema. If the built-in schema is used, read the spec schema file. If a custom or extended schema is used, also read its base schemas.
5. Parse the body according to the resolved schema.

## Functions

Each function below represents one core operation in the specmd workflow. Use the one that matches the user’s request most closely. If a request mixes multiple operations, clarify the primary intent or perform the steps in order.

### 1. Read

Intent: Understand an existing SPEC.md document and its surrounding context.

Use the Read function when the user asks to read, inspect, summarize, or validate a spec.

Steps:
1. Identify the target SPEC.md file and confirm the scope.
2. Follow the Required reading order above.
3. Report the result clearly, highlighting contradictions, missing sections, or unclear requirements.

Output: a concise understanding of the spec’s intent, structure, and notable gaps.

### 2. Define

Intent: Create a new SPEC.md document that captures a project’s intent.

Use the Define function when the user asks to create a new SPEC.md file or when no suitable spec exists.

Steps:
1. Determine whether the request is for a new project or an existing codebase.
2. Read the core schema and spec schema file(s) so the new spec follows the expected structure — read any extension or custom schemas too, if applicable.
3. If the project already contains code, inspect it to ground the spec in what exists.
4. If the project is empty, start from only what the user has actually provided. A simple spec — frontmatter, title, and description only, no sections (see the simple spec template in Additional resources) — is a complete, valid starting point; add a section only once there is real information for it.
5. Create the spec at the project root unless the user explicitly requests another location.
6. Keep the initial version focused on intent, scope, and major requirements rather than exhaustive implementation detail.

Output: a new SPEC.md file that is concise, usable, and ready for planning or implementation.

### 3. Plan

Intent: Turn a focused portion of a SPEC.md document into an actionable implementation plan.

Use the Plan function when the user needs a plan before changing code, especially when the request is scoped to a subset of the spec such as a feature, module, API surface, or a specific set of requirements.

Steps:
1. Identify the scope of the request. If the user asks for a plan for specific sections or a focused change, limit the plan to that scope rather than the entire spec.
2. Follow the Required reading order above for the relevant SPEC.md file, plus any surrounding context needed to understand the requested area.
3. Read the plan schema file so the generated plan document follows the expected structure.
4. Break the requested work into clear, ordered implementation steps that can be executed in chunks or iteratively.
5. Create a markdown plan document in the `.specmd/` folder that stands on its own: an implementation agent must be able to execute it without loading SPEC.md or this skill.
6. Keep the plan focused on the requested change and call out assumptions, risks, or unresolved details.

Output: a self-contained markdown plan document, scoped to the user’s request, that an implementation agent can execute without further reference to SPEC.md or this skill.

### 4. Sync

Intent: Keep an existing SPEC.md document aligned with the codebase as the project evolves.

Use the Sync function when the user wants an existing SPEC.md file reconciled against the current state of the codebase.

Steps:
1. Follow the Required reading order above to load the current spec, then review it together with the current codebase.
2. Identify two kinds of drift and treat them differently:
   - Additive: capabilities, endpoints, or behavior present in the codebase but not reflected in the spec. Add these to the spec.
   - Contradictory: the spec asserts something the codebase actually does differently. Flag this for user confirmation before resolving (per Core principles) rather than silently picking a winner.
3. Never remove a requirement, feature, or other stated intent solely because the codebase hasn't implemented it yet — unimplemented items are still pending work, not stale content.
4. Update the spec to reflect confirmed changes while preserving the original intent.
5. Compacting is optional and separate from reconciliation. Only compact when the spec has grown unwieldy (e.g. beyond 1,000 lines) or the user asks, following any frontmatter instructions that override the default behavior, and never let it remove unimplemented requirements (see Compacting guidance below).

Output: an updated SPEC.md file that stays accurate and additive, with no loss of not-yet-implemented intent.

#### Compacting guidance

When compacting is necessary:
- Summarize long-running paragraphs and repetitive list items.
- Remove implementation detail that is now redundant with the codebase itself (e.g. exact file layout visible in the repo).
- Replace redundancies with concise cross-references to the original content when helpful.
- Never remove or weaken a requirement, feature, or user story merely because it isn't implemented yet.

## Working guidelines

- Preserve important detail from the existing spec unless the user requests a change.
- Avoid creating or editing files unless the requested action requires it.
- Keep outputs structured, concise, and useful for downstream implementation or review.

## Additional resources

- [Core schema file](./references/schemas/core.yml): core schema for the SPEC.md framework.
- [Spec schema file](./references/schemas/spec.yml): full schema for the SPEC.md file.
- [Plan schema file](./references/schemas/plan.yml): full schema for the plan document generated by the Plan function.
- [Plan template](./references/templates/plan.md): template for the plan document generated by the Plan function.
- [Simple spec template](./references/templates/spec-simple.md): example of a simple SPEC.md file — frontmatter, title, and description only.