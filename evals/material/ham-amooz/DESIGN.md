# Ham-Amooz — authored Material sample handbook

## Identity / authority

- Canonical specimen path: `evals/material/ham-amooz/DESIGN.md`.
- Sample revision: primary-r1
- Handbook revision: h1
- Date: 2026-10-06. Single writer: engineering lead on codex/r9-material-samples.
- Lifecycle: draft. Last approved visual baseline: none.
- This is an authored synthetic example, not a customer product or independent
  agent result. Maintainer acceptance of Skill source is not fictional owner consent.
- R9.3 source baseline: e75f59fe044f94fc099d6b9579f910a8ded0e1e7;
  candidate source package version 3.1.1, no installation or release.

## Product / scope / personalization

[Raw brief](../../fixtures/material-samples/BRIEF.md) supplies a mobile-first
Persian RTL learning web app for novice adults. Primary route web-application;
no secondary route. List → one lesson → reflection answer → explicit simulated
save/retry → simulated finish exposes the learning job without a generic
dashboard, login or fabricated analytics. No backend, grade, account, admin,
durable progress, second locale or unrequested features.

Professional recommendation: calm, spacious plum grouping with a clearly labeled
primary action and an optional hint lets unfamiliar learners read before writing.
Tradeoff: the spacious composition shows less content at once than a dense list;
this brief has one relevant lesson, not an operational scanning workload.
This rationale is inference, not measured usability or guaranteed taste fit.

Active Product Pack: web-application and navigation-state, workflows-data,
interaction-access. Relevant Shared modules: navigation, forms, feedback,
state/recovery, accessibility and responsive. Design System: tokens, typography,
color, spacing, states and responsive variants. Other Product Packs inactive;
destructive actions, permission/auth, chart/data and runtime governance are not
implemented in this slice. Persian writing used for copy/RTL; bounded local-input
safety reviewed. No subagent or additional external design specialist launched.

## Foundations and actual sources

Single executable value authority:
[tokens.css](../../fixtures/material-samples/tokens.css), consumed directly by
[index.html](index.html) before [styles.css](styles.css). It supplies fixture-set
palette pairs, family/weights, font roles, spacing/shape, outline/focus and control
size. No duplicate live value table here. These are settled synthetic inputs, not
newly invented customer approvals or an admin configuration database.

Font assets reused without modification:
[regular](../../samples/dispatch-notes/fonts/Vazirmatn-Regular.ttf),
[bold](../../samples/dispatch-notes/fonts/Vazirmatn-Bold.ttf),
[license](../../samples/dispatch-notes/fonts/OFL.txt).
Only 400/700 consumed; font-synthesis none. Browser loading/identity evidence is
separate in the [stage review](../R9_4_SAMPLES.md), not inferred from CSS naming.

## Components / official evidence / exceptions

Candidate Skill references, not additional handbook authorities:

| Used pattern | Relevant guide / source | Adaptation / exception |
| --- | --- | --- |
| Filled primary, quieter outlined finish | [Actions](../../../skills/ui-ux-skill/references/material-components/actions.md); [official buttons](https://m3.material.io/components/buttons/overview) | Native link/button semantics, fixture plum roles, full labels and busy/disabled treatment. |
| Multiline answer with supporting/error text | [Forms](../../../skills/ui-ux-skill/references/material-components/forms.md); [official fields](https://m3.material.io/components/text-fields/overview) | Native textarea, explicit save, preserved literal input and visible error. |
| Grouped lesson / content list | [Content](../../../skills/ui-ux-skill/references/material-components/content.md); [official cards](https://m3.material.io/components/cards/overview) | Native article/list-detail composition, not a stable Material Web card API. |
| Header and contextual return | [Navigation](../../../skills/ui-ux-skill/references/material-components/navigation.md) | Two route contexts do not need an invented three-destination navigation bar. |
| Save/failure/result status | [Feedback](../../../skills/ui-ux-skill/references/material-components/feedback.md) | Persistent local live text, no fabricated percentage or transient-only failure. |

Official overview observations inherited from the dated R9.3 review, 2026-10-06.
Product application above is authored inference. This native specimen illustrates
a personalized selected-Material presentation; it is not full M3/Expressive or
installed-provider conformity. Existing native stack suffices; no provider needed.
Local decorative SVG book uses no downloaded icon font; no semantic icon picker.
Back arrow is contextual RTL direction, not blanket mirroring of identifiers.
No animation introduced; no decorative delayed progress or reduced-motion toggle.

## UX / responsive / recovery

Phone-first targets: 390px typical narrow, 320px stress, 768px intermediate and
1280px keyboard/wide. Transition at 760px stacks reading/help panes where the
side-by-side reading region becomes constrained; at 480px lesson artwork stacks.
These are specimen choices, not universal Material breakpoint rules.
Logical CSS and real Persian strings; identifier LESSON-01 isolated LTR.

| Requirement | Consumer / important outcome | Verification boundary |
| --- | --- | --- |
| Start/read lesson and optional hint | #lessons / #lesson, browser hash/history, heading focus | Native route/hint interaction; no backend navigation |
| Short reflection, explicit save | answer-form, persistent label/support text | Whitespace-only validation, 600-character cap, literal text output |
| Failed save/retry preserves work | fail-next harness; local error then same Save action | Actual actions needed; harness is not server-failure proof |
| Finish prerequisite | disabled until latest answer is simulated saved | Editing invalidates prior simulated completion; no grading |
| Loading/empty | list-mode harness with recovery instruction | Explicit simulations, not a live content source |
| Unsaved draft continuity | tab memory through list/detail; busy input read-only | Refresh loss disclosed; beforeunload is best effort, not durable storage |

## Samples / decisions / sequence

| Decision | State / provenance | Scope |
| --- | --- | --- |
| Persian RTL only, selected Material, native stack and settled foundations | Supplied synthetic BRIEF.md / tokens.css, not real owner consent | Authored example |
| Composition and professional rationale | Proposed by author, 2026-10-06 | primary-r1 / h1 |
| Primary visual approval | Unresolved, no actual actor/source/date | No approved sample |
| Derived dark | Not started, required after actual primary approval | No artifact or parent approved revision |
| Secondary locale/layout | Not applicable, monolingual raw brief | No extra translation or mirrored specimen |
| Broad rollout, production release, admin | None authorized by this specimen | No implementation authority inferred |

Primary proposal: [index.html](index.html), matching [sample.json](sample.json).
Feedback/corrections: none received. Observations below do not approve taste.
Preserve this proposal and foundation sources on correction; use a new sample/
handbook revision and record affected decisions without rewriting unrelated facts.
After a real scoped primary decision, derive dark from that exact accepted revision,
inspect its changed semantic pairs/states and seek separate dark acceptance.
Do not infer it from R7/R8 approval of a different historical product.

## Configurability / evidence / next action

All specimen appearance is code-only through tokens.css and styles.css. Protected
feature/action meaning is locked by raw brief. No owner controls, uploads, storage,
permission model, publication/history or fallback registry were implemented.
Font upload/selection and semantic icon configuration remain R9.5/runtime scope,
not silently added here. Future real products reuse existing prepared controls.

Checks and limits: [stage review](../R9_4_SAMPLES.md). Later contexts remain not run,
not missing primary requirements. Native device/IME/screen-reader/production
performance and server behavior are not established by local browser observations.
Next specimen decision: focused primary feedback and explicit revision-scoped
approval if its visual development is continued. Next Skill development is
independent of a fictional owner's taste; engineering lead assesses source work.
Change history: h1/primary-r1 initial authored primary, no approved baseline replaced.
