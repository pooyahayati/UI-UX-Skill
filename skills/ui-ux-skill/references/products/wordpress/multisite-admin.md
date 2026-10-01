# WordPress Plugin Multisite and Admin-Scope Rules

Use this local rule pack when the active product route includes `wordpress-plugin` and WordPress Multisite, Network Admin, network-wide settings, per-site overrides, network activation, or site-vs-network capability differences are materially in scope.

## Scope first

Before designing a Multisite surface, determine whether the setting/action applies to:

- one site;
- all sites;
- network defaults;
- selected sites;
- current user;
- network administrator only.

Do not rely on page location alone to communicate scope.

## Network Admin vs site admin

Network Admin is a distinct administrative context.

A network-level action should not masquerade as a normal site-level setting.

Where a plugin has both:

- keep labels and navigation consistent enough to recognize the plugin;
- clearly communicate current scope;
- avoid duplicating settings whose ownership belongs only at one level.

## Capabilities

UI visibility and enabled actions must follow actual WordPress capabilities.

Do not assume "Administrator" always means network authority.

Multisite may require Super Admin/network capabilities for operations that ordinary site administrators cannot perform.

The UI/UX layer must not redefine capability semantics.

## Network defaults and site overrides

When a network default can be overridden per site, make precedence explicit.

A site administrator should be able to understand:

- current effective value;
- network default;
- whether override is allowed;
- current override;
- how to return to inherited behavior.

Do not use an empty field as an ambiguous synonym for "inherit."

## Network-enforced settings

If the network locks a value:

- show the effective value;
- identify that it is controlled by Network Admin;
- disable editing without making the setting look broken;
- provide a useful explanation.

Do not display a saveable-looking control that cannot actually be changed.

## Bulk / selected-site operations

For actions across sites:

- show selection scope;
- confirm affected count;
- distinguish all-sites from selected-sites;
- handle partial failure;
- provide result summary;
- support retry for failed sites when backend behavior allows.

Do not show a single success notice when some sites failed.

## Network activation and plugin availability

If plugin availability depends on network activation or Network Admin configuration, explain that relationship in product language.

Do not instruct a site administrator to perform an action they cannot access.

## Cross-site status

For network dashboards/status lists:

- identify site;
- show relevant status;
- allow sorting/filtering when volume warrants;
- distinguish unavailable, not configured, healthy, warning, error;
- avoid loading expensive per-site diagnostics synchronously across a large network.

## Data residency / ownership

When configuration or plugin data exists at both network and site level, the UI should reflect the actual ownership model.

Do not invent copy/move/sync semantics not supported by storage architecture.

## Import / export in Multisite

Clarify whether export/import applies to:

- current site;
- network defaults;
- selected sites;
- all sites.

Prevent accidental network-wide overwrite.

## Destructive network actions

Network-wide reset/delete/rebuild operations require stronger confirmation than site-local equivalents.

Communicate:

- number/scope of affected sites;
- data categories affected;
- reversibility;
- expected duration;
- whether work is synchronous or backgrounded.

## Responsive behavior

Network lists can be large and data-dense.

On narrow `wp-admin`:

- prioritize site identity and status;
- provide detail drill-down;
- avoid squeezing all columns;
- keep bulk actions understandable.

## Persian / RTL

For Persian-facing Network Admin UI, route wording/linguistic QA to `persian-writing`.

Maintain WordPress/admin direction and mixed technical-content handling.

## Validation checklist

Test:

- single-site installation;
- multisite site admin;
- Network Admin;
- Super Admin-only action;
- network default;
- allowed site override;
- locked site setting;
- partial bulk failure;
- network-wide destructive action;
- narrow admin width;
- RTL/LTR when supported.
