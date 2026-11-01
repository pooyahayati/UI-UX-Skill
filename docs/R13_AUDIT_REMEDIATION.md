# R13: Post-3.6.0 Audit Remediation

Prepared 2026-11-01. This document defines four correction packages and their
acceptance criteria. [ROADMAP.md](../ROADMAP.md#r13-audit-remediation) is the only
live progress ledger; preparing this plan does not complete any implementation.

## Objective and authority

Resolve the four evidenced audit findings in priority order: validation-error
ownership, runtime-evidence consistency, operational component routing, and the
light-only product approval path. Preserve existing design decisions, product
isolation, data contracts and historical evidence.

The owner's original planning instruction authorized updating the roadmap and this plan.
That planning checkpoint changed only those two documents. The subsequent
execution instruction is recorded in [R13 execution](R13_EXECUTION.md#authority)
and supersedes planning-only authority within its stated scope. The completed R12 delivery authority remains attached to that
delivery; this planning instruction does not authorize implementation, new
dependencies, test-host changes, commit/push/merge, release or local installation.
Record a later execution instruction in the roadmap without asking the owner to
repeat already settled product or font choices.

Use one implementation writer and execute R13.1 through R13.4 in order. A real
blocker may justify documented independent work, not an unsupported completion
claim or weakened checks. No new Product Pack, external specialist, production
plugin, settings engine or general-purpose evaluation framework is planned.

## Audit baseline and evidence

- Audited source and remote `main`, rechecked during planning:
  `faad3b126e323e566706f6f5dd288cc1e2781c3b`.
- Released/installed baseline: 3.6.0; release tag commit:
  `986064c5c6c5583efe601dd502d6e9a3bb95539d`.
- Release/resource/product/shared/design/specialist/fixture checks and the retained
  13-case UI acceptance gate passed. The 22 WordPress contract and six R12 tests
  also passed. These successes do not cover the demonstrated gaps below.
- Actual App handlers were exercised with the existing deterministic hooks/HTTP
  harness; report mutations were performed in memory. No new browser/WordPress
  execution, production change or modified audit artifact was claimed.

| Finding | Classification | Evidence and impact |
| --- | --- | --- |
| R13-F01 | Medium; confirmed specimen behavior defect | [App submission/error handling](../evals/fixtures/wordpress-settings/plugin/app.js) clears every error on any section save and applies delayed errors without checking the submitted field value. An unchanged invalid endpoint loses its error after a report-title save; a corrected endpoint can receive the old request's error. This violates [hidden-error reachability](R12_WORDPRESS_ADMIN_DESIGN.md#r122-organization-and-findability) and [field-error retention](../skills/ui-ux-skill/references/products/wordpress/settings.md#validation-and-errors). No persisted data loss was demonstrated. |
| R13-F02 | Medium; confirmed validation/coverage defect | [Runtime evidence validator](../evals/wordpress-settings/test_contracts.py) accepts contradictory `complete`, `scope`, `omitted_observations`, missing host compatibility and non-browser observation methods despite [producer metadata](../evals/wordpress-settings/run_discovery.cjs). Removing actual observation D10 correctly fails. The existing published report is consistent; this finding concerns future false acceptance, not fabricated release evidence. |
| R13-F03 | Medium; confirmed guidance-routing gap | [Operational DataViews/DataForm advice](../skills/ui-ux-skill/references/products/wordpress/components.md#choose-by-data-and-task) exists only inside a settings-only guide. [Parent routing](../skills/ui-ux-skill/references/products/wordpress-plugin.md#required-wordpress-routing) excludes that guide for operations. A pure report-list/detail task cannot reach the advice promised by R12 A3.3. The mixed settings/list B04 scenario hides this gap. |
| R13-F04 | Medium; confirmed procedural inconsistency | [Sequential workflow](../skills/ui-ux-skill/references/design-foundation-workflow.md#phase-3--secondary-languagedirection-only-when-needed-and-authorized) and the [handbook template](../skills/ui-ux-skill/assets/templates/DESIGN.md) require dark approval before secondary-language review, while [WordPress theme scope](../skills/ui-ux-skill/references/products/wordpress-plugin.md#lightdark-appearance) makes dark conditional. A light-only bilingual product lacks a defined transition. No actual wrong model response was demonstrated. |

## Protected scope and evidence succession

- Keep stable public `@wordpress/components` mandatory for new or explicitly
  redesigned plugin-owned settings, including short forms. Operational component
  advice must not export this mandate to other surfaces.
- Preserve capabilities, nonces, validation, secret handling, storage/option keys,
  Settings API/REST boundaries, independent drafts, conflict/unknown-outcome
  recovery and the surrounding WordPress shell. Do not add a runtime dependency
  or change server contracts to correct client-side error ownership.
- Preserve shadcn/ui dashboard defaults, optional Material, need-based motion,
  bounded owner appearance controls and unrelated Product Packs. No automatic
  library, framework, dark-theme or language rollout.
- Retain original WPS/R11/R12 reports, screenshots, raw model outputs, candidate
  identities and release bindings. Corrections receive separately named R13
  successor records tied to their exact parent and actual changed paths.
- R13.1 must make its current fixture checks and fresh evidence runnable without
  weakening historical checks. Introduce only the minimum exact-parent successor
  wiring needed for the fixture/runner change; R13.2 owns the stricter completion,
  method and host-matrix validation. The new report must already contain truthful
  metadata so R13.2 does not need to rewrite earlier observations.
- The R12 release bridge binds the complete Skill candidate. Keep
  `evals/r12-release-version.json` and its original results historical; it is not a
  general bypass for R13 source changes. By the first Skill guidance change,
  current CI must select an explicit R13 candidate/result while separately
  retaining R12 integrity checks. No blanket hash exclusions or version waiver.
- Before each guidance edit, map changed resources to recorded consumed paths.
  R13.3 affects WordPress-consuming outputs, including S04 and B01–B05 where their
  recorded inputs change. R13.4 changes central approval guidance; editing
  `SKILL.md` can affect most or all selected cases. Refresh every actually affected
  selected output with an independent evaluator; reuse others only under the
  existing exact-source rules. Never relabel an old answer as a fresh run.
- Use raw requests and required resources for evaluators; withhold this plan,
  rubrics, expected answers and prior responses. Separate source review, actual
  model output, rendered behavior and owner approval in the acceptance record.

## Planned file boundaries

These are the bounded implementation targets authorized by the later execution decision.

| Package | Principal targets / permitted support |
| --- | --- |
| R13.1 | `evals/fixtures/wordpress-settings/plugin/app.js`; relevant actual-handler and browser regressions; named R13 runtime/source successor records and minimum current-check wiring. Extend `scripts/roadmap_policy.py` and its tests to cover the R13 ledger without weakening WPS/R12 checks. |
| R13.2 | `evals/wordpress-settings/test_contracts.py`, related R12/R13 evidence tests and producer metadata only where necessary; existing CI entrypoints. Preserve separate legacy-regression and discovery-report contracts. |
| R13.3 | `references/products/wordpress-plugin.md` and `references/products/wordpress/components.md` under the Skill root; prefer a short operational selection section in the existing parent. Relevant routing tests, raw operational/hybrid cases and explicit current R13 result/preparation bindings. |
| R13.4 | `SKILL.md`, `references/design-foundation-workflow.md`, `references/design-handbook.md`, `assets/templates/DESIGN.md`; inspect `references/material-foundations.md`, `references/material-samples.md` and README workflow wording for repeated gates. Modify only affected transitions/cross-links and their behavioral checks, not Material selection or product theme policy. Execution tracing also includes repeated transitions in discovery, motion, shadcn, Material activation/components and the authored Material sample validator; see the execution record. |

Use one linked R13 execution record for dated commands, results, decisions and
limitations once execution starts. Keep temporary runs, credentials and machine
state outside the repository. Portable reviewed evidence may follow existing
evaluation conventions; no second live status table belongs in this plan.

## R13.1: Preserve section and submitted-value error ownership

**Entry:** owner instruction to implement R13.1. **Priority:** first, because this
is a reproduced user-visible defect in the acceptance specimen.

Keep field errors associated with their section and the submitted value/revision.
Do not clear unrelated errors when starting or completing a section save. Apply
late validation only to values that still match the failed submission; preserve
truthful rejected/unsaved state without labelling newer valid input invalid.
Reuse existing state ownership rather than adding a form framework.

| ID | Observable acceptance |
| --- | --- |
| ERR-1 | Reject an HTTP endpoint, leave it unchanged, then successfully save a changed report title. The endpoint remains unsaved with its field error and reachable error link; the title is authoritatively saved. No section, search or back transition loses either state. |
| ERR-2 | Delay rejection of an invalid endpoint, correct it to HTTPS while pending, then deliver the old response. The corrected value remains intact and unsaved, with no stale field error/focus jump. A current rejected value still receives its error normally; do not suppress all late errors. |
| ERR-3 | Editing or successfully revalidating one field clears only its obsolete errors. Unrelated section errors survive. Credential replace/keep/remove, duplicate-submit prevention, independent drafts, peer conflicts, unknown outcomes and secret handling retain their existing semantics. |
| ERR-4 | Both failing sequences first reproduce through actual App handlers, then pass after correction. Relevant real-admin checks confirm visible help/invalidity, hidden-group reveal/focus and stored-versus-draft values on the supported synthetic hosts, with representative narrow Persian/RTL coverage. Record exact source/runner/host identities and any unavailable checks. |
| ERR-5 | The R13 ledger gains regression coverage for ordered prerequisites, single active stage, completion counts and dated evidence; all historical WPS/R12 checks remain effective. Current fixture/source checks pass via the bounded R13 successor, not changed historical hashes. |

**Exit:** ERR-1–ERR-5 pass with dated lead acceptance. R13-F02 remains explicitly
open until R13.2; actual reviewed runtime evidence, not the old metadata guard
alone, establishes R13.1's behavior. No other finding is marked resolved here.

## R13.2: Reject contradictory runtime evidence

**Entry:** accepted R13.1. **Priority:** second, before accepting subsequent
guidance changes through the strengthened evidence pipeline.

Define the required metadata by report producer. A full discovery/workspace
acceptance requires consistent full scope/completion, no omitted required
observations, real-admin browser methods and the supported host/capture matrix.
Partial or source-only observations can remain honestly recordable, but cannot
close a full runtime gate. Derive host expectations from the declared fixture
support matrix; do not freeze a newer external version or invent host coverage.

| ID | Observable acceptance |
| --- | --- |
| EVD-1 | The valid full current record passes. Independently setting `complete=false`, declaring partial scope, listing D10 as omitted, removing host compatibility, or replacing browser methods with source tracing fails full acceptance with a useful reason. |
| EVD-2 | Missing/malformed required metadata and contradictions between declared scope, omissions, actual observation IDs and methods fail. The existing negative control that removes D10 continues to fail; stale source/runner and duplicate/failed observations remain rejected. |
| EVD-3 | Missing a required host/locale/viewport/state cell or relabelling it inconsistently with its capture/observation fails. Checking only screenshot count/hash or nonempty compatibility arrays is insufficient. Preserve actual image identity and overflow checks. |
| EVD-4 | Historical regression reports without discovery-specific fields remain valid under their own explicit contract and provenance. Partial runs are not silently upgraded; existing consistent published R12 records are not described as fabricated or retroactively invalid. |
| EVD-5 | Existing CI invokes the strengthened validators and their negative cases. All named mutations fail for the intended reason, while valid fixtures and preserved historical records pass; no check is removed or weakened to make the successor green. |

**Exit:** EVD-1–EVD-5 pass. Use independent in-memory mutation tests and source
binding checks; rerun the browser only if executed inputs/producer behavior or
required coverage changed. More validator tests do not count as new browser runs.

## R13.3: Make operational component advice reachable

**Entry:** accepted R13.2. **Priority:** third, restoring the promised operational
decision route without broadening the settings-only component mandate.

Move the conditional DataViews/DataForm selection advice to the existing
WordPress parent or a justified focused operational route. Keep one canonical
description; link only where the affected surface warrants it. Component need,
public API/version support, existing build strategy and host ownership still
govern adoption. Reading guidance never installs a package.

| ID | Observable acceptance |
| --- | --- |
| ROUTE-1 | A fresh evaluator given only a large plugin-owned report-list/detail task, explicitly without settings work, can reach and apply the conditional operational selection advice without loading the settings-only guide. It compares task/stack fit rather than mandating DataViews/DataForm. |
| ROUTE-2 | A short settings-only form retains mandatory stable public WordPress controls without activating or applying operational/data-heavy requirements. Reading the shared parent does not activate those rules; separate operational-only resources are loaded only when needed. A hybrid task applies each rule to its own surface. |
| ROUTE-3 | Existing native/simple operational lists may remain native. Audit-only requests remain read-only; no forced REST/storage/build/framework migration or activation of dashboard shadcn, Material or motion follows from the word "workspace". |
| ROUTE-4 | Positive and negative routing checks preserve isolation. An independent operational-only case and the affected hybrid/settings cases pass against the actual corrected candidate. Update consumed-source-dependent outputs and current R13 CI bindings while retaining the exact R12 records. |

**Exit:** ROUTE-1–ROUTE-4 pass with raw requests, actual responses and reviewer
acceptance. Package-local resource checks must pass; a keyword mention in a guide
or a mixed settings/list case alone cannot establish operational reachability.

## R13.4: Define the scoped light-only approval transition

**Entry:** accepted R13.3. **Priority:** fourth, reconciling the shared approval
workflow with the already scoped WordPress theme policy.

Add a recorded dark-not-applicable outcome only when supported by the actual
product/host scope and valid owner decision. It is distinct from pending,
unavailable, rejected or merely untested dark review. If dark is required, keep
primary approval -> dark approval -> authorized secondary review unchanged.
If dark is explicitly not applicable, permit approved primary -> authorized
secondary review with that decision and the primary baseline recorded in DESIGN.

| ID | Observable acceptance |
| --- | --- |
| THEME-1 | A light-only native WordPress settings product has an approved Persian primary revision, evidenced exclusion/non-applicability of dark, and authorized English support. The agent proceeds to the English sample without inventing dark work or repeating settled approval questions. |
| THEME-2 | Required dark that is pending/rejected/unavailable cannot be marked not applicable to bypass its gate. Unclear theme scope triggers only the needed clarification. A monolingual product creates no secondary sample; an authorized primary-dark product does not repeat the same approved treatment. |
| THEME-3 | SKILL entrypoint, canonical workflow, handbook/template and relevant Material/README summaries use the same transition and authority rules. DESIGN records applicability reason/source, covered scope, parent revision and secondary authorization rather than a fake dark approval. |
| THEME-4 | New independent light-only bilingual and required-dark-pending scenarios produce the expected distinct behavior. Retain representative monolingual and primary-dark checks and refresh every affected selected response according to consumed-source bindings. Source text matching alone cannot close this criterion. |
| THEME-5 | No product acquires a theme toggle, second language, new appearance panel, altered foundations or implementation permission merely from this workflow correction. Existing production themes/locales and scoped owner approvals remain preserved. |

**Exit:** THEME-1–THEME-5 pass with coherent handbook records and actual behavioral
evidence. This corrects a missing applicability route; it does not abolish dark
review where the product requires it or reopen accepted visual/font decisions.

## Combined acceptance and handoff

All four packages need their own accepted evidence. After every stage, update the
roadmap's completed/active/next fields and link dated observations; a passing test
count alone is not completion. Failed or unavailable required checks stay open.

At final handoff, verify the actual current candidate with affected WordPress
handler/model/browser regressions, R13 report-integrity and independent behavioral
cases, retained historical checks, roadmap/release/resource/product/shared/design
validators and both packaged consumer routes. Review README, evaluation guidance
and status wording only for claims changed by these fixes. Record meaningful
platform skips and evidence limits; preserve the 3.6.0 version during this work
unless a later release instruction authorizes a version decision.

No publication or active installation follows from implementation acceptance.
If later authorized, use the existing exact-head CI, merge/tag binding, native
security checks, actual published-download verification and backed-up managed
local update. Do not replace 3.6.0 assets or discard Head integration.

The first implementation action is ready: reproduce ERR-1 and ERR-2 with the
actual-handler harness, retain the failing assertions, then make the smallest
section/submitted-value correction. No additional product-design choice is
needed to start R13.1 after an execution instruction.
