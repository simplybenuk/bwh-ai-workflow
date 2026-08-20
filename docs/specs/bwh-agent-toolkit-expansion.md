# BWH Agent Toolkit expansion specification

Status: `APPROVED FOR DEVELOPMENT`

## Summary

Expand `bwh-ai-workflow` into the BWH Agent Toolkit while preserving its repository and package identifier. Add nine agent-independent skills, explicit install profiles, source provenance, Cursor packaging, safe migration for existing installations, and portable validation across Codex, Claude Code, and Cursor.

The public display name becomes `BWH Agent Toolkit`. The repository URL, package name, marketplace identifier, and lock-file family remain `bwh-ai-workflow`.

## Problem

The repository already distributes a reusable delivery workflow across Codex and Claude Code, but it cannot yet act as a complete portable skill collection:

- The adopter defines the package through the `skills/bwh-*` glob rather than a catalog.
- Project installation cannot select a focused group of skills.
- The manifests and documentation describe only spec-driven delivery.
- Cursor has no package manifest or explicit host mapping.
- Third-party-derived skills have no repository-level provenance or update policy.
- The current eval suite covers workflow behavior but not skill triggering, portability, profile installation, or host-specific leakage.

## Actors

- The toolkit owner curates skills, upstream sources, profiles, and releases.
- A project maintainer installs or updates the workflow profile without receiving unrelated skills.
- A user setting up a machine installs the complete toolkit from one pinned repository source.
- An agent host discovers portable skill instructions through its own package manifest and invocation conventions.
- A future maintainer reviews upstream changes against recorded BWH adaptations.

## Goals

- Make one repository the source of truth for the BWH workflow and personal engineering skills.
- Preserve agent-independent skill behavior while supporting Codex, Claude Code, and Cursor packaging.
- Add all nine approved skills in the first toolkit specification.
- Keep existing workflow behavior, state gates, adapters, and project authority intact.
- Let project adoption select a profile and record the exact managed files.
- Make third-party origin, revision, license, and BWH changes inspectable.
- Validate triggering, outcomes, safety, and portability before calling a host supported.

## Non-goals

- Installing either reviewed upstream catalog wholesale.
- Renaming the GitHub repository or package identifier.
- Making every new skill part of the default BWH delivery sequence.
- Guaranteeing support for an untested agent host.
- Storing raw conversation history, credentials, machine configuration, or private project data in the repository.
- Treating prototype code as approved production implementation.
- Treating one architecture philosophy as a project-wide mandate.
- Removing or disabling unrelated plugins on the user's machines.

## Confirmed decisions

- Include all nine active additions in this specification.
- Use `BWH Agent Toolkit` as the public display name.
- Keep `bwh-ai-workflow` as the repository, package, marketplace, and lock identifier.
- Keep one repository with catalogued profiles rather than several repositories or plugin packages.
- Default project-local adoption to `workflow`.
- Treat a machine-level plugin installation as the `full` toolkit.
- Support Codex, Claude Code, and Cursor once their representative evals pass.
- Adapt upstream skills. Do not copy vendor paths, tools, frontmatter, model choices, or publication assumptions unchanged.

## Proposed design

### Repository catalog

Add `catalog.json` as the machine-readable source of truth. JSON avoids introducing a YAML parser into validation and installation scripts.

The catalog must contain:

- schema version;
- toolkit identifier and display name;
- each skill's name, directory, status, profiles, dependencies, and whether it needs shared contracts;
- upstream repository, path, pinned revision, license, and attribution when derived from another project;
- a short list of material BWH adaptations;
- profile membership;
- supported hosts and their validation status.

Allowed skill statuses are `active`, `pilot`, and `retired`. Only active skills may appear in an install profile. Pilot skills remain in the repository but are not installed by a default profile. Retired skills remain in source history and are absent from the active catalog.

The catalog schema version starts at `1`. Validation rejects duplicate skill names, missing directories, unknown dependencies, cycles, unknown profiles, active skills without profiles, and upstream-derived skills without provenance.

### Profiles

Define these profiles:

