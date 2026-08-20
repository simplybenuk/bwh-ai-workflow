# Architecture review report format

Use Markdown. Omit empty sections.

```markdown
# Architecture review: <bounded area>

## Scope and lens

<Survey boundary, why it was selected, architecture decisions and vocabulary read, and validation limits.>

## Ranked candidates

### 1. <candidate>

- Affected files: <paths or symbols>
- Observed cost: <maintenance, comprehension, testing, or locality evidence>
- Proposed direction: <structural direction without interface design>
- Evidence: <repository citations>
- Confidence: <high, medium, or low, with reason>
- Architecture decision conflicts: <none or named conflict>
- Cheapest useful verification: <check before committing to a spec>

## Top recommendation

<Candidate, why it ranks first, and what would disprove the recommendation.>

## Deferred or rejected ideas

<Ideas that lacked evidence or near-term pressure.>

## Next handoff

<bwh-ideate or bwh-spec after user selection.>
```
