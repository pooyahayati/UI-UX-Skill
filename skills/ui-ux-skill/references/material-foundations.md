# Product-personalized Material foundations

Load only after the [Material activation decision](material-design.md) is selected
and foundation work is genuinely in scope. This is a style overlay, not a new
token system or discovery lifecycle. Reuse [discovery](discovery-and-profile.md),
the active Product Pack and only the relevant modules routed by
[Design System architecture](design-system-architecture.md). A narrow repair
uses its affected baseline; it does not trigger this whole foundation workflow.

## Recommend for the actual product

Inspect the approved handbook, product requirements, real assets and value
sources first. Distinguish known decisions from assumptions. Fill only material
gaps: principal tasks and their consequences, audience familiarity/access needs,
brand personality, content density, primary device/input, connectivity, and how
much expression helps rather than distracts. Do not ask again for settled facts
or require a novice to choose technical role names.

Give one professional recommendation with a product/audience reason and a
meaningful tradeoff. Use plain outcomes such as easier scanning, clearer next
action or more welcoming onboarding. Calm versus expressive is not an age rule:
critical repetitive tasks may need restrained treatment; unfamiliar guided work
may benefit from selective emphasis. Preserve labels and familiar workflows in
both. A recommendation is proposed until actual acceptance or named delegation;
changing a protected global foundation still requires its owning decision.

Use [selected research](design-research.md) only for a concrete unresolved
question. Research is supporting evidence, not guaranteed usability, a universal
style prescription or owner approval. Stop this slice once the representative
workflow has enough usable foundations; retain nonblocking unknowns and revisit
triggers in the existing handbook.

## Map roles, do not replace the value authority

Inspect actual theme/token/component sources and consumers. Keep their format,
names, approved scales and resolution order. The examples below are semantic
correspondences, not mandatory aliases, a complete Material token inventory or
permission to rename the project's public contracts. Add a role only for a real
missing meaning. If sources are absent, record a proposal/gap rather than claim
implemented tokens. Do not introduce a separate Material or RTL token database.

| Material concept | Existing product contract to inspect | Personalization / constraint |
| --- | --- | --- |
| Primary / on-primary; supporting accent/container pairs | `action.primary`, matching foreground and component action roles | Retain accepted brand intent; pair foreground with its actual fill. A brand swatch is not automatically a usable control color. |
| Surface / on-surface; surface containers | `surface.canvas/default/raised`, `text.primary/secondary`, relevant container roles | Select layers by hierarchy and content; do not tint every region or flatten all surfaces to one token. |
| Outline / lower-emphasis separator | Strong interactive boundary versus decorative border roles | Keep recognizable controls and focus; a decorative separator is not a sufficient input boundary by assumption. |
| Error / on-error and error-container pair | `status.danger`, validation message/background roles | Preserve error meaning and text. Success, warning, info and chart series remain product-defined; do not repurpose tertiary as a universal status. |
| Display, headline, title, body, label roles | Existing typography roles and actual family/weight/size/line-height sources | Map only used roles; retain approved scale and readable hierarchy. Data/code roles stay product-specific, not forced into display typography. |
| Spacing/density, shape and elevation | Existing gap/gutter/control sizing, radius and layering roles | Coordinate touch/scanning needs within settled scales. Radius/shadow are not universal decoration; do not create a token for every CSS property. |
| State treatment and purposeful motion | Existing selected/current, hover, pressed, focus, busy/recovery and motion roles | Appearance cannot change semantics; focus stays distinct and essential state remains understandable without color or animation. |
| Icons | Prepared semantic family/per-use assignments and real fallback consumers | Preserve meaningful labels, family coherence and selective directional mirroring. Material Symbols is optional; a font name does not supply assets. |

Use the existing [token hierarchy](design-system/tokens-foundations.md) for
primitive/semantic/component dependencies and
[color/theme rules](design-system/color-theme.md) for contrast and status. Test
the resolved pair on its actual surface/state; do not claim accessibility from
correct role names or an automatic palette alone. If an approved raw color
cannot meet a protected floor, retain identity where safe, propose a compliant
role treatment and surface the scoped conflict rather than silently restyle.

Reuse [typography](design-system/typography.md): supplied licensed assets, real
weights and script coverage. Preserve an accepted alternative font. For a
Persian-facing foundation without one, use the existing Vazirmatn default and
inspect its real assets; an English product does not acquire Persian fonts from
the conversation. Do not impose Roboto or pretend font rendering was checked.
Supported owner font upload/selection stays under existing asset validation and
runtime governance, not a new feature created by this guide.

Use [spacing/density](design-system/spacing-density-layout.md) and
[responsive variants](design-system/responsive-variants.md): the primary target
comes from actual use, not a universal desktop/mobile canvas. Preserve meaning
when adapting layouts and retain readable text, usable hit areas, keyboard focus,
zoom and long-label tolerance. Compact data need not imply tiny touch controls;
comfortable onboarding need not enlarge every repetitive data row.

## Themes, language and expression

Plan semantic dark roles and affected states early, but produce/review only the
primary-language/direction/theme proposal first. Derive dark after that revision
is approved; secondary language/layout only after dark approval when the product
needs it and the owner authorizes it. No simultaneous language/theme gallery and
no invented bilingual scope. Use real content and existing formats; preserve
mixed-script identifiers rather than indiscriminately mirroring them.

Dark is not color inversion: maintain action/foreground pairs, readable surfaces,
status meaning and focus across supported contexts. Respect actual forced-color
and contrast preferences using the existing theme contract; do not fight them
for branding. Planning roles does not prove complete dark support.

Reuse [component states](design-system/component-states.md) and scope-relevant
Shared motion/accessibility rules. Motion must explain an action, transition or
state, not decorate every interaction; honor reduced motion and keep equivalent
information without it. If expressive treatment helps a key step, recommend it
selectively while keeping familiar navigation, labels and recovery intact.

## Handbook handoff and next boundary

In the authorized existing `DESIGN.md`, record the recommended treatment,
product-fit reason/tradeoff, actual acceptance/delegation and scope/revision,
adopted research with its limitation, exceptions and links to real value sources
and consumers. Record gaps and later validation needs. Do not copy independently
editable live values or turn an observed source into owner approval.

Keep appearance control classifications under existing locked/owner/user/code-only
rules. Only actually prepared capabilities can become runtime choices; fonts,
icons, palette, density and motion must retain protected bounds and actual
permission/storage/consumer ownership. Product without admin gets no invented
backend; host-owned surfaces keep native rules. Runtime Material adapters are
R9.5 work, not delivered by documenting them.

This guide delivers foundation decisions and source mapping only. Component
guides/stack-fit, actual sequential samples, runtime changes and independent or
rendered acceptance remain R9.3–R9.6. Keep those outcomes unverified until done.

Official role starting points reviewed 2026-10-06:
[color roles](https://m3.material.io/styles/color/the-color-system) and
[typography roles](https://m3.material.io/styles/typography/applying-type). Color
and typography role semantics were available in indexed official content; direct pages require
JavaScript. Recheck the relevant current specification and real implementation
before exact component values or coverage claims. The local mapping above is a
project integration recommendation, not a mandated Google namespace.
