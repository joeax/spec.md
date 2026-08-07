---
id: plan-20260801-003
description: Add completion tracking and lock down the Task Tracker API.
generated: 2026-08-01
state: ready
---

# Execution Plan

## Summary of Changes
- Add a dedicated endpoint for marking a task complete.
- Protect the API from unauthorized access.
- Let clients clear all tasks at once.

## Tasks
- [ ] **T01**: Add a `PATCH /tasks/:id/complete` endpoint that marks a task completed, backed by a new `store.complete(id)` helper. Return 404 if the task doesn't exist, matching the existing routes.
- [ ] **T02**: Add authentication to the task API so only authorized clients can access it.
- [ ] **T03**: Add a `DELETE /tasks` endpoint that clears every task at once, backed by a new `store.clear()` helper.

## Implementation Notes
- No test framework is configured in this project; manual/code-review verification of the endpoints is acceptable.
- Keep the in-memory `Map`-based store; no persistence layer is in scope here.
- There is currently no user or credential model anywhere in this codebase.
