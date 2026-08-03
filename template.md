---
id: app-slug # Unique spec slug; defaults from the title if omitted.
version: "1" # Spec version; use any scheme that fits the project i.e. semantic or date-based versioning
status: draft # Statuses: draft, review, stable, or deprecated.
type: web # App type: web, mobile, desktop, api, library, cli, service, system, or custom.
extends-schema: [] # Optional schema extensions that add or override sections.
tech:
  languages: [] # Primary languages used in the project.
  frameworks: [] # Main frameworks and libraries in use.
  platform: browser # Target runtime or platform.
  dependencies: [] # Additional packages beyond the frameworks list.
links:
  depends-on: [] # Specs that must exist first.
  extends: [] # Specs this one inherits from or specializes.
  related: [] # Informational links to nearby specs.
meta:
  author: Your Name # Human author or owner.
  created: yyyy-mm-dd # Original creation date.
  updated: yyyy-mm-dd # Last meaningful update date.
  changelog:
    - "yyyy-mm-dd: Initial version." # Brief history entry.
---

# Title of Application

This is a vibespec. This description provides a brief overview of the software system, its purpose, and its functionality. It should be placed immediately after the title and can be one sentence to a few paragraphs. It should be concise and require just enough information for the LLM to understand the system's intent.

## Features
- [Feature 1]
- [Feature 2]
- [Feature 3]

<!-- Note: This section can overlap with User Stories, but is focused on high-level features rather than user interactions. -->

## Requirements
[Lists universal requirements for the software system. Includes functional requirements. This can include non-functional requirements such as performance, security, and compliance. It can also include any specific constraints or limitations that should be considered during development.]

> For all requirements, you can tag them with a priority level, such as [critical], [high], [medium], or [low]. Default is medium.

### Functional
- [critical] This is a critical functional requirement that must be implemented for the system to work.
- [Functional Requirement 2]
- [low] [Functional Requirement 3]

### Technical
- [Technical Requirement 1]
- [Technical Requirement 2]

### Out of Scope
[Explicitly list what will NOT be included in this version]

### Future Considerations
[Requirements planned for later versions. This will help steer the code generation to be forwards compatible.]

## Considerations
[Outlines any specific considerations, constraints, or limitations that should be taken into account when developing or using the software system.]
- This system will be deployed out to small set of users for usability testing before being released to 10,000+ users across the organization.
- The system will be used by [user type].
- The system will be deployed on [platform/environment].

## User Stories
As a [user type], I want to [action] so that [benefit].
As a [user type], I want to [action] so that [benefit].
[Continue with all core user stories]

### User Flow
1. [Step 1 of primary user journey]
2. [Step 2 of primary user journey]
3. [Step 3 of primary user journey]

### Acceptance Criteria
- [ ] [Specific, testable criteria]
- [ ] [Specific, testable criteria]

## Architecture | Application | Application Design | Application Design | System Design
[Describes the high-level structure of the software system, including its components, modules, and their interactions. Should include diagrams, such as component diagrams, sequence diagrams, or deployment diagrams, to illustrate the architecture. Describes software patterns like facade, inversion of control/dependency injection, etc.]

## Domain | Data | Data Model | Data Design
[Describes the entities, relationships, and data structures used in the software system. It can include details about the database schema, data models, or any other relevant data design aspects.]

### Entities

#### [Entity1]
- id: string
- name: string
- email: string (should contain a '@' symbol)
- phone: string
- address: string
- notes: string

#### [Entity2]
- id: string

### Relationships
- Entity1 has a one-to-many relationship with Entity2.

[This section can include diagrams, such as ER diagrams or UML class diagrams, to visually represent the data model.]

## Folder Structure
[Describes the folder structure of the project. Use a tree view (below) or nested list.]
```
.
├── src
│   ├── main.py
│   └── utils.py
├── tests
│   ├── test_main.py
│   └── test_utils.py
└── .env
```

## Setup
[List of project installation and setup instructions.]
- Install dependencies using X.
- Generate build scripts using Y.
- Create a `.env` file to store environment variables.

> Note: If you use an AGENTS.md file for setup information, indicate that here and provide a link to the AGENTS.md file. 

### Validation
- Validate the setup by running command `xyz` and ensure it completes without errors.

## UI
[Describes the user interface components, their layout, and interactions at a conceptual level. It can include wireframes, mockups, or detailed descriptions of UI elements.]

*[Note: This section should include detailed descriptions of UI elements, their behavior, and interactions at a conceptual level.]*

### Layout
Description of the layout structure, including grid systems, spacing, and alignment.

### Pages
List of pages in the application, for web applications.

### Screens
List of screens in the application, for desktop or mobile applications.

## API
[Describes the application programming interfaces (APIs) used in the software system at a conceptual level. It can include details about RESTful APIs, GraphQL APIs, or any other type of API. For a frontend application, this help the backend that will be developed later. For a backend or full-stack application, this can steer how controllers/routes will be generated.]

> Note: If this is part of a monorepo and the backend has its own folder, you can reference the backend's SPEC.md file in the dependencies in the frontmatter.

### Endpoints
[List of API endpoints, including HTTP methods, paths, and descriptions. This can be formatted as a table or a list.]
- **GET /api/resource**: Retrieves a list of resources.
- **POST /api/resource**: Creates a new resource.
- **PUT /api/resource/{id}**: Updates an existing resource.
- **DELETE /api/resource/{id}**: Deletes a resource.

## Database
[Describes the database used in the software system, including the type of databases (e.g., SQL, NoSQL), the data model, and any relevant database technologies. This section may list out details about tables, collections, or schemas used in the database, when needed to guide the implementation. For a backend or full-stack solution, drives the implementation of database access code.]

*[Note: This section discusses the databases themselves. For the data design, refer to the Data section above.]*

## Testing

### Unit Tests
[Describes the unit tests for the software system, including the testing framework used, test cases, and any specific testing considerations.]

### Integration Tests
[Describes the integration tests for the software system, including how different components interact and any specific integration testing strategies.]

### End-to-End Tests
[Describes the end-to-end tests for the software system, including how the entire system is tested from the user's perspective, covering all user flows and interactions.]

## Deployment
[Describes how the software system is deployed, including the environment setup, deployment scripts, and any specific deployment considerations.]
- Deployment environment: [e.g., AWS, Azure, on-premises]

## Issues
[Lists all known issues of the code that was generated, including bugs, performance concerns, or areas needing improvement.]
- In `useCustomers.ts`, when the API returns a 401, the error is not handled properly, leading to an unhandled promise rejection.

## Glossary
[Defines any technical terms, jargon, or acronyms used in the vibespec.]

## References
[Lists of references, such as documentation, external resources, or related projects.]

### Related
- [Link to child vibespec](./path/to/child-vibespec.md)
- [Link to parent vibespec](./path/to/parent-vibespec.md)

### External | Online
- [Link to related document or resource](https://example.com)