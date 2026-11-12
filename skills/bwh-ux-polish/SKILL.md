---
name: bwh-ux-polish
description: Polish existing UI/UX journeys or pages through independent design reviews, scored evidence, implementation, and human-steered rounds. Use for iterative UI/UX polish with a reviewer team and a human checkpoint after every round. Do not use for a read-only audit, a throwaway layout prototype, or an ordinary UI fix without design rounds.
---

# UI/UX polish

Improve an existing experience in bounded rounds. Round 1 has two scoring passes, two sets of suggestions, and one implementation pass. Every later round has one human-steered implementation pass, one scoring pass, and one new set of suggestions. End every round at a human checkpoint, even if reviewers recommend more work or scores are low.

Apply [model routing](../../contracts/model-routing.md), [autonomy](../../contracts/autonomy.md), and [host conventions](../../contracts/host-conventions.md). The user's chosen review team supplies model-selection authority for this task, including equal-tier or cross-family reviewers. Discover actual availability and follow host delegation mechanics; do not silently substitute models or invent independent reviews.

## Establish the run

Read the project's agent instructions, design-system rules, and relevant verification skills or runbooks. Inspect the current branch, worktree, existing review artifacts, and any PR before starting. Preserve unrelated work.

Resolve these inputs before starting reviews or implementation:

- Journeys or pages, actors, important states, known problems, and exclusions. If the target is unclear, ask which journeys or pages need polishing. Infer routes and code paths from the repository once the target is known.
- The number of independent design reviewers and each reviewer's agent/provider, exact model, and supported effort where applicable. Ask for this selection unless already supplied for this run. Offer available choices if useful; never treat the example prompt's team as a default. Reuse the agreed team across rounds unless the human changes it.
- Device priorities and evidence coverage. Default to mobile-first at about 390px and desktop at about 1280px unless project conventions or the user specify otherwise. Include relevant populated, empty, loading, error, and status states.
- The local QA environment, fixtures, safe external-service stubs, required checks, and artifact location. Use documented disposable data. Do not use production or shared databases or call live payment services for polish QA.

Ask only for unresolved inputs that matter. Prepare an evidence matrix while waiting on reviewer choices. If a selected model is unavailable, name it and ask for an alternative; continue independent preparation. If independent delegation is unavailable, ask whether to proceed with a clearly labelled single-agent review. Do not report that fallback as the selected team.

Record the scope, review team, rubric, evidence matrix, initial revision, publication authority, and current phase in a run index. Prefer the project's QA artifact convention, otherwise use `.qa/runs/ux-<scope>/round-<n>/`. Keep round numbers unique within the run and preserve earlier evidence.

Update the index after each completed step. Distinguish baseline capture/review, implementation, validation, after capture/review, awaiting human, and stopped. Link completed artifacts and record pending reviewers, unfinished changes, and the human steering that commissioned the current round. These markers distinguish interrupted work from permission to begin a new pass.

## Capture and review

Use the project's existing screenshot and interaction harness. Capture reproducible screen/state/viewport pairs with stable filenames, fixtures, and UI state. Record the revision, viewport, route or journey step, fixture, and any unavailable state. Reuse or add a repeatable capture script when needed.

Screenshots establish appearance. Exercise the actual journey and inspect relevant code for behavior, keyboard/focus handling, accessible names, announcements, and other claims screenshots cannot prove. Mark missing evidence as unverified. If capture or the local stack fails, report the blocker rather than substituting invented observations or silently repairing unrelated infrastructure.

Read [review and checkpoint format](references/review-format.md) before commissioning reviews. Give every reviewer the same evidence set, scope, rubric, code paths, and read-only brief. Run independent reviews in parallel when supported; keep each reviewer unaware of peer outputs until all reviews finish. Reviewers must inspect images directly for visual scores. Start fresh reviewer contexts for each scoring pass, using the same agreed models. Retain each full review and the exact evidence/revision it assessed.

Merge the reviews without hiding disagreement. Show every reviewer's category score, supporting evidence, ranked suggestions, and confidence limits. Preserve minority objections and explain the implementation choice. Scores guide the discussion; they are not acceptance gates or proof of accessibility compliance.

