# Regression evals

Evaluate behavior, not prompt text. Each case should include a minimal project context, user request, expected output headings, expected invariants, and a scoring rubric. Use the rubric in `scoring.md`.

Track at least:

- scope and decision correctness
- task readiness and sequencing
- duplicate detection
- appropriate assumptions versus unnecessary questions
- validation and stop-rule compliance
- independent review quality and correct human-testing handoff
- tool calls, latency, and token usage

Run the same cases before and after model, prompt, routing, or tool changes. Treat a resource reduction as an improvement only when correctness and completeness remain acceptable.

Record the model, reasoning effort, prompt version, tool set, latency, input/output tokens, tool calls, retries, final state, score, and failure notes for every run. Compare the same cases across a baseline and one lower reasoning-effort setting before increasing effort.
