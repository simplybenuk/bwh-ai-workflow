# BWH agent toolkit expansion

## Idea and desired outcome

Expand `bwh-ai-workflow` from a spec-driven delivery plugin into a portable BWH agent toolkit. Keep the existing delivery workflow intact, add a small collection of independent engineering and authoring skills, and make one repository sufficient to set up a new machine or agent host.

The desired outcome is a versioned source package that installs the same core skill behavior across supported agents while keeping host paths, invocation syntax, UI metadata, and optional capabilities outside the portable skill instructions.

## Actors

- The toolkit owner, who curates skills and installs a chosen profile on a machine or project.
- A project contributor, who uses the delivery workflow and independent engineering skills.
- An agent host, which discovers and invokes skills through its own packaging conventions.
- A future maintainer, who updates upstream-derived skills without losing BWH adaptations.

## Problem and opportunity

The repository already contains reusable skills, contracts, host mappings, an adopter, and regression evals. Creating another repository would duplicate installation, versioning, provenance, and validation work.

The current repository is narrower than the intended collection. Its manifests describe only spec-driven delivery, its adopter treats every `bwh-*` directory as one workflow package, and its host contract names only Codex and Claude Code explicitly. New independent skills would blur that boundary unless the repository gains a catalog, install profiles, provenance rules, and capability-based host adapters.

## Known facts

- The repository declares its core model- and agent-agnostic.
- Codex and Claude Code manifests already expose the root `skills/` directory.
- `bwh-adopt` installs `skills/bwh-*` plus shared contracts into a consuming project and records a pinned revision.
- Existing BWH questioning is selective. It asks the human only for product, scope, success, and expensive-to-reverse decisions. It resolves technical and reversible choices as labelled assumptions.
- Existing BWH review evaluates an implementation against an approved specification. It does not survey a codebase for structural improvement candidates.
- Existing BWH development requires an approved specification. It has no explicit discovery-prototype path.
- Matt Pocock's reviewed skills are MIT licensed. This review used upstream commit `885e2ca4d842d139e9aef4e48d366c63cb1b8013`.

## Assumptions

- **A1, supported hosts.** The first portable release will test Codex, Claude Code, and Cursor. Other hosts may use manual installation but will not be described as supported until an eval passes. This is observable when the same trigger fixtures and representative task fixtures pass on all three named hosts.
- **A2, default profiles.** Project-local adoption will default to the delivery workflow. User or machine installation will default to the full toolkit. This is observable from dry-run install output and the resulting lock file.
- **A3, repository identity.** Keep the `bwh-ai-workflow` repository URL during the expansion. Change the display name and description rather than breaking existing marketplace and lock references. This is observable when existing install sources still resolve after release.
- **A4, adapted imports.** Preserve useful upstream behavior and attribution, but rewrite vendor paths, tools, invocation controls, publication assumptions, and unsafe absolutes. This is observable through a portability lint and the recorded upstream-to-local change notes.

## Candidate review

### `grill-me`

**Recommendation: add as an adapted, explicit `bwh-grill` skill.**

The seven-line wrapper is not the useful part. Its `grilling` dependency maps a design tree, asks every currently answerable decision in numbered rounds, recommends an answer for each, and continues until no branch remains. It also separates facts the agent can establish from decisions only the human can make.

This overlaps strongly with the BWH collaboration contract. Both batch questions by prerequisite, require recommendations, and prohibit asking the human for discoverable facts. The material difference is intentional intensity. BWH normally minimizes questions and resolves reversible technical choices itself. Grilling makes every decision the human's and refuses to act until the tree is empty and the human confirms shared understanding.

Do not replace BWH's default questioning with this behavior. Add an opt-in skill whose narrow trigger requires an explicit request to grill, interrogate, or exhaustively stress-test an idea. Reuse BWH's question format and evidence rules. Produce a concise decision record or handoff only when the user asks to capture the result. Route the settled result to `bwh-ideate`, `bwh-spec`, or `bwh-refine-spec` rather than acting on it directly.

Adaptations required:

- Remove `disable-model-invocation`, which is not portable frontmatter.
- Replace the Skill tool call with a self-contained workflow or a portable reference.
- Make parallel research optional when the host supports it.
- Preserve BWH's distinction between facts, reversible assumptions, and product decisions unless the user explicitly requests full decision ownership.
- Remove decorative question and recommendation icons.

### `writing-for-agents`

**Recommendation: add as `bwh-write-agent-instructions`, backed by a shared authoring reference.**

This is broader than the built-in skill creator. It applies to every document an agent reads, including skills, repository instruction files, and documents reached through pointers. Its strongest contributions are context pointers, context-load versus human-memory trade-offs, information hierarchy, checkable completion criteria, single sources of truth, pruning stale instructions, and testing whether an instruction changes behavior.