- `workflow`: `bwh-adopt`, `bwh-archive-change`, `bwh-ask`, `bwh-ideate`, `bwh-spec`, `bwh-refine-spec`, `bwh-development`, and `bwh-agent-review`.
- `engineering`: `bwh-diagnose-bugs`, `bwh-blast-radius`, `bwh-create-verification`, `bwh-review-architecture`, and `bwh-prototype`.
- `authoring`: `bwh-technical-writing`, `bwh-grill`, `bwh-write-agent-instructions`, and `bwh-skills-audit`.
- `full`: the union of `workflow`, `engineering`, and `authoring`.

Keep `bwh-domain-modeling` and `bwh-resolve-merge-conflicts` out of this release. They remain candidates for later pilot work and do not appear as active catalog entries.

### Installation and updates

Update `bwh-adopt` to use the catalog rather than `skills/bwh-*`.

For project scope:

- Default to the `workflow` profile.
- Allow the user to request another named profile.
- Resolve the host through the host convention contract.
- Copy the selected skills, their declared dependencies, and required contracts.
- Preserve unrelated skills and project-owned files.
- Detect local changes to managed files before replacement.
- Remove a previously managed skill only when the new catalog or profile excludes it, the recorded installed revision proves it was managed, and the target has no local edits.

For machine scope:

- Prefer the host's plugin installation mechanism.
- Treat the root plugin package as the `full` profile.
- Document manual pinned installation for hosts without plugin support.
- Do not copy user history or configuration into the repository or installation.

Replace the current free-form lock with lock format version `2`. Preserve compatibility with existing locks by migrating them during the first successful update. The lock must record:

- format version;
- source and pinned revision;
- installation date;
- host and install scope;
- selected profile;
- exact installed skill names;
- installed contract paths;
- catalog schema version.

Do not rewrite a version `1` lock until the associated update has copied and validated successfully.

### Agent-independent skill rules

Every portable `SKILL.md` must:

- use only `name` and `description` in shared frontmatter;
- keep all trigger conditions in the description;
- refer to other skills by bare name;
- use relative paths for bundled resources;
- use generic terms such as "project agent instruction file" and "agent home";
- describe required capabilities rather than vendor tool names;
- provide a sequential fallback when subagents are unavailable;
- provide a plain-chat fallback when structured questions are unavailable;
- keep model selection and reasoning settings outside the skill body;
- avoid host-specific paths and invocation prefixes;
- state authority boundaries for external writes, destructive actions, commits, pushes, and publication.

Host-specific metadata may live in plugin manifests, marketplace files, host contracts, or explicitly named host metadata directories. Portability validation excludes those routed paths and rejects host-specific strings elsewhere.

### Host packaging

- Update the Codex and Claude Code manifests to display `BWH Agent Toolkit` while retaining `bwh-ai-workflow` as the identifier.
- Add a Cursor plugin manifest with the same identifier, version, repository, license, and skills directory.
- Extend the host convention contract with Cursor's agent home, instruction file, manifest, and invocation form.
- Keep unknown hosts on the existing explicit-resolution path.
- Update marketplace descriptions and the root README to describe the toolkit and profiles.

A manifest being syntactically valid is not enough to call its host supported. Support requires a recorded representative trigger and outcome eval on that host.

## Skill requirements

### `bwh-diagnose-bugs`

Adapt the diagnosis loop from Matt Pocock's `diagnosing-bugs` skill.

Requirements:

- Build a repeatable signal for the reported symptom before settling on a cause.
- Reproduce and minimize the failure when feasible.
- Form several falsifiable hypotheses and test one variable at a time.
- Prefer targeted instrumentation and remove it before completion.
- Add a regression test at a seam that represents the real failure when such a seam exists.
- Verify the original symptom after the fix.
- Redact secrets from commands, logs, traces, and captured artifacts.
- Diagnose without implementing when the user asks only for diagnosis.
- Stop and report the missing access or artifact when no credible feedback loop can be built.

Do not preserve a rigid demand for a seconds-long loop when the project's only valid repro is an integration or browser path. Require the tightest credible loop, and state its cost and limitations.

