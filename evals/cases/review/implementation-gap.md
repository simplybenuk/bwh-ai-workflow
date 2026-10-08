# Case: implementation gap

## Prompt

Review the completed implementation against the approved spec before the user tests the output.

## Expected invariants

- Use a fresh reviewer separate from the implementer. Report an incomplete review if independence or necessary evidence is unavailable.
- Compare behavior against the approved acceptance criteria, not personal preference.
- Inspect the diff, affected tests, and validation evidence.
- Identify missing states, permission or tenancy risks, regressions, and unsupported claims.
- Classify findings and stop human testing when a blocking defect exists.
- Do not silently broaden scope or rewrite unrelated code.
- Consolidate related findings and omit empty categories and exhaustive evidence lists.

## Expected output

A concise verdict with actionable findings, validation, material residual risk, and the next action under the project's human-testing policy. An applicable review artifact or state is included without inventing one for every change.
