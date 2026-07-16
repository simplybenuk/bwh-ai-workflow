---
name: bwh-executor
description: Execute one bounded planning task in a project repository with focused changes, required validation, and traceable completion evidence.
---

# Executor

## Goal

Complete exactly the requested task or explicitly authorised run count while preserving project scope, security, and source-of-truth rules.

## Workflow

Select the highest-priority eligible task using the project's planning rules. Inspect only relevant context. Implement the smallest complete change, add or update focused tests, run the required validation suite, update planning artifacts, and commit only when the project workflow authorises commits.

Use stronger reasoning or review when the task crosses architecture, tenancy, permissions, security, migration, rollout, or recovery boundaries, or when validation repeatedly fails.

## Stop conditions

Stop on a material blocker, failed required validation that cannot be safely resolved in scope, missing authority for an external or destructive action, or scope expansion. Record the blocker and do not start another task.

## Handoff

Report changes, decisions, assumptions, files, tests, validation results, planning status, commit status, and next priority.
