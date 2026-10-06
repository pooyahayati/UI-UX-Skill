# Optional Material Design — activation and scope

Use this local overlay only for an actual Material style decision or an existing,
evidenced Material baseline within the affected UI scope. It is not a Product
Pack, external specialist, component library, or default house style. Classify
the product first; keep its active modules, Shared Rules and Design System
contracts authoritative. Do not load this reference merely because the product
is mobile-first, a screenshot resembles Material, or the word occurs in a
backend task. Ordinary non-Material work retains its normal route.

## Decision states

| State | Evidence and next action | Application/loading boundary |
| --- | --- | --- |
| Selected | Owner explicitly selects Material, accepts a product/audience-based recommendation, or explicitly delegates this named style decision and the agent actually selects it within that scope. | Apply only within the selected scope and approved foundations; consult only relevant available local guidance. Selection is not sample approval or implementation/library authority. |
| Recommended, unaccepted | Agent proposes Material with product/audience rationale, fit, tradeoffs and a clear owner decision. Acceptance has not been received. | Record the recommendation separately; request the material style decision when needed. Keep the approved/observed baseline; do not apply the overlay or load component catalogs. |
| Rejected | Owner declines Material or chooses another style. | Retain the chosen baseline. Do not repeatedly reopen the rejection without a new material requirement or owner request; no Material component loading. |
| Inactive | Material has not been selected or recommended for this product/scope. | Continue the ordinary product route without Material reads or changes. No mandatory style interview for a narrow task. |

If evidence is ambiguous or conflicting, leave selection unresolved and preserve
the last demonstrably approved baseline. A keyword, silence, preselected option,
supplied image, or acceptance of functionality is not style acceptance. Extract
likes/dislikes and inferred reference traits separately, with their source and
uncertainty. A rejection of a new recommendation does not erase an independently
approved existing baseline outside that decision's scope.

Professional recommendation remains part of relevant discovery: explain why a
style might fit the actual audience, tasks, brand and constraints, and offer a
useful default to an owner without design expertise. Recommend Material only
when justified; do not turn that recommendation into mandatory selection.
General coding autonomy, permission to choose colors or delegation of a small
component does not delegate the product-wide style decision.

## Existing handbook, not another authority

When handbook work is authorized, record in the existing `DESIGN.md` decision
table: subject/scope, candidate style, state above, recommendation rationale,
source/actor and actual acceptance or named delegation, rejection if applicable,
date (or explicit unknown), handbook revision and the style actually selected.
Keep the candidate/recommendation distinct from the active baseline. Preserve
inherited approvals and do not invent evidence. Use
[handbook authority](design-handbook.md) and
[incremental decisions](incremental-design-decisions.md); no second design book,
live token database or forced document creation during audits/narrow repairs.

## Scope and protected behavior

- **New/broad UI:** selected Material is a presentation overlay personalized to
  the product, audience and settled foundations. Preserve approved palette,
  actual font assets, sizing, spacing, responsive priorities, semantic roles,
  access, states and recovery. Do not impose Roboto, Google colors, uniform
  rounding, expressive motion or a new interaction model on every product.
- **Targeted correction:** reuse the evidenced baseline and only affected
  modules. No global restyle, rediscovery, sample phases or new admin panel just
  to repair one component. If selection is absent, do not introduce Material.
- **Audit only:** consult this overlay only when the existing selected baseline
  is relevant to the requested assessment. Report gaps; do not edit code,
  configuration, assets or create/migrate `DESIGN.md` without authorization.
- **Backend only:** no UI routing/application; mentioning Material does not
  activate this Skill or authorize a frontend change.
- **WordPress/host UI:** native host rules and existing plugin boundaries win.
  Selection in a plugin-owned surface does not authorize restyling the host.
- **No admin:** do not invent a backend, privileged role or settings panel.
  Existing runtime controls, when actually in scope, retain locked floors,
  permissions, validated prepared assets, preview/publication and reversal.

Use actual product language/direction, not the chat language. Preserve the
existing sequence: one responsive primary-language/direction proposal using
settled foundations; corrections and scoped approval; derived dark review;
secondary language/layout only when needed and owner-authorized. Material does
not mandate multilingual products or simultaneous variants.

## Selection is not implementation-library approval

Prefer the existing stack. A Material decision does not install a dependency,
choose Material Web, migrate a framework, add a cloud service or page builder,
appoint a new specialist, or start an agent. Respect the existing delegation and
implementation authority. Official guidance and a library's real availability
are different evidence; Android examples do not establish mobile-web support.

For a selected mode with foundation work genuinely in scope, read
[product-personalized foundations](material-foundations.md). Narrow repairs do
not load the whole foundation workflow. Use [selected research](design-research.md)
only for an active question; the same index is useful outside Material without
activating this overlay.

For selected Material with component work in scope, use the lean
[component index](material-components.md), then only the affected workflow family.
Read [stack fit](material-stack-fit.md) only for an actual implementation/provider
decision. Do not load families for recommended/unaccepted, rejected, inactive or
backend-only work. Audit-only use remains read-only; narrow tasks retain scope.

For selected Material with new/broad sample work in scope, read
[sample/handbook integration](material-samples.md). It reuses the canonical
sequential phases; narrow/audit/backend work does not load this guide.

For selected Material with runtime appearance work actually in scope, read
[bounded runtime adapters](material-runtime.md). Reuse existing governance and
connected prepared consumers; do not load this for an unrelated narrow fix,
backend-only task or a product without an authorized appearance surface.

Activation, foundations/research, component, sample and runtime instructions are
available locally. Full independent/rendered mode acceptance remains separate
R9.6 work. A guide does not establish implemented controls in a product. Do not
preload the official catalog; consult official pages only for a concrete need
and label unsupported/custom patterns honestly.

Official source starting points checked 2026-10-06:
[Material Design](https://m3.material.io/) and
[foundations](https://m3.material.io/foundations/). These describe an adaptable
design system; the consent/authority rules here are project governance, not
claims that Google mandates this workflow.
