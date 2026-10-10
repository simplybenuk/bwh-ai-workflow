---
name: bwh-agent-review
description: Independently review completed implementation against the authorised request or approved specification, project guardrails, validation, and acceptance criteria. Use before accepting delivered work; use bwh-pr-review for a complete PR or branch review before merge.
---

# Agent review

Apply the shared contracts in `../../contracts/autonomy.md`, `../../contracts/collaboration.md`, `../../contracts/completion.md`, `../../contracts/context-loading.md`, `../../contracts/handoff.md`, `../../contracts/model-routing.md`, and `../../contracts/states.md`, plus the consuming project's adapter.

## Goal

Find material defects, omissions, regressions, security risks, and validation gaps before acceptance under the project's policy.

## Review boundary

Use the authorised request as the outcome authority for bounded work. Use the approved spec and task when the formal planning path applies. A spec or PRD is not required merely to conduct review.

Review the implementation diff, relevant tests, validation results, and affected source-of-truth files. Do not expand scope, perform unrelated cleanup, or silently rewrite the implementation.

The reviewer must be separate from the implementer and start with fresh context. Give it the request or governing spec, project instructions, changed files, and necessary raw evidence, without the implementer's rationale or suggested findings. If independence cannot be established, report `REVIEW INCOMPLETE`; a self-check does not count as independent review.

## Workflow

1. Reconstruct the intended outcome and acceptance criteria from the request or approved spec and task. Establish the project's validation and acceptance policy.
2. Inspect the implementation and tests using the shared criteria in [review.md](../../contracts/review.md).
3. Verify validation evidence under that contract; run focused checks when needed.
4. Classify and support findings using that contract.
5. Identify consequential assumptions, residual risks, and any human judgment needed. Require human output testing when project policy or those risks require it, and name the observable behaviour to check. Do not add manual testing solely because the work is complete.
6. Decide whether the work meets the project's acceptance requirements. Adequate automated acceptance evidence can satisfy a project that permits it; label it as automated acceptance, never as human approval.

## Stop conditions

Return the work to `bwh-development` when a blocking finding exists, required validation fails, or implementation materially diverges from the governing request or spec. Missing necessary evidence produces an incomplete review. Do not approve work with unresolved security, tenancy, data-integrity, or permission concerns.

## Handoff

Return the verdict, supported findings, validation performed and its limits, material residual risk, and any remaining acceptance action. Persist evidence in a review artifact only when the project or chosen workflow requires one. Use project states when applicable; use `READY FOR HUMAN TESTING` or `NOT READY FOR HUMAN TESTING` only for a workflow that requires human testing.

Consolidate related findings and omit empty categories, full logs, repeated implementation summaries, and exhaustive inspected-file lists. Required publication or merge review remains a separate gate. Completed bounded work needs no automatic archive or retrospective; `bwh-archive-change` and `bwh-retro` run only when requested.
