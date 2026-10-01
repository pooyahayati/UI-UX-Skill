# WordPress Plugin Settings and Admin Forms

Use this local rule pack when the active product route includes `wordpress-plugin` and settings, configuration, admin forms, notices, import/export, license/account, or destructive configuration actions are materially in scope.

These are UI/UX rules. They do not replace WordPress security, sanitization, validation, nonce, or capability checks.

## WordPress-native settings model

Prefer WordPress-native settings conventions when the job is ordinary configuration.

When implementation uses the WordPress Settings API, preserve the mental model of:

- settings page;
- sections;
- fields;
- explicit save;
- validation/error feedback;
- capability-gated submission.

Do not invent an application-like settings shell merely because custom components are available.

A custom application-like UI is justified only when configuration itself is a substantial workflow that benefits from richer interaction.

## Settings information architecture

Group settings by user intent, consequence, and frequency.

Common groups may include:

- General
- Integrations
- Notifications
- Content/behavior
- Display/appearance
- Advanced
- Import/export
- Privacy/data
- Diagnostics
- License/account

Do not mirror:

- PHP class names;
- REST route groups;
- database tables;
- option keys;
- internal module folders.

Avoid tab-within-tab structures.

If a settings page needs many levels, reconsider the information architecture before adding another tab row.

## Defaults and inherited values

Users should understand whether a value is:

- default;
- explicitly configured;
- inherited;
- overridden;
- unavailable due to capability/environment;
- controlled at network level.

When safe, show the effective value as well as the override source.

Do not make users infer whether clearing a field means empty, default, inherited, or disabled.

## Save model

Choose and communicate one save model:

- explicit Save Changes;
- per-section save;
- immediate update;
- staged Draft -> Apply;
- network/default + site override.

Do not mix immediate and explicit-save settings without clear distinction.

When explicit saving is used:

- show unsaved state when material;
- preserve valid input after validation failure;
- explain partial failure;
- do not show success before authoritative save;
- return focus/attention to the relevant error where practical.

## Validation and errors

Validation messages should explain:

- what is invalid;
- where the problem is;
- what format/range is expected;
- whether the previous saved value is still active.

For multiple errors:

- keep field-level messages;
- provide a useful summary when the page is long or complex;
- preserve user input where safe.

Do not rely on color alone.

## Admin notices

Use WordPress notices for information that belongs in the admin notice model.

Choose severity according to consequence:

- success
- info
- warning
- error

A dismissible notice should not imply that the underlying problem is resolved.

If a notice must remain dismissed across pages/sessions, persistence must be implemented intentionally; the standard dismiss affordance alone is not a durable preference.

Avoid:

- global notices for page-local low-risk information;
- promotional nags on unrelated admin pages;
- repeated notices that cannot be acted on;
- using update-style nags for ordinary plugin messaging.

## Page-local feedback

Prefer inline/page-local feedback when the message applies only to:

- one field;
- one section;
- one connection test;
- one import/export operation;
- one local action.

Do not send every successful toggle or test result to a global admin notice.

## Advanced settings

Advanced settings should be:

- clearly separated;
- explained in terms of consequence;
- safe by default;
- discoverable to expert users without intimidating ordinary users.

Do not use "Advanced" as a dumping ground for poorly organized settings.

For dangerous expert controls, include:

- consequence;
- scope;
- recovery;
- reset/default path where available.

## Import / export

For import/export configuration:

Define:

- what is included;
- what is excluded;
- format/version;
- whether secrets are included;
- whether existing values are overwritten or merged;
- validation before apply;
- preview/diff when consequence is high;
- rollback/recovery when feasible.

Do not export secrets by default unless the user explicitly needs that and the security model allows it.

For import:

- validate before applying;
- report invalid/unknown fields;
- avoid partial silent application;
- distinguish compatibility warning from fatal error.

## Reset and defaults

Separate these concepts:

- Reset this field
- Reset this section
- Restore plugin defaults
- Remove plugin data
- Uninstall cleanup

Do not label all destructive configuration actions "Reset".

For broad reset actions:

- explain scope;
- identify irreversible consequences;
- require deliberate confirmation proportional to risk;
- offer export/backup first when useful.

## License and account surfaces

Treat license/account management as an account/integration surface, not a normal text setting.

Where relevant, show:

- current state;
- account/license identity;
- activation scope;
- expiry/renewal status;
- update entitlement if applicable;
- connect/reconnect/deactivate actions;
- errors and recovery.

Do not expose full secrets unnecessarily.

Do not imply that a successful UI action changed licensing state until authoritative confirmation is received.

## Sensitive values

For API keys, tokens, passwords, or secrets:

- distinguish stored from not configured;
- avoid revealing the full saved secret by default;
- allow replacement without forcing reveal;
- communicate whether clearing removes the credential;
- separate secret storage state from connection health.

Do not use a masked string such as `••••••` as evidence that a remote connection is working.

## Accessibility

Settings/forms should support:

- persistent labels;
- field descriptions associated with controls;
- keyboard navigation;
- visible focus;
- meaningful error association;
- no placeholder-only labeling;
- sufficient target size;
- text zoom/reflow;
- semantic grouping.

Use native controls and WordPress-native semantics when they solve the task.

## Responsive wp-admin

Test the page inside the real WordPress admin shell.

Resolve:

- narrow admin menu state;
- wrapping labels/descriptions;
- table overflow;
- button grouping;
- side-by-side fields;
- sticky bars;
- tab navigation;
- notices.

Do not validate a settings panel in isolation from `wp-admin`.

## Validation checklist

When this pack is active, test representative:

- first load with defaults;
- modified but unsaved state;
- successful save;
- validation failure;
- permission-limited state;
- advanced setting;
- sensitive credential state;
- import validation;
- reset/destructive confirmation;
- admin notice behavior;
- narrow `wp-admin`;
- RTL/LTR when supported.
