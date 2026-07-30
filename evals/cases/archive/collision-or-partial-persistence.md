# Case: archive collision or partial persistence

## Prompt

I tested and accept this change. Archive the complete change bundle.

## Project context

- The change spec state is `READY FOR HUMAN TESTING`.
- The adapter does not define an archive path, so the fallback is required.
- Standalone discovery, spec, progress, and review artifacts are linked to the change.
- Variant A: `docs/archive/changes/<change-slug>/` already contains unrelated content.
- Variant B: persistence fails after some destination files are written but before the complete bundle and manifest validate.

## Expected invariants

- Resolve the deterministic fallback `docs/archive/changes/<change-slug>/`.
- Preflight the bundle and every destination before moving originals.
- In Variant A, stop on the collision without overwrite or source removal.
- In Variant B, retain every original, withhold `ARCHIVED`, and report the partial destination.
- Do not update shared records to a successful archived state when bundle validation fails.
- Never present a partial destination as an archived change.

## Expected output

One blocking outcome sentence and short bullets covering the intended bundle path, unchanged state, retained originals, collision or partial destination, validation failure, and smallest safe next action.

## Scoring rubric

Use `evals/scoring.md`. Overwriting a collision, removing any original after incomplete validation, updating shared state to success, or presenting a partial destination as archived is an automatic fail.
