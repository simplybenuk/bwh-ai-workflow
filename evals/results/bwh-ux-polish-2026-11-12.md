# UI/UX polish instruction evaluation

Date: 2026-11-12.

## Scope and method

Static policy dry-run of the new skill and review-format reference. An independent `gpt-6-luna` reviewer at high effort read the artifacts in fresh context and assessed six supplied scenarios. No application, browser, external service, or real design panel was exercised. The reviewer did not read the routed shared contracts. Latency and token telemetry were not available. One review run, no retries.

## Findings

- Missing scope/team leads to questions and evidence preparation before reviews or implementation.
- Round 1 preserves two scoring/suggestion passes and one implementation pass, then stops.
- A subsequent commissioned round preserves the human's selected suggestion and navigation constraint, implements once, reviews once, and stops.
- Stopping preserves outstanding suggestions locally without implying design acceptance or remote-write authority.
- An unavailable model requires a replacement decision; failed capture cannot become invented evidence.
- A visible regression fix after review requires refreshed evidence and review before final scores.

The reviewer found no cadence contradiction. It flagged that resuming interrupted work depended on an underspecified run index. The skill now names phase markers and requires completed-artifact links, pending work, and the current human commission. This small clarification received local inspection, not another independent review.

Other observations concerned limits already inherent in the workflow: independent contexts cannot guarantee differences in model judgment, and classifying a product decision requires project context. The skill preserves disagreements and routes consequential decisions to the human.

## Validation and limits

The catalog, portable-skill, and package validators passed, as did all 37 repository unit tests. The skill-creator quick validator could not run because its interpreter lacks PyYAML. Whitespace validation passed.

The reusable case matrix is in `evals/cases/toolkit/bwh-ux-polish.md`. Those cases are specifications, not completed execution runs. No numeric behavioral score is assigned to this static review. Live screenshot reproducibility, selected-provider availability, design-review quality, and end-to-end implementation remain unverified.
