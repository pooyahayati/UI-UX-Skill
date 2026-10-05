# Runtime UI Governance and Owner Control Center

Use this reference when runtime appearance management is within approved scope. Its activation boundary is owned by `discovery-and-profile.md#foundation-activation-and-ownership`.

The goal is a safe control plane for presentation, not a no-code application builder.

## Setting contract and actual consumers

For each offered control, identify its human label, default/value source, allowed type/range or prepared preset, affected roles/states/themes, scope owner and write permission, dependencies, actual consumers and reset/failure behavior. Include supported body/heading/label sizes, weights and line height, spacing/control/table density, borders/radius/elevation, component variants, motion and chart/diagram presentation where relevant; a font selector or background color alone is not the agreed appearance capability. Do not invent controls for absent product surfaces.

Keep scopes explicit: public product, owned admin UI, tenant/account and permitted user preference are not interchangeable. A host-controlled surface must keep host constraints; owner appearance values cannot change another tenant, resource access or locked readability/interaction floors. `DESIGN.md` records supported contracts and links to defaults/configuration sources, not a second manually synchronized settings database.

Resolve configuration once through the existing stack's stable theme/token boundary. Map independent consumers such as chart canvases/SVG, tooltips/overlays, icons, error screens and approved assets through supported adapters; plain CSS inheritance is insufficient when a consumer bypasses it. Name these consumers in the affected verification. No control is accepted merely because a form saves a value: change it through the real panel, observe every claimed representative consumer, refresh/reopen and reverse it without editing component source.

## Decide whether to build it

New/broad work with an admin surface includes bounded appearance management in the delivery plan under the discovery activation contract. Reuse native/host controls; do not infer a new backend or unlimited customization.

For an explicitly scoped addition to an existing product, useful signals include:

- owners need to adjust branding without deployment
- the product is white-label or multi-tenant
- appearance defaults change frequently
- operators need configurable density/table defaults
- multiple environments or tenants need import/export
- user personalization needs owner-defined boundaries

For a narrow correction, do not introduce a new panel without separate scope authorization. Existing-product additions should justify their operational value; this is not an exemption from the in-scope new/broad-work requirement.

## Access model

The control center should be available only to an explicitly authorized role such as:

- System Owner
- Product Owner
- Super Admin

Do not invent a new privileged role silently if the product has an existing authorization model.

Authorization must be enforced server-side or at the trusted application boundary.

Hiding a route/menu item is not sufficient access control.

## Design-system boundary

Runtime configuration is not the design-system source of truth.

Use:

`Design System Source -> Validated Runtime Configuration -> Resolved Runtime Tokens -> Components`

Owner configuration may select approved semantic tokens, semantic values, or presets.

It must not redefine:

- token alias/reference graph;
- component state contracts;
- responsive breakpoint logic;
- product semantic meaning;
- arbitrary CSS/JavaScript;
- authorization/security;
- validation/business rules.

Read `design-system-architecture.md` and `design-system/governance-migration.md`.

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
- owner-uploaded font family/pair admitted through the validation lifecycle below
- approved type-scale preset
- compact/balanced/comfortable sizing preset

### Owner font assets

When owner Design and Appearance settings are in scope, provide font upload and
selection without requiring component-code edits. For Persian defaults, follow
`rtl-ltr-typography.md`; another accepted product font remains authoritative.
Do not reinterpret an allowlist as a permanently developer-only catalog:
validated uploads may become selectable scoped assets.

Use the existing trusted authorization/tenant and asset-storage boundaries.
Accept only supported font formats, enforce byte/count limits, validate actual
font content rather than trusting a filename or client MIME type, and retain
the required licensing/embedding information. Generate safe storage identifiers;
never accept raw CSS, arbitrary external URLs, executable files or unsanitized
family names as configuration. Bound any parsing/conversion and fail closed.
Use the platform's established upload protections, including CSRF where relevant;
[OWASP's upload guidance](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
informs implementation, not a claim that a parser or uploaded file is safe.

Register a validated asset ID with its actual family, styles/weight coverage,
script support and delivery location. Store that ID/role mapping in versioned
owner configuration; resolve trusted font declarations at the shared token
boundary for body, headings, controls and independent data/overlay consumers.
Do not require operating-system font installation on the owner or client device.

Upload first creates a private, validated candidate, not a public active font.
Preview representative product-language text, real weights, mixed-script values,
controls and relevant responsive/theme states; check loading failure and layout
reflow before publishing through the normal draft lifecycle. A rejected or failed
upload must leave published configuration unchanged with an actionable message.
Cancellation does not publish. Publication must retain history and support reset
to the product default and rollback. Preserve assets needed by published/history
revisions; replacing a font must not destructively overwrite them.

Record supported upload formats/limits, permission/scope, default, role mapping,
fallback and implementation status in `DESIGN.md`; routine selections belong to
runtime history. Test authorized upload/select/preview/publish/reopen/reset and
the relevant denial, malformed/unsupported/oversized file, cross-scope and
missing-asset cases. A static preview or selector over prepared fonts does not
prove that font upload, trusted persistence or publication is implemented.

### Editable icons

In-scope owner appearance management includes a prepared icon-family choice and
a visible gallery for changing individual semantic uses, not code-only icon
imports. Connect these choices to private preview, validation, publication,
persistence, history and rollback. Read [the icon adapter contract](implementation-strategies.md#icons)
for shared consumers, meaningful incomplete-family fallback, supported visual
controls and preserved accessibility/direction/state. Prepared safe assets only;
arbitrary uploaded SVG/code is not an appearance control.

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

Bind a draft to its owner/scope and base published revision. Publish one complete validated snapshot at the trusted write boundary, not partially applied fields. When the base moved, return a conflict and let the owner reconcile rather than silently overwrite a concurrent change; use the product's existing concurrency contract. A lost response leaves publication outcome unknown: reconcile the active revision before retrying instead of claiming failure or blindly duplicating a publication.

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

Distinguish current published values, a private preview and fallback defaults in state/evidence. A failing load must not leak a draft, combine incompatible fragments or show a saved/published success falsely. Preserve the last valid configuration and actionable recovery; invalid stored data is validated before resolution. Exercise missing, partial, invalid and failed-load boundaries relevant to the product. Reset starts from known defaults through the same controlled lifecycle; it must not silently delete history or publish an unreviewed change.

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
