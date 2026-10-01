# WordPress Plugin Product Pack

Use only when the active product route includes `wordpress-plugin`.

This Product Pack applies to plugin-owned UI inside WordPress administration, including settings, configuration, onboarding, integrations, diagnostics, tools, status screens, maintenance, and plugin-specific operational workspaces.

Product design knowledge for WordPress plugins is maintained locally in this repository. Do not depend on an external design Skill for WordPress plugin UI.

## Required WordPress routing

Before major design decisions, classify the current plugin surface.

### Settings / configuration

Load:

`wordpress/settings.md`

Use for:

- settings architecture;
- admin forms;
- save/validation behavior;
- notices;
- advanced settings;
- import/export;
- license/account configuration;
- reset/default operations.

### Onboarding / integrations

Load:

`wordpress/onboarding-integrations.md`

Use for:

- first-run setup;
- setup wizard;
- environment readiness;
- API credentials;
- OAuth/external authorization;
- connection testing;
- service/account connection;
- data sync onboarding.

### Diagnostics / operations

Load:

`wordpress/diagnostics-operations.md`

Use for:

- Site Health;
- diagnostics;
- logs;
- support information;
- background jobs;
- scheduled work;
- maintenance/repair;
- destructive data cleanup.

### Multisite / Network Admin

Load:

`wordpress/multisite-admin.md`

Use whenever:

- WordPress Multisite is supported;
- Network Admin is involved;
- network defaults or per-site overrides exist;
- bulk operations affect multiple sites;
- network activation changes product behavior.

A task may load multiple local WordPress packs.

Do not load every WordPress pack for a narrow change.

## Host environment first

The plugin UI lives inside `wp-admin`.

Preserve the WordPress administration mental model unless the plugin provides a substantial application-like workflow with a clear product reason.

The plugin owns its surface, not the surrounding WordPress administration shell.

Do not redesign:

- the WordPress admin menu;
- global toolbar;
- unrelated admin pages;
- core notices from other products;

unless the scope explicitly requires integration behavior.

## Surface type

Classify the plugin UI as one of:

### Native settings extension

Use when the product mainly exposes configuration.

Prefer WordPress-native page structure, form patterns, notices, and familiar admin conventions.

### Plugin workspace

Use when users perform repeated operational work such as:

- reviewing records;
- managing queues;
- running workflows;
- monitoring integrations;
- editing domain-specific objects.

A stronger product/application UI may be justified, while still respecting the host environment.

### Hybrid

Use when a plugin has:

- WordPress-native settings;
- plus one or more application-like operational screens.

Do not force both surface types into one visual pattern.

Settings can remain native while the operational workspace uses a stronger product design system.

## Menu placement and entry point

Choose menu placement based on product weight and frequency.

For a plugin with one ordinary settings/tools screen, prefer an appropriate existing WordPress menu rather than claiming a new top-level destination.

A dedicated top-level menu is more defensible when the plugin represents a substantial repeated-use product/workspace.

Before creating a top-level menu, ask:

- Is this a frequent destination?
- Does the plugin have multiple coherent subpages?
- Is it more than ordinary configuration?
- Would placing it under Settings or Tools make discovery materially worse?

Do not create a top-level menu for branding/status alone.

## Admin navigation

Within the plugin, navigation should reflect user jobs.

Prefer:

- a small set of stable plugin sections;
- consistent page titles;
- predictable current-location state;
- clear parent/child relationships.

Avoid:

- tab-within-tab navigation;
- tabs used for unrelated product areas;
- duplicating the same destinations in both side navigation and tabs;
- icon-only plugin navigation without labels;
- custom navigation that visually conflicts with the WordPress admin shell.

If the plugin has an application-like workspace, distinguish global WordPress navigation from plugin-local navigation.

## Capability boundaries

UI visibility and actions must follow actual WordPress capabilities.

Do not design against role names such as "Administrator" when the implementation uses capabilities.

Distinguish:

- can see page;
- can view status;
- can edit configuration;
- can perform operational action;
- can delete/reset data;
- can manage network-level configuration.

Do not:

- show enabled-looking actions that the current user cannot perform;
- rely on hiding a control as the security boundary;
- imply that UI permission changes backend authorization.

When implementation uses the standard Settings API submission path, account for the capability model imposed by WordPress rather than designing an impossible lower-privilege save flow.

## Capability-limited UX

For a user who may view but not modify:

