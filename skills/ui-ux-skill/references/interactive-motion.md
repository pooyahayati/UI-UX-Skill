# Interactive motion for web products

Load when implementing or reviewing interactive web animation, selecting a motion provider, or defining owner motion controls. Apply [shared motion rules](shared/motion.md) and the active Product Pack first. This is optional implementation guidance, not a new product route, visual style, external specialist or automatic dependency installation.

## Choose from the product need

Identify the task/state change, audience, interaction frequency, existing stack and approved motion baseline. Recommend the smallest useful treatment and explain its purpose; a quiet interface is not a defect. Preserve explicit user choices, established components and native host requirements. An audit or narrow correction does not authorize migration or an appearance panel.

| Need | Preferred starting point | Boundary |
| --- | --- | --- |
| Color, focus, simple disclosure or small state transition | Existing component behavior and CSS | No animation dependency solely for a hover effect. Never delay focus visibility. |
| Coordinated enter/exit, layout continuity or product-justified gestures in a compatible React app | [Motion for React](https://motion.dev/docs/react) | Select for a concrete need, not every web app. Keep business state independent of animation completion. |
| A ready animated disclosure, sheet, tab, control or icon that fits the product | Selected [Animate UI components](https://animate-ui.com/docs/components) | An independent, Motion-based open-code distribution, not an official shadcn/ui extension or a replacement for the whole component foundation. |

Keep shadcn/ui's dashboard foundation decision separate from the motion decision; other products do not acquire a dashboard route. Keep Material style separate too. In non-React or native-host products, reuse compatible platform capabilities; do not add React or promise that React examples are portable. Preserve WordPress settings' native component contract.

For a specifically evidenced need, [AutoAnimate](https://auto-animate.formkit.com/) can simplify list insertion/removal/reordering, while [GSAP](https://gsap.com/docs/v3/) can support complex timelines or scroll-led presentation. Neither is a default or an extra engine to install alongside Motion without justification. Avoid two engines controlling the same element/property.

## Adoption and maintenance

Before adding a provider/component, inspect the actual framework, existing animation engine, primitive family, styling setup, package manifest and lockfile. Verify current official API, framework compatibility, maintenance, license and dependency/security implications for the selected source. Premium examples or services are separate choices; do not assume they are included or authorized.

Animate UI distributes editable source built with React, Tailwind CSS and Motion. Review the selected component and dependencies before importing it; preserve local modifications, accessible semantics and primitive APIs. Do not copy its whole registry, install its tooling/agents, or overwrite an existing customized component. Record upstream source/revision and local changes so later updates are reviewable. Reuse one compatible Motion dependency where applicable.

Apply approved palette, fonts, spacing, density, shape and semantic icons from `DESIGN.md`; demos are not a new visual baseline. Map shared durations, easing, displacement and interaction variants through existing semantic tokens/adapters. Centralize repeated decisions without creating a separate token system or unnecessary abstraction. Animated icons keep their semantic assignments, accessible labels, state pairs and meaningful static fallback.

## Patterns by job

| Interaction | Useful motion | Behavior that must survive motion being interrupted or off |
| --- | --- | --- |
| Filter/disclosure | Explain the region opening/closing | Expanded state, keyboard access and immediate usable content; hidden/exiting content is not accidentally focusable. |
| List insertion or reorder | Show where the changed record went | Stable record identity, focus/selection and correct data order. Do not animate every cell of a live/virtualized table. |
| List to detail, sheet or dialog | Preserve location/context | URL/back behavior where applicable, semantic open state, escape/dismissal and focus return; do not retain an invisible input-blocking overlay. |
| Multi-step form | Clarify the active step | Draft values, validation messages and correct focus on the new step; rapid repeated actions cannot skip required validation. |
| Save, copy or other feedback | Briefly acknowledge the real result | Pending, failure, uncertain and confirmed outcomes remain distinct; no timer-based success or invented progress percentage. |
| Drag/swipe | Reinforce direct manipulation when the task needs it | Keyboard and visible non-drag alternatives, cancellation and touch scrolling; gestures cannot be the only way to complete the task. |

Keep high-frequency operational surfaces restrained. Avoid looping decorative backgrounds, cursor effects, scroll hijacking or routine celebratory motion in work queues. Never require a hover, animation or scroll effect to reveal essential content. Mirror motion only when its meaning follows layout direction; preserve time, physical direction and quantitative data semantics. Propagate actual direction into overlays/portals and verify the chosen primitive's behavior.

## Accessibility and resolved motion policy

Use a shared resolved policy for CSS, Motion components, copied Animate UI components, animated icons and independent consumers. A library provider does not automatically govern CSS animations, imperative animation calls, video or every third-party primitive.

- Respect `prefers-reduced-motion` on first use and when it changes. Product settings may reduce motion further, never override an operating-system or user request for less motion.
- Motion's `MotionConfig reducedMotion="user"` supports the OS preference; `useReducedMotion` supports specific alternatives. The documented reduction disables transform/layout animation but retains other values such as opacity. It is not a complete implementation of an owner-selected **off** mode. Resolve that mode explicitly for every claimed consumer; do not set `reducedMotion="never"` to enforce owner branding.
- Under reduced motion, replace large movement, parallax and looping effects with immediate state changes or a brief non-spatial alternative where useful. In off mode, eliminate animated transitions, including fades, while preserving static progress/status, focus and all actions.
- Do not make mutations, validation, navigation, cleanup or focus restoration depend solely on `animationend`, exit duration or a callback that may not run. Interrupted, disabled and failed-load paths must settle to a usable state without losing drafts or duplicating actions.
- Preserve keyboard order, focus visibility, labels and status announcements; animation and color alone are not feedback. Manage leaving overlays with the primitive's supported lifecycle instead of leaving hidden interactive content behind.
- Avoid an initial burst before preferences/configuration resolve. Use a static usable initial state where client preference is unknown, preserve server/client markup compatibility, and clean up listeners/animations on unmount or route change.

The [Motion accessibility guide](https://motion.dev/docs/react-accessibility) and [Animate UI accessibility guide](https://animate-ui.com/docs/accessibility) describe provider configuration; neither establishes product accessibility merely by installing the package.

## Owner settings and handbook

When appearance management is already in scope, expose a human-labeled motion level through the [existing runtime lifecycle](runtime-ui-governance.md): **off**, **subtle**, **standard**. Reuse accepted equivalent presets; do not rename/reset persisted choices silently. Preserve the approved product default; if none exists, recommend subtle for task-heavy web apps and record it as a proposal, not owner approval.

Owner level is the product ceiling; an available personal preference can lower it. Apply platform/accessibility constraints before rendering: for example, owner standard + OS reduced uses the reduced-motion treatment; owner off + user standard stays off; user off stays off. OS reduction remains effective even if no personal settings page exists. Do not expose a setting that disables this protection.

Keep preset definitions and supported duration/easing bounds in design-system source. Owners select approved presets, not raw JavaScript, CSS, keyframes, spring objects, import paths or remote registries. Do not expose arbitrary duration multipliers that can slow tasks or distort progress. Implement only controls with real consumers; animation-library selection is a development decision, not a runtime owner switch.

Reuse existing authorization/scope, private draft, preview, validation, publication, history, reset and rollback. Unknown/invalid values are rejected at write time; loading failures retain a safe last-valid/default policy and cannot enable stronger motion than the effective preference allows. Preserve prior configuration and history with compatible migration if a schema changes. No admin surface means no invented role/backend; a narrow animation fix does not authorize a new panel.

In the existing `DESIGN.md` sections, record the selected provider or no-library decision and rationale, affected interactions, token/preset sources, reduced/off alternatives, directional meaning, supported owner/user controls and actual verification gaps. Link executable values and runtime history rather than duplicating them. Use the [canonical primary, applicable-theme and authorized-secondary gates](design-foundation-workflow.md#phase-2--theme-applicability-and-required-dark-review); animation does not reopen settled foundations or require unnecessary language variants.

## Verify the affected behavior

Check a representative real interaction, not only a static screenshot:

- Normal, reduced and off policies, including preference changes while a transition is running; verify CSS and independent consumers as well as provider-controlled elements.
- Keyboard/touch alternatives, focus/overlay lifecycle, interruption/repeated activation, real pending/error/uncertain/success states and preserved drafts.
- Actual product direction, narrow/wide layout and relevant theme under the current approval phase; long labels and mixed-script identifiers where applicable.
- When owner controls exist: private preview isolation, authorized publish/reopen/reset/rollback, denied/invalid changes, configuration-load failure and owner/user/OS precedence. Verify changed consumers, not just persisted form values.
- Representative mobile performance and added route payload when a dependency or broad motion is introduced; compare observed behavior, avoid per-frame full-app state updates, and reduce work in long lists. Do not assert a frame rate or bundle saving without measurement.

Report source review, automated checks, rendered interaction evidence and owner approval separately. Documentation is not a tested runtime adapter or evidence for a future product. Official provider documentation reviewed 2026-10-16; recheck relevant APIs and compatibility at adoption.
