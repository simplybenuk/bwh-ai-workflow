# Case: implementation gap

## Prompt

Review the completed implementation against the approved spec before the user tests the output.

## Expected invariants

- Compare behavior against the approved acceptance criteria, not personal preference.
- Inspect the diff, affected tests, and validation evidence.
- Identify missing states, permission or tenancy risks, regressions, and unsupported claims.
- Classify findings and stop human testing when a blocking defect exists.
- Do not silently broaden scope or rewrite unrelated code.
- Consolidate related findings and omit empty categories and exhaustive evidence lists.

## Expected output

One verdict sentence and no more than six short bullets covering actionable findings, validation, material residual risk, human test focus when ready, a review artifact when one exists, and the next handoff state.
