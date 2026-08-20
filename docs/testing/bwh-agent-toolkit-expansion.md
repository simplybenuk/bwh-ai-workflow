# BWH Agent Toolkit human testing

Status: `PENDING HUMAN TESTING`

Approved specification: `docs/specs/bwh-agent-toolkit-expansion.md`

Use a release candidate from a clean checkout at one recorded commit. Do not change catalog host status or publish a release until every required check below has evidence.

## Fresh full installation

Use a disposable project with no existing toolkit installation.

1. Preview a `full` installation for the chosen host.
2. Confirm the preview selects all 17 active skills and the shared contracts.
3. Run the installation.
4. Confirm the version 2 lock records the stable source, exact commit, host, `full` profile, 17 skills, contracts, and managed-file digests.
5. Confirm an unrelated local skill and project instruction file remain unchanged.
6. Invoke one new skill through the host and complete its representative outcome.
7. Record the host, commit, profile, observed skill count, lock path, output evidence, and result.

Expected result: the complete toolkit is available from one pinned source and no project-owned file changes.

## Existing workflow update

Use a disposable copy of a real version 1 workflow-only project. Include its adapter, context map, project instruction file, an unrelated local skill, and one locally customized managed-file variant for the conflict check.

1. Preview an update without naming a profile.
2. Confirm it defaults to `workflow` and selects exactly the original eight skills.
3. Confirm the customized managed file blocks replacement and leaves the old lock and installed files unchanged.
4. Resolve the fixture conflict explicitly, then rerun the update.
5. Confirm the version 1 lock changes to version 2 only after validation succeeds.
6. Confirm the adapter, context map, project instruction file, unrelated skill, specifications, PRDs, and source-of-truth documents remain unchanged.
7. Run the project checks and one existing end-to-end workflow smoke test.
8. Record the old and new revisions, selected profile, conflict evidence, preserved files, validation output, and result.

Expected result: the project remains workflow-only unless the tester explicitly chooses a broader profile.

## Host checks

Run one representative trigger and outcome on each packaged host.

| Host | Trigger route | Representative outcome | Evidence | Result |
| --- | --- | --- | --- | --- |
| Codex | `bwh-review-architecture` and `bwh-blast-radius` in fresh threads | Architecture review completed. Blast-radius review classified confirmed, cleared, and unproven claims without edits. | User supplied both outputs on 2026-08-20. Blast-radius behavior scored 5/5. Commit and host/model metrics were not captured. | Behavior pass, metadata pending |
| Claude Code | Pending | Pending | Pending | Pending |
| Cursor | Pending | Pending | Pending | Pending |

For each run, record the host version, toolkit commit, model and reasoning setting when exposed, tool set, latency, tokens when exposed, tool calls, retries, score, and failure notes. Keep host status `pending` when a required metric or outcome cannot be established.

## Skill output focus

Exercise these observable decisions across the host runs or extra focused runs:

- diagnosis-only work reports evidence without implementing;
- blast-radius review separates confirmed, cleared, and unproven claims;
- generated verification uses disposable state, a read-only doctor, second-view evidence, and owned cleanup;
- technical writing routes new product or engineering specifications to the specification workflow;
- grill mode triggers only on an explicit request and waits after each question round;
- agent instructions keep host mechanics in routed references;
- architecture review stops before interface design;
- prototype output remains isolated and unapproved for production;
- skills audit does not read raw history or mutate an installation by default.

## Acceptance record

- Fresh full installation: `PENDING`
- Existing workflow update: `PENDING`
- Codex representative run: `PENDING`
- Claude Code representative run: `PENDING`
- Cursor representative run: `PENDING`
- Human decision: `PENDING`

### Codex observation 1

On 2026-08-20, the user started a fresh Codex thread and ran `bwh-review-architecture` successfully. This confirms that Codex loaded the machine-level skill and routed the request to it. Keep the formal Codex representative run pending until the tester records the toolkit commit, exposed host and model metrics, and evidence that the review stopped before interface design or implementation.

### Codex observation 2

On 2026-08-20, the user asked `bwh-blast-radius` to review removing `bwh-ask` from the full profile without editing files. The response passed all five behavior checks. It made no changes, separated confirmed, cleared, and unproven risks, cited repository evidence and proof levels, recommended `python3 scripts/validate_catalog.py` as the smallest verification, and stopped without implementing the invalid change. The formal Codex gate remains pending only for the required commit and exposed host/model run metadata.

If testing finds a defect, return the change to `bwh-development` with the evidence. If every check passes and the human accepts the output, hand the change to `bwh-archive-change`.