BWH overlaps at the principle level. `context-loading.md` asks agents to load the smallest relevant context, and the workflow contracts rely on shared references instead of duplication. BWH does not currently explain how to design a reliable trigger, when to split reference material, how to identify no-op instructions, or how to evaluate instruction load.

The adapted skill should use the generic term "project agent instruction file" and support skills, contracts, adapters, and host instruction files. Keep host-specific invocation mechanics in references owned by each host adapter. Do not copy the upstream claim that `disable-model-invocation` has the same behavior everywhere.

Adaptations required:

- Generalize `AGENTS.md` and `CLAUDE.md` references.
- Replace vendor invocation fields with a capability table in host packaging.
- Retain the concepts of context pointers, progressive disclosure, completion criteria, pruning, and behavioral evals.
- Cut coined terminology that does not improve an observable instruction-writing decision.
- Add eval cases for false triggering, missed triggering, stale references, and duplicated rules.

### `improve-codebase-architecture`

**Recommendation: add as an adapted `bwh-review-architecture` skill with a documented design lens.**

This does not duplicate `bwh-agent-review`. The BWH review asks whether a completed change satisfies its approved specification. The upstream skill surveys recently changed or painful parts of an existing codebase, finds shallow modules and leaky seams, and proposes structural candidates before any implementation is authorized.

The upstream skill has useful discipline. It scopes the survey to code that changes often, reads domain language and ADRs, applies a deletion test, distinguishes interface from implementation, classifies dependencies, and asks the user to choose a candidate before designing an interface.

Its current delivery is too coupled to the rest of Matt Pocock's collection. It requires `codebase-design`, `grilling`, `domain-modeling`, optional design variants from parallel agents, and an HTML report that loads Tailwind and Mermaid from CDNs. It also insists that its architecture vocabulary replace ordinary terms. That is too rigid for a general toolkit.

The BWH version should treat deep modules as one named review lens, not the only valid architecture theory. It should produce a repository-approved Markdown report by default, with diagrams only when they improve understanding. HTML can be an optional host capability. The report must cite files and evidence, mark conflicts with ADRs, rank candidates, and stop before implementation. A selected candidate then enters `bwh-ideate` or `bwh-spec`.

Adaptations required:

- Make subagents optional rather than required.
- Replace CDN-backed HTML with portable Markdown as the default.
- Permit project vocabulary such as component, service, or API when those are authoritative domain or architecture terms.
- Keep the deletion test, interface-depth test, dependency classification, test-seam analysis, and recent-change focus.
- Separate architecture review from architecture implementation.
- Add an eval that rejects speculative refactors with no observed maintenance or testing cost.

### `prototype`

**Recommendation: add as an adapted `bwh-prototype` discovery skill.**

This fills a real BWH gap. `bwh-ideate` compares options in prose and `bwh-development` begins only after human approval. A throwaway prototype can answer a disputed state-model or UI question before the specification commits to the wrong design.

The upstream split is sound. Logic prototypes use a self-contained HTML file to expose state transitions to non-developers. UI prototypes create several structurally different variants and make comparison easy. Both require the question to be stated first and the answer captured afterwards.

Several upstream rules conflict with BWH safety and publication boundaries. It places prototypes beside production code, may use real application routes, and instructs the agent to commit the result to a throwaway branch. It also says to skip tests and suggests lifting prototype logic into production. Those actions could bypass the human approval gate or leave unsafe code behind.

The BWH version should run in an isolated temporary directory or worktree by default. It may use a project prototype location only when the adapter defines one. It should verify that the prototype runs, but should not add production-grade tests to throwaway code. The conclusion becomes discovery or specification evidence. Moving code into production, committing a branch, or publishing remains a separate authorized action.

Adaptations required:

- Keep the one-question limit and the logic-versus-UI branch.
- Isolate prototype code and data from production by default.
- Require real mutations and external services to use stubs or disposable environments.
- Record the question, observations, conclusion, and unresolved uncertainty.
- Treat prototype code as evidence, not approved implementation.
- Require separate authority for commits, pushes, or publication.

## Proposed toolkit scope

The first specification should cover these active additions:

- `bwh-diagnose-bugs`
- `bwh-blast-radius`
- `bwh-create-verification`
- `bwh-technical-writing`
- `bwh-grill`
- `bwh-write-agent-instructions`
- `bwh-review-architecture`
- `bwh-prototype`
- `bwh-skills-audit`

Keep `bwh-domain-modeling` and `bwh-resolve-merge-conflicts` as pilots until their interaction with project adapters and safety contracts is tested.

## Packaging and profiles

