# R9.6 — Local verification and remaining acceptance gate

Date: 2026-10-06. Initial checkpoint status: **In progress, not full mode acceptance**.
This is engineering-lead source review, executable regression and browser
observation. It is not an independent fresh-agent result or customer approval.
The subsequent authorized [forward review and scoped acceptance](R9_6_FORWARD_REVIEW.md)
closes the representative behavioral gate. The evidence and initial disposition
below remain historical; R9.6 is now scoped engineering-complete, not integrated.

## Authority and source

The owner requested the next step after R9.5. Single writer on
`codex/r9-material-acceptance`, inheriting R9.5
`29c07d4771eb4e064936091ffe438325c5173537`; R9.1–R9.4 remain integrated through
PR #28 at `7c8fa2aaa64ed05ea711aeef58f82601728fc7b8`. No new push/merge,
dependency, external specialist, host installation, release or deployment was
authorized. The original checkout/main and settled R7/R8 owner reviews remain
untouched. No further font test is requested.

## Executed checks, separated by evidence class

| Class | Current result | Limit |
| --- | --- | --- |
| Python regressions | 68 methods passed in unittest discovery, including 26 runtime methods. Two new tests exercise concurrent Material/custom publications and whole-history recovery from a corrupt active Material record. | Discovery also runs the five executable-baseline methods through their import in sample preparation; method count is not 68 unique scenarios. No model behavior claim. |
| Runtime concurrency | Exactly one owner wins the publication race; the complete winning config/tokens survive reopening, the losing private draft survives, tenant B stays at defaults, rollback appends history. | Synthetic SQLite/Store, not production load testing. |
| Runtime recovery | Corrupt active schema-3 Material falls back to the whole previous valid Material config, retaining heading/body roles, reduced motion and meaningful icon fallback. Original history bytes and the active pointer are not silently rewritten. | Stored-state evidence, not a screenshot or manual failure injection into the owner's running browser. |
| Existing authority/lifecycle | Fresh runtime suite checks private preview/publication, strict input denial, actor/tenant separation, origin/CSRF/header boundaries, prior schemas, restart, reset and rollback. | Existing trusted loopback fixture; no new authentication engine or production certification. |
| JavaScript | Syntax checks for both authored samples passed; 11 existing dialog keyboard assertions passed. | DOM model, not real browser or assistive technology. |
| Source/registry checks | Release, roadmap, product isolation, Shared Rules, Design System, specialist registry, fixture structure, authored Material phases and historical result structure passed. | The historical five-product result was structurally checked, not independently rerun. Local official quick validation remains unavailable because `yaml` is absent. |
| Raw preparation | All 26 Material cases prepared in isolated external copies: 10 activation, 6 foundations, 6 components and 4 samples. Existing preparation tests verify exact raw copies and overwrite refusal. | Preparation is not a forward evaluation. `RUN.json` contains scoring invariants and must not be supplied to an independent evaluator. |

The first sandboxed run failed to open temporary databases and clean temporary
directories (Windows access restrictions). Repeating the same suites with scoped
host execution and external workspace TEMP/TMP passed. No application fix, relaxed
validation, dependency installation or deleted user data was used to bypass it.

## Lead source-directed scenario review — not a blind model run

Reviewed the current candidate, raw prompts/briefs and existing authored outputs.
The lead already knows the policies and invariants. The decisions below are
concrete source-directed assessments, not independently scored passes.