- show useful read-only state when product requirements permit;
- explain that the setting is controlled by another authority;
- avoid presenting disabled controls without explanation;
- do not repeatedly invite an unavailable action.

For inaccessible content:

- prefer correct menu/page access control;
- use permission-denied messaging only when the user legitimately reaches the route.

## WordPress-native vs custom application UI

Reuse WordPress-native conventions when they fit the task.

A custom component system may be appropriate when the plugin provides a substantial product workspace, but visual difference must earn its complexity.

A custom interface must still respect:

- WordPress admin context;
- capabilities;
- localization;
- accessibility;
- notices/status integration;
- responsive admin behavior;
- safe navigation back to WordPress.

Do not build a visually disconnected mini-SaaS for a simple settings page.

Do not force an existing coherent product workspace back to default form-table styling merely for cosmetic consistency.

## Settings API awareness

When implementation uses the WordPress Settings API, design around its real contract:

- settings pages;
- sections;
- fields;
- explicit submission;
- validation/sanitization;
- error reporting;
- capability checks.

Use the local `wordpress/settings.md` pack for detailed UI rules.

The UI/UX Skill does not replace implementation security.

## Notices and messaging

Choose the message surface by scope.

Use global/admin notice patterns for conditions that genuinely matter at admin-page scope.

Use page-local or inline feedback for:

- field validation;
- connection tests;
- local status;
- one operation.

Avoid promotional or low-value notices across unrelated WordPress screens.

A dismissible notice is not a substitute for resolving an ongoing product problem.

## Onboarding and activation

Activation is not automatically onboarding.

If activation redirects or introduces setup, preserve WordPress expectations and avoid trapping users.

Use `wordpress/onboarding-integrations.md` when first-run/setup is material.

The first-run objective should be the first successful product outcome, not completion of every optional setting.

## Integrations

External service integration should model:

- configuration;
- authorization;
- connection state;
- service health;
- synchronization state;

as separate concerns.

Do not make a masked API key look equivalent to a healthy remote connection.

Use `wordpress/onboarding-integrations.md`.

## Diagnostics and Site Health

Prefer WordPress Site Health integration for environment/health checks that fit its model.

Use a plugin-local diagnostics workspace for domain-specific operational detail that would be noisy in Site Health.

Do not create a second fake "Site Health" page that duplicates WordPress core concepts.

Use `wordpress/diagnostics-operations.md`.

## Background work

WordPress plugins often perform work outside the immediate request:

- imports;
- exports;
- sync;
- indexing;
- cache generation;
- migrations;
- cleanup;
- scheduled tasks.

Design this work as stateful operations, not as a submit button followed by an indefinite spinner.

Use `wordpress/diagnostics-operations.md`.

## Dangerous and destructive actions

Separate ordinary configuration from:

- reset;
- disconnect;
- delete data;
- uninstall cleanup;
- rebuild;
- repair;
- migration;
- bulk operations.

Explain:

- scope;
- consequence;
- reversibility;
- expected duration;
- recovery.

Do not group harmless utilities and destructive actions inside the same undifferentiated button row.

## Privacy and personal data

When the plugin collects, stores, exposes, logs, or sends personal data:

- make product-level privacy controls understandable;
- avoid collecting unnecessary data;
- avoid exposing personal data to roles/capabilities that should not see it;
- distinguish plugin settings from WordPress privacy/export/erasure tools;
- integrate with WordPress privacy tooling when implementation requires it;
- disclose external data transfer where relevant;
- avoid leaking personal data/secrets through logs and support exports.

Do not duplicate WordPress personal-data export/erasure UX merely to create a branded plugin flow when core tooling is the correct system surface.

Do not claim privacy-law compliance based on UI design.

## Data ownership and uninstall semantics

Clarify differences between:

- plugin configuration;
- cached/derived data;
- synchronized remote data;
- WordPress content;
- user/personal data;
- logs;
- generated files.

If the plugin offers "Delete data on uninstall", explain what data that means.

Do not let a broad checkbox conceal deletion of materially different data categories.

## Updates and migrations

When plugin updates require migrations or background upgrades:

- distinguish "plugin updated" from "data migration complete";
- show blocking vs non-blocking migration state;
- preserve usable areas when safe;
- explain when features are temporarily unavailable;
- provide repair/retry only when backend support exists.

Do not present an update-complete success state while required migration is still failing.

## Compatibility and dependencies

