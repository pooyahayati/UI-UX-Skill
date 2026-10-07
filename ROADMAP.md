# UI/UX Skill Roadmap

Current status, completed stages and maintenance boundaries. Detailed execution notes are in the [dated archive](docs/archive/ROADMAP-2026-10-06.md); archived pending states are not current blockers. The current maintenance objective is [R10 audit remediation](#r10-audit-remediation).

## Current state

- Last updated: **2026-10-07**.
- Current release: **[v3.2.0](https://github.com/pooyahayati/UI-UX-Skill/releases/tag/v3.2.0)**, published 2026-10-06.
- Current objective: **Finalize R10 delivery.** All five repairs have local acceptance; R10.1–R10.4 are integrated and R10.5 awaits final delivery review/CI.
- Implementation: **Completed**; **9 of 9 correction stages completed**. This count covers R0–R8 only, not the new maintenance backlog.
- Active implementation stage: **None**. The R0–R8 tracker is closed; R10 activity is tracked separately below.
- Next implementation stage: **None**; all six R9 packages and all five R10 repairs are locally completed. R10.5 still needs remote delivery verification.
- Next delivery action: **Review and integrate R10.5 with exact-head CI, then finalize the release/install gate.** The owner authorized R10.4 integration and continuation into R10.5. No R10.5 push, merge, new version publication or local installation/update has occurred; these delivery outcomes must be verified separately.
- Product handbook: **`DESIGN.md`**. Product-specific approval is separate from Skill engineering acceptance.
- Documentation maintenance: cleanup integrated through [PR #33](https://github.com/pooyahayati/UI-UX-Skill/pull/33) at `ce5bfb5`. R10 planning delivery is tracked by [PR #34](https://github.com/pooyahayati/UI-UX-Skill/pull/34) from `codex/audit-remediation-roadmap`; Skill/package/release versions remain unchanged.

### Correction stage tracker

Canonical current tracker; dates and evidence preserve bounded acceptance, not universal product/device certification.

| Stage | Deliverable | Status | Dependencies | Accountable role | Completed on | Acceptance evidence / PR |
| --- | --- | --- | --- | --- | --- | --- |
| R0 | Controlled kickoff, policy consistency, and ownership | Completed | Owner authorized kickoff; valid working checkout | Engineering lead / maintainer (single implementation writer) | 2026-10-04 | [R0 execution record](docs/archive/ROADMAP-2026-10-06.md#r0-execution-record) |
| R1 | Adaptive discovery and professional recommendations | Completed | Locally accepted R0 | Current design role; engineering lead accepts; single writer | 2026-10-04 | [R1 execution record](docs/archive/ROADMAP-2026-10-06.md#r1-execution-record) |
| R2 | Living `DESIGN.md` contract and profile migration | Completed | Integrated R1 | Current design role; one handbook writer | 2026-10-04 | [R2 execution record](docs/archive/ROADMAP-2026-10-06.md#r2-execution-record) |
| R3 | Sequential product-aware samples and versioned approval | Completed | R1, R2 | Design role; product owner approves actual product designs | 2026-10-04 | [R3 independent forward review](evals/samples/SEQUENTIAL_FORWARD_REVIEW.md) |
| R4 | Incremental decisions and bounded agent handoffs | Completed | R2, R3; scoped continuation and separate lead review accepted | Engineering lead (single writer) | 2026-10-05 | [R4 forward review](evals/samples/INCREMENTAL_FORWARD_REVIEW.md) |
| R5 | Parametric appearance governance with real consumers | Completed | R2, integrated R4 | Engineering lead with design input | 2026-10-05 | [R5 delivery acceptance](docs/archive/ROADMAP-2026-10-06.md#r5-delivery-acceptance--2026-10-05) |
| R6 | Editable semantic icons and icon families | Completed | Integrated R5 | Engineering lead with design input | 2026-10-05 | [R6 delivery acceptance](docs/archive/ROADMAP-2026-10-06.md#r6-delivery-acceptance--2026-10-05) |
| R7 | Integrated language, direction, theme, and visual quality | Completed | Contracts begin in R1/R3; final gate after R6 | Design role; engineering lead accepts | 2026-10-06 | [R7 scoped acceptance](docs/archive/ROADMAP-2026-10-06.md#r7-final-scoped-acceptance--2026-10-06); [PR #27](https://github.com/pooyahayati/UI-UX-Skill/pull/27) |
| R8 | Behavioral evaluation, package verification, release readiness | Completed | Accepted R0–R7 | Engineering lead / maintainer | 2026-10-06 | [R8 readiness](evals/samples/CANDIDATE_READINESS.md#final-scoped-readiness--2026-10-06); [PR #27](https://github.com/pooyahayati/UI-UX-Skill/pull/27) |

### Planned extension tracker

R9 is separate from the nine correction stages, not a tenth correction stage.

| Stage | Deliverable | Status | Dependencies | Accountable role | Completed on | Acceptance evidence / PR |
| --- | --- | --- | --- | --- | --- | --- |
| R9 | Optional Material Design module, product personalization, component guidance, and curated design-research references | Completed | Accepted R7 and R8; authorized R9 kickoff | Engineering lead / maintainer; current design role advises | 2026-10-06 | [R9.6 scoped acceptance](evals/material/R9_6_FORWARD_REVIEW.md); [integrated R9.5/R9.6](docs/archive/ROADMAP-2026-10-06.md#r95r96-delivery-checkpoint--2026-10-06) |

## Optional Material Design

Optional per product, not a mobile-first default or automatic library adoption. Existing product routes, approved foundations, permissions and stack remain authoritative.

### R9 package tracker

| Package | Deliverable | Status | Dependencies | Acceptance record |
| --- | --- | --- | --- | --- |
| R9.1 | Bounded activation, routing, and policy consistency | Completed | Accepted R7/R8; authorized kickoff | [2026-10-06 scoped source/policy acceptance](evals/material/R9_1_ACTIVATION.md); integrated PR #28 |
| R9.2 | Product-personalized foundations and curated research | Completed | Accepted R9.1 | [2026-10-06 scoped source-guidance acceptance](evals/material/R9_2_FOUNDATIONS.md); integrated PR #28 |
| R9.3 | Scoped component guidance and stack-fit assessment | Completed | Accepted R9.2 | [2026-10-06 instruction acceptance](evals/material/R9_3_COMPONENTS.md); integrated PR #28, not full mode acceptance |
| R9.4 | Sequential responsive samples and handbook integration | Completed | Accepted R9.2/R9.3 | [2026-10-06 source/workflow acceptance](evals/material/R9_4_SAMPLES.md); integrated PR #28, specimen approval unresolved |
| R9.5 | Material appearance controls through existing runtime contracts | Completed | Accepted R9.4; preserved R5/R6 contracts | [2026-10-06 scoped acceptance](evals/material/R9_5_RUNTIME.md); integrated PR #29 |
| R9.6 | Behavioral/rendered evaluation and candidate readiness | Completed | Accepted R9.1–R9.5 | [2026-10-06 scoped acceptance](evals/material/R9_6_FORWARD_REVIEW.md); integrated PR #29 |

See the [R9 plan and execution record](docs/archive/ROADMAP-2026-10-06.md#planned-post-correction-extension--r9-optional-material-design) for original tasks and exit criteria.

## R10 audit remediation

Bounded stabilization maintenance for the five findings from the 2026-10-07 deep audit, not a new capability exception or a reopening of all R7/R8/R9 acceptance. The owner integrated the plan, then authorized local R10.1 work with all remediation integration/publication/local updates held until final R10 acceptance.

- Planning readiness: **Ready for implementation handoff**; see [scope, tasks, regression scenarios and exit criteria](docs/AUDIT_REMEDIATION.md).
- Remediation implementation: **Completed**; **5 of 5 packages completed** (R10.1–R10.4 integrated; R10.5 locally accepted).
- Active remediation package: **None**; local fixes and the combined local gate are complete.
- Next remediation package: **None**; final remote integration, release and installation remain separate delivery gates.
- Accountable role: **Engineering lead / maintainer, one implementation writer**. Additional agents are not required or authorized by this plan.
- Delivery state: **R10.1 integrated through [PR #35](https://github.com/pooyahayati/UI-UX-Skill/pull/35) at `14d78cb`; R10.2 through [PR #36](https://github.com/pooyahayati/UI-UX-Skill/pull/36) at `ab20b75`; R10.3 through [PR #37](https://github.com/pooyahayati/UI-UX-Skill/pull/37) at `d813e33`; R10.4 through [PR #38](https://github.com/pooyahayati/UI-UX-Skill/pull/38) at `e88693e`.** R10.4 [pre-merge checks](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37602004111) and [post-merge checks](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37602163431) passed; publication was skipped. R10.5 is locally completed on `codex/r10-5-specialist-integrity`, not pushed or remotely CI-verified. Version stays `3.2.0`; no release or local installation/update has been performed for R10.

| Package | Audit finding / deliverable | Severity | Status | Execution prerequisite | Acceptance evidence |
| --- | --- | --- | --- | --- | --- |
| R10.1 | [F01: protect package output and preserve data on failure](docs/AUDIT_REMEDIATION.md#r101-safe-release-packaging) | High | Completed | Owner-authorized local kickoff; baseline `4f13176` | [Local verification](docs/AUDIT_REMEDIATION.md#r101-verification-record-2026-10-07); [PR #35](https://github.com/pooyahayati/UI-UX-Skill/pull/35), pre/post-merge CI passed |
| R10.2 | [F02: repair and validate packaged resource routes](docs/AUDIT_REMEDIATION.md#r102-resource-route-integrity) | High | Completed | Integrated R10.1; owner-authorized next package | [Local verification](docs/AUDIT_REMEDIATION.md#r102-verification-record-2026-10-07); PR #36, pre/post-merge CI passed |
| R10.3 | [F03: recover stale appearance drafts without losing intended edits](docs/AUDIT_REMEDIATION.md#r103-stale-draft-recovery) | Medium | Completed | R10.2 integrated through PR #36 at `ab20b75`; owner-authorized continuation | [Local verification](docs/AUDIT_REMEDIATION.md#r103-verification-record-2026-10-07); PR #37, pre/post-merge CI passed |
| R10.4 | [F04: reject contradictory behavioral-evaluation verdicts](docs/AUDIT_REMEDIATION.md#r104-consistent-evaluation-verdicts) | Medium | Completed | R10.3 integrated through PR #37; owner-authorized continuation | [Local verification](docs/AUDIT_REMEDIATION.md#r104-verification-record-2026-10-07); PR #38, pre/post-merge CI passed |
| R10.5 | [F05: verify the specialist package, not only its entrypoint](docs/AUDIT_REMEDIATION.md#r105-specialist-package-integrity) | Medium | Completed | R10.4 integrated through PR #38; owner-authorized continuation | [Local and combined verification](docs/AUDIT_REMEDIATION.md#r105-verification-and-integrated-local-acceptance-2026-10-07): Windows/Linux regressions, live read-only package check and both consumer packages passed; remote CI pending delivery |

The sequence is a single-writer delivery order, not a claim that every package has a code dependency on its predecessor. R10.2's packaged-resource verification does depend on safe packaging. Each package needs its defect regression and affected existing checks before completion. R10.5 also closes the [integrated acceptance gate](docs/AUDIT_REMEDIATION.md#integrated-acceptance-and-delivery-boundary); it cannot complete the workstream with another finding unresolved.

Keep current statuses, counts, active/next package and dated acceptance links here. The detailed plan is not a competing status ledger. Earlier audit checks are a baseline, not proof that any R10 finding is fixed.

## Design contract

- Inspect existing decisions; ask only product-relevant missing questions and recommend professional defaults.
- Review one responsive primary-language/direction sample using settled palette, fonts, scales and spacing. Record corrections and approval of the actual revision.
- Derive dark mode after primary approval; add secondary language/layout only after dark approval, confirmed need and owner authorization. Monolingual products need no extra locale sample.
- Keep `DESIGN.md` as the living handbook. Distinguish proposals, approved design decisions and active runtime configuration.
- Plan Design and Appearance controls only for in-scope products with admin. Prepared parameters/assets must reach real consumers through trusted validation, private drafts, publication, history and rollback.
- Preserve editable semantic icons, mixed-script behavior and accessibility/safety floors. New libraries, arbitrary assets, code execution or unrelated product redesign are not routine no-code changes.

Detailed [requirements](docs/archive/ROADMAP-2026-10-06.md#agreed-correction-requirements), [agent boundaries](docs/archive/ROADMAP-2026-10-06.md#agent-responsibility-and-delegation-contract), [parameter contract](docs/archive/ROADMAP-2026-10-06.md#appearance-parameter-contract) and [acceptance scenarios](docs/archive/ROADMAP-2026-10-06.md#planned-acceptance-scenarios) remain archived without weakening their scope.

## Acceptance and known limits

- R7/R8 are accepted for documented Skill/synthetic-fixture scope; [integrated quality](evals/samples/INTEGRATED_QUALITY_REVIEW.md), [candidate readiness](evals/samples/CANDIDATE_READINESS.md) and [owner/font acceptance](docs/archive/ROADMAP-2026-10-06.md#explicit-owner-acceptance-of-the-font-review--2026-10-06) retain attribution and failed/unavailable captures. Do not reopen font tests absent a concrete defect.
- R9's [six-case forward review](evals/material/R9_6_FORWARD_REVIEW.md) retains F01 reference-read ordering, shared-session and device/assistive-technology limits. It is not an all-case fresh-model or universal conformance claim.
- Structural checks, model observations, rendered/runtime tests and owner approval are distinct. The [historical five-product result](evals/real-world/RESULTS.md) retains its original version/date/model provenance.
- The [authored Material specimen](evals/material/ham-amooz/DESIGN.md) is proposed, dark unstarted and secondary N/A. These are hypothetical product approval states, not unfinished Skill engineering stages.
- Product behavior, permissions, data integrity, active-route isolation and existing stack choices remain protected. No external design specialist was added; `persian-writing` remains required for Persian-facing UI.
- All five R10 findings have scoped local regression acceptance; R10.1–R10.4 are integrated and R10.5 awaits remote delivery verification. No fresh all-scenario agent evaluation or R10 release/install success is claimed.

## Release checkpoint

- [PR #31](https://github.com/pooyahayati/UI-UX-Skill/pull/31) delivered compatible minor 3.2.0 at `2c30f9b1ac70529efc1addeb2f833c264018312c`; [publication workflow](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37403411984) succeeded.
- [PR #32](https://github.com/pooyahayati/UI-UX-Skill/pull/32) recorded publication on main at `048b64054d2b27d70da4dd0b1cb737e74ba81db3`; [post-merge checks](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37403960207) passed and correctly skipped duplicate publication.
- Downloaded 88-member Skill / 95-member plugin archives matched canonical release Git blobs, version, CRC and SHA256SUMS. Native source/package secret scans passed. Windows/Linux ZIP-byte identity was not claimed.
- Full [release provenance, hashes and limits](docs/archive/ROADMAP-2026-10-06.md#v320-release-checkpoint--2026-10-06) are retained. This cleanup does not change published assets or installed files.

### R5 executable checkpoint — 2026-10-05

Historical compatibility target for fixture links: the executable synthetic runtime scope and initial limitations remain in the [original R5 checkpoint](docs/archive/ROADMAP-2026-10-06.md#r5-executable-checkpoint--2026-10-05).

### R5 delivery acceptance — 2026-10-05

R5 has bounded engineering acceptance; [original source/scan/CI and recovery evidence](docs/archive/ROADMAP-2026-10-06.md#r5-delivery-acceptance--2026-10-05) remains distinct from later stages and production security certification.

### R6 delivery acceptance — 2026-10-05

R6 semantic-icon scope and [original acceptance/verification](docs/archive/ROADMAP-2026-10-06.md#r6-delivery-acceptance--2026-10-05) are retained; no raw runtime fixture or its byte binding changed.

### Design evidence remediation follow-up

The [QF01–QF07 remediation record](evals/samples/REMEDIATION_PLAN.md) and [historical roadmap entry](docs/archive/ROADMAP-2026-10-06.md#design-evidence-remediation-follow-up) retain failures, scoped verification and attributed owner/font acceptance. Earlier pending states are historical.

## Progress-update protocol

1. Before an authorized stage, inspect current source, applicable instructions and prerequisite evidence; record stage, owner, scope, dependencies and acceptance criteria.
2. Record actual partial work and blockers. `Completed` requires dated evidence, relevant checks and lead acceptance; real product-owner approval must be attributed.
3. Update tracker/count/next action together. Keep R10 maintenance separate from the completed R0–R8/R9 capability-stage counts; record each R10 package's dated acceptance, checked revision, actual checks and unresolved limits.
4. Keep proposed/local work distinct from passing integration. Do not infer delivery permission from completion; never invent PRs, CI results or approvals.
5. Preserve old evidence in the dated archive; use `Reopened` for invalidated acceptance. Keep caches/generated reports outside product source.

Allowed states: `Not started`, `In progress`, `Blocked`, `Completed`, `Reopened`. A future stage is not blocked solely because its prerequisite has not started. This roadmap is the single current status source; do not add a competing status document.

## Historical capability stages

The six original stages remain completed as recorded. Full deliverables and acceptance details are in the [execution archive](docs/archive/ROADMAP-2026-10-06.md#completed-capability-history).

## Stage 1 — Website Product Pack

**Status:** Completed. [Original record](docs/archive/ROADMAP-2026-10-06.md#stage-1--website-product-pack).

## Stage 2 — WordPress Plugin Product Pack

**Status:** Completed. [Original record](docs/archive/ROADMAP-2026-10-06.md#stage-2--wordpress-plugin-product-pack).

## Stage 3 — Dashboard Product Pack

**Status:** Completed. [Original record](docs/archive/ROADMAP-2026-10-06.md#stage-3--dashboard-product-pack).

## Stage 4 — Shared Product UI Rules

**Status:** Completed. [Original record](docs/archive/ROADMAP-2026-10-06.md#stage-4--shared-product-ui-rules).

## Stage 5 — Design System Hardening

**Status:** Completed. [Original record](docs/archive/ROADMAP-2026-10-06.md#stage-5--design-system-hardening).

## Stage 6 — Real-World Product Evaluation

**Status:** Completed. [Original record](docs/archive/ROADMAP-2026-10-06.md#stage-6--real-world-product-evaluation).

The historical run was an **in-session source-based behavioral evaluation**; it **did not independently execute** a fresh browser/device or separate Codex/Claude run. Those unavailable checks are **not represented as completed checks**. Later scoped evidence remains separately attributed.

## Feature Freeze — 3.1.0 Stabilization

**Status:** Active with limited correction exception

**Correction exception:** Authorized for R0–R8 only.

**Outside this exception:** Stabilization maintenance only, except for the separately named R9 exception below.

Allowed correction scope:

- design foundation;
- the living handbook;
- visual approval;
- safe parametric appearance management.

The completed exception is not permission for new Product Types, new major capability families, additional external design specialists or a general-purpose page builder. `persian-writing` remains the only external specialist.

Allowed maintenance: deduplication, context isolation, correctness, validation, documentation, packaging and release reliability. Further capability expansion requires a separate explicit decision.

**Separate R9 exception:** Optional Material Design only.

**R9 kickoff:** Authorized local R9.1 implementation on 2026-10-06 after accepted R7/R8.

Allowed R9 scope:

- optional Material activation and routing;
- product-personalized foundations and curated research;
- scoped component guidance and stack-fit assessment;
- sequential responsive samples and handbook integration;
- appearance controls through existing runtime contracts;
- bounded behavioral/rendered evaluation and candidate readiness.

All six packages are completed within that scope. Outside the two named exceptions, stabilization maintenance only. Further push/merge, release, installation and deployment require actual authority; earlier delivery permission is not silently inherited.
