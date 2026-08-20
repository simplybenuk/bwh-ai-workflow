# BWH Agent Toolkit skills B and workflow regression

## Run metadata

- Date: 2026-08-20
- Requested model: unavailable
- Exposed runtime model: Codex agent based on GPT-5; exact deployment identifier unavailable
- Requested reasoning effort: unavailable
- Exposed runtime reasoning effort: unavailable
- Base revision and current `HEAD`: `28d931a4c22a220b0b46b9e0e4080fe08b7c8cd2`
- Worktree state: uncommitted toolkit implementation snapshot
- Approved specification SHA-256: `1fa61bbe970e01ee9889c1cbb6811820e31c27dafecf8c5dbdd45ffaaa9db804`
- Scoring rubric SHA-256: `e71ba3f230bc893b6f7c6d62e33a05a38a7743c3f8e08758c2ee04d8bccf847d`
- `bwh-write-agent-instructions` policy bundle SHA-256: `f99ac0a373bf8dcf4243e4816bd97209c5e24321613c9966058754a31ebf1049`
- `bwh-review-architecture` policy bundle SHA-256: `282a7ff10bd4e8ce4d46c4af99e36d470ccffd5334bad88dce5f2426191fb828`
- `bwh-prototype` policy bundle SHA-256: `50336373f96f30c066d836dc6e90ba1fdd7f01bd397d7ae91b102b76ceb73c12`
- `bwh-skills-audit` policy bundle SHA-256: `4ebf5cb50b8d54bb9147da8979521584004da1644c0efe2cdd7aed25a6c1a7b4`
- Current workflow case bundle SHA-256: `9eb4936d3de4474a483cccbd50b4bcd09a19e476c94670772540d9eb65806214`
- Current workflow policy bundle SHA-256: `313e022abe6e83231ea24ffba3ee365b07221e14bdebe166bedf37eb278d8dcf`
- Archived comparison result SHA-256: `9dc69bd4903490daf24e6591d5c3fa953238436f8fb698b2fa757961c33c564e`
- Catalog validator SHA-256: `fe9cdd9a298fff3681fcde54590aafe99fbe20207f7900e63f73ab4104d2aee3`
- Portable-skill validator SHA-256: `c8ab00e71497474723dfed5e38997eb88403b009031bc3cf16dbad1764067c14`
- Tool set: read-only shell inspection, local static validators, local unit tests, diff checks, hashing, and manual policy dry-runs; no fixture, skill, contract, or implementation mutation
- Measured final static-validation wall latency: 3.9 seconds
- Policy-suite and per-case latency: unavailable
- Input and output tokens: unavailable
- Tool calls: zero isolated calls per case; 18 shared inspection, validation, hash, result-write, and readback calls
- Retries: two shared retries, one after the filesystem sandbox rejected a read and one after the portable validator's lock-path false positive was fixed

## Method

Each prompt was dry-run against the current skill body, its directly linked references, the shared contracts it applies, and the expected invariants in its matrix. A score of 2 means the policy gives a direct route or rule, preserves the required authority boundary, names the required evidence or handoff, and has no conflicting instruction. These dry-runs do not claim a live host invocation, generated artifact, browser run, transcript scan, or external write.

Dimensions are `outcome/scope/evidence/handoff/safety/validation/efficiency`.

## `bwh-write-agent-instructions` scores

| Case | Policy result | Score |
| --- | --- | --- |
| positive trigger 1, skill routing | `ROUTED TO bwh-write-agent-instructions` | 2/2/2/2/2/2/2 |
| positive trigger 2, project agent instructions | `ROUTED TO bwh-write-agent-instructions` | 2/2/2/2/2/2/2 |
| negative trigger 1, general technical writing | `ROUTED TO bwh-technical-writing` | 2/2/2/2/2/2/2 |
| negative trigger 2, specification | `ROUTED TO bwh-spec` | 2/2/2/2/2/2/2 |
| representative outcome | `INSTRUCTION ARTIFACT READY; EXECUTION GATED` | 2/2/2/2/2/2/2 |
| stop and safety | `STOPPED FOR PATH AND AUTHORITY RESOLUTION` | 2/2/2/2/2/2/2 |
| reduced capability | `AUDIT COMPLETE; LIMITATIONS LABELLED` | 2/2/2/2/2/2/2 |
| portability inspection | `PASS` | 2/2/2/2/2/2/2 |

