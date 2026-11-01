# shadcn/ui implementation guidance

Load for a selected shadcn/ui implementation, an affected existing shadcn/ui surface, or component-foundation selection under the active Dashboard Product Pack. Keep product classification and local mode routing intact. This is an implementation reference, not a new Product Pack, external specialist or permission to install another Skill.

## Selection and compatibility

Dashboard component-foundation selection defaults to shadcn/ui unless the user explicitly instructs otherwise. Do not require a second library-choice approval for a compatible new dashboard within an authorized build. State the default and apply it; retain ordinary scope, dependency and visual-approval boundaries. For other products, use it when explicitly selected or already suitable in the established stack; do not preload dashboard rules.

Inspect the actual frontend framework, host, installed components and styling setup. An existing component library, a locked stack or a native host is a real constraint, not permission for an automatic migration. Audit-only and narrow changes preserve the current implementation. If compatibility is unresolved, explain the concrete gap and recommend a compatible approach; do not claim shadcn/ui support by silently adding React or substituting an unofficial port. Explicit user alternatives take priority without repeated persuasion. WordPress-admin settings retain their native component contract even when a secondary dashboard route is active.

Material is a separate visual-style choice. A Material request alone neither mandates Material UI nor rejects shadcn/ui. Preserve the selected style and evaluate component fit; an explicit request for a different implementation library overrides the dashboard default. Never claim that theming shadcn/ui establishes complete Material conformance.

## Adopt only the needed components

The [official introduction](https://ui.shadcn.com/docs) describes a code-distribution approach: component source becomes part of the product and needs its own maintenance. Do not vendor the upstream repository into this Skill.

Use the current [installation guide](https://ui.shadcn.com/docs/installation) for the actual framework. Inspect the product's shadcn configuration, package manifest, lockfile, aliases and existing CSS before initializing. Choose documented stable components and a consistent primitive family; check the actual family/API rather than mixing examples from different providers. Resolve current versions at adoption and retain the product lockfile, without hard-coding a perpetual version in Skill policy.

Install only components and dependencies needed by the authorized workflow. Review generated file and dependency changes; preserve customized components and existing configuration. Regenerating a component is not a safe upgrade by default. Track upstream source/revision and local deviations; diff updates and exercise affected interactions before accepting them. External registries, paid blocks and additional agents/tools are separate choices, not implied by this default.

## Product foundations and owner controls

Start from the approved palette, fonts, type scale, spacing, density, shape, motion and icon decisions in `DESIGN.md`. Upstream presets and blocks are implementation starting points, not approval to replace those decisions or invent dashboard features.

Map resolved semantic tokens to the documented [theme variables](https://ui.shadcn.com/docs/theming), including background/foreground pairs, primary, muted, destructive, border, input and focus ring. Map sidebar and chart roles where used. Keep primary and dark values coherent, and route typography, spacing and component variants through shared sources instead of page-level overrides.

Where owner appearance management is in scope, follow [runtime governance](runtime-ui-governance.md): validated draft, preview, publication, history and rollback. Map allowed font uploads, semantic icon assignments, density and colors through prepared adapters. A generated theme file is not an implemented owner settings panel. Do not expose arbitrary CSS/JS, import paths or component code. Preserve accessibility floors, permissions, workflow semantics and stored valid preferences; only expose controls that demonstrably affect their consumers.

## Component choices by job

Use the active product's workflow and state contracts, then consult only the relevant official component documentation.

| Job | Starting point | Product-specific checks |
| --- | --- | --- |
| Navigation | [Sidebar](https://ui.shadcn.com/docs/components/sidebar), breadcrumbs, sheet | Role-visible destinations, current location, collapse/mobile behavior and focus return; do not impose a fixed shell. |
| Records and work queues | [Data Table](https://ui.shadcn.com/docs/components/data-table) | The guide composes a table using TanStack Table, not a complete product data backend. Define row identity, server/client filter scope, selection across pages and bulk-action permissions. |
| Trends and metrics | [Chart](https://ui.shadcn.com/docs/components/chart) | The documented chart approach uses Recharts. Preserve units, time range, freshness, missing-data semantics and accessible exact-value alternatives; no decorative charts. |
| Editing and filtering | [Components index](https://ui.shadcn.com/docs/components): field, input, select, combobox, date picker | Labels, validation, unsaved values, asynchronous search and recovery. Date language, calendar system and timezone are separate requirements. |
| Feedback and confirmation | [Components index](https://ui.shadcn.com/docs/components): alert, dialog, alert dialog, skeleton | Truthful pending/error/uncertain/success states, keyboard/focus and local refresh. A toast alone must not hide a recoverable error. |

## Language, RTL and responsive review

For materially needed animated interactions, use [interactive motion guidance](interactive-motion.md).
shadcn/ui remains the component foundation, not a complete motion engine. CSS is
sufficient for simple transitions; Motion and selected Animate UI source are
conditional complements, not mandatory installs or permission to replace local
components. Preserve the selected primitive family and resolved owner/user motion
policy, including static accessible alternatives.

Use the product's primary language/direction, not the chat language. For Persian without an approved alternative, retain the Skill's Vazirmatn default and the required Persian-writing route. Verify actual font files and weights; a CSS family declaration alone is insufficient.

Follow current [RTL guidance](https://ui.shadcn.com/docs/rtl) for the chosen setup. Automatic CLI transformations depend on supported styles and RTL configuration; existing generated components may require migration. Check direction propagation through providers and portals, logical positioning and directional animation. Inspect sidebar, calendar and pagination behavior separately; do not assume a root direction attribute fixes every component. Mirror only directional icons, never charts or quantitative meaning.

Keep mixed-script identifiers isolated and localize dates/numbers deliberately. Calendar support must be checked for the selected component/version; translated labels alone do not create a Persian calendar.

Use [the existing sequential review](design-foundation-workflow.md): one responsive primary-language/direction proposal applying settled foundations, corrections and approval, then the applicable theme gate, then only needed and owner-authorized secondary language/layout. Required dark needs approval; reuse approved primary-dark coverage or an evidenced light-only non-applicability decision as defined by that workflow. Do not produce simultaneous alternatives because a preset generator supports them.

For affected components, test realistic narrow and wide widths, long labels, keyboard/focus, overlay dismissal/return, validation/recovery and the actual direction/theme under review. Preserve table semantics and prioritize columns or deliberate horizontal comparison instead of forcing every table into cards. Check contrast and chart alternatives in dark mode; inspect hydration/theme flash and route payload when relevant. Library accessibility or mobile claims are not product test evidence.

## Decision and evidence record

Use the existing `DESIGN.md` sections for components, decisions and verification: selection source (dashboard default, explicit choice or existing stack), overrides/compatibility constraints, component source/revision and primitive family, semantic mappings, prepared owner controls, affected states and actual validation gaps. Do not create a second handbook or duplicate live token values.

Official documentation was consulted on 2026-10-16. Recheck the relevant linked API, compatibility and maintenance facts when implementing; this reference is not an exhaustive copied component catalog or a runtime dependency installation.
