# UI prototype

Use a UI prototype for layout, hierarchy, or interaction questions.

## Variants

- Build three variants by default and at most five.
- Make variants structurally different. Change layout, information hierarchy, or primary action, not only color or copy.
- Use representative content and density without connecting live mutations.
- Make the current variant obvious and stable across reloads when the chosen environment supports a shareable selector.
- Expose relevant interaction state and protect text-entry controls from global keyboard shortcuts.

Prefer an isolated copy or adapter-defined prototype route. If the safest useful context requires an existing application shell, use a non-production environment and keep the prototype gate unmistakable. Never rely on a production-only guard as the sole isolation mechanism.

## Evidence

Demonstrate every variant at the target viewport or interface. Record what each variant tests, the observed trade-offs, and which question remains for the reviewer. Choosing a winner does not authorize promotion to production.
