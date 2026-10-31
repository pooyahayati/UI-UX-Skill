# R12 raw behavioral requests

These are raw evaluator requests, not reviewer criteria. Give a fresh evaluator
only its selected request, the candidate Skill and the stated raw artifacts.
Keep the plan, execution record and expected outcomes out of evaluator input.

## B01 — Short settings

Our WordPress plugin has two settings: a report name and an email-enabled switch.
It supports WordPress 6.8, uses the Settings API, and has no build pipeline. We
authorize a redesign of this settings page. The product language is English.
Give an implementation handoff with a concrete control/layout sketch and the
integration checks a developer needs. Keep the existing save/option contracts.
Do not install anything or claim you tested our site.

## B02 — Hybrid admin

Design the navigation and interaction contract for a Persian reporting plugin
inside WordPress admin. It has report naming, scheduled email recipients,
connection credentials and a callback address, plus a report list/detail page and
background delivery status. Administrators say they cannot find the callback
address because they call it a webhook. Each settings section saves independently;
an unsaved edit must survive moving elsewhere. Specify actual destination/focus,
disabled-field and validation-error behavior and an example settings inventory.
Do not change the backend or install packages.

## B03 — Audit boundary

Audit only the design approach of an existing WordPress plugin: its short settings
page uses legacy HTML controls, and the jobs screen has a custom table. I might
want Material or shadcn for a future redesign. Today a long label clips on mobile.
Explain the findings and a bounded recommended next step. Do not edit files or
implement the redesign.

## B04 — Component compatibility

Our plugin supports WordPress 6.8 and ships a no-build script using the core
shared runtime. A teammate proposes importing current @wordpress/ui components,
DataViews and ThemeProvider into every settings screen to modernize it. We have
one short settings form and a separate list of thousands of report records.
Review the proposal and give a practical version-aware component decision.
No dependency installation or framework migration is authorized.

## B05 — Visual approval sequence

We are redesigning a Persian-only WordPress plugin. Its DESIGN.md already chooses
Vazirmatn, WordPress-compatible blue/neutral colors and comfortable spacing.
The owner wants to review the settings design first and is considering dark
appearance later. English support has not been requested. Describe the first
reviewable deliverable and what can happen after feedback. You have no running
WordPress host in this evaluation; do not claim screenshots or acceptance.
