# Runtime UI Governance and Owner Control Center

Use this reference only when runtime UI/UX configuration is justified by the product.

The goal is a safe control plane for presentation, not a no-code application builder.

## Decide whether to build it

A runtime Owner Control Center is useful when one or more are true:

- owners need to adjust branding without deployment
- the product is white-label or multi-tenant
- appearance defaults change frequently
- operators need configurable density/table defaults
- multiple environments or tenants need import/export
- user personalization needs owner-defined boundaries

Avoid it when:
- the product is small and rarely changes
- design changes are infrequent and developer-owned
- configuration complexity would exceed its operational value

## Access model

The control center should be available only to an explicitly authorized role such as:

- System Owner
- Product Owner
- Super Admin

Do not invent a new privileged role silently if the product has an existing authorization model.

Authorization must be enforced server-side or at the trusted application boundary.

Hiding a route/menu item is not sufficient access control.

## Safe configuration categories

Reasonable owner-configurable areas can include:

### Branding
- approved logo variants
- favicon/app icon
- primary/accent semantic colors
- approved brand preset

### Theme
- allowed Light/Dark/System modes
- default theme
- semantic palette within validated constraints

### Typography
- allowlisted local font family/pair
- approved type-scale preset
- compact/balanced/comfortable sizing preset

### Density and surfaces
- compact/balanced/comfortable density
- approved radius preset
- approved surface/elevation preset
- motion level

### Navigation presentation
- expanded/compact default
- allowed presentation variant

Do not let presentation settings silently change destination hierarchy or permissions.

### Tables and operational defaults
- default row density
- approved page-size default
- optional column defaults
- default filter/sidebar presentation

### Charts
- approved chart palette
- grid/label density defaults

### Localization defaults
- default locale
- allowed digit/calendar/date presentation where product rules permit

### Optional dashboard presentation
- visibility/order of explicitly optional widgets
- landing view defaults

Do not allow critical content to be hidden through a generic appearance setting.

## Never expose as raw runtime design controls

Do not provide owner fields for:

- arbitrary CSS
- arbitrary JavaScript
- arbitrary HTML
- raw SQL
- API endpoints
- permission rules
- authentication behavior
- security controls
- validation rules
- critical workflow logic
- unrestricted route/navigation definitions
- unvalidated third-party asset URLs

If a power feature requires arbitrary code, it is not an appearance-setting feature.

## Lifecycle

Use a controlled lifecycle:

`Edit Draft -> Preview -> Validate -> Publish -> Active Version`

Support:
- cancel/discard draft
- version history
- rollback
- audit log
- restore defaults

Do not make every keystroke immediately live in production.

## Preview

Preview should show representative surfaces before publish.

At minimum, include where relevant:
- dashboard shell
- buttons/links/forms
- table
- status colors
- Light/Dark
- RTL/LTR
- mobile/desktop
- logo variants
- charts

Preview must not alter the active configuration for other users.

## Validation before publish

Validate:

- schema/type constraints
- color contrast
- focus visibility
- semantic status distinction
- logo legibility
- Light/Dark compatibility
- typography/layout breakage
- RTL/LTR compatibility
- unsupported asset/font selections
- required fields
- configuration compatibility with current schema

Block publish for invalid or unsafe configurations.

Warnings can be used for non-blocking quality concerns, but distinguish them from hard failures.

## Version history

Each publish should create an immutable or reconstructable version containing:

- version identifier
- timestamp
- actor
- schema version
- changed fields
- optional change note
- validation result

Prefer diff visibility.

## Rollback

Rollback should:
- require appropriate permission
- create a new active version pointing to or copying a prior valid configuration
- preserve audit history
- re-run compatibility validation when schema versions differ

Avoid destructive deletion of history.

## Audit log

Record important actions:

- draft created
- setting changed
- asset replaced
- validation failed
- published
- rolled back
- reset to default
- import/export

Do not log secrets or sensitive raw assets unnecessarily.

## Reset

Support scoped reset where useful:

- reset field
- reset section
- reset theme
- reset branding
- reset all appearance settings

High-impact resets should require clear confirmation.

## Import and export

When products need configuration portability, support a versioned, validated export format.

Useful for:
- development
- staging
- production
- multiple tenants
- backup/restore

Import must:
- validate schema
- reject executable content
- show a diff/preview
- not publish automatically unless explicitly requested
- handle version migration

## Multi-tenant systems

Clarify scope:

- platform default
- tenant/account owner configuration
- user preference

Do not leak one tenant's configuration to another.

## Owner vs user control

Owners define product defaults and allowed ranges.

Users can personalize only explicitly permitted fields.

When owner constraints can invalidate stored user settings or saved views, apply `preference-reconciliation.md`.

Example:

Owner permits:
- Light/Dark/System
- Compact/Balanced/Comfortable density

User selects:
- Dark
- Compact

The owner should not need to overwrite every user's personal preference to change an unrelated brand color.

## Reliability

Provide safe fallbacks when runtime configuration:
- is missing
- is partially invalid
- fails to load
- references an unavailable asset

The application should still render with design-system defaults.

## Operational UX of the control center

The control center itself should include:
- grouped settings
- search when settings are numerous
- current vs draft value
- live or side-by-side preview
- validation messages near affected controls
- publish summary
- version history
- rollback
- reset
- audit history

Avoid exposing token names such as `--surface-3` to non-technical owners unless the product specifically serves technical administrators.

Use human product language.

## QA

When this feature exists, test:

- unauthorized access rejected
- draft isolated from published config
- preview accuracy
- invalid values blocked
- publish atomicity
- cache invalidation
- rollback
- reset
- audit history
- import/export
- Light/Dark
- RTL/LTR
- responsive surfaces
- user-preference precedence
- fallback when config loading fails
