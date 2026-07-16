# Regression evals

Evaluate behavior, not prompt text. Each case should include a minimal project context, user request, expected invariants, and a scoring rubric.

Track at least:

- scope and decision correctness
- task readiness and sequencing
- duplicate detection
- appropriate assumptions versus unnecessary questions
- validation and stop-rule compliance
- independent review quality and correct human-testing handoff
- tool calls, latency, and token usage

Run the same cases before and after model, prompt, routing, or tool changes. Treat a resource reduction as an improvement only when correctness and completeness remain acceptable.