### `bwh-blast-radius`

Adapt pstack's `blast-radius` skill.

Requirements:

- Inspect the change, callers, data contracts, timing, external consumers, configuration, and pinned dependency behavior relevant to the change.
- Identify the smallest set of safety claims on which the change depends.
- Prove important safety claims by running real code when feasible.
- Distinguish confirmed risks, cleared risks, and unproven claims.
- Cite repository evidence for every retained risk.
- Recommend the cheapest check that would catch the material failure before merge.
- Work without requiring `how`, `why`, `arena`, or a named model.
- Remain read-only unless the user separately authorizes a test or helper artifact.

### `bwh-create-verification`

Adapt pstack's `create-verification-skill`.

Requirements:

- Inspect how the project's primary user-facing system starts, accepts input, exposes state, isolates instances, and shuts down.
- Resolve the target agent home through the host contract.
- Generate a project-local `verify-<app>` skill with launch, doctor, drive, evidence, and cleanup instructions.
- Seed a small feature map grounded in actual routes, commands, menus, or documentation.
- Prefer an existing browser, CLI, API, or test driver before inventing a new one.
- Verify one mapped feature end to end before calling the generated skill complete.
- Preserve evidence during cleanup and terminate only processes started by the verification run.
- Avoid production mutations. Use a documented disposable or dry-run environment where user-visible behavior would otherwise write externally.

The generated skill follows the target host's path conventions. The portable generator must not hard-code `.cursor`, `.claude`, or `.agents`.

### `bwh-technical-writing`

Adapt pstack's `technical-writing` skill.

Requirements:

- Choose the document's purpose before drafting: tutorial, how-to, reference, or explanation.
- Use repository vocabulary, real paths, symbols, flags, and commands.
- Keep instructions direct, sequenced, and testable.
- State expected results where a reader must verify a step.
- Keep reference content factual and separate it from procedures when the distinction matters.
- Apply plain-language and anti-slop rules without forcing uniform sentence length or removing useful technical terms.
- Cover READMEs, runbooks, ADRs, specifications, PR descriptions, and commit messages.
- Avoid duplicating `bwh-write-agent-instructions`, which owns documents whose primary reader is an agent.

### `bwh-grill`

Adapt Matt Pocock's `grill-me` and `grilling` behavior as an explicit mode.

Requirements:

- Trigger only when the user explicitly asks to be grilled, interrogated, or exhaustively questioned.
- Map dependent decisions as a tree and ask only the current frontier in each round.
- Number questions and provide a recommended answer for each.
- Establish discoverable facts through repository or tool evidence rather than asking the user.
- Recompute the frontier after every answer until no branch remains.
- Wait for the user's confirmation that shared understanding has been reached.
- Do not act on the result.
- On request, persist a concise decision record and hand it to `bwh-ideate`, `bwh-spec`, or `bwh-refine-spec`.

Unlike normal BWH questioning, this explicit mode may return reversible technical decisions to the human. That behavior applies only for the duration of the requested grilling session.

### `bwh-write-agent-instructions`

Adapt Matt Pocock's `writing-for-agents` concepts.

Requirements:

- Cover skills, shared contracts, adapters, project agent instruction files, and documents reached through pointers.
- Treat trigger wording as part of the behavior being designed.
- Distinguish always-loaded instruction cost from the human cost of remembering explicit skills.
- Keep ordered steps prominent and move branch-specific reference material behind direct pointers.
- Require checkable completion criteria for procedural steps.
- Preserve one source of truth for each rule.
- Remove cached facts that an agent can cheaply read from the environment.
- Identify stale, duplicated, irrelevant, and behaviorally inert instructions.
- Evaluate positive triggers, negative triggers, missed triggers, and representative outcomes.
- Keep host-specific invocation mechanics in routed host references rather than the portable skill.

### `bwh-review-architecture`

Adapt Matt Pocock's `improve-codebase-architecture` and required design references.

Requirements:

- Accept an explicit subsystem or infer a bounded survey area from recent change history.
- Read project architecture decisions and domain vocabulary before judging structure.
- Inspect observed maintenance, comprehension, testing, or change-locality costs.
- Use module depth, interface size, seam placement, dependency classification, deletion tests, and test locality as one declared review lens.
- Permit the project's authoritative vocabulary even when it differs from the imported lens.
- Produce an evidence-backed Markdown report with ranked candidates, affected files, observed cost, proposed direction, confidence, ADR conflicts, and the reason for the top recommendation.
- Use a diagram only when it clarifies a relationship.
- Reject speculative refactors with no observed cost or plausible near-term change pressure.
- Stop before interface design or implementation.
- Route a selected candidate to `bwh-ideate` or `bwh-spec`.

Parallel readers and an HTML rendering are optional host capabilities. The default report must work offline and without a browser or CDN.

### `bwh-prototype`

Adapt Matt Pocock's `prototype`, `LOGIC.md`, and `UI.md` workflows.

Requirements:

- State one decision question before building.
- Choose a logic prototype for state, data shape, or transition questions.
- Choose a UI prototype for layout, hierarchy, or interaction questions.
- Use an isolated temporary directory or worktree unless the project adapter defines a safe prototype location.
- Keep data in memory by default and use disposable dependencies when persistence is the question.
- Make the prototype trivial for the intended reviewer to run.
- Expose relevant state and provide representative scenarios.
- For UI work, create structurally distinct variants rather than cosmetic variants.
- Verify that the prototype runs and can demonstrate the stated question.
- Capture observations, conclusion, unresolved uncertainty, and the affected discovery or specification decision.
- Treat the code as evidence, not approved implementation.
- Require separate authorization to copy code into production, commit, push, or publish it.

Do not require production-grade tests for throwaway code. Do require a repeatable launch check and evidence that the prototype answers its named question.

### `bwh-skills-audit`

Create a BWH-owned audit skill informed by pstack's `automate-me` idea and this repository's catalog.

Requirements:

- Compare the source catalog, installed lock, installed skill directories, and current source revision.
- Report missing skills, unexpected skills, version drift, local modifications, broken references, invalid frontmatter, and inactive profile entries.
- Separate personal skills, plugin-managed skills, built-in skills, and project-local skills.
- Never delete caches or edit plugin-managed files directly.
- Default to read-only reporting.
- Require explicit user approval before installation, update, profile change, retirement, or plugin removal.
- Make usage analysis optional and scoped to the current host.
- When usage analysis is requested, emit aggregate counts only and never persist raw prompts or transcripts.
- Recommend retirement only when there is both no observed use and no declared future need.
- Record review date and recommendation in a local report, not in private history files.

## Provenance and licensing

Add `THIRD_PARTY_NOTICES.md` and catalog provenance for every derived skill.

Initial sources:

- Matt Pocock `skills`, commit `885e2ca4d842d139e9aef4e48d366c63cb1b8013`, MIT license.
- Cursor `plugins/pstack`, commit `60c641e4fad674784b30abcf9f8915dea39df38d`, MIT license.

The notice must name each upstream path used. The catalog must record material adaptations. Upstream updates require a diff from the recorded revision and a review of triggers, host assumptions, authority boundaries, references, and eval behavior before changing the pinned revision.

## Security and privacy

- Do not include credentials, authentication files, machine identifiers, project names from private history, or raw conversation content in the repository.
- Treat transcript access as private and optional. `bwh-skills-audit` may process it only for aggregate local analysis after an explicit request.
- Redact secrets from diagnosis and verification evidence.
- Keep prototypes and verification runs away from production data and external mutations unless the user authorizes a disposable environment designed for that purpose.
- Do not load remote scripts or CDN assets in required validation paths.
- Do not overwrite locally modified managed skills without showing the conflict and obtaining a replace, merge, or skip decision.
- Keep commit, push, pull-request creation, publication, and plugin removal as separately authorized actions.

## Rollout and compatibility

Release the toolkit expansion as version `0.2.0` after all required tasks pass review.

Rollout order:

