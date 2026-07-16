# Wolds Record adapter

This adapter is the project-specific layer for the Wolds Record repository.

It should define the repository's `AGENTS.md` rules, source-of-truth paths, PRD task shape, organisation-scoping requirements, mandatory npm validation suite, branch policy, release/review rules, and the human output-testing checklist. Keep those constraints here rather than in the reusable workflow skills.

## Tool routing

The adapter should document the repository tools and their routing rules:

- `rg` / `rg --files` for targeted discovery before broader reads;
- local file inspection for source-of-truth and implementation context;
- `npm run typecheck`, `npm run test`, `npm run test:coverage`, and `npm run lint` for required validation;
- migration and current-schema inspection before changing Supabase selects or payloads;
- browser or smoke checks for user-visible changes when available.

Before an action, resolve required discovery and validation prerequisites. If a read is empty, partial, or suspiciously narrow, try one meaningful fallback before concluding that evidence is absent. External writes, destructive actions, and scope expansion require confirmation.
