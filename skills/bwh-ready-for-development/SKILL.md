---
name: bwh-ready-for-development
description: Convert a human-approved specification into small, sequenced, independently verifiable PRD tasks and confirm that the work is ready for agentic development.
---

# Ready for Development

## Goal

Turn an approved spec into executable work without inventing scope, while making dependencies, acceptance criteria, and validation explicit enough for `bwh-development`.

## Workflow

1. Confirm the referenced spec is the approved artifact or ask for the missing approval state.
2. Read the spec first, then the smallest planning context needed to place work correctly.
3. Extract outcomes, requirements, non-goals, affected surfaces, dependencies, risks, rollout constraints, and verification needs.
4. Check active, backlog, and completed work for duplicates.
5. Create small, outcome-oriented tasks sequenced from foundations and contracts through integrations, UX, and polish.
6. Validate the consuming project's PRD schema and run a readiness check for every task.

Each task must have clear scope, acceptance criteria, dependencies, affected areas, and a verification step. Prefer 2–6 tasks for a normal feature; split cross-cutting or risky work further.

## Stop conditions

Stop before editing the PRD when the spec is not approved, cannot be found, contains a material unresolved decision, or cannot be decomposed without inventing scope.

## Handoff

Return the task count, categories/chunks, dependency order, duplicate checks, assumptions, readiness gaps, and validation evidence. Recommend `bwh-development` only when the readiness gate passes.