For measured evidence, follow [measurement integrity](../../contracts/improvement-rounds.md#measurement-integrity). Keep observed task completion, taps/steps, target dimensions, contrast checks, and automated findings separate from subjective design scores. Select measures relevant to the scope and keep their scenario/coverage fixed; screenshots alone cannot establish real-user task success. Show native units and unknown coverage rather than translating measurements into an invented objective design score. The UI-specific cadence and checkpoint format in this skill remain authoritative.

## Round 1

1. Capture the baseline into `before/`. Obtain independent baseline scores and suggestions from the agreed team.
2. Save the merged scorecard and ranked change list before editing. Choose improvements within the authorised polish scope. Routine local design changes can proceed in this first round without an extra approval gate. Ask before changes requiring a product decision or expanded authority, and continue independent in-scope work where possible. A user's request for review-only or approval before edits takes precedence.
3. Implement one pass using that list. Follow the shared-component and validation rules below. Record which suggestions were implemented, deferred, rejected, or blocked and why.
4. Capture the same evidence into `after/`. Commission fresh independent reviews of the resulting UI. Give each reviewer the baseline evidence and their model's baseline scores for comparison, but no peer reviews and no target score. Require new scores and new ranked suggestions, including regressions and unresolved findings.
5. Present the completed round using the checkpoint format. Then stop and wait for human input. Do not implement the second set of suggestions in this round.

## Later rounds

At the checkpoint, clarify which suggestions to take, reject, adjust, or defer. Human feedback can add a bounded direction or explicitly delegate prioritisation. A request for another round without a clear selection is not permission to guess at unresolved design choices; ask for the missing steering.

For each commissioned round:

1. Record the human's selected changes, constraints, and unresolved decisions against the previous suggestion IDs. Use the previous verified after-set and scores as the baseline. Recapture and re-score only if intervening code, fixtures, scope, or reviewer changes make that baseline unsuitable; disclose the comparability limit.
2. Make one implementation pass guided by that feedback, run required validation, and capture the same views again.
3. Get fresh independent scores and suggestions from the agreed team. Compare with the prior round and original baseline where comparable.
4. Present the checkpoint and stop again. Never auto-start another round because a score threshold has not been met.

Resume from the run index after a context or session change. Check the current revision against the recorded evidence before continuing. Do not repeat an already completed improvement pass or treat an old commission as approval for another round.

## Change and verification rules

Use existing components, semantic tokens, and house copy style. Put new reusable patterns in the project's design system and its showcase/catalog where one exists. Keep route-specific styles focused on layout.

Before changing a shared component or token, search its consumers. Check affected screens with screenshots or relevant layout tests, and report effects beyond the target pages. Mark app-wide design changes explicitly.

Preserve behavior unless a behavior change is explicitly in scope. Ask about consequential product decisions, security or permission changes, data rules, or specification edits. A design review does not authorise these changes. Retain tenant scoping, access controls, and privacy rules.

Run the project's required checks against the final code for every round, including relevant layout and journey checks. Record commands and actual results; label failures, skipped checks, and unavailable coverage. Fix in-scope regressions before the checkpoint. If a fix changes reviewed UI, refresh the affected evidence and review before claiming final scores. Never present scores for an older revision as scores for the final code.

## Human checkpoint and stopping

Provide before/after evidence, each reviewer's scores and deltas, implemented changes and reasons, effects elsewhere, validation results, and the next ranked suggestions. Call out disagreements and product questions. Ask the human to stop, select or modify suggestions for another round, or provide a new direction. This stop is required by this skill's human-steered design process; agent consensus cannot waive it.

If the human stops, save remaining suggestions for future consideration in the project's existing deferred-findings convention, or `docs/deferred-findings.md` if none exists. Include IDs, affected journey/state, evidence paths, proposed changes, priority, and the reason for deferral. Record rejection separately from deferral. Follow project issue policy only with the necessary remote-write authority; otherwise save issue-ready details locally. Mark the run stopped and report the log location. Stopping does not mean accepting the design or claiming the suggestions were implemented.

## Publication when authorised

Local review artifacts are sufficient unless the user authorises publication. Commit, push, PR creation, PR updates/comments, asset uploads, and review requests retain their separate authority boundaries. Do not inherit remote permissions, branch names, target branches, or service settings from an example prompt.

When authorised, keep the work on the chosen branch and reuse one draft PR across rounds. Confirm the project's integration target; never mark ready or merge without explicit authority. Prepare the scorecard and round report locally before publishing them. Include mobile-first before/after pairs, scores, change rationale, effects elsewhere, and actual check results.

Keep screenshot binaries out of feature-branch history. Use an authorised asset-hosting method or separate asset branch when needed. Check evidence for secrets and personal data before uploading; public URLs make the images public. If no approved upload method exists, retain local artifacts and explain the publication gap. Do not create issues, upload images, or post comments merely because the example workflow did so.
