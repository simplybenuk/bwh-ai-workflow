# Review criteria contract

Apply the consuming project's guardrails and source-of-truth precedence. Review
the requested outcome and relevant risks; do not turn a bounded review into an
unrelated audit or require planning artifacts the project does not need.

## Implementation and outcome

- Check requirement coverage, edge states, failure behaviour and user-visible
  outcomes, including responsive behaviour where relevant.
- Trace affected callers, persisted data and interfaces beyond the changed
  lines. Check compatibility, permissions, tenancy, security and data integrity.
- For risky changes, require evidence from the relevant schema, migrations,
  access controls, rollout or recovery checks. Verify current database fields
  against the project's schema authority rather than generated types alone.
- Read applicable coding standards and guardrails. Check the relevant domain,
  design and dependency contracts instead of relying on the author's account.

## Validation evidence

Verify reported checks against the reviewed revision, command, result and
environment. Run focused, safe checks when evidence is missing or suspicious;
distinguish what they prove from mocked or unavailable boundaries. Missing
evidence is a gap, not proof of safety. Preserve the project's required checks
and acceptance policy.

## Findings

Classify findings as blocking, should-fix or informational. Support each with a
location or test, a concrete failure condition and its consequence. Separate
confirmed defects from missing evidence and unsupported suspicions. Consolidate
related findings; do not reproduce full logs or an exhaustive file inventory.
