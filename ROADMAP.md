# UI/UX Skill Roadmap

The live work queue is below. Completed work is summarized in [history](#completed-history); detailed execution and release evidence stays in the dated archives.

## Current state

| Item | State |
| --- | --- |
| Updated | 2026-10-10 |
| Released baseline | [v3.3.0](https://github.com/pooyahayati/UI-UX-Skill/releases/tag/v3.3.0); publication and local update verified 2026-10-07 |
| Current workstream | WordPress plugin settings UX (WPS) |
| Planning readiness | Plan prepared; detailed scope and exit criteria linked below |
| Completed WPS packages | 7 of 7 |
| Active WPS package | None |
| Next WPS package | None |
| Execution authority | [Owner-authorized execution and release](evals/wordpress-settings/EXECUTION.md#execution-authorization--2026-10-10) |
| Accountable role | Engineering lead / maintainer; one implementation writer |
| Delivery | Local acceptance complete; exact-candidate CI, merge and release verification pending; no local installation |

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

### Current action: Integration and release

All seven implementation packages are locally accepted. Complete the authorized delivery:

1. Push the reviewable branch and verify exact-candidate remote CI.
2. Merge only after passing checks; publish through the existing release workflow.
3. Download and independently verify the actual published artifacts and record provenance.

See [WPS-6 exit criteria](docs/WORDPRESS_SETTINGS_ROADMAP.md#wps-6-local-acceptance-and-reviewable-handoff).

## Scope and acceptance rules

- Stabilization maintenance remains the default. WPS execution needs its own bounded instruction; completed R0–R8 and R9 exceptions are not new authority.
- Preserve other product routes, shared rules, permissions, data contracts and approved `DESIGN.md` decisions. No new Product Types, external design specialists, general-purpose page builder or repository-wide framework is authorized.
- The WPS plan permits only named settings behavior, dedicated evaluation support and a narrowly additive CI hook. An out-of-scope need requires a recorded scope decision, not weaker existing checks.
- Keep primary-language/direction review, later dark-mode review and optional secondary-language approval sequential. Existing acceptance remains scoped; do not reopen accepted font tests without a concrete defect.
- Source checks, agent observations, rendered/runtime evidence and owner approval are distinct. Example-product approval is not Skill engineering acceptance.
- Completion does not authorize push/merge, publication, installation or deployment. Preserve user changes; do not infer new delivery permission from historical approvals.

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

The historical five-product evaluation was source-based in the same session, not an independent browser/device run. R7/R8 and R9 acceptance is bounded to its recorded evidence; hypothetical specimen approvals are not unfinished Skill stages. See [full limitations](docs/archive/ROADMAP-2026-10-09.md#acceptance-and-known-limits).

## Updating this roadmap

- Allowed package states: `Not started`, `In progress`, `Blocked`, `Completed`, `Reopened`. Only one WPS package is active at a time; an unstarted prerequisite alone is not a blocker.
- Update the package row, completed count, active/next package and authority together. Started work needs an execution-record link; completion needs dated acceptance evidence and satisfied prerequisites.
- Record the checked revision, actual checks, remaining limits and lead acceptance in the linked record. Keep local changes separate from integration/publication evidence.
- Retain useful completed evidence in tables/archives, not repeated execution prose. Archives are historical snapshots, never competing live trackers.
