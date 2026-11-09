# Model guidance and host mechanics

Last reviewed: 2026-11-09
Freshness warning threshold: 60 elapsed UTC days, including day 60.

This is a maintained routing policy, not a model availability registry or a universal benchmark ranking. Version numbers, token price, and effort names do not establish capability order. Runtime tools determine actual identifiers, settings, access, and concurrency limits. Use only supported combinations.

## Claude family

Source: Addy Osmani, [Which Claude model should you build with?](https://claude.dev/blog/which-claude-model-should-you-build-with/), published 2026-11-09. The user supplied the article on the review date; the source URL could not be independently retrieved. Recheck it on refresh. The guidance below is based on that supplied text.

Ascending policy tiers: Haiku 5.5 < Sonnet 5.5 < Opus 5.5 < Fable 5.2.

| Model | Suitable work | Starting effort |
| --- | --- | --- |
| Haiku 5.5 | File and log reading, extraction, classification, checkable summaries | medium |
| Sonnet 5.5 | Scoped edits, repeated investigations, ordinary document work | medium for coding; host default for documents |
| Opus 5.5 | Complex engineering, difficult debugging, long agent loops, consequential synthesis | medium, then high if justified |
| Fable 5.2 | Hard architecture, major migrations, scientific or quantitative work | medium, then high if justified |

The article recommends Opus as the normal starting main model. That recommendation does not authorise changing the current parent or breaching its ceiling. Restricted research models such as Mythos are outside this policy. Keep large reading tasks on short focused child prompts. Cache and retry costs can outweigh a lower token rate. Avoid embedding prices that will age independently of this guide.

In Claude Code, inspect the agent tool's actual model controls. Where supported, an agent definition's `model` field selects its model. Do not rely on an inherited default or an environment-wide subagent model override to enforce the ceiling. Aliases such as `haiku` or `sonnet` need runtime resolution to the ranked version; an alias alone does not prove it. Do not change the user's environment or global agent configuration.

## OpenAI family

Sources: [Models](https://learn.chatgpt.com/docs/models), retrieved 2026-11-09, and the user's supplied documentation excerpt on that date. Official task positioning supports these recommendations. The ordering below is this toolkit's conservative delegation policy, not a claim that every task has the same benchmark ordering.

Ascending policy tiers: GPT-6 Luna < {GPT-6.1 Terra, GPT-6.1 Sol} < GPT-6 Astra.

Terra and Sol share a tier because the sources position them for different strengths without establishing a strict relative capability order. Neither may autonomously delegate to the other. Earlier Sol versions and unlisted models are unranked until reviewed; do not infer order from version numbers.

| Model | Suitable work | Starting effort |
| --- | --- | --- |
| GPT-6 Luna, `gpt-6-luna` | Extraction, summaries, repeatable checks, focused coding | high |
| GPT-6.1 Terra, `gpt-6.1-terra` | Writing, visual interpretation, app interactions | runtime default |
| GPT-6.1 Sol, `gpt-6.1-sol` | Repeated complex coding, source synthesis, long tasks | runtime default |
| GPT-6 Astra, `gpt-6-astra` | Most demanding reasoning and judgment | low, called Light in some clients |

Effort is separate from model tier. Compare settings on representative tasks; a higher effort does not supply missing skills. Luna supports up to max, not ultra. Use runtime-supported values rather than copying settings between generations. Retired or absent models are not fallback choices.

In Codex, inspect the native subagent schema before selecting a model and reasoning effort. Set the model explicitly. If model overrides require fresh context, use that mode and provide a bounded brief. Do not inherit the parent and call it cheaper. For Cursor or any other host, use only model and effort controls its tools actually expose. If it cannot select and confirm a lower model, perform the work locally and report that limitation.

When a host provides a separate orchestration tool, follow its routing and capability-discovery instructions. Cross-provider delegation requires that tool when the host mandates it, plus an approved cross-family choice or ordering. Never simulate delegation through new top-level threads or direct API calls to bypass host limits.

## Refresh checklist

Verify current official provider guidance, supported host identifiers, retirements, and effort controls. Record retrieval or supplied-source status. Establish explicit relative capability evidence before ranking a new model. Leave unresolved relationships incomparable. Refresh both families before advancing this shared review date; otherwise retain the old date and record which family was checked. Check freshness against UTC calendar dates, not file modification time or the article's publication date alone.