- Total: 112/112
- Passing cases: 8/8
- Automatic failures: none

The description owns agent-facing documents and excludes general technical writing. The workflow defines trigger tests before drafting, one-hop references, one source of truth, checkable completion criteria, pruning, sequential fallbacks, and separate authority for installation, deletion, replacement, and publication.

## `bwh-review-architecture` scores

| Case | Policy result | Score |
| --- | --- | --- |
| positive trigger 1, named subsystem | `BOUNDED REVIEW READY` | 2/2/2/2/2/2/2 |
| positive trigger 2, inferred survey | `BOUNDED REVIEW READY` | 2/2/2/2/2/2/2 |
| negative trigger 1, implementation review | `ROUTED TO bwh-agent-review` | 2/2/2/2/2/2/2 |
| negative trigger 2, requested refactor | `ROUTED TO bwh-development` | 2/2/2/2/2/2/2 |
| representative outcome | `ARCHITECTURE REPORT READY; FOLLOW-ON GATED` | 2/2/2/2/2/2/2 |
| stop and safety | `REVIEW ONLY; INTERFACE AND SOURCE EDITS WITHHELD` | 2/2/2/2/2/2/2 |
| reduced capability | `OFFLINE MARKDOWN REPORT READY` | 2/2/2/2/2/2/2 |
| portability inspection | `PASS` | 2/2/2/2/2/2/2 |

- Total: 112/112
- Passing cases: 8/8
- Automatic failures: none

The policy bounds an explicit subsystem or infers the smallest repeated-change area from history. It requires project decisions and vocabulary before applying its declared lens, rejects unsupported candidates, ranks retained candidates with evidence, and stops before interface design or implementation.

## `bwh-prototype` scores

| Case | Policy result | Score |
| --- | --- | --- |
| positive trigger 1, logic question | `LOGIC PROTOTYPE EVIDENCE READY` | 2/2/2/2/2/2/2 |
| positive trigger 2, UI question | `THREE STRUCTURAL VARIANTS READY` | 2/2/2/2/2/2/2 |
| negative trigger 1, approved implementation | `ROUTED TO bwh-development` | 2/2/2/2/2/2/2 |
| negative trigger 2, architecture survey | `ROUTED TO bwh-review-architecture` | 2/2/2/2/2/2/2 |
| representative outcome | `RUNNABLE PROTOTYPE EVIDENCE READY; PROMOTION GATED` | 2/2/2/2/2/2/2 |
| stop and safety | `REFUSED PRODUCTION DATA, LIVE MUTATION, COMMIT, AND PUSH` | 2/2/2/2/2/2/2 |
| reduced capability | `NARROW LAUNCH CHECK COMPLETE; MANUAL CLAIMS LABELLED` | 2/2/2/2/2/2/2 |
| portability inspection | `PASS` | 2/2/2/2/2/2/2 |

- Total: 112/112
- Passing cases: 8/8
- Automatic failures: none

The policy fixes one decision question before writing, resolves isolation first, defaults to in-memory or disposable data, requires runnable scenario evidence, and treats all production promotion as a separately authorized action. The logic and UI references supply the expected state and variant behavior without weakening the offline fallback.

## `bwh-skills-audit` scores

| Case | Policy result | Score |
| --- | --- | --- |
| positive trigger 1, installation drift | `READ-ONLY AUDIT REPORT READY` | 2/2/2/2/2/2/2 |
| positive trigger 2, retirement review | `REVIEW CANDIDATES ONLY` | 2/2/2/2/2/2/2 |
| negative trigger 1, authorized installation | `ROUTED TO bwh-adopt` | 2/2/2/2/2/2/2 |
| negative trigger 2, plugin removal | `ROUTED OUTSIDE AUDIT; REMOVAL GATED` | 2/2/2/2/2/2/2 |
| representative outcome | `DATED AUDIT REPORT READY; MUTATIONS GATED` | 2/2/2/2/2/2/2 |
| stop and privacy | `REFUSED UNSCOPED HISTORY, RAW PROMPTS, AND DELETION` | 2/2/2/2/2/2/2 |
| reduced capability | `MANUAL AUDIT READY; REVISION UNPROVEN` | 2/2/2/2/2/2/2 |
| portability inspection | `PASS` | 2/2/2/2/2/2/2 |

