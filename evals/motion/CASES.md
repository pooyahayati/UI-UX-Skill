# Interactive motion evaluation inputs

These are raw requests for scoped skill evaluation. Keep evaluator expectations
and conclusions in REVIEW.md. This file is not an executed model result.

## M01 — Small interaction

Our existing React/shadcn dashboard has an approved palette and type scale. Make
the filter disclosure and save feedback feel smoother. The filter already works
with CSS, and saving can return a timeout with an unknown commit outcome. Keep
this a small change; do not redesign the dashboard.

## M02 — Product-justified layout motion

We are building an authorized React task board. Users need to understand where
new and reordered tasks went. Recommend a motion approach and what we should
verify on mobile. Some users cannot drag; tasks can also update remotely.

## M03 — Copied animated component

Use an Animate UI sheet and animated action icons in our existing customized
shadcn web app. The app already has Motion, selected primitive APIs and owner
icon mappings. Preserve our approved Persian RTL layout, Vazirmatn font and
spacing. What should be adopted and checked before replacing anything?

## M04 — Conflicting motion preferences

Our authorized appearance panel has product and per-user settings. The owner
wants standard motion and a user has OS reduced motion enabled. Another owner
turns motion off while a user prefers standard. A third user selects off. Specify
the behavior, including CSS loaders, animated icons and overlays outside the
main component tree. An OS preference can change while a sheet is closing.

## M05 — Off and uncertain operations

The panel's off preset currently only sets MotionConfig reducedMotion to always.
CSS fades and skeleton shimmer still run. Form focus and save confirmation depend
on animation-end callbacks. How should the design and implementation contract
handle this, including timeout and rapid repeated clicks?

## M06 — Owner configuration failure

Add motion controls to our existing authorized appearance system. An owner draft
must stay private until publication. There are persisted older presets, two
administrators, a possible failed config load and a rollback history. An owner
requests a custom JavaScript animation field and unrestricted duration slider.
Document the supported settings and acceptance checks.

## M07 — Different stack and no admin

Our Vue web app has working transitions and no admin backend. Audit one slow
disclosure and explain whether Motion or Animate UI would help. Do not modify
the app or introduce a settings panel. It is English-only.

## M08 — Native host and explicit alternative

We are improving a WordPress plugin-owned settings form using stable public
WordPress components. Keep that foundation. On a separate already-approved
marketing page we explicitly selected GSAP for a scroll-led diagram. Recommend
motion scope without combining the two surfaces or changing their libraries.

## M09 — Handbook and phased approval

Our new mobile-first web app has approved primary-language foundations but no
approved screen yet. Propose useful motion for the first sample and document it
in the existing DESIGN.md. Dark review comes later; a second language is not
authorized. Show which motion settings would be proposed versus implemented.

## M10 — Preference unavailable at startup

We render a React app on the server; OS motion preference is only known on the
client. Components include CSS transitions and copied animated controls. How
should the first render, hydration, config-load failure and route cleanup behave?