1. Add the catalog, validator, provenance, and profile definitions without changing installed behavior.
2. Migrate `bwh-adopt` and lock handling while preserving the workflow default.
3. Update host manifests and add Cursor packaging.
4. Add the nine skills in independently reviewable tasks.
5. Run existing workflow evals and new trigger, outcome, safety, profile, and portability evals.
6. Update README installation and migration instructions.
7. Publish only after human output testing confirms an existing workflow update and a fresh full installation.

Existing version `1` locks remain readable. Existing project installations receive the `workflow` profile unless their recorded files or user request establish a broader selection. The migration must not infer that an existing project wants `full`.

Rollback consists of reinstalling the previously pinned revision and restoring its lock. No project adapter, source-of-truth document, specification, PRD, or local skill may be deleted during rollback.

## Validation plan

### Static validation

- Parse every shared skill frontmatter and require exactly `name` and `description`.
- Confirm folder names match skill names.
- Resolve every relative file reference.
- Validate the catalog schema, profiles, dependencies, provenance, and source paths.
- Reject host-specific paths, invocation syntax, vendor tool names, and model names from portable skill bodies, with explicit allowlists for host packaging and cited upstream provenance.
- Check plugin and marketplace manifests for valid JSON and consistent identifier, version, repository, display name, and skills path.
- Check executable helpers for declared interpreters and executable permissions.
- Run `git diff --check`.

### Installer validation

- Dry-run fresh project installation of `workflow` for each supported host layout.
- Dry-run requested `engineering`, `authoring`, and `full` profiles.
- Migrate a version `1` lock to version `2` after a successful fixture update.
- Preserve an unrelated local skill.
- Detect and preserve a locally modified managed skill.
- Remove an unmodified formerly managed skill only after the fixture profile drops it.
- Prove failed copy or validation leaves the old lock and installed files recoverable.

### Skill evals

Each new skill needs:

- at least two positive trigger cases;
- at least two negative trigger cases, including its closest overlapping BWH skill;
- one representative successful outcome case;
- one stop or safety case;
- one no-subagent or reduced-capability case;
- one portability inspection case.

Specific required distinctions:

- `bwh-grill` must not replace normal BWH question minimization.
- `bwh-technical-writing` must not trigger for agent instruction design owned by `bwh-write-agent-instructions`.
- `bwh-review-architecture` must not behave like post-implementation `bwh-agent-review`.
- `bwh-prototype` must not treat prototype output as approved development.
- `bwh-blast-radius` must not invent risks unsupported by repository evidence.
- `bwh-skills-audit` must not expose raw prompts or mutate installations during a review.

### Regression and host validation

- Run all existing workflow evals before and after the change.
- Record model, reasoning effort, prompt version, tool set, latency, tokens, calls, retries, result, and score using the existing eval convention.
- Treat any human-gate, privacy, permission, fabricated-evidence, or destructive-install violation as an automatic failure.
- Record one representative trigger and outcome run on Codex, Claude Code, and Cursor before marking each host supported.
- Do not lower existing workflow correctness or safety scores to gain portability or reduce tokens.

## Acceptance criteria

- **AC1:** All package and marketplace identifiers remain `bwh-ai-workflow`, while every public display name and current description identifies `BWH Agent Toolkit`.
- **AC2:** `catalog.json` validates and lists every active existing and new skill, all four profiles, dependencies, statuses, and required provenance.
- **AC3:** Project adoption defaults to `workflow`, accepts another named profile, installs its exact resolved skill set, and records it in a version `2` lock.
- **AC4:** A version `1` workflow installation updates without receiving engineering or authoring skills unless requested.
- **AC5:** A machine-level plugin installation exposes the complete active toolkit from one pinned repository revision.
- **AC6:** Codex, Claude Code, and Cursor manifests resolve the same portable `skills/` source and pass their packaging checks.
- **AC7:** All nine named skills exist, have only portable shared frontmatter, resolve every reference, and meet their individual requirements.
- **AC8:** Every upstream-derived skill records repository, path, pinned revision, license, attribution, and material adaptations.
- **AC9:** Portable skill bodies pass the host-leakage check and still provide fallbacks for unavailable optional capabilities.
- **AC10:** Existing BWH workflow evals pass with no human-gate or safety regression.
- **AC11:** Every new skill passes its positive, negative, outcome, stop, reduced-capability, and portability cases at the repository's pass threshold.
- **AC12:** Installer fixtures prove preservation of unrelated and locally modified skills, recoverable failure, and correct profile pruning.
- **AC13:** No repository artifact contains raw transcripts, secrets, authentication data, or private machine configuration.
- **AC14:** The README documents full machine setup, project workflow adoption, profile selection, supported hosts, pinned updates, provenance, and rollback.
- **AC15:** Human output testing completes one fresh `full` installation and one update of an existing workflow-only project before release.

