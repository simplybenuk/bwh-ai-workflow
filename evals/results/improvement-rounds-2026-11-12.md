# Improvement-rounds instruction evaluation

Date: 2026-11-12.

## Scope and method

Eight new domain skills, the shared improvement-rounds contract, and the UI/UX skill's measured-evidence extension were reviewed. Two bounded `gpt-6-luna` agents at high effort drafted separate groups of domain files. The primary agent inspected all files, integrated them, and clarified clean-room trials, learning effects, local documentation drafts, and API decision boundaries.

A separate `gpt-6-luna` reviewer at high effort read the final instructions in fresh context. It performed a read-only static review and eight decision exercises without the expected answers. No application or live benchmark was executed. Token and latency telemetry were unavailable. One independent review run, no retries.

## Decision exercise outcomes

| Scenario | Observed reviewer response |
| --- | --- |
| Missing performance target and team | Ask for scope and reviewer count/exact models; continue independent preparation only. |
| Timing samples both have 100 ms median | Report inconclusive within variation and stop at checkpoint; no automatic next round. |
| API uses fewer calls but breaks supported clients | Report and address compatibility regression rather than call it a usability win. |
| Zero automated accessibility findings without manual checks | Limit result to automated scope; manual coverage unknown, no compliance claim. |
| Documentation reader used hidden implementation knowledge | Disclose contamination and require a clean-room trial for unassisted-success claims. |
| Six simulated recovery scenarios succeed | Report 6/6 in the fault matrix; do not claim production availability. |
| Human selects S2 and preserves navigation | Implement only compatible commissioned work, assess/suggest once, checkpoint again. |
| Test correction changes assessed paths after review | Refresh affected measurements and review; correction is within the existing pass. |

The independent reviewer found no substantive cross-skill contradiction in cadence, team selection, measurement integrity, or authority. These responses satisfy the static decision checks. No numeric live behavioral score is assigned.

## Validation

- All 37 repository unit tests passed.
- Catalog, portable-skill, and host-package validators passed.
- Skill-creator quick validation passed for all eight new skills and UI/UX polish using `/usr/bin/python3`, which has PyYAML. This resolves the earlier UI/UX creation session's missing-PyYAML validation gap without installing dependencies.
- Disposable pinned-source installations passed for the engineering and authoring profiles on the Codex host and full profiles on the Claude Code and Cursor hosts. Installed skill and shared-contract references validated. Temporary fixtures were removed; no real project or machine-level installations changed.
- Whitespace validation passed.

The reusable matrix is `evals/cases/toolkit/improvement-rounds.md`. It includes routing probes, authority/stop cases, and adverse measurement cases. Specifying those cases is not evidence that every case has been executed. Live capture, benchmark reproducibility, assistive-technology coverage, real-reader outcomes, real-provider review quality, and end-to-end delivery remain unverified.
