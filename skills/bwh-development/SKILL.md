---
name: bwh-development
description: Execute bounded PRD tasks in a project repository with focused changes, required validation, planning traceability, and a handoff to independent agent review.
---

# Development

## Goal

Implement the requested task or authorised run count while preserving the approved spec, project scope, security, and source-of-truth rules.

## Workflow

1. Select the next eligible task using the project's planning rules.
2. Inspect only relevant context and confirm the task is still consistent with the approved spec.
3. Implement the smallest complete change and add or update focused tests.
4. Run the project's required validation suite and resolve failures that are in scope.
5. Update planning artifacts and commit only when the project workflow authorises commits.
6. Hand the completed work to `bwh-agent-review` before human output testing.

Use stronger reasoning or additional review when the task crosses architecture, tenancy, permissions, security, migration, rollout, or recovery boundaries, or when validation repeatedly fails.

## Stop conditions

Stop on a material blocker, failed required validation that cannot be safely resolved in scope, missing authority for an external or destructive action, or scope expansion. Record the blocker and do not start another task.

## Handoff

Report changes, decisions, assumptions, files, tests, validation results, planning status, commit status, and the next priority. Explicitly state that the next handoff is `bwh-agent-review`.
