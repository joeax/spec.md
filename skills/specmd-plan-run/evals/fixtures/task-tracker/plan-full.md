---
id: plan-20260801-001
description: Add completion tracking to the Task Tracker API.
generated: 2026-08-01
state: ready
---

# Execution Plan

## Summary of Changes
- Add a dedicated endpoint for marking a task complete.
- Record when a task was completed.
- Let clients filter the task list by completion state.

## Tasks
- [ ] **T01**: Add a `PATCH /tasks/:id/complete` endpoint that marks a task completed, backed by a new `store.complete(id)` helper. Return 404 if the task doesn't exist, matching the existing routes.
- [ ] **T02**: Add a `completedAt` timestamp field to the Task model. It should be set when a task is completed via `store.complete`, and cleared back to `null` if the task is later un-completed via `PUT /tasks/:id`.
- [ ] **T03**: Add a `GET /tasks?completed=true|false` query filter to the list endpoint so clients can filter by completion state. With no query param, behavior is unchanged (returns all tasks).

## Implementation Notes
- No test framework is configured in this project; manual/code-review verification of the endpoints is acceptable.
- Keep the in-memory `Map`-based store; no persistence layer is in scope here.
- `completedAt` is derived state tied to `completed` — the two should never disagree.
