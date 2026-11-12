# Human-steered improvement rounds

Use this contract only when a skill or request calls for iterative improvement rounds. Domain skills own their evidence methods and change constraints. This contract owns the cadence, reviewer independence, measurement integrity, and human checkpoints.

Apply [model routing](model-routing.md), [autonomy](autonomy.md), [context loading](context-loading.md), and [host conventions](host-conventions.md). The consuming project's rules remain authoritative.

## Establish the run

Read project instructions and relevant verification guidance. Inspect existing work, evidence, and branch state before changing files. Establish the bounded journeys, tasks, subsystem, or documents to improve, exclusions, environment, required checks, and what must remain correct. Ask for the target if unclear.

Ask how many independent reviewers and which agents/providers, exact models, and supported efforts the human wants, unless already specified for this run. That explicit choice authorises those models for the agreed reviews, including equal-tier or cross-family choices. Check actual availability through host tooling, reuse the team across rounds, and do not silently replace a model. Name unavailable choices and ask for an alternative while continuing independent preparation. If independent delegation is unavailable, ask whether to accept a clearly labelled single-agent assessment. A partial team is incomplete until the human changes the agreed team.

Select representative scenarios, evidence collection commands, baseline conditions, metrics, and domain review categories before implementation. Use existing project budgets and correctness checks. Propose missing targets transparently; do not present invented targets as project requirements. When a consequential target or trade-off is unresolved, ask while continuing unaffected preparation.

Prefer disposable local environments and synthetic fixtures. Production mutations, shared-service load, fault injection outside the isolated environment, paid workloads, and external publication require specific authority. Read-only existing telemetry can supplement local evidence within available permissions. Do not install dependencies or alter global tooling merely to work around a capability gap without the appropriate authority.

Keep a run index under the project's evidence convention, otherwise `.qa/runs/<skill>-<scope>/round-<n>/`. Record scope, team, human commission, revision or working diff, evidence protocol, raw artifact links, validation, suggestion dispositions, and pending work. Update after each completed phase: baseline collection/review, implementation, validation, after collection/review, awaiting human, or stopped. Preserve earlier rounds. This index is the resumption record, not a new project-wide planning requirement.

## Measurement integrity

Keep three things distinct in reports:

- Observed results in native units or explicit counts, with the method and coverage.
- Targets or budgets and pass/fail/unknown status against them.
- Reviewer judgments, optionally scored out of 10 with cited evidence and consistent anchors.

Do not turn raw measurements into subjective scores or average them together. If a project already defines an objective scoring formula, record the formula, version, inputs, direction, and fixed thresholds before comparing rounds. Retain raw values. Never tune weights or thresholds after seeing results. Tool-generated scores are derived indicators with tool/version/configuration recorded, not substitutes for measurements.

For each chosen measure, record unit, desired direction, scenario, source/command, revision, fixture and dataset size, environment/tool versions, and relevant device, cache, concurrency, or timing conditions. Set a proportionate sampling plan before the baseline. For noisy measurements, repeat under comparable conditions and retain samples, sample count, median or another justified summary, and spread. Do not cherry-pick the best attempt or manufacture confidence intervals. Mark small changes within observed variation as inconclusive; deterministic checks need no arbitrary repetitions.

Measure the same scenarios before and after. Retain failed runs and explain exclusions. Report absolute change and relative change where meaningful. With a zero baseline, percentage change is undefined; show the absolute change. Missing data is unknown, not zero or a pass. Small samples cannot establish tail percentiles or population outcomes. Distinguish lab/synthetic results from observed real-user results and describe proxies as proxies.

Preserve the denominator and scope for counts, rates, and task success. Include failures, timeouts, and correctness/resource regressions alongside speed or success improvements. If scope, tool, fixture, environment, or workload changes, mark the comparison invalid or limited and establish a new baseline. Retain the old series rather than silently rewriting it. Agree any protocol revision before measuring its new baseline.

For judgment scores, use domain-specific categories, evidence, and fixed anchors: 1-2 severe obstacles, 3-4 substantial recurring problems, 5-6 usable with clear weaknesses, 7-8 strong with specific gaps, 9-10 strong evidence across the assessed scope with little remaining friction. Use N/A with a reason for unsupported categories. An overall score is reasoned judgment, not a required mean. Never claim compliance, safety, or production readiness from reviewer agreement or a composite score alone.