| Scenario / raw source | Reviewed decision and reason |
| --- | --- |
| Explicit/accepted/named style delegation; Field Notes | A selected Material proposal may use the scoped overlay. Preserve Inter, teal roles, 8px base, 12px corners and English/LTR; no library/framework/admin is implied. Named delegation still needs an actual style choice and does not approve its future sample. Unsupplied token/font paths remain gaps, not rendered proof. |
| Recommendation awaiting acceptance; Field Notes | Familiar phone controls are a plausible recommendation, not permission. Retain the current custom appearance; record the proposal and material owner decision without applying the component catalog. |
| Rejected reference / inactive narrow correction | Readable labels in an image do not override rejection. Fix only the requested label/spacing under the custom baseline, without rediscovery or another admin surface. Mobile-first alone does not choose Material. |
| Selected narrow / read-only audit / backend / WordPress host | Reuse only relevant existing guidance for the narrow or audit scope; audits do not write. Backend work does not route UI. Considering Material for a plugin-owned surface does not authorize restyling wp-admin. |
| Queue Notes; OPERATIONS.md and TOKENS.json operations | Recommend restrained emphasis on assigned work, scan-friendly hierarchy and draft/retry status for repeated outdoor operational tasks. Retain #174b6b action, Inter 16/24px, 8px base and 12px corners. Keep readable touch targets independent of compact data density and minimize repeated motion. Do not invent an admin or substitute a provider for an unspecified stack. |
| Practice Steps; LEARNING.md and TOKENS.json learning | Recommend one calm next action, short progressive explanation and welcoming empty/error copy for novice phone learners. Retain #6c3fb3 action, Vazirmatn 16/24px, supplied line-height roles, 8px base, 12px corners and Persian/RTL. Preserve LESSON-style identifiers as technical LTR content. Font bytes were not supplied by this raw brief; do not claim rendering there. |
| Sequential samples / ambiguous or stale approval | Style selection is not primary approval. Ham-Amooz remains primary-r1/h1 proposed. Focused corrections preserve foundations; ambiguous or stale-parent approval cannot start dark. Secondary remains N/A unless product need and named owner authority arise after dark approval. No bilingual/light-dark gallery is required. |
| Component/provider scope | Selected Material guides affect presentation, not general interaction semantics. A missing web component remains a custom composition/gap; a catalog, native image or roadmap does not prove a stable provider API. Preserve existing React/host/native primitives where appropriate; no runtime dependency selected for Skill maintenance. |

Personalization is thus a product/task hypothesis with explicit tradeoffs, not a
claim of measured usability benefit or universal Google appearance. The raw
briefs and authored sample remain separate; do not use this review as an answer
key for fresh evaluation.

## Fresh browser observations

Candidate application sources were unchanged in this package; the two new tests
do not modify sample UI. Observed in the Codex in-app browser on Windows:

- **Ham-Amooz primary-r1 / h1, Persian RTL/light, 320×800:** actual document
  client/scroll widths both 305px. Keyboard Enter opened the lesson and moved
  focus to its title. Two lesson actions measured about 49.4px high; the answer
  field was 223px wide. Simulated save entered an identifiable busy state with
  disabled Save; the injected failure retained the literal mixed-script answer
  and explained retry. Keyboard retry produced explicit in-page simulation
  success, not server confirmation. Returning to the list retained the answer.
- **List state/recovery:** selected loading and empty fixture states showed
  distinct explanatory text and recovery through the same test control. Returning
  to Ready restored the lesson. These are synthetic states, not network throttling.
- **1280×900 lesson:** document client/scroll widths both 1265px; the saved
  answer survived route navigation and resizing. Real screenshot showed readable
  Persian hierarchy, technical ID and form. Inspected controls had 0s transitions;
  this low-motion source does not need animation to communicate save state.
- **Runtime private preview:** current-source fresh owner tab actually 1600×900.
  Material/ocean/serif-heading preview retained system body and reduced motion
  (`--duration:0ms`), with field and disclosure about 48px high. A separate
  anonymous reader reload still showed published version 3 and forest/icon fallback.
  Only unsaved preview was changed; no new draft/publication/history was created.
- **Overlay keyboard/geometry:** current private Material overlay derived #eef0f3
  and Georgia title, width about 560.4px; Close received focus, Tab remained inside,
  Escape closed and returned focus to Open overlay example. These are actual
  browser interaction/geometry observations, not screen-reader conformance.

