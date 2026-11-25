# Integration Guide

This guide explains how to integrate SPEC.md with other SDD workflows, such as OpenSpec, SpecKit, and BMad.

> This guide is a work in progress. If you have suggestions for how to improve it, please submit an issue or PR.

## OpenSpec

Currently, OpenSpec requires you to store system-wide specs in its own space: `./openspec/specs/`. There is an [open proposal](https://github.com/Fission-AI/OpenSpec/issues/664) to allow configuration of the spec path.

Our current recommendation is to keep your SPEC.md files in the standard location (`./specs/`) and prompt your agent to sync the OpenSpec specs to your core SPEC.md specs. This is not ideal and deeper integration work is planned to automate this.

config.yaml example TBD

### Requirements

OpenSpec uses structured requirements syntax adopting [RFC 2119 keywords](https://github.com/Fission-AI/OpenSpec/blob/main/docs/writing-specs.md). We recommend you stay consistent if OpenSpec is part of your workflow. Here is an example:

```markdown
# Requirements

## Functional Requirements

- The system SHALL allow users to create an account.
- The system SHALL allow users to reset their password.

## Non-Functional Requirements

- The system SHALL respond to user actions within 2 seconds.
- The system SHALL be available 99.9% of the time.
```

## SpecKit

In the SpecKit `constitution.md` file, specify the path to your SPEC.md files. Provide explicit instructions to reference your SPEC.md specs for all planning and design work. 

In addition, a preset is planned to allow you to use SPEC.md templates in your workflows.