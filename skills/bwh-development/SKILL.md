---
name: bwh-development
description: Implement authorised scoped requests or approved planned tasks with focused changes, project validation, and independent review. Use for requested fixes, features, and implementation work.
---

# Development

Apply the shared contracts in `../../contracts/autonomy.md`, `../../contracts/collaboration.md`, `../../contracts/completion.md`, `../../contracts/context-loading.md`, `../../contracts/handoff.md`, `../../contracts/model-routing.md`, and `../../contracts/states.md`, plus the consuming project's adapter.

## Goal

Complete the requested change while preserving project scope, security, source-of-truth rules, and any approved specification that governs the work.

## Authority and planning

A clear request with defined scope authorises local implementation. Bounded scope does not mean a small change. A substantial settled feature can use an internal implementation sequence or task list, and delegation within project rules, without a written spec, PRD, progress log, state transition, or new human approval prerequisite.

Use the formal planning path when explicitly requested, required by applicable project policy, or needed to resolve consequential product decisions. Multiple independently verifiable delivery chunks alone do not require it. For the formal path, confirm human approval of the governing spec and any project-required readiness artifacts before implementation. Update the project's plan or PRD from the approved task outline when its planning rules require it, checking active, backlog, and completed work for duplicates. Preserve existing approved specs and non-goals in either path. Stop on missing required approval; do not infer approval from a draft being complete.

## Workflow

1. Read the request, project adapter, relevant instructions, and authoritative context. Establish the intended behaviour, acceptance criteria, validation requirements, and allowed actions. Use the project's planning rules to select a task when working from a plan.
2. Resolve routine technical choices from evidence. Ask only for missing consequential decisions, and continue unaffected work while waiting.
3. Implement the smallest complete change. Add or update focused tests when needed to verify the changed behaviour; preserve every project-required check.
4. Run required validation, including real schema, access-control, rollout, or recovery checks for affected risks. Resolve failures that are in scope. Mocked evidence does not prove a live boundary is safe.
5. Record material decisions and validation proportionally. Update existing planning or progress artifacts when required by project policy or the chosen formal workflow. Commit only with separate authority.
6. Hand the result to a fresh independent reviewer using `bwh-agent-review`. Reuse adequate review evidence for unchanged inputs; additional review should cover a different risk, changed work, or an explicit project requirement.

Use stronger reasoning or additional review when the task crosses architecture, tenancy, permissions, security, migration, rollout, or recovery boundaries, or when validation repeatedly fails.

## Stop conditions

Stop on a material blocker, failed required validation that cannot be safely resolved in scope, missing authority for an external or destructive action, or material scope expansion. Report the blocker and do not start another planned task. Do not manufacture planning artifacts to resolve a gate that does not apply to bounded work.

## Handoff

Lead with what changed and why. Include required validation results and their limits, material assumptions or blockers, relevant files or existing artifacts, commit status when relevant, and the `bwh-agent-review` handoff. Keep the format proportional to the change.

After review, follow the project's acceptance policy. Human output testing is conditional on that policy, consequential residual risk, or a decision only the human can judge. When required checks and review pass and no required work remains, bounded work can finish. Do not automatically archive it or start a retrospective.