Add a repository catalog that explicitly lists skills, source provenance, local adaptations, status, dependencies, and install profiles. Stop using the `skills/bwh-*` glob as the package definition.

Suggested profiles:

- `workflow`: the existing ideation, specification, refinement, development, review, archival, and adoption skills.
- `engineering`: diagnosis, blast-radius analysis, verification generation, architecture review, and prototyping.
- `authoring`: technical writing, agent-instruction writing, grilling, and skill audit.
- `full`: all active profiles.

Project adoption defaults to `workflow`. User or machine setup defaults to `full`. A lock records the selected profile and exact installed skill names so updates can distinguish managed files from local additions.

## Agent-independent core

Portable skill instructions must:

- Use only `name` and `description` as shared frontmatter.
- Refer to skills by bare name and resources by relative path.
- Describe capabilities instead of vendor tools.
- Keep model selection outside the skill body.
- Provide a safe fallback when structured questions, subagents, browser control, or artifact viewers are unavailable.
- Keep host paths, invocation prefixes, UI metadata, and plugin manifests in host packaging.

Add Cursor to the host contract and ship a Cursor manifest. Treat Codex, Claude Code, and Cursor as supported only after representative evals pass on each host.

## Scope

- Reposition the repository as the BWH Agent Toolkit without changing its GitHub URL.
- Introduce an explicit skill catalog and install profiles.
- Adapt the approved upstream skills rather than copying them unchanged.
- Extend installation, update locks, provenance, validation, and evals.
- Preserve the current workflow states and human approval gates.
- Document and test Codex, Claude Code, and Cursor packaging.

## Non-goals

- Installing either upstream catalog wholesale.
- Making the existing BWH delivery workflow invoke every new skill automatically.
- Claiming support for an agent host that has not passed representative evals.
- Storing conversation history, credentials, machine configuration, or private project data in the toolkit repository.
- Replacing project architecture conventions with one mandatory design philosophy.
- Allowing prototypes or architecture reports to bypass specification approval.

## Success signals

- A fresh machine can install the `full` profile from one pinned repository revision.
- A consuming project can install or update only the `workflow` profile without receiving unrelated skills.
- The same portable skill fixtures pass on Codex, Claude Code, and Cursor.
- Every upstream-derived skill records its source path, commit, license, and material adaptations.
- Host-specific strings are absent from portable skill bodies except inside explicitly routed host references.
- Existing BWH workflow evals pass unchanged after the catalog and profile migration.
- Each new skill has at least one positive trigger, one negative trigger, one representative outcome case, and one portability case.

## Risks

- Broad skill descriptions could increase false triggering and context load.
- Imported skills may encode conflicting autonomy, publication, or approval assumptions.
- A single plugin containing many skills may become hard to navigate without profiles and a router.
- Supporting several hosts may encourage lowest-common-denominator instructions that lose useful host capabilities.
- Prototype and architecture skills can create scope expansion unless they stop at evidence and hand off to the delivery workflow.
- Upstream updates may silently restore vendor-specific behavior unless provenance and adaptation diffs are reviewed.

## Dependencies

- A catalog format and deterministic installer or adopter update.
- Host mappings and manifests for Codex, Claude Code, and Cursor.
- Portable skill validation and forbidden-host-string checks.
- Upstream attribution and license notices.
- Representative trigger and outcome evals.
- Migration handling for existing lock files that do not record profiles or installed skill names.

## Material options

### Option A: one flat plugin with all skills

Smallest implementation, but every installation receives every skill and the adopter cannot preserve a focused project setup. Reject because it recreates the clutter this review is meant to reduce.

### Option B: one repository with catalogued profiles

Keep one source and one set of host manifests. Install selected profiles and record exact managed skills. This gives new-machine portability without forcing every project to load the whole toolkit. Recommended.

### Option C: one repository containing several separately packaged plugins

Cleaner marketplace separation, but it adds manifest, release, and installation complexity before the skill set is stable. Keep as a later option if profile support proves insufficient.

## Decisions still needed

- Confirm whether the first specification should include all nine active additions or split the imported skills into a second release after packaging and profile support land.
- Confirm whether the public display name should become `BWH Agent Toolkit` while the package and repository identifier remain `bwh-ai-workflow`.

## Context used

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
- `skills/bwh-agent-review/SKILL.md`
- `skills/bwh-development/SKILL.md`
- `skills/bwh-ideate/SKILL.md`
- `skills/bwh-refine-spec/SKILL.md`
- `skills/bwh-spec/SKILL.md`
- Matt Pocock `grill-me`, `grilling`, `writing-for-agents`, `improve-codebase-architecture`, `codebase-design`, and `prototype` skill files and their direct references at the pinned commit above.
