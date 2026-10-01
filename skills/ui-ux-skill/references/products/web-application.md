# Web Application Product Pack

Use only when the active product route includes `web-application`.

This Product Pack applies to browser-based products whose primary purpose is doing work inside an application rather than consuming marketing content.

## Product model

Establish:

- primary user roles;
- core jobs and workflows;
- route/page structure;
- authenticated vs public surfaces;
- application shell;
- navigation depth;
- persistent vs transient state;
- save/submit behavior;
- failure and recovery paths.

Do not design a web application as a collection of unrelated landing pages.

## Application shell

Choose navigation based on destination count, hierarchy, frequency, and role.

Preserve stable orientation across routes.

Avoid:

- duplicate global navigation;
- deep nested navigation without strong information architecture;
- hiding important destinations behind icon-only controls;
- changing navigation patterns page by page.

## Routed workflows

For multi-step tasks, make current position, next action, validation, and recovery understandable.

Preserve deep links and browser navigation semantics unless the product deliberately uses another model.

Unsaved changes, interrupted workflows, and destructive exits should be handled explicitly when the task can lose meaningful work.

## State model

Design first-class states for:

- initial/loading;
- empty;
- partial;
- error;
- permission denied;
- stale;
- offline/disconnected when relevant;
- success/confirmation;
- background processing.

Do not rely on toast notifications as the only explanation for critical state changes.

## Forms and data entry

Treat forms as workflows.

Use clear labels, useful grouping, visible validation, preserved valid values, and explicit save semantics.

Match field complexity to user expertise.

Do not turn every setting into a modal or every action into a multi-step wizard.

## Responsive web behavior

Responsive behavior is product architecture.

Determine what should:

- reflow;
- collapse;
- move into a drawer/sheet;
- become a dedicated route;
- remain horizontally scrollable;
- disappear only when truly secondary.

Do not emulate a native mobile app merely because the viewport is narrow.

## Keyboard, focus, and browser behavior

For productivity-oriented applications, support efficient keyboard/focus behavior when it materially improves repeated work.

Do not break standard browser expectations without a product reason.

## Authentication and account surfaces

Keep authentication, account, billing, and security-sensitive screens visually coherent with the product while preserving their engineering/security boundaries.

The UI/UX Head may improve presentation but must not redefine authentication or permission semantics.

## Validation

For web applications, validate representative:

- shell/navigation;
- primary workflow;
- secondary route;
- form/data-entry flow;
- permission/error state;
- deep-link/reload behavior where relevant;
- responsive widths;
- keyboard/focus behavior where relevant;
- active theme/direction;
- browser-rendered output.
