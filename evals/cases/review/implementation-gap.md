# Case: implementation gap

## Prompt

Review the completed implementation against the approved spec before the user tests the output.

## Expected invariants

- Compare behavior against the approved acceptance criteria, not personal preference.
- Inspect the diff, affected tests, and validation evidence.
- Identify missing states, permission or tenancy risks, regressions, and unsupported claims.
- Classify findings and stop human testing when a blocking defect exists.
- Do not silently broaden scope or rewrite unrelated code.

## Expected output headings

`verdict`, `blocking_findings`, `should_fix_findings`, `informational_findings`, `validation_evidence`, `residual_risks`, `human_test_focus`, `next_handoff`