If the plugin depends on:

- another plugin;
- a theme capability;
- PHP/WordPress version;
- extension;
- remote service;
- REST access;
- cron/background processing;

communicate unmet requirements in actionable product language.

Avoid exposing raw version-comparison logic or internal dependency identifiers as the primary UX.

## Import / export

Import/export should specify scope and consequence.

Use `wordpress/settings.md` for configuration import/export.

Use `wordpress/diagnostics-operations.md` for long-running data import/export jobs.

Do not assume configuration export and operational data export are the same feature.

## Multisite / Network Admin

When Multisite is relevant, load `wordpress/multisite-admin.md`.

Never assume single-site "Administrator" semantics apply to Network Admin.

Make network-vs-site scope explicit.

## Responsive wp-admin

Validate plugin UI inside the actual WordPress admin shell.

Account for:

- expanded/collapsed admin navigation;
- narrow viewport;
- toolbar;
- notices;
- tables;
- plugin-local navigation;
- fixed/sticky controls;
- modal/dialog behavior.

Avoid fixed-width interfaces that collide with the admin shell.

For dense operational tables, prefer priority + drill-down over squeezing every column into mobile width.

## Accessibility

Plugin admin UI should support:

- semantic page structure;
- keyboard navigation;
- visible focus;
- labels/descriptions;
- understandable validation;
- non-color status meaning;
- zoom/reflow;
- reduced motion where relevant;
- accessible dialogs/menus;
- meaningful progress/status announcements.

Use native WordPress/HTML semantics before recreating standard controls.

Do not claim accessibility compliance without appropriate evidence.

## Localization, Persian, and RTL

WordPress plugin UI must be localization-safe.

Design for:

- translatable strings;
- text expansion;
- plurals/counts;
- date/time/number localization;
- language-specific direction;
- mixed technical LTR content;
- translated notices/errors;
- longer button/menu labels.

For Persian-facing UI, the REQUIRED external `persian-writing` specialist owns Persian linguistic validation.

This Product Pack retains ownership of:

- WordPress admin structure;
- interaction;
- responsive behavior;
- RTL architecture;
- component layout;
- accessibility;
- mixed-direction UI handling.

Do not treat Persian admin UI as a mirrored English screenshot.

## Light/Dark appearance

Do not invent a plugin dark mode merely because the product supports custom styling.

Use Light/Dark behavior only when:

- the host/admin environment genuinely supports it;
- the plugin provides its own substantial workspace where theme control is product-owned;
- the user explicitly requested it.

Preserve contrast and status meaning across supported appearance modes.

## Plugin QA matrix

For significant WordPress plugin work, validate representative:

### Environment

- supported WordPress version/context;
- required dependency/service states;
- single-site;
- Multisite when supported;
- `wp-admin` shell.

### Permissions

- intended full-access capability;
- read-only/limited capability when product supports it;
- denied/inaccessible state;
- Network Admin/Super Admin when relevant.

### Settings

- defaults;
- edit/save;
- validation failure;
- advanced setting;
- reset;
- import/export when present.

### Onboarding/integration

- fresh install;
- prerequisite failure;
- invalid credentials;
- connect/disconnect;
- partial setup/resume;
- successful completion.

### Operations

- healthy status;
- warning/error;
- background job;
- stuck/failed job;
- retry/cancel when supported;
- destructive maintenance.

### Admin environment

- WordPress notices;
- plugin-local notices;
- narrow admin width;
- tables/forms;
- keyboard-only path;
- focus;
- zoom/text scaling;
- RTL/LTR;
- Persian linguistic QA when relevant.

### Data/privacy

- personal-data exposure boundaries;
- support/log export;
- uninstall/delete-data controls;
- multisite scope when relevant.

Do not claim plugin-wide validation for a local pack or environment state that was not exercised.

## Current canonical WordPress references

When WordPress behavior may have changed, prefer current WordPress Developer Resources.

Relevant canonical guidance includes:

- Plugin Handbook — Settings / Settings API
- Plugin Handbook — Administration Menus
- Plugin Handbook — Roles and Capabilities
- WordPress Site Health APIs
- WordPress admin notice hooks/guidance
- Plugin Handbook — Privacy
- Plugin Handbook — Internationalization
- Advanced Administration Handbook — Multisite / Network Admin

Official WordPress guidance refreshes implementation/context details; this local Product Pack remains the design authority.
