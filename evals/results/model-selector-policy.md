# Model selector policy evaluation

Date: 2026-11-09

New policy evaluated in a fresh-context, read-only native subagent on `gpt-6-luna`, effort `high`. Parent was `gpt-6.1-sol`, effort `medium`. No child models were launched by the evaluator. Token and latency telemetry were not available. These are policy dry-runs, not evidence of cost savings or end-to-end task quality.

| Raw case | Observed decision | Assessment |
| --- | --- | --- |
| Sol parent; Sol low, Terra, Luna, Astra available; file evidence job | Use Luna at supported high effort and verify citations. Same-model low and peer Terra are ineligible; Astra needs permission. | Pass |
| Sonnet parent; failed Haiku extraction | Improve evidence or resolve on parent. Failure does not authorise Opus. | Pass |
| Review date 2026-11-09; task date 2027-01-08 | Warn once at exactly 60 days, recommend refresh, continue safe work. | Pass |
| Unknown parent; inherited subagent only | Work locally and disclose inability to verify a lower tier. | Pass |
| Brief summary; user forbids subagents | Summarize locally without escalation or workflow artifacts. | Pass |

The independent review reported missing routing in seven skills. Main-agent inspection found those skills already applied `contracts/model-routing.md` in their opening shared-contract instructions. The report had matched only the new Markdown link spelling. The existing references were converted to clickable links for consistency. No missing execution instruction was found in those seven files. The reviewer otherwise found the tier, permission, and freshness rules consistent.

Main-agent checks confirmed day 59, day 60, and day 61 date arithmetic. Repository tests cover selector resolution and dependencies for every profile. Catalog, skill portability, package, and skill-creator validators check structure. A disposable Git snapshot of current skills, contracts, and catalog is used for real installation and reference validation across all three hosts and all four profiles. This does not constitute live model invocation testing in those hosts.

Remaining evidence gaps: representative paired implementation/specification runs measuring cost, latency, defects, and rework; live routing in each supported host. The broader matrix in `evals/cases/toolkit/model-selector.md` is specified for future runs; only the five policy cases above were independently exercised here.
