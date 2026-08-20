# Host conventions contract

The BWH Agent Toolkit keeps shared skill behavior independent of any agent host. Host packaging, install paths, instruction files, and invocation forms belong in this routed contract or a host manifest.

## Host resolution

Resolve the host from repository evidence in this order:

1. An explicit host named by the user or recorded in `<agent-home>/bwh-ai-workflow.lock`.
2. An existing agent home in the project.
3. An existing project agent instruction file.
4. A host-specific plugin manifest in the toolkit source.
5. If the evidence is absent or ambiguous, ask rather than guessing.

A project may host more than one agent. Treat each host as a separate install target with its own agent home and lock. Never move or remove another host's installation by implication.

## Per-host mapping

| Host | Agent home | Project agent instruction file | Plugin manifest | Explicit skill invocation |
| --- | --- | --- | --- | --- |
| Claude Code | `.claude/` | `CLAUDE.md` | `.claude-plugin/plugin.json` | `/bwh-<skill>` |
| Codex | `.agents/` | `AGENTS.md` | `.codex-plugin/plugin.json` | `$bwh-<skill>` |
| Cursor | `.cursor/` | `AGENTS.md` or a project rule selected by the user | `.cursor-plugin/plugin.json` | `/bwh-<skill>` |
| Other or unknown | ask | ask | none | host default |

For Cursor, prefer an existing `AGENTS.md`. If only project rules exist, ask which rule owns toolkit pointers before editing one. Do not invent a rule filename.

## Layout invariants

- Skills live in `<agent-home>/skills/<skill-name>/`.
- Contracts live in `<agent-home>/contracts/`, so `../../contracts/<name>.md` resolves from an installed skill.
- The lock lives at `<agent-home>/bwh-ai-workflow.lock`.
- Project adapters and context maps live at project-documented locations outside the agent home.
- A project install defaults to the `workflow` profile.
- A machine-level plugin install exposes the `full` profile from the package's `skills/` directory.

Refer to the instruction file as "the project agent instruction file" in portable output. Refer to other skills by bare name. Keep the paths and invocation forms in this contract out of portable skill bodies, shared templates, and project artifacts except where the adapter records the resolved host and install layout.
