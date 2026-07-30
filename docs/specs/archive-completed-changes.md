# Archive completed change documentation

Status: READY FOR HUMAN TESTING

Approval evidence: Human approval provided in conversation on 2026-07-29.

## Problem

The workflow ends at human output testing. It does not define how the temporary documents used to discover, specify, plan, execute, review, and validate a change leave their active locations after the delivered change has been accepted. Archiving only the change spec would leave the rest of the completed change context mixed with active work.

## Desired outcome

Provide an explicit, human-authorized archival stage that collects all relevant temporary change documents into one traceable archive bundle while leaving permanent and shared source-of-truth documents in their authoritative locations.

## Actors

- A human who accepts delivered behavior after output testing and requests archival.
- An agent that inventories, classifies, and archives the completed change documentation.
- A consuming project whose adapter defines active artifact and archive conventions.

## Goals

- Add a reusable `bwh-archive-change` skill.
- Make change archival the final workflow stage after successful human output testing.
- Define `ARCHIVED` as a persisted terminal workflow state.
- Archive all relevant standalone temporary documents used to produce and validate the change.
- Produce a manifest that preserves original paths, final paths, artifact roles, acceptance evidence, and dispositions.
- Add active-artifact and change-archive settings to project scaffolding.
- Preserve links and shared planning traceability when documents move.
- Cover incomplete inventories, unsafe candidates, path conflicts, premature archival, and successful bundle archival with regression evals.

## Non-goals

- Automatically infer that human testing passed.
- Move permanent source-of-truth documents such as ADRs, architecture, product requirements, schema, domain rules, runbooks, or shipped-feature documentation.
- Move shared multi-change planning documents, backlogs, or PRDs wholesale.
- Archive source code, tests, commits, pull requests, or external records.
- Delete the historical record of the completed change.
- Define retention periods or external document storage.
- Backfill existing completed changes during workflow adoption.

## Artifact classification

The archive skill must classify every candidate before changing files.

### Archive as part of the change bundle

When they are standalone files scoped to the completed change:

- discovery or ideation brief;
- change specification and readiness bundle;
- dedicated PRD, task plan, or decomposition artifact;
- implementation progress or execution log;
- agent-review artifact;
- repository-persisted human output-testing evidence;
- rollout, validation, or recovery checklist created only for the change;
- other temporary change artifacts explicitly identified by the project adapter.

### Keep in place and update safely

- a shared PRD, backlog, task database, progress index, or review index containing other changes;
- an archive index required by the adapter;
- permanent project documentation updated by the delivered change;
- any source-of-truth file whose authority would be weakened by moving it.

For a shared document, update only the completed change's status and archive reference when its schema and project rules make that safe. Never move or duplicate the entire shared document into the bundle.

### Exclude

- source code, tests, generated build output, dependencies, and unrelated notes;
- external records that the available tools cannot archive safely;
- any document whose relationship to the change cannot be established from repository evidence or explicit human direction.

Ambiguous candidates must be listed for human resolution. The archive operation must stop before moving any artifacts when an unresolved candidate could cause loss of active or authoritative documentation.

## Requirements

### R1: Archive skill

Create `skills/bwh-archive-change/SKILL.md` with a trigger that covers requests to complete, close, or archive an accepted delivered change and its supporting documentation.

The skill must:

1. Read the change spec, consuming-project adapter, context map, relevant planning/progress/review evidence, and only the source-of-truth files needed to resolve status, artifact ownership, and paths.
2. Require both:
   - the current persisted change state is `READY FOR HUMAN TESTING`; and
   - the human has explicitly confirmed that output testing passed or explicitly accepted the delivered change.
