# SPEC.md

SPEC.md is a simple, minimalist, open format for spec-driven development. Write a single SPEC.md for your entire project, or decompose your project into multiple SPEC.md files for each module or subproject.

> SPEC.md is the successor to [Vibespec](https://github.com/joeax/vibespec)

## Explore

* Full [specification](specification.md) for the SPEC.md format.
* Example [template](template.md) file to preview the format and syntax.


## Problem Statement

Spec-driven development was meant to fill a void in the AI-assisted software development workflow, a natural progression from ad hoc prompt engineering methods. However, many existing spec frameworks are heavy and opinionated, while being designed for large, enterprise teams. In addition, product requirements documents (PRDs) and software requirements documents (SRDs) are often too high-level, human-centered, and lack the detail needed for effective code generation. 

### What SPEC.md is

- A simple, expressive, extensible agent-optimized format for writing software specifications
- A source-of-truth document for your software project that can be used to generate code, tests, and documentation
- A single, packaged agent skill to help you define specs, plan changes, and sync your spec with your codebase

### What SPEC.md is not

- There is no tooling to run - simply install the agent skill
- There is no prescribed workflow: SPEC.md has no opinion on how you plan, implement, or subdivide work into composible tasks
- It does not care whether you use AI-DLC, BMad Method, or any other agent-driven development methodology
- It does not lock you into any IDE, coding agent, or LLM model
- It does not replace [AGENTS.md](https://agents.md), but rather complements it by describing "the what" and "the why" of your software project, while AGENTS.md describes "the how": the conventions, rules, and constraints of how you want your software project to look

## Design Goals

1. **Simple**: Provide a spec format that can be set up, understood, and operationalized in minutes
2. **Agent-optimized**: Be agent-optimized, allowing for easy integration with agents and other AI tools
3. **Flexible**: As simple as a single sentence, or as complex as a PRD
4. **Lightweight**: Focused on small projects or teams
5. **Extensible**: Can be extended to accommodate evolving software types
6. **Composable**: Can be decomposed into multiple SPEC.md files for larger projects or teams
7. **Non-opinionated**: Does not prescribe a specific workflow, methodology, or toolchain
8. **Non-exhaustive**: Does not force you to cover every possible feature, user path, or edge case

## Setup

Install the SPEC.md agent skill using the [skills.sh](https://www.skills.sh/) installer:

```bash
npx skills add joeax/specmd@specmd
```

## Usage

The `specmd` skill comes packaged with a set of commands that allow you to generate, update, and manage your SPEC.md file:

- **Define**: Generate a new SPEC.md file based on your existing codebase or a new project idea.
- **Plan**: Generate a plan for implementing the features and requirements defined in your SPEC.md file.
- **Sync**: Sync your SPEC.md file with your existing codebase to ensure it is up-to-date.

## Getting Started

### Existing Codebase

For existing, brownfield projects, simply prompt your agent to generate a SPEC.md file based on your existing codebase:

```
Inspect the codebase and generate a SPEC.md file.
```

### New Projects

For a brand new project, we recommend using the **Snowflake Method** to create your SPEC.md file. This method allows you to start with a simple idea and iteratively expand it into a complete specification.

> The **Snowflake Method** is a technique popularized by [Randy Ingermanson](https://www.advancedfictionwriting.com/articles/snowflake-method/), a software engineer turned fiction writer, for writing a novel by starting with a simple idea and gradually expanding it into a full story.

#### Step 1: One-Paragraph Summary

Write a one-paragraph summary of your software project, capturing the core idea and main objectives. You are free to provide some basic implementation details, like supported platforms, programming languages, or frameworks. The goal is to provide a clear and concise overview of the project.

Here is an example:

```markdown
# Task Manager App

A simple task management app that helps users organize their tasks, set deadlines, and track progress. The app allows users to create, edit, and delete tasks, categorize them by project, and receive notifications for upcoming deadlines. The app is built using React for the frontend and Node.js for the backend, with a MongoDB database to store user data. It supports both web and mobile platforms.
```

#### Step 2: Expand into a Basic Spec

In this step, use the `specmd` skill to expand your one-paragraph summary into a more detailed specification. Include key features, user stories, and high-level architecture. The goal is to provide a clear blueprint for your project.

Sample prompt:

```
Turn this spec into a more detailed spec with frontmatter. We will be using React 19, Node.js 20, and MongoDB 7. Include features, user stories, architecture, and data design.
```

#### Step 3: Generate the Application

Once you have a detailed SPEC.md file, you can use the `specmd` skill to generate the initial codebase for your application. This will create a scaffolded project structure based on the specifications defined in your SPEC.md file.

Sample prompt:

```
Generate an application from this spec. If a specific requirement is not defined, make you best guess based on the spec and your knowledge of best practices.
```

#### Step 4: Evolve it into a Detailed Spec

As you progress through the development of your project, continue to evolve your SPEC.md file by adding more details, like specific UI components, API endpoints, and data models. This will help ensure that your specification remains up-to-date and relevant throughout the development process.

Use the same step for **Existing Codebase** above to sync your SPEC.md with your codebase.


## Development workflow

The development workflow typically involves iterating between updating your SPEC.md file, generating plans, and implementing them. This can be done in a variety of ways: either in a single coding chat session, or as different steps in your agent workflow.

### Example

Let's say your project is a backend microservice written in Python and using FastAPI, and you want to add a new API endpoint to your project. The recommended steps are:

1. Update your SPEC.md file to include the new API endpoint, its purpose, and any relevant details.

2. Combine the `specmd` skill with your plan agent to generate an execution plan for the API endpoint. Include any user story or task details from an external system such as JIRA, write your own task document, or simply prompt the agent.

	Example task description:

	```markdown
	Generate a plan to implement the `/roles` API endpoint from SPEC.md.
	```

	This will create a plan document in `.specmd/plans/` that outlines the steps needed to implement the new API endpoint.

	> SPEC.md has no opinion on how you document or store tasks. However, if you are not using a project management tool, we recommend committing task markdown files to your repository for traceability.

3. Instruct your implementation agent to implement the plan. At this point, your `SPEC.md` file nor the `specmd` skill needs to be loaded into context. The plan document contains all the information needed for the implementation agent to complete the task.

4. After the implementation agent has completed the task, sync your SPEC.md file with your codebase and/or document any changes or deviations along with remediations in the Issues section of your SPEC.md file. 

	> Plan documents are disposable. After the work is complete and the branch merged to main, you can delete it.


## Spec Format

A SPEC.md document is structured with a specific format that includes frontmatter, a title, description, specification, and sections. The structure is designed to be flexible and can be adapted to fit the needs of the software system being described.

> Browse the full [SPEC.md format](specification.md) for more details.
> Browse the [template](template.md) file to preview the format and syntax, or use as a starting point.

### Simple Example

```markdown
# Tetris Clone
This is a spec for a Tetris clone that allows users to play the classic game in their web browser.
The game should have a simple UI, support keyboard controls, and keep track of the score. It should be 
built using vanilla JavaScript and TypeScript.
```

### Detailed Example

Here is more detailed example with frontmatter.

```markdown
---
id: tetris-clone
version: 2026-07-28
scope: project
status: draft
tech:
    type: web
    languages: TypeScript, HTML
    frameworks: none 
---

# Tetris Clone
This is a spec for a Tetris clone that allows users to play the classic game in their web browser. The game should have a simple UI, support keyboard controls, and keep track of the score. It should be built using vanilla JavaScript and TypeScript.

## Requirements
- The game should have a simple UI with a grid for the Tetris blocks.
- The game should support keyboard controls for moving and rotating the blocks.
- The game should keep track of the score and display it on the screen.
- The game should be responsive and work on different screen sizes.
```

### Typical Roles

SPEC.md is role-agnostic, but it's important to clarify the roles of the agents in your workflow. Here are some typical roles that may be involved in a spec-driven development workflow. Each of these roles may touch a different part of the SPEC.md file, but all roles should be aware of the overall project vision and goals.

| Role | Description | Sections in SPEC.md |
|------|-------------|-------------------------|
| Product Manager | Defines high-level requirements and priorities. | Requirements, User Stories |
| Architect | Designs the system architecture and ensures alignment with the overall vision. | Data Model, Architecture, Considerations |
| Developer | Implements features and fixes bugs according to the SPEC.md file. | Features, UI, API, Database, other custom sections |
| QA Engineer | Tests the software to ensure it meets the specifications and quality standards. | Testing, Issues |
| DevOps Engineer | Manages deployment, CI/CD pipelines, and infrastructure. | Deployment |

### Spectrum Principle

Every section exists on a spectrum from conceptual to concrete. You are free to choose the degree of granularity and detail you want to provide in each section. The key is to provide enough information for the agents to understand the intent of the software system, while leaving room for them to infer or fill in the gaps.

For more information, see [Specification > Sections > Spectrum Principle](specification.md#spectrum-principle).

## Spec Management

### Spec drift

You are ultimately responsible for keeping your SPEC.md file up-to-date and in sync with your codebase. If you find that your SPEC.md file is out of sync with your codebase, use the `specmd` skill to update a new SPEC.md. We recommend adding a spec syncing step in your agent workflow.

### Focus on intent

Specs are meant to describe the intent of your software system. While you are free to provide details to direct the implementation, understand the tradeoffs of doing so. Remove implementation details once the code has been generated, as the code itself becomes the source of truth for it.

Avoid the "everything under the sun" doomed waterfall mentality forced by other frameworks. The key thing here is what your SPEC.md file DOESN'T document: one-off edge cases, future state, and unwritten requirements. These are things that are better left to the agents to figure out.

### Spec linking

Similar to how you can structure AGENTS.md files, consider breaking up SPEC.md files. Have the root SPEC.md describe the intent of the whole system, then individual SPEC.md files for each module or subproject. 

## Examples

TBD

## Best Practices

- Use the Snowflake Method described above: start with a few sentences, then iterate as needed.
- Resist the urge to document every facet. Focus on key features, user stories, and high-level architecture. Let the agents fill in the gaps or infer from context.
- Keep your SPEC.md files lean and mean. Too much bloat raises token costs. If you find becoming overly descriptive or with too much overlap, summarize it down.
- Avoid spec drift by regularly syncing your SPEC.md file with the codebase.
- Prefer generating a plan document rather than directly implementing a change. This 2-step approach allows you to review the plan document before proceeding.
- Avoid implementing massive changes all at once. This may exceed your context window and/or overload the agent. Implement things as a human would: in small, incremental steps.
- Periodically check for updates to the `specmd` skill.
- Keep coding conventions, restrictions, and rules in your coding agent's instruction files/system prompts/AGENTS.md file.

## Comparison with other spec frameworks

It's important to note that SPEC.md is not trying to compete with other spec-driven frameworks. Instead, it is designed to be a lightweight, flexible, and agent-optimized alternative for small teams and projects. As a matter of fact, in some cases you may be able to fit SPEC.md with other spec-driven agentic workflows.

> If you find the SPEC.md file growing in size and complexity, you want want to consider one of these other spec-driven development workflows that are more suitable for larger teams and projects.

### Comparison Table

| | **SPEC.md** | **BMad Method** | **GitHub Spec Kit** | **Amazon Kiro** | **specs.md** |
|---|---|---|---|---|---|
| **What it is** | Spec format + agent skill | Multi-agent workflow framework | CLI + slash-command toolkit | Full IDE (fork of Code OSS) | Pluggable methodology framework |
| **Tooling required** | None — install a skill | CLI installer, npm package | CLI (`uv`/`specify`) | Dedicated IDE | CLI + IDE extension |
| **Artifacts per feature** | 1 spec file (+ 1 plan on demand) | PRD, architecture, sharded epics, story files | spec.md, plan.md, tasks.md, research.md, data-model.md, contracts/ | requirements.md, design.md, tasks.md | requirements.md, system-context.md, unit specs, bolt records |
| **Scope** | Any component, app, or system | Whole project, agile-team shaped | Single feature within a repo | Single feature within a repo | Domain/enterprise, DDD-shaped |
| **Cross-spec linking** | Spec graph (native) | Doc handoff between agents | None | None | Bounded-context relationships |
| **Agent model** | Any single agent | Named personas (PM, Architect, Dev, QA) | Any agent via integrations | Kiro's own agent | Phase-specific agents |
| **Principles/conventions doc** | Defers to AGENTS.md | Baked into PM/Architect personas | `constitution.md` | Steering Files | `standards/` in memory-bank |
| **Methodology opinion** | None — bring your own | Agile/Scrum-shaped | SDD, nine-article constitution | EARS notation, wave execution | DDD mandatory (AI-DLC flow) |
| **Best for** | Solo devs, small teams, fast iteration | Teams wanting agile ceremony w/ agents | Teams wanting GitHub-native SDD | Teams fully inside Kiro's IDE | Complex domains, multi-team, regulated environments |



