# WordPress Plugin Product Pack

Use only when the active product route includes `wordpress-plugin`.

This Product Pack applies to plugin-owned UI inside WordPress administration, including settings, configuration, onboarding, diagnostics, tools, status screens, and plugin-specific operational admin screens.

## Host environment first

The plugin UI lives inside `wp-admin`.

Preserve the user's WordPress mental model unless the plugin intentionally provides an application-like admin experience with a clear product reason.

Do not redesign the surrounding WordPress administration shell as part of plugin settings work.

## Screen placement and scope

Before designing, establish:

- where the plugin is reached in WordPress administration;
- whether the screen is settings, tools, status/diagnostics, onboarding, or a dedicated operational workspace;
- whether settings are site-wide, user-specific, network-wide, or context-specific;
- which roles/capabilities may view or change them.

UI presentation must follow actual capability boundaries.

## Settings architecture

Group settings by user intent and consequence, not by PHP class, database table, API module, or internal implementation structure.

Prefer a small number of clear groups.

Avoid deeply nested tabs and tab-within-tab structures.

Make defaults understandable.

Clearly distinguish:

- ordinary settings;
- advanced settings;
- connection/integration settings;
- destructive/reset operations;
- diagnostics/status;
- import/export;
- license/account information when applicable.

## WordPress-native vs custom application UI

Reuse existing WordPress/admin conventions when they fit the task.

A custom component system may be appropriate when the plugin provides a substantial application-like workflow, but do not create a visually disconnected mini-product merely for simple configuration.

If the existing plugin already has a coherent component system, improve it rather than forcing a full return to default controls.

## Saving and feedback

Make save scope explicit.

Users should understand:

- what will be saved;
- whether changes apply immediately;
- whether reload/reconnect/rebuild is required;
- whether a setting affects the whole site/network;
- whether unsaved changes exist.

Use clear success, validation, and error feedback.

Do not rely on a generic success notice when only part of a settings operation succeeded.

## Integrations and credentials

For API keys, tokens, service connections, or external integrations:

- separate connection status from configuration;
- make test/reconnect/disconnect states understandable;
- avoid exposing secrets after storage when the product does not need to reveal them;
- preserve engineering/security constraints from the higher-level Head.

Do not invent secret-storage or authorization behavior as a UI decision.

## Dangerous operations

Separate reset, uninstall cleanup, delete-data, disconnect, reindex, regenerate, or destructive maintenance operations from normal settings.

Explain consequence and scope.

Require deliberate confirmation when appropriate.

## Onboarding

If the plugin has setup/onboarding:

- optimize for first successful outcome;
- distinguish required from optional setup;
- allow safe resume;
- do not trap experienced users in unnecessary wizard steps;
- make completion state understandable.

## Diagnostics and status

When relevant, provide:

- clear current status;
- actionable failures;
- environment/integration checks;
- copy/export support information when useful;
- separation between user-fixable and developer/host issues.

Do not dump raw debug output as the primary UX.

## Responsive behavior

Remember that `wp-admin` itself changes at narrower widths.

Validate plugin screens inside the actual admin shell rather than testing the plugin panel in isolation.

Avoid fixed-width layouts that collide with the admin menu or mobile admin behavior.

## RTL and localization

For Persian/RTL WordPress admin UI, the required `persian-writing` specialist still owns Persian-language validation.

This Product Pack owns the WordPress plugin settings structure and UI behavior, not Persian linguistic rules.

## Validation

For WordPress plugin UI, validate representative:

- entry point/menu placement;
- main settings groups;
- save/validation feedback;
- capability-limited state;
- dangerous action;
- integration/credential state when relevant;
- WordPress notices and surrounding admin shell;
- responsive `wp-admin`;
- RTL/LTR if supported;
- Light/Dark only when the host/plugin genuinely supports those modes.