## Agent-resolved assumptions

- **A1, catalog format:** Use JSON to avoid a new parser dependency. Verify through AC2 and the static catalog test.
- **A2, release version:** Use `0.2.0` because the package keeps backward-compatible identifiers and adds substantial capability. Verify through manifest consistency checks in AC1 and AC6.
- **A3, install defaults:** Project scope defaults to `workflow`; plugin or machine scope means `full`. Verify through AC3, AC4, and AC5.
- **A4, architecture output:** Use Markdown as the required report format and make HTML optional. Verify through the reduced-capability architecture eval in AC11.
- **A5, prototype isolation:** Use an OS temporary directory or isolated worktree unless the adapter defines a safe location. Verify through the prototype safety eval in AC11 and privacy requirement AC13.
- **A6, host support:** Package all three hosts in this release, but label a host supported only after its recorded eval passes. Verify through AC6 and AC11.
- **A7, imported names:** Prefix adapted skills with `bwh-` to avoid collisions and make ownership clear. Verify through AC2 and AC7.
- **A8, pilots:** Defer domain modeling and merge-conflict resolution rather than expanding this release beyond the nine confirmed additions. Verify through the active catalog in AC2.

## Risks and mitigations

- **False triggering:** Nine descriptions add routing competition. Keep descriptions narrow and enforce negative trigger fixtures.
- **Context cost:** More model-invoked metadata consumes context. Keep descriptions concise, use explicit triggers for `bwh-grill`, and measure representative prompt size and behavior.
- **Workflow conflict:** Imported skills may bypass approval or action boundaries. Apply BWH autonomy and human-gate contracts and add automatic-fail safety cases.
- **Installation damage:** Profile changes could remove local work. Record exact managed skills, compare against the installed revision, preserve local edits, and update locks last.
- **Host drift:** Agent package formats may change independently. Keep behavior in portable skills, isolate packaging, and require host validation per release.
- **Upstream drift:** Later imports may restore removed vendor assumptions. Pin revisions and require an adaptation diff before updates.
- **Prototype leakage:** Throwaway routes or data could reach production. Default to isolated storage and require separate authority for promotion or publication.
- **Architecture churn:** A survey could recommend fashionable but unnecessary restructuring. Require observed costs, ADR review, ranked confidence, and a stop before implementation.
- **Privacy leakage:** Usage auditing could capture sensitive prompts. Make history analysis opt-in, aggregate in memory, and prohibit raw persistence.

## Proposed task outline

### P0: Add catalog, provenance, and validation base

Create `catalog.json`, its validator, profile definitions, and `THIRD_PARTY_NOTICES.md`. Register existing workflow skills first without changing install behavior.

Verification: catalog tests cover valid data, duplicate names, missing paths, unknown dependencies, cycles, invalid profile membership, and incomplete provenance.

### P1: Make adoption profile-aware

Update `bwh-adopt`, host contracts, templates, lock format, and fixture coverage. Support version `1` lock migration and exact managed-file tracking.

Depends on: P0.

Verification: installer fixtures satisfy AC3, AC4, and AC12.

### P2: Rebrand packaging and add Cursor

Update the public display name and descriptions, preserve identifiers, add Cursor packaging, and extend host documentation.

Depends on: P0.

Verification: manifest consistency, path resolution, and host packaging checks satisfy AC1 and AC6.

### P3: Add `bwh-diagnose-bugs`

