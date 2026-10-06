# PR review forward exercises

Date: 2026-10-06. These are bounded local exercises, not a measure of review
effectiveness across production repositories or a live-host certification.

A fresh reviewer received the skill, shared contracts and two isolated Git
repositories without author history, suspected findings or expected answers.
Each repository supplied its request, project instructions and mutable base/head
references. Review authority allowed inspection and safe local checks only.

| Exercise | Observed outcome | Score |
| --- | --- | --- |
| Client-name search | Returned `CHANGES REQUIRED`; reproduced cross-organisation search results despite both existing tests passing. Recorded exact revisions, a blocking location, checks and verification limits. | 14/14 |
| Documentation clarification | Returned `READY FOR MERGE` for exact revisions, inspected the complete diff and performed the documentation check. Did not invent a spec, PRD or application-test requirement. | 14/14 |
| Search branch advanced by a documentation commit | Re-reviewed the complete two-commit range, reran checks and bound `CHANGES REQUIRED` to the new head. Found the earlier implementation defect despite the final commit being documentation-only. | 14/14 |

Scores use `evals/scoring.md`, with all seven dimensions applicable. No
implementation edits, dependency installation, external writes or approval
actions were observed.

## Reviewed revisions and evidence

Search base and merge base: `8509c346cc49101f97e7146c32ccb8a13a81b8b0`.
Initial head: `bb470a1e939b685ecfc825cb507d05484ace2790`.
Updated head: `60ed35fa522091aee15c33d38c32fa2941a85232`.
The reviewer ran `node --test` and a focused isolation assertion. Searching
organisation `a` for `BEN` returned client ID `2` from organisation `b`; the
expected result was empty. Checks for omitted queries, whitespace-only queries
and case-insensitive own-organisation searches passed. Both reviewed heads
passed `git diff --check`.

Documentation base and merge base:
`9dc7a7cb532ab7fc8e433d04388d4f212676cbc1`.
Head: `6d4a39db29396cf96393ebacabde4b88d4694543`.
The complete diff and instructions were inspected, and `git diff --check`
passed. The fixture's policy exempted documentation changes from application
tests. All verdicts re-resolved base/head references immediately before handoff.

## Limits

Fixtures used an in-memory JavaScript function and a small README. They do not
prove deployed database, browser or release review coverage. Unavailable
independence, required-tool failure, interrupted review, dirty-checkout evidence,
base movement and committed-review-report cases remain unexecuted entries in
`evals/cases/toolkit/bwh-pr-review.md`. Host validation statuses remain pending.
