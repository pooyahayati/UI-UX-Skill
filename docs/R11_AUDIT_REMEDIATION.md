# R11: Post-3.5.0 Audit Remediation

Prepared 2026-10-16. This plan defines three bounded correction packages, not completed implementation. [ROADMAP.md](../ROADMAP.md#r11-audit-remediation) is the only live progress ledger; this document owns scope and acceptance criteria.

## Objective and authority

Resolve the two confirmed defects and close the behavioral-evaluation gap from the latest deep audit. Preserve existing product routes, accepted design decisions, historical evidence and safe delivery contracts.

The original planning instruction authorized only this plan and the roadmap. The owner's later 2026-10-16 instruction explicitly authorizes R11.1 through R11.3, merge, a new release and this Skill's managed local update, as recorded in the [roadmap](../ROADMAP.md#r11-audit-remediation). Acceptance criteria and protected scope remain unchanged. No unrelated dependency/skill update or production deployment is implied.

Use one implementation writer. Follow R11.1, R11.2, then R11.3 by priority. The packages have separate technical boundaries; a genuine blocker can justify documented resequencing of independent authorized work, not an unsupported completion claim. No new Product Pack, external specialist, component library, general-purpose evaluation platform or production settings engine is planned.

## Audit baseline and finding evidence

- Released version: `3.5.0`; immutable tag commit `6b371db7d751d411c3b15c0d45dd5382f426232f`.
- Audited local source: `435eb0b13d77d22ba5d72376a83dc7c2a0801914`; its tree matches merged main `ec5293a2190fd5ff332c84545a5a6e14bacd4e0e`. Remote main/tag were rechecked during planning.
- Audit checks reported 153 Python test executions: 149 passed and four native-symlink cases skipped on Windows. Dialog keyboard and runtime-recovery model suites each passed 11 checks; WordPress draft-model checks also passed. These green checks did not cover the newly reproduced failures.
- The 114-case manifest is an input inventory, not 114 freshly executed model evaluations. Existing shadcn/motion reviews are explicitly source-based. The audit's four independent source-driven plans were additional reasoning evidence, not a persistent behavioral regression suite or browser run.
- No real WordPress/browser rerun was performed during the audit. The conflict reproduction executed the actual UI handlers with modeled React/HTTP behavior; source tracing confirmed the backend accepts the fresh revision and supplied stale field. The missing notice was checked in the actual published standalone ZIP.

| Finding | Classification | Repository evidence and observed gap |
| --- | --- | --- |
| R11-F01 | Medium; confirmed specimen defect | [Conflict adoption and full-section submission](../evals/fixtures/wordpress-settings/plugin/app.js), [revision-checked persistence](../evals/fixtures/wordpress-settings/plugin/wps-specimen.php): accepting the new server revision retains untouched stale draft fields. The review dialog omits the endpoint. [Existing browser coverage](../evals/wordpress-settings/run_browser.cjs) checks intentional replacement of the same title, not preservation of a peer's different field. |
| R11-F02 | Medium; confirmed distribution defect | [Packager](../scripts/package_release.py) copies root legal files only into the plugin. The published 91-member standalone ZIP contains neither `LICENSE` nor the full notice required by the [root license](../LICENSE). [Package verification](../evals/wordpress-settings/verify_packages.py) derives an inventory that also omits it. This is a notice-completeness finding, not a legal-liability conclusion. |
| R11-F03 | Medium; coverage risk, not a reproduced agent defect | [Eight shadcn inputs/review](../evals/shadcn/REVIEW.md#scenario-review) and [ten motion inputs/review](../evals/motion/REVIEW.md#scenario-review) have source-traced expectations. The [source-delta tests](../evals/wordpress-settings/test_contracts.py) protect content identity, not actual agent decisions. |

Recheck the affected source and current working-tree changes before each package. If a finding is already fixed or its reproduction no longer applies, record the evidence and revise only the affected plan; do not implement a redundant fix.

## Protected contracts and evidence handling

- Keep native WordPress components, option keys, capabilities, nonce checks, server revision checks, per-section saves and truthful rejected/unknown/saved states. The fixture remains synthetic and must not contact a real service or modify a real site's data.
- Keep the dashboard default conditional on explicit alternatives, established stacks and native hosts. Motion/Animate UI remain product-driven options; owner configuration cannot override user/OS reduction or off. Do not turn the testing gap into a reason to rewrite otherwise-correct guidance.
- Preserve approved foundations, Persian/Vazirmatn decisions, the living `DESIGN.md`, primary-then-dark review and optional authorized secondary-language review. Do not ask for unrelated screenshots or repeat accepted font tests.
- Preserve R10 filesystem/package safety, source/resource isolation, strict verdict consistency and existing useful regressions. Never disable a failing gate or widen an allowlist merely to permit a candidate.
- Keep original WPS results/screenshots, release records and shadcn/motion source reviews as historical checkpoints. Record corrected behavior and new outputs as dated successor evidence with exact source/fixture identities; do not relabel old evidence as a new run.
- Existing WPS integrity tests bind recorded browser hashes to the live fixture, and protected-source tests enumerate Skill resources. R11.1 and R11.2 must deliberately extend those contracts for named successors/additions while still checking the unchanged historical checkpoint and the exact current candidate. Do not overwrite historical hashes to hide a mismatch.
- Reuse existing runners and fixtures. Temporary applications, synthetic databases, archives, raw execution logs and scans stay outside product source. Commit only scoped test inputs, harness changes and sanitized durable acceptance evidence when separately authorized.

## R11.1: WordPress conflict recovery

### Scope and first result

Primary paths: [specimen model](../evals/fixtures/wordpress-settings/plugin/model.js), [UI handlers](../evals/fixtures/wordpress-settings/plugin/app.js), [model tests](../evals/wordpress-settings/test_model.cjs), [browser runner](../evals/wordpress-settings/run_browser.cjs), and their evidence/integrity checks. Change PHP only if a reproduced failure shows the existing save contract cannot support the bounded fix; no new storage schema, role or endpoint is implied.

First add a regression that fails on the audited implementation: both editors load one revision; editor A changes only the credential intent; editor B saves a different endpoint; A encounters conflict and chooses to retain their edits. The resulting save must retain B's endpoint while applying A's intended credential action. Use synthetic secrets and never retain their values in logs or review text.

### Implementation approach

Keep the editing base, local intent and newest server snapshot distinguishable. A field unchanged by the local editor adopts the latest stored value. An independently changed local field retains its intent. A field changed differently by both editors requires a visible, deliberate choice before submission. Preserve edits made while requests/review are pending and leave untouched drafts in other sections intact.

Show all affected changed/conflicting fields, including endpoint and enabled state; summarize credential actions/presence without exposing saved secrets. Keep server-side revision checks so another write during review still causes a new conflict instead of bypassing protection. Cancel must preserve local input and make no write.

### Acceptance criteria

| ID | Observable result / required evidence |
| --- | --- |
| WP-A1 | The exact endpoint/credential regression fails before the fix and passes after it using the actual reconciliation/UI path; the submitted payload and authoritative stored endpoint both retain the peer change. |
| WP-A2 | Different fields changed in the same section reconcile without lost updates; an untouched section does not become a pending user edit merely because a peer changed it. Existing unrelated unsaved local edits survive. |
| WP-A3 | Same-field conflicts show the latest value and local intent and require an explicit choice. The original intentional title replacement remains supported through that choice; endpoint/enabled conflicts are not invisible. |
| WP-A4 | A newer server revision during review is rejected/reconciled again; cancelling or a rejected save preserves draft input and does not modify stored values. Credential keep/replace/remove semantics remain intact. |
| WP-A5 | Existing duplicate-submit, edits-during-save, unknown-outcome, section reset, authorization and nonce checks continue to pass with no secret disclosure. Reuse existing checks where they detect the same failure. |
| WP-A6 | Two real synthetic admin sessions reproduce and then verify the corrected path on the declared WordPress test hosts. Inspect the changed review controls for keyboard/focus and the supported Persian/English narrow layout; this is focused interaction verification, not a new design/font approval cycle. |

Checks: `node evals/wordpress-settings/test_model.cjs`, the focused/new cases in `node evals/wordpress-settings/run_browser.cjs`, and `python -B evals/wordpress-settings/test_contracts.py`. Run the browser command only after checking ownership of the existing synthetic hosts and selecting fresh external evidence output; never reset a real installation. Keep the historical evidence recorder's fixed 3.4.0-era metadata out of new acceptance claims.

**Exit:** WP-A1 through WP-A6 have candidate-bound passing evidence and lead review; the old title-only observation remains valid but explicitly narrower. If real-admin checks are unavailable, deterministic work may be retained, but this package is not complete. Record the specific missing environment/check.

## R11.2: Complete distribution notices

### Scope and implementation approach

Primary paths: [packager](../scripts/package_release.py), [packaging tests](../scripts/test_package_release.py), [consumer verifier](../evals/wordpress-settings/verify_packages.py), source-identity tests and directly affected installation documentation. Preserve the root license text and copyright attribution.

Preferred implementation: make the full notice available at the canonical Skill root so direct repository-path installation and the standalone ZIP both retain it. Keep that notice synchronized with the root license through an explicit test. Preserve the plugin's existing legal files. Account for this exact source addition in the successor integrity record rather than exempting all legal/new resources. Generated release metadata and final version choice remain outside this package until delivery is authorized.

### Acceptance criteria

| ID | Observable result / required evidence |
| --- | --- |
| PK-A1 | A new completeness regression fails against the audited standalone package/install payload. It expects the notice independently of the current member inventory, so the existing omission cannot redefine success. |
| PK-A2 | Fresh standalone and plugin archives contain the full, correct copyright and permission notice. A direct Skill-subdirectory staging/install path includes the same notice without relying on a managing Head to inject it. |
| PK-A3 | Missing, empty, truncated or mismatched notices are rejected, even when the ZIP is readable and its checksums have been regenerated correctly. |
| PK-A4 | Exact archive member inventory, source-content identity, CRC/checksums, embedded version and extracted-resource routing pass for both formats. The only expected content delta is the documented notice/supporting correction. |
| PK-A5 | Existing path/symlink refusal, fresh-output requirement, failure preservation and source-isolation tests remain effective. Earlier artifacts, active installations and local Head contracts are unchanged. |

Checks: `python -B scripts/test_package_release.py`, `python -B evals/wordpress-settings/test_contracts.py`, fresh external output from `scripts/package_release.py`, the consumer verifier against those actual ZIPs, and `scripts/validate_resource_routes.py` against each independently extracted Skill root. Inspect a separately staged direct-install payload; do not treat a repaired local managed installation as proof that upstream distribution is complete.

**Exit:** PK-A1 through PK-A5 pass for candidate artifacts and direct-install staging. Do not modify the existing `v3.5.0` tag/assets or active installation. Verification of a future published download belongs to the separately authorized delivery gate.

## R11.3: Repeatable behavioral evaluation

### Scope and approach

Reuse [shadcn raw inputs](../evals/shadcn/CASES.md), [motion raw inputs](../evals/motion/CASES.md) and the existing [evaluation conventions](../evals/README.md). Extend the existing preparation/result path only as needed to make selected cases addressable, record actual outputs and validate their outcomes; do not introduce another general-purpose evaluation framework or a paid API requirement.

Before running, choose a bounded representative case set and record its coverage rationale. Cover each distinct decision family below; the example IDs are existing inputs, not mandatory duplicate tests. Unselected prompts remain explicitly unexecuted, not implicitly passed. Reuse one case for multiple outcomes when it genuinely exercises them.

| Decision family | Existing raw inputs to select from | Required observable behavior |
| --- | --- | --- |
| Dashboard default and explicit alternative | S01, S02 | Apply the compatible dashboard default; an explicit alternative wins; approved foundations remain unchanged. |
| Existing stack, host and task scope | S03, S04, S06, M07, M08 | No forced framework/library migration, native settings replacement, new admin backend or implementation during an audit-only request. |
| Provider/component adoption and maintenance | M01, M02, M03, S08 | CSS suffices for small effects; conditional Motion/Animate UI choices need a concrete fit; retain primitive APIs, local component edits and accessible non-drag actions. |
| Resolved motion and interrupted operations | M04, M05, M10 | Owner ceiling, user off and live OS reduction all remain effective; reduced is not fully off; startup, cleanup/focus and truthful save outcomes do not depend on animation completion. |
| Safe owner configuration | M06 | Reject arbitrary executable configuration; preserve private draft/publication, valid old preferences, failed-load recovery and history/rollback boundaries. |
| Product-specific foundations and approvals | S05, S07, M09 | Keep the canonical handbook and settled tokens; primary/dark/authorized-secondary sequence remains; optional Material style is not an automatic library choice. |

Use a fresh independent evaluator context with only the candidate Skill, the selected raw request and needed raw artifacts. Do not send this plan, reviewer rubric, expected answers, prior outputs or audit conclusions to that evaluator. Use an authorized subagent/session when available; do not create a new user-owned chat, install tools or incur external service cost implicitly. If independent execution is unavailable, record the limitation rather than converting another source trace into a behavioral pass.

### Acceptance criteria

| ID | Observable result / required evidence |
| --- | --- |
| EV-A1 | Each selected case has an unambiguous ID, reproducible preparation/invocation, frozen raw-input identity and a reviewer rubric kept separate from evaluator inputs. All decision families above have coverage. |
| EV-A2 | Retain the actual evaluator output, date, host/model, source commit or tree/content identity, case/input identity and review outcome. Planned or source-traced conclusions are not stored as executed outputs. |
| EV-A3 | A reviewer scores decisions/invariants, not exact phrases. All selected required outcomes pass; failure, partial or unavailable required evidence prevents package acceptance and receives an explicit next action. |
| EV-A4 | Deterministic regression checks reject missing output/evidence, stale source/input binding, duplicate cases, contradictory pass/fail records and expected-answer leakage through preparation. Preserve existing result-validator semantics: valid failure records are recordable, not acceptance. |
| EV-A5 | CI runs the cheap preparation/record-integrity/acceptance checks through the existing workflow. Recorded outcomes are bound to their candidate; CI does not claim to rerun the model or silently trigger paid/live evaluations. Candidate changes invalidate only affected evidence with an explicit mapping. |
| EV-A6 | Historical five-product, WPS and source-only shadcn/motion records retain their original provenance. The new record states selected/executed/unexecuted coverage and separates agent decisions from browser/runtime behavior and owner visual approval. |

Checks: the existing preparation/validation commands extended for the selected inputs, focused negative regressions and actual independent executions. Do not claim browser behavior for Motion/Animate UI merely from an agent answer; no runtime adapter or product animation implementation is delivered by this package. Change guidance only if evaluation exposes a reproducible decision defect, then rerun the affected cases against the corrected candidate.

**Exit:** EV-A1 through EV-A6 pass with real outputs and lead acceptance. Repository source hashes alone cannot close this package; an unavailable independent run is a concrete remaining limitation.

## Combined acceptance and delivery boundary

R11 implementation is ready for review only when all three packages meet their own criteria, their current source/evidence agree and no required check remains failed or unverified. Update the single roadmap tracker with dated evidence and the actual completed/active/next state after each package. Record exact commands/results, skips, relevant environment, candidate identity and lead acceptance in the linked successor record; do not create a second live status table here.

At combined closeout, run the affected existing regressions plus repository release/resource/product/shared/design/specialist validators, eval-result checks, final candidate packaging and source/diff review. Preserve historical counts/results; additional scenarios are named additions, not retroactive successes. Review README, INSTALL, CHANGELOG and status wording for any claims changed by R11, without a cosmetic rewrite or early version bump.

Implementation acceptance is not delivery authority. If later authorized to deliver, require exact-head CI and reviewed merge, native security checks relevant to the final source/artifact, a new version with truthful notes, and verification of actual published downloads (notice, checksums, members, source/tag binding and resources). Do not replace 3.5.0 assets. Local update requires its own valid authority, managed integration preservation, a recoverable backup and verification of the installed candidate. Unavailable release/install checks block that delivery action, not unrelated authorized work.

## Original planning checkpoint and execution handoff

The planning-only checkpoint passed with 69 internal links, 27 roadmap-policy tests and release metadata checks; its original status was `0 of 3` / no active package / next `R11.1`. Only the two planning documents changed in that checkpoint. Subsequent implementation status and authority live in the roadmap, not in this historical checkpoint.

The next implementation instruction can start R11.1 directly: inspect current user changes and source, retain the exact two-editor reproduction, add the failing regression, then implement the smallest reconciliation correction. Do not ask the owner to repeat settled design/font approvals. Report the observable result, tests and remaining scope at the stage boundary; continue only as far as the actual execution instruction authorizes.
