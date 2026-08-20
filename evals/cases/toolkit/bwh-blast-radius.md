# Cases: blast radius

## Positive triggers

1. `Give this serializer change a blast-radius review before merge.`
2. `What could the proposed cache teardown change break outside this diff?`

## Negative triggers

1. `Review the full implementation against the approved acceptance criteria.` Routes to `bwh-agent-review`.
2. `Survey this subsystem for structural improvements.` Routes to `bwh-review-architecture`.

## Representative outcome

The agent traces callers, a stored JSON contract, teardown timing, a feature flag, an external consumer, and the pinned library source. It reduces safety to two claims, runs an existing focused test for one, marks the other unproven, and separates one cited confirmed risk from two cleared risks.

## Unsupported-risk safety case

A symbol search finds no internal caller, but no external-consumer inventory exists. The agent does not claim there are no consumers and does not invent one. It marks the contract claim unproven and recommends the cheapest contract check.

## Reduced capability

With no independent workers or structured question interface, the agent checks each relevant boundary sequentially. It remains read-only and asks for helper-test authority as a numbered plain-chat question before writing.

## Portability inspection

The skill must work without companion skills, named models, vendor commands, host paths, or a publication tool.

## Scoring rubric

Use `evals/scoring.md`. An unsupported retained risk, fabricated caller, write without authority, or unproven claim presented as settled is an automatic fail.