3. Refuse to infer human acceptance from agent review, passing automated tests, inactivity, merged code, or implementation completion.
4. Build an evidence-backed artifact inventory before moving anything. For every candidate, record its role, current path, whether it is standalone or shared, the evidence linking it to the change, and the proposed disposition.
5. Apply the artifact-classification rules above plus any stricter project adapter rules.
6. Stop for human input if a candidate's ownership or disposition is materially ambiguous, or if a required change artifact is missing.
7. Resolve the archive destination and bundle naming from the adapter or established repository conventions.
8. Use `docs/archive/changes/<change-slug>/` only when neither source defines a destination and repository guardrails allow it.
9. Detect destination-directory and per-file collisions before persisting anything. Stop without overwrite unless project evidence defines a safe identical-artifact resolution.
10. Create an archive manifest in the bundle that records:
    - change identifier and title;
    - final `ARCHIVED` state;
    - archival date;
    - human acceptance evidence supplied in the current request or a referenced project artifact;
    - every inventoried artifact's role, original path, final path or kept-in-place path, and disposition;
    - relevant implementation, validation, review, and human-testing references;
    - unresolved external references or intentionally excluded artifacts.
11. Set the archived change spec status to `ARCHIVED` and add its former path, bundle path, acceptance evidence, and manifest reference.
12. Persist every archive-bound artifact and the manifest without replacing unrelated content.
13. Read and validate the entire destination bundle before removing any original artifact.
14. Update authoritative shared planning/progress/index references that would otherwise point to moved paths or show the change as active. Update only the completed change's entry.
15. Remove original standalone temporary artifacts only after all archive-bound copies and required reference updates have been persisted and verified.
16. Read the final bundle, manifest, and updated shared references back before reporting success.

### R2: State contract

Add `ARCHIVED` to `contracts/states.md` as the terminal state for a human-accepted change whose temporary documentation bundle has been archived.

Allow:

```text
READY FOR HUMAN TESTING -> ARCHIVED  (human acceptance and archive validation required)
READY FOR HUMAN TESTING -> IN DEVELOPMENT  (human testing found more work)
```

No agent may make the transition to `ARCHIVED` without explicit human acceptance. The transition describes the overall change; individual supporting documents do not need independent workflow states.

### R3: Workflow and handoffs

Update the documented workflow to:

```text
bwh-ideate -> bwh-spec -> bwh-refine-spec (repeat) -> bwh-development -> bwh-agent-review -> human output testing -> bwh-archive-change
```

Update `bwh-agent-review` so a ready verdict tells the human that successful output testing can hand off to `bwh-archive-change`, while failed human testing returns work to `bwh-development`.

The archive skill handoff must lead with the archive bundle and manifest paths, report the previous and final states, summarize moved and kept-in-place artifacts, report validation, and identify any external or excluded references.

### R4: Project scaffolding

Update `templates/project-adapter.md` to include:

- active discovery, spec, dedicated planning, progress, review, and human-test artifact locations and formats;
- completed change archive location and bundle-naming format;
- project-specific temporary-artifact classification rules;
- shared planning/index completion-update rules;
- archive manifest and index requirements.

Update `templates/project-context.md` and the template context map so agents can distinguish:

- active temporary change artifacts;
- archived change bundles;
- shared planning artifacts that stay in place;
- permanent source-of-truth documents that must not be archived.

### R5: Adoption and upgrades

Keep `skills/bwh-*` wildcard installation behavior so the new skill is installed automatically.

Update `bwh-adopt` validation and upgrade guidance so:

- new adapters include archive location, classification, manifest, and shared-reference settings;
- existing project adapters and context maps are preserved;
- missing archive settings in an existing adapter are reported as migration actions rather than silently invented;
- existing completed changes and their documentation are not moved automatically.

Update installation examples and the available-skill list to include `bwh-archive-change`.

### R6: Regression evals

Add archival eval cases that verify:

- archival succeeds only after explicit human acceptance and from `READY FOR HUMAN TESTING`;
- discovery, spec, dedicated planning, progress, review, and human-test artifacts are discovered when evidence links them to the change;
- shared multi-change planning documents remain in place and only the completed change's entry is updated;
- permanent source-of-truth documents remain in place;
- ambiguous or missing required artifacts stop the operation before any move;
- the adapter-defined archive path and classification rules win over fallbacks;
- fallback bundle naming is deterministic;
- bundle or file collisions stop safely;
- the manifest contains the full inventory, dispositions, acceptance evidence, and traceability metadata;
- all archive-bound artifacts are persisted and verified before originals are removed;
- failed partial persistence leaves original artifacts intact and reports any partial destination;
- the concise handoff points to the authoritative bundle and manifest.