Adapt the pinned upstream diagnosis workflow and add trigger, outcome, stop, redaction, and reduced-capability evals.

Depends on: P0.

### P4: Add `bwh-blast-radius`

Adapt the pinned pstack workflow without its routing dependencies. Add proof-level and unsupported-risk evals.

Depends on: P0.

### P5: Add `bwh-create-verification`

Adapt project-local verification generation through the host contract. Add a fixture project and one end-to-end generated-skill check.

Depends on: P0 and P1.

### P6: Add `bwh-technical-writing`

Adapt the technical writing standard, keep it distinct from agent instruction authoring, and add document-mode fixtures.

Depends on: P0.

### P7: Add `bwh-grill`

Implement the explicit design-tree interview and its handoff without changing default BWH collaboration behavior.

Depends on: P0.

### P8: Add `bwh-write-agent-instructions`

Adapt context-pointer, hierarchy, completion, pruning, and behavioral-eval guidance into portable instructions and references.

Depends on: P0.

### P9: Add `bwh-review-architecture`

Adapt the architecture survey and design references, use Markdown output, and hand selected candidates to ideation or specification.

Depends on: P0 and P8.

### P10: Add `bwh-prototype`

Adapt logic and UI prototype branches with isolation, evidence capture, and production-promotion guards.

Depends on: P0 and P1.

### P11: Add `bwh-skills-audit`

Build the catalog and lock audit workflow, optional aggregate usage analysis, and mutation approval boundary.

Depends on: P0 and P1.

### P12: Complete integration, regression, and documentation

Run the full catalog, profile, skill, regression, privacy, and host validation matrix. Update README setup, migration, provenance, supported-host, and rollback guidance. Prepare the human output-testing checklist.

Depends on: P2 through P11.

Verification: AC1 through AC15 have evidence or an explicitly assigned human test.

## Task dependency summary

```text
P0 -> P1 -> P5
         -> P10
         -> P11
P0 -> P2
P0 -> P3
P0 -> P4
P0 -> P6
P0 -> P7
P0 -> P8 -> P9
P2..P11 -> P12
```

## Affected areas

- `README.md`
- `.codex-plugin/`
- `.claude-plugin/`
- new `.cursor-plugin/`
- `.agents/plugins/marketplace.json`
- `.claude-plugin/marketplace.json`
- `catalog.json`
- `THIRD_PARTY_NOTICES.md`
- `contracts/host-conventions.md`
- `contracts/context-loading.md` if portable pointer rules require a direct reference
- `skills/bwh-adopt/`
- nine new directories under `skills/`
- `templates/project-adapter.md`
- `templates/project-context.md`
- `evals/` fixtures, scoring extensions, and recorded host results
- new validation and installer helper scripts

## Open questions

None. Technical details may change during development when validation proves an assumption wrong, but any change to scope, public identity, supported hosts, install defaults, privacy boundaries, or approval gates returns the specification to `bwh-refine-spec`.

## Development readiness

- Scope is bounded to packaging, installation, nine named skills, provenance, validation, documentation, and compatibility.
- Product identity and install defaults are confirmed.
- Each skill has an explicit responsibility, overlap boundary, safety rule, and eval requirement.
- Tasks are ordered by shared dependencies and end in independently verifiable states.
- Human approval is still required before `bwh-development` may begin.
- Human output testing is defined in AC15 and remains required before release.

## Context files read

- `docs/discovery/bwh-agent-toolkit-expansion.md`
- `README.md`
- `.codex-plugin/plugin.json`
- `.claude-plugin/plugin.json`
- `contracts/autonomy.md`
- `contracts/collaboration.md`
- `contracts/completion.md`
- `contracts/context-loading.md`
- `contracts/handoff.md`
- `contracts/host-conventions.md`
- `contracts/model-routing.md`
- `contracts/states.md`
- `skills/bwh-adopt/SKILL.md`
- `skills/bwh-spec/SKILL.md`
- `evals/README.md`
- `evals/scoring.md`
- the built-in skill creation guidance
- the installed `unslop` guidance
