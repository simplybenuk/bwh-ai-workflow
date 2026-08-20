# Skills audit report format

Use this structure. Omit empty finding groups, but always keep validation gaps and approvals.

```markdown
# Skills audit

- Review date: <date>
- Host scope: <resolved current host>
- Toolkit source revision: <revision or unknown>
- Installed revision: <revision or unknown>
- Selected profile: <profile or unknown>
- Usage window: <dates and aggregate-only statement, or not requested>

## Findings by ownership

### Personal skills

### Plugin-managed skills

### Built-in skills

### Project-local skills

For each finding record category, skill, status, evidence, and recommended action.

## Integrity checks

Record missing skills, unexpected skills, version drift, local modifications, broken references, invalid frontmatter, inactive profile entries, and checks that could not run.

## Retirement review

Recommend retirement only when both fields are `yes`:

- No observed use: <yes/no/unknown and evidence window>
- No declared future need: <yes/no/unknown and source>

## Approval gates

List each proposed installation, update, profile change, retirement, plugin removal, or replacement as a separate action awaiting explicit approval.
```