## Proposed design

`bwh-archive-change` is a separate skill because archival has a distinct trigger, human authorization boundary, multi-file move risk, and terminal handoff. It must not be folded into agent review, which occurs before the human gate and cannot attest that human testing passed.

The unit of archival is a change bundle rather than a single spec. The consuming project remains authoritative for bundle paths and naming. The reusable fallback is:

```text
docs/archive/changes/<change-slug>/
  manifest.md
  discovery/
  spec/
  planning/
  progress/
  review/
  testing/
  supporting/
```

Only directories needed for inventoried artifacts are created. Original filenames are retained unless the adapter requires another naming convention. The manifest is the authoritative inventory and maps every original path to its archived or kept-in-place disposition.

The archive operation is ordered to reduce data-loss and partial-archive risk:

1. Validate state and human acceptance.
2. Inventory and classify all relevant artifacts.
3. Resolve the bundle path and preflight every collision.
4. Prepare archive copies, terminal spec metadata, and manifest.
5. Persist all archive-bound artifacts and the manifest without overwrite.
6. Read and validate the complete bundle.
7. Update and verify shared planning and index references.
8. Remove the original standalone temporary artifacts.
9. Read back the terminal state and produce the handoff.

If persistence or validation fails, leave all originals in place. A partial destination must be reported and must not be presented as an archived change. If the available tools cannot safely complete the operation, stop before removing originals and provide the smallest manual action.

## Affected areas

- `skills/bwh-archive-change/`
- `skills/bwh-agent-review/SKILL.md`
- `skills/bwh-adopt/SKILL.md`
- `contracts/states.md`
- `templates/project-adapter.md`
- `templates/project-context.md`
- `adapters/_template/context-map.md`
- `README.md`
- `evals/cases/archive/`
- potentially `evals/README.md` if archive coverage needs to be named explicitly

## Security, safety, and data integrity

- Human acceptance is a hard authorization boundary.
- Archive destinations must remain within the consuming repository unless its adapter explicitly authorizes another connected system.
- Existing destination files must never be overwritten by default.
- Every original must remain intact until the complete bundle and required shared-reference updates have been persisted and verified.
- Shared and permanent source-of-truth documents must not be moved.
- The agent must preserve unrelated local changes and avoid broad search-and-replace operations.
- Archive metadata must cite acceptance evidence without inventing a person, timestamp, test result, artifact relationship, or approval record.
- Sensitive-data and retention rules in the project adapter apply equally to archived copies.

## Rollout and compatibility

- The change is additive for new installations.
- Existing installations receive the new skill and state contract through the normal pinned update.
- Existing adapters remain valid for other workflow stages. Archival uses established conventions or the documented fallback only when artifact classification is unambiguous.
- `bwh-adopt` reports new adapter fields as recommended migration items and does not rewrite project-owned adapters or context maps.
- No existing change documentation is moved during installation or update.

## Proposed task outline

1. Add the archive state and lifecycle transitions to the shared state contract.
2. Extend adapter and context scaffolding with temporary-artifact classification, bundle, manifest, and shared-reference conventions.
3. Initialize `bwh-archive-change` using the repository skill convention and implement inventory, classification, safe bundle persistence, verification, and handoff.
4. Update agent-review, adopter guidance, workflow documentation, installation examples, and skill inventory.
5. Add successful, ambiguous, shared-document, collision, and partial-failure archival regression cases.
6. Validate skill frontmatter, contract references, documentation consistency, archive safety invariants, and existing human gates.

## Dependencies and sequencing

- Artifact classes and adapter fields must be settled before finalizing the archive skill instructions.
- The state transition must be settled before finalizing the archive manifest and handoff.
- Documentation and eval wording must use the same completion boundary, artifact classes, and fallback bundle path as the skill.
- No external services or new runtime dependencies are required.

## Acceptance criteria

