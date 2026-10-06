---
name: bwh-pr-review
description: Independently review a complete pull request or branch before merge and return a revision-bound verdict. Use for local pre-merge review, release PRs and re-review after changes; not implementing review feedback or the specification acceptance lifecycle.
---

# Pull request review

Apply `../../contracts/autonomy.md`, `../../contracts/context-loading.md` and
`../../contracts/review.md`, plus the consuming project's adapter when present.
Resolve project instructions through `../../contracts/host-conventions.md`.

## 1. Establish independence

Use a fresh reviewer separate from the implementer. In an author session,
delegate to a worker or session without inherited author history. Give a raw
brief containing the repository, requested outcome, target/base/head references,
project document locations, available checks and permitted side effects. Do
not supply implementation rationale, suspected findings or prior conclusions.
An already independent reviewer proceeds directly. Record the independence
basis before reviewing.

If independent execution is unavailable, useful self-analysis is allowed only
when clearly labelled non-independent. Return `REVIEW INCOMPLETE`; it cannot
satisfy an independent-review gate.

## 2. Pin the complete range

Resolve the intended base and head to immutable commit SHAs and record their
merge-base SHA. Inspect the whole merge-base-to-head range, including every
commit's combined effect, deletions, configuration and documentation. Reviewing
only the last commit or the working-tree diff is insufficient.

Read applicable project instructions, adapter, coding standards or guardrails,
and authoritative requirements. A bounded fix may use the user request and
relevant tests; a spec or PRD is not compulsory. Apply release requirements when
reviewing a release. The scope is established when revisions, intended outcomes
and applicable project gates are explicit. Missing or ambiguous revisions make
the review incomplete; do not substitute the current checkout silently.

## 3. Review outcomes and evidence

Apply the shared review criteria to the full range and relevant surrounding
callers, tests and user paths. Check current schema when data access or
migrations are affected. Trace claims to authoritative sources and code rather
than accepting the author's summary.

Verify claimed tests and run focused safe checks when needed. Executed checks
must use the pinned head; dirty implementation files cannot prove that committed
revision. Do not overwrite the author's work to obtain a clean checkout. Record
checks performed, results, unrun checks and material limits. Unavailable tools
or environments do not lower the evidence standard. This step is complete when
findings and evidence gaps are classified with concrete support.

## 4. Bind the verdict and handoff

Immediately before issuing the verdict, re-resolve the original base/head
references. A changed head or relevant base invalidates current readiness until
the new range is reviewed. On interrupted review, recheck revisions and context,
reuse only evidence whose inputs remain unchanged, and complete the unreviewed
scope before issuing a verdict.

Use the project's review-artifact convention, or return a plain result when
none exists. Prefer storing evidence outside the reviewed range. If committing
a report advances head, inspect that successor diff and give a fresh plain-result
attestation to the new SHA. Do not repeatedly rewrite the report to include its
own commit SHA. Implementation changes require renewed review.

Return exact base, head and merge-base SHAs, independence basis, findings with
severity and evidence, performed/unrun checks, material limits and one verdict:

- `READY FOR MERGE`: independent review is complete, no material defect remains,
  and evidence satisfies the project's local review gate.
- `CHANGES REQUIRED`: supported defects or failed required checks need correction.
- `REVIEW INCOMPLETE`: independence, scope or necessary evidence is missing.

The verdict describes this review, not completion of CI, project acceptance or
publication gates. Hosted review is optional unless current project policy
requires it; report an unmet policy gate instead of overriding it.

## Authority

Review authorises inspection, safe non-destructive checks and a local review
artifact. It does not authorise implementation edits, dependency installation,
shared-database resets, publication, approval or merge. Return findings to the
implementer; fixes and external actions require their own authority.
