# Forms and Data Entry

Use when forms, settings, data entry, validation, save/submit behavior, or multi-step input is materially in scope.

This Shared Rule defines the cross-product data-entry contract. Product Packs own product-specific commitment, lifecycle, host, and platform behavior.

## Form as task

A form should reflect a user task, not the storage schema.

Group fields by meaning and decision.

Do not expose database/module structure merely because it exists.

## Labels and instructions

Use persistent visible labels for important fields.

Clarify:

- required vs optional;
- expected format;
- units;
- scope;
- consequence;
- unusual constraints.

Placeholder text is not a substitute for the only label.

Keep help text near the field or section it explains.

## Input semantics

Use an input/control that matches the data and task.

Prefer native input behavior when it provides appropriate semantics, keyboard, validation, autofill, and accessibility.

Do not build custom controls when standard controls solve the problem adequately.

## Defaults

Defaults should reduce work without silently making consequential decisions.

Distinguish:

- system default;
- inherited value;
- user-entered value;
- suggested value.

Do not preselect a high-impact option merely to increase completion.

## Validation timing

Validate at a time that helps correction.

Use:

- constraint guidance before failure when useful;
- inline validation for local issues;
- submission validation for cross-field/business rules;
- asynchronous pending state when validation depends on remote work.

Do not show an error before the user has had a reasonable chance to provide a valid value.

## Error identification

When an error is detected:

- identify the affected field/task;
- describe the problem in text;
- explain correction when possible;
- preserve valid values;
- avoid color-only indication.

For long or complex forms, add a useful error summary when it improves recovery.

## Preserve user work

A failed submission should not erase valid entered data unless security/privacy requirements demand it.

For multi-step flows, do not ask for the same information again when it can safely be reused or selected.

## Save and submit semantics

The interface must make clear whether an action:

- saves a draft;
- saves final state;
- submits for processing;
- applies immediately;
- queues background work;
- only validates/tests.

Button labels should describe the actual result where practical.

Do not show completion before authoritative state confirms it.

## Disabled controls

Do not use disabled fields/buttons as unexplained dead ends.

When a relevant control is unavailable:

- explain the prerequisite;
- indicate the authority/scope if permission-limited;
- provide recovery when appropriate.

## Multi-step flows

For a multi-step form:

- use steps only when decomposition helps;
- show meaningful progress;
- preserve previous valid input;
- allow safe backward navigation;
- distinguish review from submission;
- avoid redundant entry.

Do not create a wizard merely to make a short form look sophisticated.

## Sensitive data

When collecting secrets, credentials, personal data, or security-sensitive input:

- minimize collection;
- explain purpose when needed;
- avoid unnecessary reveal;
- preserve privacy in summaries/logs;
- do not infer successful verification from the presence of a stored value.

## Keyboard and focus

Form controls must be keyboard operable.

After validation/submission:

- move focus only when it improves recovery;
- do not unexpectedly steal focus;
- ensure errors/status are discoverable;
- keep focused fields visible.

## Success state

After successful completion, clarify:

- what changed;
- whether processing continues;
- next step;
- how to return/edit if applicable.

Do not clear the interface before the user can understand the result.

## Validation

Verify:

- initial/default state;
- valid submission;
- invalid field;
- multiple errors;
- async validation when relevant;
- preserved valid input;
- required/optional clarity;
- keyboard-only completion;
- zoom/text scaling;
- narrow layout;
- RTL/LTR and localized string expansion where supported.
