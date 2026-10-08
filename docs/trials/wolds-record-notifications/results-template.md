# Notifications paired trial results

Evaluator-only record. Do not give either implementation thread the other run's
answers, architecture, code, findings or results.

## Inputs and protocol

| Input | Original | Simpler |
| --- | --- | --- |
| Wolds baseline | | |
| Toolkit commit | | |
| Shared brief/protocol SHA-256 | | |
| Preparation manifest and source diff | | |
| Model/reasoning/tools/reviewer | | |
| Dependency and database baseline | | |
| Thread/run and order | | |
| Product clarifications or protocol deviations | | |

## Completion evidence

Record evidence paths and failures, not just a pass label. A security,
permission, fabricated-evidence or required-approval violation fails the run.
An unavailable required check leaves verification incomplete.

| Required outcome/check | Original | Simpler |
| --- | --- | --- |
| Header/account/navigation/sign-out | | |
| Announcements, severity, dismissal and failures | | |
| Real owner and vet receipts, idempotency and persistence | | |
| Issuer recipient, tenant/access boundaries and revoked membership | | |
| Unread/read-state behaviour and failure handling | | |
| Accessibility, layout, zoom and print | | |
| Impersonation, identity changes, refresh and races | | |
| Typecheck/lint/build/tests/coverage | | |
| Layout and production-build browser journeys | | |
| Migration/database checks and disposable-fixture cleanup | | |
| Independent review and material defects resolved | | |
| Project acceptance and remaining human requirements | | |
| Final status and evidence limitations | | |

## Effort and rework

Use measured usage when exposed by the harness. Leave unavailable metrics
explicitly unavailable. Exclude common setup artifacts from the count of
workflow-created artifacts. Separate setup, active delivery, human wait and
environment-blocked time.

| Measure | Original | Simpler |
| --- | --- | --- |
| Start/end and active/wait/blocked time | | |
| Input/output tokens or exposed usage | | |
| Tool calls and retries, if exposed | | |
| Human product questions and workflow approvals | | |
| Human review/testing time | | |
| Planning/progress/state artifacts created | | |
| Material independent-review findings | | |
| Rework and repeated validation | | |

## Decision

State which outcomes are proved, unresolved defects and whether the comparison
was controlled. Explain the adoption choice against completed behaviour and
human effort. Keep the original and simpler feature outputs available for any
later integration. Commit, publication and merge remain separate actions.
