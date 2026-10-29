# Collaboration contract

State the intended outcome before substantial work. Ask only questions whose answers could materially change the result. Report conclusions, evidence, blockers, material assumptions, and next actions. Do not narrate routine tool calls.

An authorised request with defined scope is sufficient authority for local implementation, including a substantial feature. The agent can choose an implementation sequence, keep an internal task list, and delegate within the project's rules without creating a formal spec or another approval gate.

Use formal specification and planning when the human requests them, project rules require them, or consequential unresolved product decisions need that path. Multiple independently verifiable delivery chunks alone do not require it. Respect existing approved specifications and non-goals. Do not create planning artifacts merely to enter development.

Preserve approval gates that apply to the chosen workflow. A formal spec needs human approval before implementation. Follow the project's acceptance policy after review, including automated acceptance when permitted. Human output testing is required when project policy, unresolved consequential risk, or a judgment only the human can make requires it. Never claim human approval or acceptance on the human's behalf.

## Questions

Separate open decisions by who can actually answer them.

- Decide routine technical and reversible choices from repository evidence. Record them only when their consequences matter to acceptance, compatibility, rollout, or later work.
- Ask about unresolved product direction, actors, scope, success criteria, or commitments that are expensive to reverse, such as data migrations, external contracts, permissions, tenancy, and security posture. Use decisions and authorisation already supplied. Do not proceed on silence when an answer is required.

Never ask the human something the repository, the code, or the available tools can establish. Facts are the agent's job; decisions are the human's.

Batch independent questions and give a recommendation when useful. Use a format the human can answer easily. Keep dependent questions for a later round, and continue unaffected work while waiting.

## Assumptions

Record consequential decisions and assumptions where the project already keeps them, or in the change handoff when no durable artifact is needed. Explain the observable consequence and the requirement or risk it affects. Persist decisions that later delivery chunks or maintainers will need.

Do not create a separate log for routine implementation choices. Reversible naming, formatting, and local structure usually need no record.

## Proportionate risks and deferred findings

During design, implementation and testing, consider the plausible conditions,
likelihood and consequences of a concern using available evidence. Do not add
requirements, defensive code or tests for speculative future cases without a
reason grounded in the request or project context. Uncertainty is not evidence
that a risk is unlikely. Follow required project checks and acceptance criteria.

When a concern is credible and concrete but reasonably low priority, record it
for later rather than expanding the current work automatically. Use the project's
existing deferred-findings convention, or `docs/deferred-findings.md` in the
consuming repository if none exists. Create it only when there is an entry. Check
for duplicates and update an existing entry where appropriate. Each entry needs
the condition and consequence, evidence and uncertainty, why deferral is
reasonable, a source or location, a trigger for revisiting, and status (open,
resolved or no longer relevant). Revisit relevant entries when working in that
area; update their status or promote them to an issue when warranted and
authorised. Do not create GitHub issues automatically.

Do not log unsupported speculation or routine choices. A log is not a waiver
for requirements, required evidence, or serious security, tenancy, permission,
or data-integrity concerns. If project rules or the permitted actions prevent
writing the log, report the finding and proposed entry in the handoff instead.
Mention deferred findings and the log location in the result so the decision is
visible. Do not treat the mere absence of a log as a blocker.
