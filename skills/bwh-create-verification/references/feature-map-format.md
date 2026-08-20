# Feature map format

The generated `features/README.md` records shared preconditions, driving conventions, evidence rules, and links to feature files. It must identify the disposable environment and prohibit driving an unowned instance.

Each feature file uses this shape:

```markdown
# <User-facing feature>

<One sentence describing the observable behavior.>

## Sub-features

- `<stable-id>`: <behavior>

## How to get to it (user POV)

- <Every supported user entry point.>

## Driving it with <existing harness>

Preconditions:

- <Required isolated state.>

- <User action, exact command, and observable result.>

## Gotchas

- <Known trap that could invalidate the result.>
```

Name real handles and commands. Capture the action and the result. When the feature writes state, confirm it through a second user-facing or read-only view. Do not count one entry point as proof for a different mapped entry point.
