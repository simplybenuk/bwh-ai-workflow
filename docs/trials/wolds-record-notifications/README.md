# Wolds Record paired workflow trial

The trial compares delivery of the same notifications feature from identical
Wolds code, using the original toolkit and the simpler candidate. It includes
live owner-consent and veterinary-declaration receipt notifications.

## Pinned inputs

| Input | Original run | Simpler run |
| --- | --- | --- |
| Checkout | `/home/ben/projects/wolds-record/feature-notifications-trial-original` | `/home/ben/projects/wolds-record/feature-notifications-trial-simpler` |
| Branch | `feature/notifications-trial-original` | `feature/notifications-trial-simpler` |
| Wolds code baseline | `5353a474eaa9dd7f616c911614e91e8f3d44796e` | Same |
| Toolkit source | `/home/ben/projects/bwh-ai-workflow` | `/home/ben/projects/bwh-ai-workflow-simpler` |
| Toolkit revision | `039c6b2d814578927db60a191ddf4d97e34c095b` | Candidate commit recorded by its installed lock after preparation |
| Host/profile | Codex, `full`, 20 skills | Same |
| Product input | [Shared brief](brief.md) | Identical bytes |
| Trial instructions | [Shared protocol](protocol.md) | Identical bytes |

The original toolkit is the candidate branch's parent, so the treatment is the
reviewed instruction change. Wolds previously had an older toolkit installed;
both trial checkouts receive the same full profile from this paired source.
The original run is therefore this pinned parent, rather than a reproduction
of every historical Wolds setup detail.

Both checkouts preserve the committed Wolds spec-skill addendum in
`docs/agents/bwh-spec-project-addendum.md`, linked from the project adapter.
This separates project wiring from managed toolkit files. Both also have the
same trial-specific planning-policy exception, allowing their installed
toolkit to determine the planning route. Other project guardrails and checks
remain binding. The machine-level Claude installation is outside this Codex
trial and is not updated.

## Preparation and launch

1. Review and authorise a local commit of the completed simpler-toolkit work.
   The installer requires a clean source checkout at an exact commit.
2. Dry-run and install that source into the simpler Wolds checkout. Verify both
   locks, managed-file hashes, common preparation files and unchanged app code.
   Record the exact candidate revision and input hashes in the local evaluator
   manifest at
   `/home/ben/projects/wolds-record/tools/notifications-workflow-trial/preparation.json`,
   outside the toolkit source checkout.
3. Prepare equivalent dependencies and verify an idle, disposable local test
   environment using the Wolds runbooks. Do not copy production credentials or
   reset the shared stack as part of preparation. Establish the pinned migration
   history separately before each run; unresolved ownership blocks DB testing.
4. Open a fresh thread in the original checkout and paste
   [the original launch handoff](launch-original.md). Use the same model,
   reasoning setting, tools and reviewer conditions for both threads.
5. After the first run and its cleanup, open a fresh thread in the simpler
   checkout and paste [the simpler launch handoff](launch-simpler.md). Keep the
   first implementation and its findings out of that thread.
6. Evaluate both against the same brief and checks using
   [the results template](results-template.md). Retain both outputs before
   selecting work for any later integration.

Supply identical product answers to both runs when a shared missing decision
is discovered. Record workflow-specific approval pauses separately. If a
material change to the brief is necessary after one run begins, record the
protocol deviation and bring both runs to the same final requirements before
comparing them. Required approvals cannot be inferred from elapsed time.

Do not launch the trials while the candidate commit, installation or environment
is still pending. Toolkit validators and fixture tests establish structural
validity. They do not establish which workflow delivers this feature better.

## Comparison

Required behaviour, security, evidence and cleanup come first. A faster run
with missing receipt events, weakened access checks or unrun required tests
has not completed the task. Compare elapsed active time, waiting time, actual
usage where available, human interventions, planning artifacts, material review
defects and rework only alongside those outcomes. Separate common environment
setup and outages from delivery time.

One paired feature is useful evidence for adoption. It cannot establish that
either workflow is better for every kind of work. No winner is selected here.
