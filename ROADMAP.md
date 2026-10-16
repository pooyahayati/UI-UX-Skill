# UI/UX Skill Roadmap

The live work queue is below. Completed work is summarized in [history](#completed-history); detailed execution and release evidence stays in the dated archives.

## Current state

| Item | State |
| --- | --- |
| Updated | 2026-10-16 |
| Released baseline | [v3.5.0](https://github.com/pooyahayati/UI-UX-Skill/releases/tag/v3.5.0); published artifacts and local installation verified 2026-10-16 |
| Current workstream | [R11: three audit remediations](#r11-audit-remediation); implementation and delivery authorized |
| Planning readiness | Scope, acceptance criteria and verification defined in the [R11 plan](docs/R11_AUDIT_REMEDIATION.md); implementation evidence in the [execution record](docs/R11_EXECUTION.md) |
| Completed R11 packages | 2 of 3 |
| Active R11 package | R11.3 |
| Next R11 package | Combined verification and authorized delivery |
| Completed WPS packages | 7 of 7 |
| Active WPS package | None |
| Next WPS package | None |
| Execution authority | [R11 implementation, merge, release and managed local update](#r11-audit-remediation) |
| Accountable role | Engineering lead / maintainer; one implementation writer |
| Delivery | v3.5.0 remains the installed/released baseline until the R11 candidate passes all acceptance and delivery gates |

## R11 audit remediation

**Owner decision, 2026-10-16:** update the roadmap for the three findings from the latest deep audit and prepare step-by-step fixes with explicit acceptance criteria. This instruction authorizes planning/documentation only. Implementation starts with a subsequent instruction; earlier release/install permissions retain their original completed scope and are not extended to R11.

**Superseding execution decision, 2026-10-16:** the owner explicitly authorized R11.1 through R11.3 in order, followed by merge, a new release, then a managed local update of this Skill. This supersedes the planning-only restriction for R11, not its acceptance criteria. Branch/commit/push/PR operations are included in that delivery; unrelated skills, production sites and product dependencies remain outside scope. Preserve local Head integration and a recoverable installation backup. [Execution evidence](docs/R11_EXECUTION.md) records checks and stage acceptance.

The [R11 implementation plan](docs/R11_AUDIT_REMEDIATION.md) contains the audited baseline, finding evidence, affected paths, protected contracts, observable acceptance and required checks. Two findings are confirmed defects; the third is a behavioral-test coverage risk, not a demonstrated routing/motion defect. This table is the **only live R11 status ledger**.

| Package | Deliverable | Status | Entry condition | Acceptance / next action |
| --- | --- | --- | --- | --- |
| R11.1 | Preserve peer changes during WordPress specimen conflict recovery | Completed | Accepted 2026-10-16 | [21 real-admin observations, handler/model regressions and 14 integrity tests](docs/R11_EXECUTION.md#r111) |
| R11.2 | Include the license notice in every standalone distribution path | Completed | Accepted 2026-10-16 | [Notice, package/direct-stage verification and regressions](docs/R11_EXECUTION.md#r112) |
| R11.3 | Add repeatable behavioral evaluation for shadcn/ui and interactive motion | In progress | Authorized; accepted R11.2 | [Independent outputs, negative cases and regression integration](docs/R11_AUDIT_REMEDIATION.md#r113-repeatable-behavioral-evaluation); [execution](docs/R11_EXECUTION.md#r113) |

Execute in the listed priority order, one active package at a time. A package is complete only with its recorded acceptance evidence, not because its implementation or plan exists. An unavailable required check remains unverified; unrelated passing checks cannot substitute for it. If a blocked check requires resequencing independent work, record the reason and actual active/next package without marking the blocked package complete.

**Next action:** complete R11.3, then verify the combined candidate and deliver. Final combined readiness and the authorized delivery remain subject to the [R11 closeout gates](docs/R11_AUDIT_REMEDIATION.md#combined-acceptance-and-delivery-boundary).

## Release 3.5.0

**Owner authorization, 2026-10-16:** commit, push and merge the shadcn/ui and interactive-motion changes, publish a new release, then update this Skill locally. This supersedes the delivery exclusions in the two original source-only decisions below for these additions only. Preserve existing local Head integration and a recoverable backup; do not update unrelated skills or product dependencies. Version 3.5.0 is the additive-feature release after 3.4.0.

| Step | State | Acceptance / evidence |
| --- | --- | --- |
| Final source, metadata, regression and native security verification | Completed | [2026-10-16 candidate checks and limitations](docs/releases/3.5.0.md#local-candidate-checks-2026-10-16) |
| Commit, push, PR checks and merge | Completed | [PR #45](https://github.com/pooyahayati/UI-UX-Skill/pull/45); exact-head CI and merge recorded |
| Automated GitHub release and downloaded-artifact verification | Completed | [Merge/tag, actual downloads and native scan](docs/releases/3.5.0.md#github-publication-and-downloaded-artifacts) |
| Managed local update and closeout | Completed | [91 upstream files, integration, compatibility and retained backup](docs/releases/3.5.0.md#verified-local-installation) |

The release workflow on `main` is the sole publisher for this version. Do not create competing tags or overwrite existing assets. A failed required check stops the affected delivery action; preserve the previous release/install until its replacement is verified.

## Interactive motion

**Owner decision, 2026-10-16:** add the agreed interactive-animation guidance, with Motion and Animate UI chosen by product need and accessibility/owner-setting safeguards. This authorizes the bounded Skill source, documentation and evaluation update; it does not authorize new product dependencies, external specialists, publication or local installation. The shadcn/ui dashboard foundation decision remains valid and separate.

Plan: add one conditionally loaded implementation reference; connect existing motion, implementation, shadcn and appearance routes plus the handbook template; verify selection/no-install cases, reduced/off and owner/user/OS boundaries, protected-source isolation and packaged resource reachability. Preserve historical WPS and shadcn checkpoint evidence; record later changes as a separate exact-parent delta, not an exemption.

| Work | State | Evidence / next action |
| --- | --- | --- |
| Guidance, owner policy and handbook routing | Completed | [Implementation and ten-case source review](evals/motion/REVIEW.md#scenario-review) |
| Source isolation, regression and package checks | Completed | [2026-10-16 checks and limitations](evals/motion/REVIEW.md#verification-record); original historical evidence retained |
| Integration / release / local installation | Completed | Authorized by the later [3.5.0 delivery decision](#release-350); [verified delivery](docs/releases/3.5.0.md) |

Acceptance: compatible products choose the smallest useful motion treatment, not automatic dependencies; explicit choices and existing/native stacks remain authoritative; all claimed consumers honor reduced/off behavior; owner controls are bounded and cannot weaken accessibility; handbook/approval sequencing is preserved. Checks must distinguish Skill guidance from actual product runtime evidence.

## shadcn/ui dashboard default

**Owner decision, 2026-10-16:** add shadcn/ui guidance in the appropriate Skill location and make it the dashboard default unless the user explicitly instructs otherwise. This is the bounded authority for this addition; it supersedes stabilization-only scope for the named change, not for unrelated features or delivery actions.

The Dashboard Product Pack owns default selection. A shared implementation reference owns component adoption, personalization, RTL/dark/mobile checks and owner-control mapping. Explicit user alternatives win; established stacks, scoped repair boundaries and WordPress host requirements remain protected. No new Product Type, external specialist or application dependency is added.

| Work | State | Evidence / next action |
| --- | --- | --- |
| Dashboard default and implementation guide | Completed | [2026-10-16 source/scenario and consumer checks](evals/shadcn/REVIEW.md) |
| Regression and scope preservation | Completed | [2026-10-16 verification and limits](evals/shadcn/REVIEW.md#verification-record); historical WPS evidence retained |
| Integration / release / local installation | Completed | Authorized by the later [3.5.0 delivery decision](#release-350); [verified delivery](docs/releases/3.5.0.md) |

Acceptance: compatible new dashboards choose shadcn/ui without another library-choice question; explicit alternatives and existing-stack/host constraints are respected; templates do not override approved foundations; primary/dark/secondary review stays sequential. [Scoped cases and review](evals/shadcn/REVIEW.md) retain evidence limits.

## WordPress settings extension (WPS)

**Goal:** clearer, reliable plugin-owned settings pages inside `wp-admin`, using stable public `@wordpress/components`, including simple forms. This is not a redesign of all plugin-management screens or other products.

The [detailed implementation plan](docs/WORDPRESS_SETTINGS_ROADMAP.md) owns scope, allowed files, scenarios and exit criteria. This table is the **only live package-status ledger**. Planning does not complete WPS-0.

| Package | Deliverable | Status | Execution prerequisite | Acceptance evidence |
| --- | --- | --- | --- | --- |
| WPS-0 | Baseline, protected files and bounded kickoff | Completed | Owner instruction to execute WPS | [2026-10-10 baseline acceptance](evals/wordpress-settings/EXECUTION.md#wps-0--2026-10-10) |
| WPS-1 | Mandatory components and settings-only routing | Completed | Accepted WPS-0 | [2026-10-10 route acceptance](evals/wordpress-settings/EXECUTION.md#wps-1--2026-10-10) |
| WPS-2 | Task-based layout, visual criteria and reliable saving | Completed | Accepted WPS-1 | [2026-10-10 interaction acceptance](evals/wordpress-settings/EXECUTION.md#wps-2--2026-10-10) |
| WPS-3 | Stable component and compatibility guidance | Completed | Accepted WPS-2 | [2026-10-10 guidance acceptance](evals/wordpress-settings/EXECUTION.md#wps-3--2026-10-10) |
| WPS-4 | Simple and multi-topic specimens in real WordPress admin | Completed | Accepted WPS-3; authorized test environment | [2026-10-10 real-admin acceptance](evals/wordpress-settings/EXECUTION.md#wps-4--2026-10-10) |
| WPS-5 | Behavioral, data-preservation and isolation evaluation; dedicated CI gate | Completed | Accepted WPS-4 | [2026-10-10 evaluation acceptance](evals/wordpress-settings/EXECUTION.md#wps-5--2026-10-10) |
| WPS-6 | Local acceptance, package verification and reviewable handoff | Completed | Accepted WPS-5 | [2026-10-10 local acceptance](evals/wordpress-settings/EXECUTION.md#wps-6--2026-10-10) |

### Original WPS workstream complete

All seven packages and the authorized GitHub release are complete. [Delivery evidence](evals/wordpress-settings/EXECUTION.md#integration-and-publication) includes exact-candidate CI, merge/tag binding, installer smoke checks and independent verification of actual downloads.

The original WPS packages stay closed with their historical evidence. The newly audited specimen conflict defect is queued separately in [R11.1](#r11-audit-remediation); it does not invalidate the narrower title-conflict test that previously passed or authorize a production-plugin migration. No new local installation or deployment is authorized.

## Scope and acceptance rules

- Stabilization maintenance remains the default. WPS execution needs its own bounded instruction; completed R0–R8 and R9 exceptions are not new authority.
- Preserve other product routes, shared rules, permissions, data contracts and approved `DESIGN.md` decisions. No new Product Types, external design specialists, general-purpose page builder or repository-wide framework is authorized.
- The WPS plan permits only named settings behavior, dedicated evaluation support and a narrowly additive CI hook. An out-of-scope need requires a recorded scope decision, not weaker existing checks.
- Keep primary-language/direction review, later dark-mode review and optional secondary-language approval sequential. Existing acceptance remains scoped; do not reopen accepted font tests without a concrete defect.
- Source checks, agent observations, rendered/runtime evidence and owner approval are distinct. Example-product approval is not Skill engineering acceptance.
- Completion does not authorize push/merge, publication, installation or deployment. Preserve user changes; do not infer new delivery permission from historical approvals.
- R11 is bounded to its three audited findings and the tests/documentation needed to verify them. Planning does not reopen completed design approvals, change release metadata or authorize implementation.

## Completed history

These rows summarize closed work, not pending tasks. Historical limitations and original evidence remain attached to their checkpoint.

| Work | Final state | Evidence |
| --- | --- | --- |
| Original stages 1–6: product packs, shared rules, design system and evaluation | Completed | [Original capability history](docs/archive/ROADMAP-2026-10-06.md#completed-capability-history) |
| R0–R2: controlled kickoff, discovery and living `DESIGN.md` | Completed, 2026-10-04 | [Correction-stage records](docs/archive/ROADMAP-2026-10-09.md#correction-stage-tracker) |
| R3–R4: sequential samples, approval and incremental decisions | Completed, 2026-10-04–05 | [Correction-stage records](docs/archive/ROADMAP-2026-10-09.md#correction-stage-tracker) |
| <a id="r5-executable-checkpoint--2026-10-05"></a><a id="r5-delivery-acceptance--2026-10-05"></a>R5: safe runtime appearance controls | Completed, 2026-10-05 | [Executable scope](docs/archive/ROADMAP-2026-10-06.md#r5-executable-checkpoint--2026-10-05); [acceptance](docs/archive/ROADMAP-2026-10-06.md#r5-delivery-acceptance--2026-10-05) |
| <a id="r6-delivery-acceptance--2026-10-05"></a>R6: editable semantic icons | Completed, 2026-10-05 | [Acceptance](docs/archive/ROADMAP-2026-10-06.md#r6-delivery-acceptance--2026-10-05) |
| <a id="design-evidence-remediation-follow-up"></a>R7–R8: integrated visual quality, evaluation and readiness | Completed, 2026-10-06 | [Acceptance and limits](docs/archive/ROADMAP-2026-10-09.md#acceptance-and-known-limits); [QF01–QF07 evidence](evals/samples/REMEDIATION_PLAN.md) |
| <a id="optional-material-design"></a>R9: optional Material Design | Completed; 6 of 6 packages, 2026-10-06 | [Package records](docs/archive/ROADMAP-2026-10-09.md#r9-package-tracker) |
| <a id="r10-audit-remediation"></a>R10: five audit repairs | Completed; 5 of 5 packages, 2026-10-07 | [Acceptance and integration](docs/archive/ROADMAP-2026-10-09.md#r10-audit-remediation); [detailed regressions](docs/AUDIT_REMEDIATION.md) |
| <a id="release-checkpoint"></a>Releases 3.2.0, 3.2.1 and 3.3.0 | Published; recorded artifact and local-install checks completed | [Release provenance, hashes and limits](docs/archive/ROADMAP-2026-10-09.md#release-checkpoint) |
| Initial WPS planning | Integrated, 2026-10-09; implementation not started | [PR #42](https://github.com/pooyahayati/UI-UX-Skill/pull/42) |
| WPS-0–WPS-6 and release 3.4.0 | Completed and published, 2026-10-10; 7 of 7 packages | [Acceptance, source/runtime limits and release provenance](evals/wordpress-settings/EXECUTION.md); [published package checks](evals/wordpress-settings/RELEASE_PUBLISHED.json) |
| Dashboard shadcn/ui default, optional interactive motion and release 3.5.0 | Completed, merged, published and installed locally, 2026-10-16 | [Exact source, CI, downloaded packages, security and managed-install verification](docs/releases/3.5.0.md) |

The historical five-product evaluation was source-based in the same session, not an independent browser/device run. R7/R8 and R9 acceptance is bounded to its recorded evidence; hypothetical specimen approvals are not unfinished Skill stages. See [full limitations](docs/archive/ROADMAP-2026-10-09.md#acceptance-and-known-limits).

## Updating this roadmap

- Allowed package states: `Not started`, `In progress`, `Blocked`, `Completed`, `Reopened`. Keep one active implementation package in the current workstream; an unstarted prerequisite alone is not a blocker. The historical WPS ledger and live R11 ledger remain separate.
- Update the package row, completed count, active/next package and authority together. Started work needs an execution-record link; completion needs dated acceptance evidence and satisfied prerequisites.
- Record the checked revision, actual checks, remaining limits and lead acceptance in the linked record. Keep local changes separate from integration/publication evidence.
- Retain useful completed evidence in tables/archives, not repeated execution prose. Archives are historical snapshots, never competing live trackers.
