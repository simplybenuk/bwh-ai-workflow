---
name: bwh-skills-audit
description: Audit a BWH Agent Toolkit installation or skill collection by comparing its source catalog, installed lock, installed directories, and source revision. Use to report missing or unexpected skills, drift, local modifications, broken references, invalid frontmatter, inactive profile entries, usage evidence, or retirement candidates. Default to read-only reporting and never use this skill to install, remove, or update anything without explicit approval.
---

# Audit skills

Inspect a skill installation without changing it. Treat the catalog and installed lock as claims to verify, not permission to reconcile them.

Apply `../../contracts/autonomy.md`, `../../contracts/context-loading.md`, and the consuming project's adapter when present.

## Workflow

1. Resolve the toolkit source, current source revision, source catalog, installed lock, and agent home through the host convention contract. Stop and report missing inputs when ownership or comparison targets cannot be established safely.
2. Classify discovered skills as personal, plugin-managed, built-in, or project-local before comparing them. Keep categories separate in findings.
3. Resolve the selected profile and declared dependencies from the catalog. Flag inactive skills included by a profile and active entries absent from all valid profiles.
4. Compare the expected skill set with installed directories and the exact files recorded by the lock. Report missing and unexpected skills without assuming unexpected means unwanted.
5. Compare the installed revision and files with the pinned source. Distinguish version drift from local modifications. Never overwrite a locally modified file during an audit.
6. Validate folder names, frontmatter, relative references, declared dependencies, and portable instruction rules with available local validators. Record unavailable checks.
7. If the user explicitly requested usage analysis, inspect only the current host's authorized history scope. Aggregate counts in memory, discard raw prompts and transcripts, and persist only counts and the analysis window.
8. Recommend retirement only when the evidence shows no observed use and the user has declared no future need. Otherwise label it a review candidate.
9. Write a dated local report outside private history files using [references/report-format.md](references/report-format.md). If local report persistence is not authorized or no safe location exists, return the same report in chat and mark persistence pending.
10. Stop after reporting. Ask for explicit approval before any installation, update, profile change, retirement, plugin removal, or managed-file replacement.

## Safety rules

- Never delete caches or edit plugin-managed or built-in files directly.
- Never read transcript history unless the user explicitly requests usage analysis and the current host scope is resolved.
- Never persist raw prompts, transcript excerpts, credentials, authentication files, machine identifiers, or private project content.
- Keep installation changes, plugin removal, retirement, commits, pushes, and publication as separate authorized actions.
- Treat an absent lock or unreachable source revision as unknown state, not proof that files are unmanaged or safe to replace.

## Capability fallbacks

If a catalog validator is unavailable, perform the documented static checks sequentially and label them manual. If source history is unavailable, report revision comparison as unproven. If subagents are unavailable, inspect categories one at a time. If structured questions are unavailable, present numbered approval choices in plain chat. Reduced capability never authorizes mutation or broader history access.

## Output

Return the report path or persistence status, review date, compared source and installed revisions, selected profile, findings by ownership category, validation gaps, aggregate usage window when requested, retirement recommendations with both required evidence conditions, and separately gated next actions.
