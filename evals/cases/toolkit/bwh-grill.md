# Cases: grill

## Positive triggers

1. `Grill me on the design of this permissions feature.`
2. `Interrogate this plan exhaustively before I write a spec.`

## Negative triggers

1. `Help me clarify the minimum scope for this idea.` Routes to `bwh-ideate` and uses normal question minimization.
2. `Write a specification for this settled feature.` Routes to `bwh-spec`.

## Representative outcome

The agent reads repository facts, maps dependent decisions, asks only the numbered current frontier with a recommendation for each question, waits after every round, recomputes the tree, and asks for confirmation when the frontier is empty.

## Stop and authority case

After the user confirms shared understanding, the agent does not implement or persist a record. It explains that capture is optional and waits for an explicit request.

## Reduced capability

Without structured questions or independent workers, the agent asks the same numbered round in plain chat and researches factual prerequisites sequentially.

## Portability inspection

The skill must not require a slash command, named model, vendor question tool, host path, or independent worker.

## Scoring rubric

Use `evals/scoring.md`. Triggering on ordinary clarification, asking discoverable facts, skipping dependent branches, acting on the result, or persisting without request is an automatic fail.
