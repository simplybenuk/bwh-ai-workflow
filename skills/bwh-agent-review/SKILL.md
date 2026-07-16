---
name: bwh-agent-review
description: Independently review completed implementation against the approved specification, project guardrails, tests, and user-visible acceptance criteria before human output testing.
---

# Agent Review

## Goal

Find material defects, omissions, regressions, security risks, and validation gaps before the human tests the product output.

## Review boundary

Review the approved spec, PRD task, implementation diff, relevant tests, validation results, and affected source-of-truth files. Do not expand scope or perform unrelated cleanup. Do not silently rewrite the implementation.

## Workflow

1. Reconstruct the intended outcome and acceptance criteria from the approved spec and task.
2. Inspect the implementation and tests for requirement coverage, edge states, failure behavior, permissions, tenancy, data integrity, and responsive or user-visible behavior where relevant.
3. Verify the reported validation evidence; run focused checks when evidence is missing or suspicious.
4. Classify findings as blocking, should-fix, or informational.
5. Decide whether the work is ready for human output testing.

For risky changes, require evidence from the relevant schema, migrations, access controls, rollout, or recovery checks. Treat missing evidence as a gap, not proof that the behavior is safe.

## Stop conditions

Stop and return the work to `bwh-development` when a blocking finding exists, required validation fails, or the implementation materially diverges from the approved spec. Do not approve work with unresolved security, tenancy, data-integrity, or permission concerns.

## Handoff

Return a concise review verdict, findings with file or test evidence, validation performed, residual risks, and the human output-testing focus. The final handoff should explicitly say either `READY FOR HUMAN TESTING` or `NOT READY FOR HUMAN TESTING`.
