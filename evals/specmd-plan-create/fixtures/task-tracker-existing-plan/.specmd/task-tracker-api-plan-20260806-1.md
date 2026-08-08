---
id: task-tracker-api-plan-20260806-1
description: Implement task priority levels (low/normal/high) for the Task Tracker API.
generated: 2026-08-06
state: ready
spec: task-tracker-api
---

# Execution Plan

## Summary of Changes
- Add a `TaskPriority` domain type (`"low" | "normal" | "high"`) and a `priority` field on the `Task` entity, defaulting to `"normal"` when not supplied.
- Allow `priority` to be set on task creation (`POST /tasks`) and changed on update (`PUT /tasks/{id}`).
- Reject invalid `priority` values on create/update with a validation error.
- Allow the task list (`GET /tasks`) to be filtered by `priority` and sorted by `priority`, so clients can sort and filter by urgency per the spec's stated intent.
- Ensure `priority` is included in all task representations returned by the API.

## Tasks
- [ ] **T01**: Add `TaskPriority` type (`"low" | "normal" | "high"`) to `src/models/task.js`.
- [ ] **T02**: Add a `priority: TaskPriority` field to the `Task` model in `src/models/task.js`, defaulting to `"normal"` when not provided.
- [ ] **T03**: Update task creation logic in `src/store.js` to persist the `priority` field on new tasks.
- [ ] **T04**: Update `POST /tasks` in `src/routes/tasks.js` to accept an optional `priority` field in the request body, defaulting to `"normal"` when omitted.
- [ ] **T05**: Update `PUT /tasks/{id}` in `src/routes/tasks.js` to allow updating a task's `priority`.
- [ ] **T06**: Validate `priority` values on create and update, rejecting anything outside `"low" | "normal" | "high"` with a 400 response.
- [ ] **T07**: Update `GET /tasks` in `src/routes/tasks.js` to support filtering results by a `priority` query parameter (e.g. `?priority=high`).
- [ ] **T08**: Update `GET /tasks` to support sorting results by a `sort` query parameter (e.g. `?sort=priority`), ordered ascending `low` -> `normal` -> `high` by default.
- [ ] **T09**: Ensure `priority` is included in task objects returned by `GET /tasks`, `GET /tasks/{id}`, `POST /tasks`, and `PUT /tasks/{id}`.

## Implementation Notes
- Scope is limited to the "Support task priority levels (low, normal, high) so clients can sort and filter by urgency" item under Requirements > Future Considerations in `SPEC.md`. It carries no explicit priority tag (defaults to `[normal]`) and isn't part of the current Functional requirements, but is now in scope per the user's explicit request to plan this feature.
- No source files exist in the project yet beyond `SPEC.md` — the `src/` tree described in Folder Structure hasn't been scaffolded. All tasks reference the paths that Folder Structure specifies as the eventual home for this code and start unstarted (`[ ]`); an earlier plan covering the base CRUD API (Features/Functional Requirements) is a prerequisite this plan assumes is either already complete or run first.
- Default priority (`"normal"`) is a smallest-reasonable-assumption: the spec names the three levels but doesn't state a default. State this assumption to the user before deviating from it.
- Sort/filter query parameter names (`priority`, `sort`) and the ascending `low -> normal -> high` default order are inferred to match common REST conventions; the spec doesn't specify exact parameter names or ordering direction. Flag for confirmation if a different contract (e.g. `order=asc|desc`, a different parameter name) is expected downstream.
- No `## Testing` section exists in `SPEC.md` and this item isn't tagged `[critical]`/`[high]`, so no testing tasks are included per the plan schema's coverage guidance. Adding unit tests for validation and filter/sort behavior is recommended once a test framework is chosen for the project.
- No database is in scope; persistence is the existing in-memory `src/store.js`, valid for the lifetime of the server process per the spec's Functional requirements.
