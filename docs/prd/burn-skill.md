# `burn` skill development plan

Status: `READY FOR HUMAN TESTING`

Approved specification: `docs/specs/burn-skill.md`

## Objective

Add the portable `burn` skill, register it in the `engineering` and `full` profiles, and cover its trigger, throughput, usage limits, refill behavior, and stop rules with repository eval cases and validation.

## Duplicate check

- The existing toolkit expansion PRD (`docs/prd/bwh-agent-toolkit-expansion.md`) covers nine other skill additions and is at `READY FOR HUMAN TESTING`; its tasks are complete.
- The catalog currently has no `burn` entry.
- Existing toolkit eval cases do not cover `burn`.
- This is a separate approved addition, so this PRD tracks it without reopening the completed toolkit expansion tasks.

## Tasks

| Task | Outcome | Dependencies | Status |
| --- | --- | --- | --- |
| B0 | Write portable `burn` skill instructions | None | COMPLETED |
| B1 | Register `burn` in catalog profiles and README | B0 | COMPLETED |
| B2 | Add trigger and outcome eval cases | B0, B1 | COMPLETED |
| B3 | Run required repository validation and prepare review handoff | B0–B2 | COMPLETED |
| B4 | Independent acceptance review | B3 | COMPLETED |

## Execution notes

- Keep the implementation within the approved spec. The primary agent owns usage-window rules, selection, integration, and stopping behavior described by the skill.
- `burn` belongs in `engineering` and `full`. Do not add it to the default `workflow` profile.
- Follow portable skill frontmatter and host-capability fallback rules.
- Do not commit or publish. Those actions require separate authorization.

## Progress and validation record

- Development started after human approval of `docs/specs/burn-skill.md`.
- Implemented `skills/burn/SKILL.md`, registered it in `engineering` and `full`, listed it in the README, and added a catalog regression assertion and `burn` policy eval cases.
- `python3 -m unittest discover -s tests -q`: 35 tests passed.
- `python3 scripts/validate_catalog.py`: passed.
- `python3 scripts/validate_skills.py`: passed.
- `python3 scripts/validate_package.py`: passed for Codex, Claude Code, and Cursor manifests.
- `git diff --check`: passed.
- Focused policy eval cases are added but have not been run by an eval harness.

## Next handoff

Run human output testing against the focus below. If testing finds more work, return this PRD to `IN DEVELOPMENT` and continue with `bwh-development`. After successful human acceptance, use `bwh-archive-change`.

## Independent review

Verdict: `READY FOR HUMAN TESTING`

### Findings

- **Blocking:** None.
- **Should-fix:** None.
- **Informational:** The policy eval fixtures are present, but no eval harness run is recorded. Automated validators check packaging and structure rather than simulating host usage telemetry or overnight wake/resume behavior.

### Review evidence

- Compared the approved spec's requirements and acceptance criteria with `skills/burn/SKILL.md`, catalog/profile registration, README description, regression assertion, and `evals/cases/toolkit/burn.md`. The implementation covers explicit triggering, estimated versus live usage, both reset windows, the 2–3% weekly target, stop reserve, bounded work selection, efficient delegation and sequential fallback, authority boundaries, and handoff reporting.
- Confirmed `burn` is registered in `engineering` and `full`, is absent from `workflow`, and is represented in the README and catalog regression test.
- Re-ran `python3 -m unittest discover -s tests -q` (35 tests passed), `python3 scripts/validate_catalog.py`, `python3 scripts/validate_skills.py`, `python3 scripts/validate_package.py` (Codex, Claude Code, and Cursor manifests), and `git diff --check`; all passed.
- Did not run policy evals: the repository contains case fixtures and a scoring rubric but no recorded executable harness for this eval set.

### Residual risk

The generic skill cannot itself guarantee that a host exposes trustworthy usage counters, timers, or resumable overnight execution. It specifies conservative fallbacks, but the host-specific capabilities and actual interruption behavior have not been demonstrated by these repository checks.

### Human output-testing focus

- Confirm the skill triggers only for an explicit request to spend expiring usage, and that ordinary improvement requests follow the normal workflow.
- With supplied estimates and with live host readings if available, check that the agent distinguishes sources, monitors weekly and rolling five-hour windows, and stops at the weekly 2–3% target or the earlier safety reserve.
- Exercise a five-hour refill and verify the agent only waits/resumes when the host can monitor it, leaves no delegated work running during the wait, and stops all work before the weekly reset.
- Confirm the skill selects useful project-grounded work, delegates only independent work when that improves throughput, and leaves external writes, commits, publication, and deployment behind their existing authorization gates.
- Verify installation through `engineering` and `full`; confirm the default `workflow` profile does not install `burn`.

Successful human output testing hands the accepted change to `bwh-archive-change`; findings that require code or instruction changes return it to `bwh-development`.
