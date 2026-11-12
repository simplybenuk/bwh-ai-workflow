---
name: bwh-documentation-usability
description: Improve whether readers can use published project documentation to complete real tasks through bounded edits and iterative review. Use for documentation-usability rounds; exclude standalone audits, bug fixes, agent-instruction changes, and product-code work.
---

# Improve documentation usability

Use this skill when the user commissions iterative improvement to human-facing documentation as readers use it. Use technical writing for a straightforward documentation edit without an improvement-round commission. Use agent-instruction writing for material whose primary reader is an agent.

## Required workflow

1. Read and follow [improvement rounds](../../contracts/improvement-rounds.md) for cadence, reviewers, evidence, checkpoints, and authority.
2. Read and follow [model routing](../../contracts/model-routing.md) for toolkit model selection and delegation.
3. Read project instructions and the technical-writing guidance. Identify the published documentation set and its authoritative sources.

The shared contract owns round cadence and measurement integrity. This skill defines the reader tasks and documentation boundary.

## Bound reader tasks

1. Identify the intended audience, their starting knowledge, the published pages, and the task they need to complete.
2. Select a few representative tasks from the request, support tickets or issues, common entry paths, or stated project goals. Label inferred tasks as inferred.
3. Read the full linked path a reader would follow, including prerequisites, navigation labels, examples, and referenced downloads.
4. Record the current document revision, publication state, environment, and task denominator. State exclusions, especially code behavior, agent prompts, and unrelated content.
5. Use an independent clean-room reader who follows only the stated prerequisites and reader-visible material in scope. Supply the current version locally; do not publish to conduct a trial. Do not brief the reader with the answer or private implementation context.

If no independent clean-room reader is available, report that evidence as unavailable. A model or author attempt can reveal broken instructions but is only a proxy; it does not establish novice comprehension or real-reader outcomes.

## Collect reader evidence

For each selected task, preserve the instructions presented, starting conditions, available tools, source revision, links and commands tried, completion result, and any help or correction needed. Keep the denominator explicit: attempted, completed, failed, timed out, or excluded, with a reason for exclusions.

Where useful and feasible, record elapsed time and number of detours or clarification requests. Treat time as a task-specific observation, not a universal measure of comprehension. Do not force timing where it would distract the reader or distort the task. Verify commands, links, expected results, and referenced files against the current source. Keep failed attempts.

## Review and improve

Assess applicable categories separately and cite page sections or reader evidence:

- whether the reader can find the right starting point and prerequisites;
- whether steps are complete, ordered, and actionable;
- whether examples, terms, and expected results support the task;
- whether links, commands, and stated behavior are accurate;
- whether warnings and recovery instructions appear before they are needed;
- whether the voice and level of detail suit the stated audience.

Mark unsupported categories N/A with a reason. Keep reader task results and timings distinct from reviewer judgments. Do not convert an author or agent proxy into an objective comprehension claim.

Prefer focused edits that address an observed reader obstacle while preserving the intended audience, established voice, and source-of-truth boundaries. Verify every command, link, name, and behavioral claim against current materials. Do not alter agent instructions or expand into product code. If the underlying behavior is wrong or a product change is needed, record it as a separate suggestion for the human.

## Validate and checkpoint

1. Implement one bounded documentation pass based on commissioned suggestions.
2. Repeat the same clean-room tasks using only the revised reader-visible material and unchanged prerequisites where possible. Prefer fresh matched readers or contexts; disclose learning effects when reusing a reader. Local draft trials need no publication.
3. Compare task completion counts, failure points, help requests, and any selected timing observations. Describe reader identity only as permitted and relevant; preserve privacy.
4. Recheck all changed commands, links, expected results, and claims against current sources. Note anything that could not be verified.
5. Complete the after review and suggestion pass required by the improvement-rounds contract.
6. Present before/after reader evidence, document changes, validation limits, and ranked suggestions at the human checkpoint. Stop for direction before another round.

Keep the full task transcript or notes with the run record where appropriate. Missing reader access or data is unknown, not a pass.
