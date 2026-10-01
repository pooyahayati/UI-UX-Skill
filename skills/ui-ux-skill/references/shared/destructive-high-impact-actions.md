# Destructive and High-Impact Actions

Use when delete, reset, revoke, disconnect, overwrite, bulk change, irreversible action, or other consequential operations are materially in scope.

## Classify consequence

Before designing confirmation, classify the action.

### Low consequence / reversible

Prefer direct action with clear feedback and undo when safe.

### High consequence but recoverable

Explain scope and recovery.

Confirmation may be appropriate when accidental activation is plausible and costly.

### Irreversible or security-sensitive

Require deliberate confirmation proportional to consequence.

Do not apply the same confirmation pattern to every action.

## Scope clarity

Before execution, users should understand what is affected.

Examples:

- one item;
- selected items;
- all visible;
- all matching filter;
- account;
- workspace;
- site;
- network;
- organization;
- stored data;
- remote connection.

Do not hide scope in secondary text for high-impact operations.

## Action naming

Use specific verbs.

Prefer:

- Delete record
- Remove access
- Revoke token
- Disconnect service
- Restore defaults
- Delete stored plugin data

over ambiguous:

- Reset
- Remove
- Confirm
- Continue

when the consequence is materially different.

## Confirmation

A confirmation should add information, not merely ask "Are you sure?"

Where appropriate include:

- object/scope;
- consequence;
- reversibility;
- dependent effects;
- required follow-up.

Avoid confirmation fatigue for routine reversible actions.

## Strong confirmation

Typed confirmation, reauthentication, approval, or additional verification may be appropriate for highly consequential operations, but only when product/security policy justifies it.

The UI/UX layer must not invent or bypass security requirements.

## Undo and recovery

Prefer undo/recovery over confirmation when:

- reversal is safe;
- the action is frequent;
- accidental activation is plausible;
- recovery is easier than interruption.

Do not offer Undo when the backend cannot guarantee reversal.

## Bulk high-impact action

For bulk actions:

- show affected count/scope;
- distinguish selected vs all-filtered/all;
- preview impact when useful;
- report partial failure;
- preserve failed items/context;
- avoid duplicate execution.

## Background destructive work

If deletion/reset runs asynchronously:

- distinguish scheduled/queued from completed;
- show job status;
- prevent conflicting repeated requests;
- communicate when effects become final.

Do not say "Deleted" if deletion has only been queued.

## Permission and authorization

Visibility and enabled state follow authorization.

A confirmation dialog is not an authorization boundary.

Do not imply users can perform an action merely because the control is visible.

## Focus and accessibility

Confirmation UI must support:

- clear title/consequence;
- keyboard operation;
- visible focus;
- predictable initial focus;
- accessible names;
- non-color severity;
- safe Escape/Cancel behavior where permitted.

Do not make the destructive action the only visually discoverable control.

## Validation

Verify:

- reversible action;
- irreversible action;
- cancellation;
- failed execution;
- partial bulk failure;
- duplicate-submit protection;
- async completion when relevant;
- permission denied;
- keyboard/focus behavior;
- localized/RTL consequence text.
