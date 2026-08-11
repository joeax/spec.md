---
id: plan-20260801-002
description: Add completion tracking and bulk-clear support to the Task Tracker API.
generated: 2026-08-01
state: ready
---

# Execution Plan

## Summary of Changes
- Add a dedicated endpoint for marking a task complete.
- Record when a task was completed.
- Let clients filter the task list by completion state.
- Let clients clear all tasks at once.

## Tasks
- [ ] **T01**: Add a `PATCH /tasks/:id/complete` endpoint that marks a task completed, backed by a new `store.complete(id)` helper. Return 404 if the task doesn't exist, matching the existing routes.
- [ ] **T02**: Add a `completedAt` timestamp field to the Task model. It should be set when a task is completed via `store.complete`, and cleared back to `null` if the task is later un-completed via `PUT /tasks/:id`.
- [ ] **T03**: Add a `GET /tasks?completed=true|false` query filter to the list endpoint so clients can filter by completion state. With no query param, behavior is unchanged (returns all tasks).
- [ ] **T04**: Add a `DELETE /tasks` endpoint that clears every task at once, backed by a new `store.clear()` helper.

## Implementation Notes
- No test framework is configured in this project; manual/code-review verification of the endpoints is acceptable.
- Keep the in-memory `Map`-based store; no persistence layer is in scope here.
- `completedAt` is derived state tied to `completed` — the two should never disagree.
- `DELETE /tasks` is a distinct, more destructive operation from the existing `DELETE /tasks/:id` and should be reviewed carefully before being exposed without auth (out of scope here, but worth flagging).
