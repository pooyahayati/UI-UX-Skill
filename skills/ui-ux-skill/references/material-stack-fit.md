# Material style is not a library decision

Read when implementation choice is genuinely in scope for a selected Material
surface. Reuse [implementation strategies](implementation-strategies.md) and
existing component/token contracts. For a narrow repair or audit, inspect the
installed provider; do not start a shopping tour or install a package.

## Decision procedure

First identify the actual stack, host, installed versions, required components,
target mobile browsers/devices, SSR/hydration needs and existing theme boundary.
Prefer configuration/extension of working primitives. If a real gap remains,
compare at most two or three suitable routes **for that product**, not all
frameworks. Check current evidence before a dependency decision:

| Criterion | Needed evidence / disqualifier |
| --- | --- |
| Maintenance / security | Stable release and installed revision, support policy, actual maintenance/security notices and dependency review. A recent automated commit or star count is not active feature support. |
| Coverage | Required component and variant → exact documented stable export/API. Separate supported, preview, custom composition and unavailable. A roadmap promise or native implementation is not web availability. |
| Browser / integration | Product target browsers versus provider policy; test forms, events, focus, portals/shadow DOM, SSR/hydration and fallback where used. A vendor support table is not actual product testing. |
| Accessibility / direction | Keyboard/touch, naming, focus, zoom, assistive technology and locale needs. Verify actual overlays and data/input semantics; library claims do not establish conformance. |
| Theming / admin | Approved semantic sources → supported provider extension points → all affected consumers/states/themes. Inspect actual font assets and effective density/shape/icon controls; do not promise runtime support from build-time Sass. |
| Cost / licensing | Measure incremental production JS/CSS/fonts/icons on representative routes, not an invented kB budget. Verify exact package, asset and premium-feature licenses/costs. |
| Exit cost | Current adapter/component contract, replacement scope and migration risk. Avoid private internals or a second framework solely to obtain a visual style. |

If required evidence is missing, preserve the existing stack and mark the
candidate undecided/review-required. Use an authorized bounded spike only when
it answers a decision-critical gap. Scope/style consent alone does not authorize
installation, upgrades, framework migration, premium subscription or a specialist.

## Dated provider starting points — not universal defaults

Official observations below were checked **2026-10-06**. Recheck the relevant
provider and installed version at adoption; do not embed permanent version pins
in Skill policy. These routes illustrate conditional fit, not a ranking.

- **Existing native/host/framework primitives:** first choice when sufficient.
  Theme supported variants through existing semantics. Custom composition can
  be Material-personalized without claiming an official component implementation.
  For WordPress, preserve host-owned controls and boundaries; do not inject another
  framework into wp-admin for aesthetics.
- **Material Web:** official [repository](https://github.com/material-components/material-web)
  identifies M3 web components under Apache-2.0 and maintenance mode. Its
  [roadmap](https://github.com/material-components/material-web/blob/main/docs/roadmap.md)
  distinguishes baseline components from unbuilt ones; cards also have historical
  preview evidence, not assumed stable availability. It is not a complete web
  catalog or unconditional greenfield default. [Support](https://github.com/material-components/material-web/blob/main/docs/support.md)
  documents browser targets and system-token theming; reconcile dated tables
  with the actual release. [Size guidance](https://github.com/material-components/material-web/blob/main/docs/size.md)
  informs bundling, not a product benchmark. Import only needed components and
  check form/custom-element integration and shadow-root theme/focus behavior.
- **React / Material UI:** consider when React is already the stack and its
  installed primitives meet the task. [Overview](https://mui.com/material-ui/getting-started/)
  explicitly says Material Design 2; do not label it automatic M3/Expressive.
  [Core repository](https://github.com/mui/material-ui) declares MIT; advanced
  products/assets require their own license check. [Theming](https://mui.com/material-ui/customization/theming/)
  offers provider/token/component customization; [RTL](https://mui.com/material-ui/customization/right-to-left/)
  includes HTML, theme and styling-engine direction, with portal caveats.
  Check [supported components](https://mui.com/material-ui/getting-started/supported-components/),
  [platforms](https://mui.com/material-ui/getting-started/supported-platforms/) and
  [bundle guidance](https://mui.com/material-ui/guides/minimizing-bundle-size/)
  against actual needs. A themed M2 component is not proof of every newer M3 variant.
- **Angular Material:** consider only when Angular is already suitable/selected.
  The official [component repository](https://github.com/angular/components)
  identifies the maintained Material/CDK packages, MIT licensing and Angular-linked
  support policy, including browser/assistive-technology targets. Recheck installed
  APIs and the live [theming guide](https://material.angular.dev/guide/theming)
  for actual M3/Expressive coverage and effective runtime tokens; framework fit
  is not a reason to migrate a React, Vue, static or host-native product to Angular.

Older [Material Components Web](https://github.com/material-components/material-components-web)
reports no active maintenance; do not recommend it as a new M3 solution. Android,
Compose, Flutter and iOS examples can inform a matching native product but cannot
establish DOM behavior, mobile-web performance or component availability.
No additional provider or external Skill is installed by consulting these links.

## Bounded decision record

Use the existing handbook/engineering decision location, not a second library
registry: actual need/stack, required coverage, nearest suitable alternatives,
chosen/rejected route with reasons, observed source/date/version, unresolved
evidence, permission and a minimal verification/exit plan. Keep style acceptance,
dependency authority and tested implementation separate. If there is no product
stack (for example Skill maintenance), the justified decision is **no runtime
dependency selected**; hypothetical fit examples do not approve one for customers.
