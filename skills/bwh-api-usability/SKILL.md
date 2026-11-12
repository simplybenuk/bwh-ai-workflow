---
name: bwh-api-usability
description: Improve an API's usability for its consumers through bounded implementation and iterative review of contracts, examples, errors, and common tasks. Use for API usability rounds; exclude standalone audits, bug-only fixes, documentation-only edits, and unrequested breaking changes.
---

# Improve API usability

Use this skill when the user commissions iterative work on how consumers discover, understand, and successfully use an API. Route standalone architecture surveys to architecture review, isolated defects to bug diagnosis, and docs-only changes to technical writing.

## Required workflow

1. Read and follow [improvement rounds](../../contracts/improvement-rounds.md) for cadence, independent review, measurement integrity, checkpoints, and authority.
2. Read and follow [model routing](../../contracts/model-routing.md) for toolkit model selection and delegation.
3. Read project instructions, API compatibility policy, contract tests, release notes, and verification guidance.

The shared contract owns round mechanics. This skill owns the consumer tasks, API evidence, and safeguards.

## Define scope and consumer tasks

1. Identify the API surface, consumer type, version or release boundary, and the usability concern named by the user.
2. Trace representative consumer tasks from an available starting point through successful response handling. Examples include authentication, a paginated read, a validation failure, and a retryable failure when those apply.
3. Inspect public schemas, SDKs, examples, reference docs, tests, and implementation. Note which source is authoritative and where representations disagree.
4. Choose a bounded task set and fixtures that exist already or can be created locally. Record exclusions and the current compatibility guarantees.
5. Do not send load, mutate production data, call paid services, or test real customer credentials without explicit authority.

## Measure executable usability

For selected tasks, use executable consumer flows when practical: contract tests, SDK examples, scripts, or isolated fixtures. Record the exact fixture and dataset size, API/schema revision, client/runtime versions, environment, command or request sequence, denominator, and results.

Choose a proportionate subset of measures that helps answer the task:

- task completion and correct interpretation of the response;
- calls, setup steps, retries, and elapsed time under the stated fixture;
- error classes, confusing or missing fields, and recovery path;
- behavior for authentication, pagination, idempotent retry, or validation where in scope;
- compatibility outcomes for supported old clients or schema versions.

Retain failed attempts and report counts with their denominator. Repeat only where timing or variable service behavior makes it useful. State the fixture and coverage; synthetic calls do not establish real-world consumer success. Do not describe fewer calls or faster timing as better usability without confirming task correctness.

## Review and change

Assess these judgment categories separately and cite the relevant contract, example, execution, or code:

- consistency between public contract, implementation, SDK, and published guidance;
- clarity of common task shape, naming, defaults, and response structure;
- usefulness and predictability of errors and recovery;
- discoverability of authentication, pagination, limits, and retry behavior when applicable;
- compatibility impact and migration burden.

Use N/A with a reason where a category does not apply. Keep these reviewer judgments separate from task counts, calls, errors, and timings. Do not infer broad usability from a small fixture or use a composite score as proof.

Rank proposed changes with stable IDs, evidence, affected task, benefit, risk, and effort. Prefer targeted changes that remove demonstrated consumer friction while preserving published contracts. Make no breaking change, auth-policy change, data-model migration, or rollout commitment unless specifically commissioned. If a useful fix requires one, ask before implementing it and continue independent in-scope work where possible.

## Validate and checkpoint

1. Make one bounded pass using commissioned recommendations.
2. Run relevant contract, compatibility, and consumer-flow checks. Compare the same tasks against the same known fixtures and supported client versions.
3. Verify error paths and adjacent consumers affected by the change. Report breaks, regressions, missing environments, and unmeasured behavior.
4. Refresh affected evidence if fixes alter the contract or result.
5. Complete the after assessment and suggestions required by the improvement-rounds contract.
6. Present the evidence and implementation at the required human checkpoint, including compatibility findings and unresolved decisions. Stop until the human steers another round.

Report unavailable checks as unknown, not passed. Preserve raw traces, request/response examples, or test output with the run record under the project's evidence convention.