For human or agent task trials, record permitted starting knowledge, assistance, and prior exposure. Use fresh matched attempts where practical; if participants repeat the task, disclose learning effects. Isolate a trial's reader/consumer from implementation knowledge when claiming unassisted completion. A synthetic attempt establishes only its observed outcome, not human comprehension, satisfaction, or team productivity.

## Review passes

Give each reviewer the same scope, rubric, raw evidence, methods, relevant code/documents, and read-only brief. Ask them to complete the job themselves, validate the measurement interpretation, cite evidence, identify uncertainty/regressions, score applicable judgment categories, and rank proposed changes by benefit, risk, and effort. Recommendations include stable IDs, affected scenario, problem, proposed change, evidence, and decisions needed.

Use fresh reviewer contexts per pass and run independent jobs in parallel when supported. Withhold peer outputs until every reviewer finishes. For after reviews, supply baseline evidence and that model's earlier assessment for comparison, with no desired score. Retain full responses, exact model identity, and evidence revision. If reviewers cannot access necessary raw artifacts or use the required driver, mark that coverage unavailable rather than inventing an assessment.

Merge duplicate recommendations while retaining attribution and disagreement. Show every reviewer's judgment scores separately from the shared measured results. Reviewers interpret the same measurements; they do not each invent their own objective result. Preserve minority objections and distinguish proposed, implemented, deferred, rejected, and blocked suggestions.

## Round 1

1. Collect baseline evidence using the recorded protocol. Obtain independent assessments and the first set of suggestions. Save the merged assessment and proposed changes before editing.
2. Make one bounded implementation pass using in-scope recommendations. The invocation authorises routine local improvements in that scope unless the user requested approval before editing. Ask before consequential product/architecture/security decisions, behavior changes outside scope, or expanded authority. Continue unaffected work when possible.
3. Run project-required checks, verify correctness and affected consumers, and collect comparable after evidence. Fix in-scope regressions. If any fix changes assessed behavior, evidence, or relevant code, refresh the affected measurements and review before claiming final results.
4. Obtain fresh independent assessments and a second set of suggestions. Present the checkpoint and stop for human input. Do not implement that second set within this round.

This is two assessment/suggestion passes and one improvement pass. Corrections required to validate that pass do not commission another round.

## Later rounds and resumption

The human can stop, select or modify suggestions, add bounded direction, or explicitly delegate prioritisation for another round. Record that steering and its exclusions. Ask if the commission leaves material choices unresolved; silence, low scores, and missed targets never commission more work.

Each later round makes one human-steered improvement pass, validates and collects evidence, obtains one fresh independent assessment and suggestion pass, then presents a checkpoint and stops. Use the previous verified after evidence as baseline when still comparable. Rebaseline only when intervening changes make it unsuitable, and explain why. Resume interrupted work from the run index and check the current revision; do not repeat completed changes or treat the previous commission as permission for a new round.

## Checkpoint, stopping, and publication

Save a round report with scope, team, revision, measured before/after results and uncertainty, targets, individual judgment scores where applicable, evidence links, changes and reasons, effects elsewhere, actual check results, and next ranked suggestions. Call out trade-offs, disagreement, blockers, and unverified claims. Present the evidence in a form the human can inspect, using screenshots, traces, query plans, task transcripts, or other domain artifacts as appropriate.

Ask the human to stop, select/adjust suggestions for another round, or provide direction. Mark the run `awaiting human` and stop implementation and review work. Agent consensus and successful metrics do not waive this required checkpoint.

On stop, log remaining suggestions with IDs, scenario, evidence, priority, proposed change, and reason for deferral using project convention or `docs/deferred-findings.md`. Keep rejected suggestions distinct. Mark the run stopped and report the log location. Stopping is not design acceptance or a claim that unresolved work is complete.

Keep artifacts local unless publication is authorised. Commit, push, PR creation, PR updates/comments, issue creation, uploads, review requests, and merge retain separate authority boundaries. Prepare reviewable material first. If authorised, reuse one draft PR and the chosen branch across rounds; never mark ready or merge without explicit authority. Keep bulky raw evidence out of feature history and use only approved, appropriately private hosting. Follow project issue policy with the necessary authority; otherwise retain issue-ready details locally.