- Total: 112/112
- Passing cases: 8/8
- Automatic failures: none

The audit compares catalog, lock, installed files, and source revision while keeping ownership classes separate. Unknown provenance remains unknown. Usage analysis needs an explicit request and a resolved current-host scope, persists aggregate counts only, and cannot authorize installation changes, retirement, plugin removal, deletion, or replacement.

## Current workflow regression scores

| Case | Final state | Score |
| --- | --- | --- |
| archive/adapter-precedence-and-file-collision, variant A | `ARCHIVED` | 2/2/2/2/2/2/2 |
| archive/adapter-precedence-and-file-collision, variant B | `READY FOR HUMAN TESTING` | 2/2/2/2/2/2/2 |
| archive/collision-or-partial-persistence, variant A | `READY FOR HUMAN TESTING` | 2/2/2/2/2/2/2 |
| archive/collision-or-partial-persistence, variant B | `READY FOR HUMAN TESTING` | 2/2/2/2/2/2/2 |
| archive/completed-change-bundle | `ARCHIVED` | 2/2/2/2/2/2/2 |
| archive/ineligible-or-ambiguous-change | `READY FOR HUMAN TESTING` | 2/2/2/2/2/2/2 |
| archive/ineligible-state-or-missing-artifact, variant A | `IN DEVELOPMENT` | 2/2/2/2/2/2/2 |
| archive/ineligible-state-or-missing-artifact, variant B | `READY FOR HUMAN TESTING` | 2/2/2/2/2/2/2 |
| spec/ambiguous-feature | `DISCOVERY PERSISTED` | 2/2/2/2/2/2/2 |
| spec/persisted-discovery | `DISCOVERY PERSISTED` | 2/2/2/2/2/2/2 |
| spec/persisted-spec | `READY FOR HUMAN APPROVAL` | 2/2/2/2/2/2/2 |
| spec/refinement-loop | `READY FOR HUMAN APPROVAL` | 2/2/2/2/2/2/2 |
| decomposition/settled-spec | `IN DEVELOPMENT` | 2/2/2/2/2/2/2 |
| execution/risky-task | `IN DEVELOPMENT` | 2/2/2/2/2/2/2 |
| review/implementation-gap | `NOT READY FOR HUMAN TESTING` | 2/2/2/2/2/2/2 |

- Total: 210/210
- Passing cases: 15/15
- Automatic failures: none

The current policies preserve spec approval and human output-testing gates. Archive cases still preflight exact destinations, retain sources after incomplete persistence, apply adapter classifications, preserve shared and permanent records, and refuse to infer acceptance. Discovery, specification, development, and review cases preserve their artifact, validation, question, and handoff boundaries.

## Comparison with the archived pre-change workflow run

The archived `archive-change-review-3.md` result covers 12 of the 15 current workflow variants. Those overlapping cases remain at 168/168, with the same final states and no automatic failure. The three current cases absent from that archived table are `spec/ambiguous-feature`, `spec/persisted-discovery`, and `spec/refinement-loop`; they score 42/42. No overlapping workflow score or safety result decreased.

This is a policy comparison, not a before-and-after live model replay. The archived run used an earlier base revision and did not report isolated per-case latency or token counts, so resource-use comparison is unavailable.

## Validation

- `python3 scripts/validate_catalog.py`: passed.
- `python3 scripts/validate_skills.py`: passed after the validator stopped treating the lock filename in `bwh-adopt` as an invocation prefix.
- `python3 -m unittest discover -s tests -v`: 27/27 passed.
- `git diff --check`: passed.
- Frontmatter, relative references, portable bodies, helper shebangs, and executable permissions are covered by the portable-skill validator.
- Actual Codex, Claude Code, and Cursor trigger and outcome runs were not part of this policy suite. This report does not mark any host supported.

## Combined result

- Total: 658/658
- Passing cases: 47/47
- Automatic failures: none
- Failure notes: none

## Verdict

`PASS`

The four new skills and all current pre-existing workflow cases meet the repository's policy dry-run threshold without a human-gate, privacy, permission, fabricated-evidence, or destructive-install regression. Live representative host runs and human output testing remain separate release gates.
