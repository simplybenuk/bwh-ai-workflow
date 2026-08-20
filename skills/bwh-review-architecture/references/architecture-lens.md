# Architecture review lens

Use these ideas consistently inside one report, while preserving the project's own vocabulary.

## Terms

- A **module** is a unit with an interface and implementation at any scale.
- An **interface** is everything a caller must know, including invariants, ordering, errors, configuration, and performance constraints.
- **Depth** is useful behavior hidden behind a comparatively small interface.
- A **seam** is a place where behavior can vary without editing the caller.
- An **adapter** supplies one implementation at a seam.
- **Locality** measures how well knowledge, change, defects, and verification stay together.

## Checks

### Interface size and depth

List what callers must know. Compare that burden with the behavior hidden by the module. A pass-through that merely renames underlying operations is likely shallow.

### Deletion test

Imagine removing the module. A useful module's complexity would spread back into callers. If the complexity simply disappears, the module may be unnecessary indirection.

### Seam placement

Classify relevant dependencies:

- in-process computation;
- locally substitutable dependency;
- remote system owned by the project;
- external system outside project control.

Use the category to judge whether a seam is real and where tests can cross it. Do not prescribe a new interface during the review.

### Test locality

Check whether tests exercise observable behavior through the same interface callers use. Flag tests that require broad internal knowledge or change during unrelated internal refactors.

### Change locality

Use recent representative changes to count where one concept had to be understood or edited. Repeated edits across unrelated callers are stronger evidence than file count alone.
