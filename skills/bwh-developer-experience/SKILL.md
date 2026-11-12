---
name: bwh-developer-experience
description: Improve setup, build, test, and debugging workflows through human-steered implementation and review rounds. Exclude standalone audits, ordinary bug fixes, documentation-only edits, and global tooling changes.
---

# Improve developer experience

Use this skill when the user commissions an iterative improvement to the developer journey. For standalone reviews, route to the relevant review skill; for a defect, use bug diagnosis; for a documentation-only edit, use technical writing.

## Required workflow

1. Read and follow [improvement rounds](../../contracts/improvement-rounds.md) for cadence, team, measurement, evidence, checkpoints, and authority.
2. Read and follow [model routing](../../contracts/model-routing.md) for toolkit model selection and delegation.
3. Read project instructions, onboarding material, existing verification guidance, and relevant build/test scripts before acting.

The improvement-rounds contract controls the shared process. This skill defines the developer-experience scope and evidence.

## Bound the developer journey

1. Identify the project, developer role, operating system or environment, and the journey the user wants improved.
2. Trace the journey from a clean checkout or stated starting point through setup, first useful action, build/test feedback, and recovery from a common failure.
3. Inspect current instructions, scripts, dependency setup, configuration, tests, and recent changes. Record the revision and existing local modifications.
4. Select a small number of representative tasks with the user or infer and label a narrow set when the request is clear.
5. State exclusions, including unrelated product behavior, deployment, global tooling, and any service or credential changes.

Keep comparisons reproducible. Prefer a disposable checkout, container, or account and a clean cache. If reuse is needed, record cache state and keep it the same before and after. Do not alter global tools, shared credentials, or secrets as a convenience.

## Evidence plan

Before editing, choose only measures that fit the selected journey. Useful observations include:

- elapsed time for setup, first successful build, selected tests, and feedback after an intentional safe failure;
- number of explicit steps or commands needed, including retries;
- setup/build/test failures, error messages, and recovery steps;
- whether the developer reaches the expected artifact or test result.

Record the task, starting state, environment and tool versions, checkout revision, cache condition, command sequence, elapsed samples, and failures. For timing noise, repeat a proportionate number of times under comparable conditions and show samples or a justified summary and spread. Keep failed attempts in the record. Do not claim population outcomes from a synthetic run.

Use agent-driven or scripted attempts only as proxies for friction in the documented workflow. Label them synthetic; they do not establish outcomes for real novice developers. Do not require every listed measure when it would add no useful evidence.

## Review and improve

Review applicable categories separately, with cited evidence:

- discoverability of the next step and prerequisites;
- setup burden and clarity of failure recovery;
- speed and usefulness of build/test feedback;
- consistency across documented and executable workflows;
- accessibility of local development without special privileges.

Mark unsupported categories N/A with a reason. Keep reviewer judgments distinct from elapsed times, step counts, and task outcomes. Do not turn proxies into objective quality scores or claim that a score proves developer satisfaction.

Rank suggestions by benefit, risk, and effort. Prefer bounded changes to setup scripts, defaults, local checks, or feedback messages that address observed friction. Preserve project conventions and supported environments. Avoid broad dependency refreshes, secret handling changes, global configuration, and speculative workflow redesign without explicit authority.

## Validate and checkpoint

1. Implement one bounded pass from the commissioned suggestions.
2. Run the project's applicable checks and repeat the same developer tasks with the same disposable starting conditions where possible.
3. Compare outcomes, elapsed samples, steps, retries, failures, and recovery. Call out any changed fixture or environment that limits comparison.
4. Verify that existing supported setup paths and expected build/test behavior remain correct. Fix in-scope regressions and refresh affected evidence.
5. Obtain the after review and suggestions required by the improvement-rounds contract.
6. Present a checkpoint with the changed files, before/after evidence, limits, trade-offs, and ranked suggestions. Stop for the human's direction; do not begin another improvement pass from an assessment alone.

If a measure cannot be collected, report it as unknown and continue with unaffected evidence. Keep run artifacts and the resumption record at the project convention or the location specified by the contract.