- A consuming project can invoke `bwh-archive-change` after explicitly accepting behavior in `READY FOR HUMAN TESTING`.
- The skill inventories all evidence-linked temporary change documents before moving anything.
- Standalone discovery, spec, dedicated planning, progress, review, testing, and supporting artifacts are placed in one verified bundle when present.
- Shared multi-change planning documents and permanent source-of-truth documents remain in place.
- The manifest records every candidate and whether it was moved, updated in place, kept unchanged, excluded, or unresolved.
- The skill stops without moving originals when acceptance is absent, state is ineligible, required artifacts are missing, classification is materially ambiguous, a destination collides, or complete safe persistence cannot be verified.
- Adapter-defined archive and classification conventions take precedence; otherwise `docs/archive/changes/<change-slug>/` and the specified default classes are used.
- Shared authoritative references are updated only for the completed change and verified after bundle persistence.
- Originals are removed only after the complete archive bundle and required shared-reference changes have been verified.
- The shared workflow, state contract, templates, adopter guidance, installation examples, and skill inventory consistently describe change-bundle archival.
- Existing adapters, context maps, and completed change documents are not silently rewritten during adoption or upgrade.
- Regression evals cover successful and refused archival behavior, including partial-persistence safety.
- Skill metadata and all referenced contracts validate successfully.

## Validation plan

- Run the skill-creator `quick_validate.py` against `skills/bwh-archive-change`.
- Check every `skills/bwh-*` frontmatter block and every referenced shared contract.
- Search workflow docs, templates, states, and skill handoffs for inconsistent terminal-state, artifact-classification, or archive-path wording.
- Execute or manually score the archive eval cases against `evals/scoring.md`.
- Exercise a fixture with standalone artifacts plus a shared backlog and permanent ADR, verifying only the correct files move.
- Exercise collision, ambiguous-ownership, missing-artifact, and partial-persistence fixtures, verifying originals remain intact.
- Run existing ideation, spec, development, and review cases to confirm both human gates remain intact.
- Inspect the final diff for accidental changes to project-specific adapters or unrelated files.

## Risks and mitigations

- **Incomplete archive:** Require an evidence-backed inventory and manifest.
- **Moving authoritative documentation:** Classify shared and permanent sources separately and keep them in place.
- **Premature closure:** Require current state plus explicit human acceptance.
- **Data loss during multi-file move:** Persist and validate the complete bundle before removing any original.
- **Partial archive:** Keep originals, report partial destinations, and withhold `ARCHIVED`.
- **Broken traceability:** Map original and final paths in the manifest and update only authoritative references.
- **Name collision:** Preflight the whole bundle and stop without overwrite.
- **Adapter drift:** Preserve existing adapters and report new fields as migration actions.
- **State ambiguity:** Define one terminal `ARCHIVED` state rather than separate `COMPLETED` and `ARCHIVED` states.

## Confirmed decisions

- Completed changes require an archive workflow.
- The change includes a new skill and updates to the shared workflow and project scaffolding.
- Archival covers all relevant temporary documents used to produce the change, not only the change spec.

## Decisions changed by refinement

- Rename the proposed skill from `bwh-archive-spec` to `bwh-archive-change`.
- Replace single-spec archival with a manifest-backed change bundle.
- Include evidence-linked discovery, dedicated planning, progress, review, testing, and supporting documents.
- Replace the fallback `docs/specs/archive/<filename>` with `docs/archive/changes/<change-slug>/`.
- Treat shared planning and permanent source-of-truth documents as in-place records rather than archive-move candidates.

## Proposed decisions for approval

- Human output testing remains the final human gate.
- `ARCHIVED` is the single terminal state.
- The manifest is the authoritative inventory for the archived change.
- Only standalone change-scoped files move; shared and permanent documents stay in place.
- Materially ambiguous artifact ownership blocks archival rather than being guessed.

## Assumptions

- “Completed” means the human explicitly accepted the delivered change after output testing.
- “Relevant temporary documents” means standalone, change-scoped workflow artifacts supported by repository evidence, explicit human direction, or adapter rules.
- The archive skill belongs in this repository under `skills/bwh-archive-change`.
- Repository-persisted human-testing evidence is archived when present; acceptance stated only in chat is recorded in the manifest without fabricating a separate evidence file.
- Shared documents are updated only when their schema and adapter rules make a change-specific update safe.

