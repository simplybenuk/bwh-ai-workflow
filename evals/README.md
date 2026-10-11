# Regression evals

Evaluate behaviour, not prompt text. Each case should include minimal project context, a user request, expected outcomes and invariants, and a scoring rubric. Require output headings only when a project format or actual consumer needs them. Use the rubric in `scoring.md`.

Track at least:

- scope and decision correctness
- task readiness and sequencing
- duplicate detection
- appropriate assumptions versus unnecessary questions
- validation and stop-rule compliance
- independent review quality and compliance with the project's acceptance policy
- complete, human-authorized archival with safe artifact classification and source preservation
- tool calls, latency, and token usage

Run the same cases before and after model, prompt, routing, or tool changes. Treat a resource reduction as an improvement only when correctness and completeness remain acceptable.

Record the model, reasoning effort, prompt version, tool set, latency, input/output tokens, tool calls, retries, final state, score, and failure notes for every run. Compare the same cases across a baseline and one lower reasoning-effort setting before increasing effort.

The request-driven cases in `cases/execution/` use the small SQLite project in
`cases/execution/fixtures/records/`. Copy it to a disposable directory for each
run and provide only the case's prompt and raw project context to the worker.
Keep expected outcomes and scoring notes with the evaluator. Establish a local
Git baseline when evaluating implementation diffs. Do not install the toolkit
globally or use production resources.

For a paired workflow comparison, keep the task, fixture revision, model,
reasoning effort, tools, and review conditions identical. Change only the skill
and contract revision. Record artifacts created, human interventions, review
defects, and rework alongside time and usage. A completed implementation run
and its fresh review provide behavioural evidence. Reading the instructions and
predicting outcomes is only a static policy dry-run; label it accordingly and
do not report it as proof of delivery performance.
