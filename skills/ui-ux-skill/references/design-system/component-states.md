# Design System Component States

Use when designing or auditing reusable interactive components.

A component is incomplete until its relevant states are defined.

## State inventory

Consider, as applicable:

- default
- hover
- focus-visible
- active / pressed
- selected
- disabled
- read-only
- loading / busy
- error / invalid
- warning
- success
- expanded / collapsed
- checked / unchecked
- mixed / indeterminate
- dragging / drop-target
- current / active-location

Do not require every component to implement every state.

## State semantics

Each state should have:

- behavioral meaning;
- visual treatment;
- semantic/programmatic state when applicable;
- keyboard/pointer behavior;
- accessibility behavior;
- theme resolution.

Do not define state only by color.

## Focus

Focus-visible must remain distinct from:

- hover;
- active/pressed;
- selected;
- current location.

Do not remove focus indication for aesthetic consistency.

## Disabled vs read-only

Disabled means the control is not currently operable.

Read-only means the value is visible but not editable.

Do not use them interchangeably.

Where the user needs to understand why an action is unavailable, provide appropriate context rather than an unexplained disabled control.

## Loading / busy

A busy component should communicate whether:

- the action has started;
- duplicate activation is blocked;
- current data remains valid;
- cancellation is possible.

Do not change a button label/state in a way that removes the user's understanding of the original action.

## Validation state

Error/warning/success state should not replace the underlying control label or meaning.

Use text or semantic messaging in addition to visual styling.

## Selection state

Selected/current/checked states must remain distinguishable from focus and hover.

For navigation, current location should not be represented only through focus styling.

## State token model

Prefer stable component-state token roles where a shared semantic token is too broad.

Examples:

- button.primary.background.default
- button.primary.background.hover
- input.border.focus
- input.border.invalid
- row.background.selected

Do not create state tokens that duplicate the exact same semantic alias without a component-specific reason.

## Theme matrix

Relevant states should be reviewed across:

- Light
- Dark
- High Contrast / Forced Colors where supported.

State meaning must survive theme resolution.

## Direction and localization

State treatments must tolerate:

- RTL/LTR;
- longer labels;
- translated validation messages;
- mixed-script content.

Do not put essential state meaning in a physical-direction-only icon.

## Interaction tests

For reusable components verify:

- pointer;
- keyboard;
- focus-visible;
- activation;
- disabled/read-only;
- loading;
- error;
- selected/current;
- reduced motion where animated;
- theme contexts;
- RTL/LTR.

## Product variants

Product Packs may define component variants for their workflow density or host platform.

Those variants must preserve the component state contract.

Do not create a "compact" product variant that loses focus, validation, or target clarity.