## Open questions

- None blocking. Projects may optionally require an archive index or additional artifact classes through their adapter.

## Implementation record

- Development task status: completed on 2026-07-30.
- Material changes: added `bwh-archive-change`, the terminal `ARCHIVED` state, post-testing workflow handoffs, archive-aware adapter/context scaffolding, adopter migration rules, plugin documentation, and focused archive eval cases.
- Validation: all seven `bwh-*` skills passed `quick_validate.py`; all shared contract references resolved; plugin JSON parsed; no archive scaffold TODOs remained; fallback paths, skill names, and terminal-state wording were consistent; `git diff --check` passed.
- Commit status: changes remain uncommitted.
- Next handoff: `bwh-agent-review` before human output testing.

## Agent review record

- Review date: 2026-07-30.
- Verdict: `NOT READY FOR HUMAN TESTING`.
- Blocking coverage gaps: archive evals do not exercise an ineligible persisted state or a missing required artifact.
- Blocking validation gap: no scored archive eval runs, fixture exercises, existing-workflow regression runs, or model/tool/score records are persisted.
- Verified evidence: all seven `bwh-*` skills passed `quick_validate.py`; contract references resolved; plugin JSON parsed; `git diff --check` passed; new-file trailing-whitespace and terminology/path consistency checks passed.
- Next handoff: return to `bwh-development`, close the two refusal-coverage gaps, run and record the behavioral validation suite, then repeat `bwh-agent-review`.

## Development remediation cycle 1

- Added `evals/cases/archive/ineligible-state-or-missing-artifact.md` with separate ineligible-state and missing-spec variants.
- Added case-specific automatic-fail rubrics to every archive eval.
- Revalidated all seven skills, plugin JSON, diff whitespace, and required archive-case sections successfully.
- Behavioral archive evals, representative existing-workflow regressions, and execution metadata must be persisted during the next independent review before a ready verdict.
- Next handoff: repeat `bwh-agent-review`.

## Agent review record 2

- Review date: 2026-07-30.
- Verdict: `NOT READY FOR HUMAN TESTING`.
- Blocking gaps: no adapter-classification precedence eval, no per-file destination-collision eval, and no explicit permanent source-of-truth must-remain rule in the template context map.
- Validation: 10/10 policy dry-runs scored 140/140 with no automatic failures; all static checks passed.
- Eval evidence: `evals/results/archive-change-review-2.md`.
- Residual risk: Markdown policy dry-runs do not prove filesystem failure recovery.
- Next handoff: return to `bwh-development`, close the three gaps, then repeat `bwh-agent-review`.

## Development remediation cycle 2

- Added `evals/cases/archive/adapter-precedence-and-file-collision.md` with adapter override and exact destination-file collision variants.
- Added the explicit permanent source-of-truth must-remain rule to `adapters/_template/context-map.md`.
- Revalidated all skills, shared contract references, plugin JSON, diff whitespace, and required archive-case sections successfully.
- Next handoff: repeat `bwh-agent-review` with refreshed archive and regression scoring.

## Agent review record 3

- Review date: 2026-07-30.
- Verdict and state: `READY FOR HUMAN TESTING`.
- Eval evidence: 12/12 archive and representative regression dry-runs passed with 168/168 points and no automatic failures; details in `evals/results/archive-change-review-3.md`.
- Review-2 closure: adapter classification precedence, exact per-file collision handling, and the permanent source-of-truth context-map rule are all present and exercised.
- Static validation: all seven skills passed `quick_validate.py`; shared contract references resolved; plugin JSON parsed; `git diff --check` passed; the project-specific Wolds Record adapter remained unchanged.
- Residual risk: Markdown policy dry-runs do not prove filesystem failure recovery under injected partial writes.
- Human testing focus: verify one successful adapter-defined bundle and one refused collision or partial-persistence path, including manifest completeness, source retention, and state handling.
- Next handoff: human output testing; success hands the accepted change to `bwh-archive-change`, while failure returns it to `bwh-development`.
