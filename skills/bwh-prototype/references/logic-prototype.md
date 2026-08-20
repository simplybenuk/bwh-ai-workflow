# Logic prototype

Use a logic prototype for state, transitions, data shape, or business rules.

## Shape

- Keep the logic separate from its display or driver.
- Choose the smallest fitting form: pure functions, reducer, state machine, or a small state-owning module.
- Expose the full relevant state after each action in domain language.
- Provide free exploration plus repeatable scenarios for the happy path, an edge case, and an invalid transition when relevant.
- Keep state in memory unless persistence is the decision under test.

The host artifact may be a self-contained page, a small command-line program, or a focused test harness. Choose the form the intended reviewer can run with the least setup.

## Evidence

Record the initial state, actions, resulting states, and the observation that answers the decision question. A successful launch alone does not answer a state-model question.
