---
id: task-tracker-api
title: Task Tracker API
version: "1"
status: draft
type: api
tech:
  languages: JavaScript
  frameworks: Express
  platform: Node.js
metadata:
  author: Guy Smiley
  updated: 2026-07-20
---

# Task Tracker API

A small REST API for tracking tasks. Clients can create, list, update, and delete tasks.

## Features
- Create, list, update, and delete tasks.
- Each task has a title and a completed state.

## Requirements

### Functional
- The API shall support creating, listing, retrieving, updating, and deleting tasks.
- Tasks shall be persisted for the lifetime of the server process.

### Future Considerations
- Support task priority levels (low, normal, high) so clients can sort and filter by urgency.

## Domain

### Entities

#### Task
- id: uuid
- title: string (required)
- status: TaskStatus
- createdAt: datetime

### Types
- TaskStatus: "todo" | "in-progress" | "done"

## API

### Endpoints
- **GET /tasks**: List all tasks.
- **POST /tasks**: Create a task.
- **GET /tasks/{id}**: Retrieve a single task.
- **PUT /tasks/{id}**: Update a task.
- **DELETE /tasks/{id}**: Delete a task.

## Folder Structure
```
src/
├── server.js
├── store.js
├── models/
│   └── task.js
└── routes/
    └── tasks.js
```
