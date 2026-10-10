# Notifications workflow trial

Deliver the accompanying `brief.md` in this checkout using its project-installed
BWH workflow. The brief defines the authorised product scope. Choose the
architecture and implementation sequence from current project evidence.

## Workflow and authority

Read `.agents/bwh-ai-workflow.lock` and use the skills in `.agents/skills/`,
with their referenced local contracts. Start with the local `bwh-development`
skill; use local planning skills if that workflow requires them. Machine-level
copies and another checkout's skills are not this run's workflow.

For this trial, the installed toolkit decides when formal specification, PRD
decomposition and spec approval are required. This replaces the execution-scope
rule in `docs/agents/workflow.md` that requires planning merely because delivery
has multiple chunks. It also takes precedence over generic planning-pipeline
descriptions in project documents for this new feature. Preserve approved
domain specifications, source-of-truth locks, tenancy, permissions, migration
rules, design-system rules, required validation and project acceptance policy.

If the assigned workflow requires a formal spec, author it using the project's
conventions and request its approval before implementation. The product brief
does not approve a technical spec that has not yet been written. Agents may
create feature planning artifacts required by their assigned workflow; this
permission does not unlock durable reference specifications.

Use the model and reasoning setting selected at launch throughout the run.
Use the same setting for any implementation or independent review agents. This
trial setting takes precedence over model-routing suggestions. Delegate within
the assigned workflow and project rules. A fresh independent reviewer receives
the brief, relevant project instructions, final implementation and raw evidence.
Do not provide the implementer's rationale or conclusions as review findings.

Local implementation, tests, planning and owned disposable test fixtures are
authorised. Commits, pushes, pull requests, review comments, merges, releases,
production changes and shared-database resets require separate explicit
authorisation. Keep the final work uncommitted unless that authority arrives.

## Context and execution

Work only in the assigned checkout. Do not read the other trial, previous
notifications implementation, its spec or review, or other branches' versions
of this feature. Do not search all Git refs for an existing solution. Existing
source and applicable references at this checkout's pinned baseline are valid
context. The evaluator keeps prior work separately.

You may read the evaluator's preparation manifest at
`/home/ben/projects/wolds-record/tools/notifications-workflow-trial/preparation.json`
to verify revision pins and setup metadata. It contains no implementation
results. This permission does not extend to another run's source or findings.
Before beginning delivery, require its status to be `ready_for_launch` and both
toolkit revisions to be recorded. Otherwise report preparation incomplete.

Run the trials sequentially. Check the QA lease and other active tasks before
database-dependent work. Follow the repository's ownership and cleanup
runbooks. A shared stack with another run's migrations or data is not a clean
baseline. If the required database state cannot be established safely, report
the blocker and continue independent work. Do not reset a shared stack to
remove it. Required checks remain incomplete until they actually run.

Ask about missing consequential product decisions. Routine implementation
choices are the agent's responsibility. The evaluator will give both runs the
same answer to a shared product question. Do not relax the brief or required
checks to improve speed.

Complete the feature, required verification and independent review. Address
material review findings and recheck affected work. Follow project acceptance
policy, including actual human testing when required. Finish with the result,
evidence, remaining requirements and material decisions. Do not automatically
archive the change or start a retrospective.

## Measurement

Record the model, reasoning setting, toolkit revision, start/end times, checks
and review evidence in the final handoff or existing required project records.
Report human questions, approvals, material rework and any evidence limitations.
Use actual harness usage figures when available; mark unavailable figures
instead of estimating them. The evaluator records planning artifacts and total
human effort outside this checkout. Measurement should not create a new
workflow of its own.