External captures are retained outside Git. The 320px top and scrolled segments
and 1280px primary capture were visually inspected; they are viewport segments,
not a full-page/pixel-diff claim. An older open owner tab still had prior CSS and
showed a 44px disclosure; a fresh tab loaded the current 48px rule. The stale-tab
measurement is excluded from current-source acceptance. Both new owner-overlay
captures showed inconsistent viewport framing/clipping; they are retained but
excluded from positive visual evidence. No UI change was inferred from that
capture limitation. Existing R9.5 inspected overlay/public-dark evidence is reused
only for unchanged UI sources, not as proof of a new model outcome/package.

OS reduced-motion emulation, actual touch hardware, other browsers, real slow
network/device profiling, assistive technology and zoom/forced-colors were not
executed. Pointer and keyboard interactions plus target geometry do not prove
those contexts. No new customer approval, dark specimen or secondary locale was
created to fill a matrix. The previous accepted Persian-font review stays accepted.

## Official sources and candidate delivery checks

Rechecked 2026-10-06: [Material Web README](https://github.com/material-components/material-web)
and [roadmap](https://github.com/material-components/material-web/blob/main/docs/roadmap.md)
still report maintenance mode rather than a planned new-feature catalog.
[Material Symbols](https://developers.google.com/fonts/docs/material_symbols)
remains an optional licensed asset route with named styles/axes, not an installed
family in these fixtures. No provider adopted. The direct
[M3 color page](https://m3.material.io/styles/color/the-color-system) returned only
the JavaScript shell through the web reader; that is not a fresh full specification
review. Existing dated source links/mappings remain useful with this stated limit;
exact adoption/variant claims require the provider's current implementation evidence.

Fresh exact-commit package evidence is retained externally in the R9.6 handoff:
two builds, complete inventories, canonical source bytes, embedded versions, CRC,
reproducibility and resource hashes. Check all currently routed Material/research
guides there; do not substitute an R8 or R9.5 archive as this package's proof.
No new Skill semantics/runtime engine was changed by this test/report package;
version remains 3.1.1. An eventual release still needs its own classification,
changelog and authority. Current local checks are not new GitHub CI.

## Initial remaining gate and separate lead disposition (superseded)

Lead accepts the **local verification slice**, not full R9.6 or optional-mode
behavioral readiness. No new runtime defect was reproduced. Required forward
behavioral evidence for the newly routed mode is still missing: this lead's
source review, prepared cases and old R8 outcomes cannot replace it. No new
independent agent was authorized, so none was launched and no invented result
was entered into result.json. R9/R9.6 stay In progress.

Next bounded action, after owner authorization: one read-only independent
fresh-context evaluator, no installation/specialist/framework, using only the
exact candidate Skill, raw fixture and prompt for selected, unaccepted, rejected,
backend, contrasting-audience and stale-approval cases. Do not pass this report,
past outcomes or scoring invariants. Record the actual host/model/trigger,
loaded references, response/artifact/changed files and unavailable evidence;
lead then independently scores the retained outputs, resolves any required
finding and records full or scoped acceptance honestly. Additional device claims
remain unverified unless actually tested. Integration, release and installation
are separate next permissions, not implied by that review.

## Final scoped disposition — 2026-10-06

The owner subsequently approved one read-only independent evaluator. The linked
[six-case forward review](R9_6_FORWARD_REVIEW.md) retains actual responses,
attributed resource reads, separate lead scoring and the F01 reference-order
observation. Correct product routing, preserved foundations and bounded consent
decisions were observed; strict loader-order compliance is not established.
The lead accepts the representative R9.6 exit using that independent slice plus
this local evidence and exact Skill package binding. All six R9 packages have
scoped engineering acceptance, not universal model/device conformance or actual
customer approval. R9.5/R9.6 integration, current-head GitHub CI and any release,
deployment or installation remain separate. No test/source gate or version was
relaxed to close this stage; settled R7/R8 reviews are not reopened.
