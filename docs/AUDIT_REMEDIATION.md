# R10: Deep Audit Remediation Plan

Prepared 2026-10-07. This document defines the work and acceptance criteria for five confirmed audit findings. [ROADMAP.md](../ROADMAP.md#r10-audit-remediation) is the single current progress ledger.

## Objective and authority

Remove the five evidenced failure modes with bounded fixes and regression coverage. Preserve the existing design workflow, product scope, historical evidence and installation boundaries. This is stabilization maintenance, not a redesign or a new capability family.

The owner authorized planning and its documentation-only integration through PR #34, then local R10.1 implementation on 2026-10-07 with delivery held. The subsequent explicit instruction authorizes integration of accepted R10.1 and local implementation of R10.2, overriding the earlier integration hold for R10.1 only. Work proceeds one package at a time. New publication and local Skill installation/update remain held until every R10 fix is completed and finalized. Do not bump release metadata or publish during an intermediate package. Later implementation acceptance alone does not authorize another merge.

The next owner instruction on 2026-10-07 additionally authorized R10.2 integration and local R10.3 implementation. This does not authorize intermediate R10.3 delivery, publication or installed-Skill changes.

The subsequent owner instruction authorized R10.3 integration and local R10.4 implementation. It does not authorize R10.4 delivery, R10.5 implementation, publication or installed-Skill changes. Prior checkpoint delivery limits below describe their original observation times; the roadmap records current integration state.

The following owner instruction authorized R10.4 integration and continuation into R10.5. This checkpoint completes the local repairs/combined verification and prepares final delivery; it does not claim that R10.5 was pushed/merged or that a release/install operation occurred. Final remote CI and actual artifact/installation checks remain distinct from local implementation acceptance.

Planning deliverables are this execution plan, the R10 tracker, an isolated local branch and verified document consistency. Implementation deliverables are the scoped fixes, regression tests and recorded acceptance described below; they do not exist merely because they are planned.

## Audit baseline and evidence limits

- Audited source: `99880c0d1d0e8e16aa77db7ebb215704f857d26d`; its tree matches merged main `ce5bfb5306f3ff0660c1ae7a0f6c76de793cf007` (PR #33). Remote main was read and matched that merge when preparing this plan.
- Source/release version: `3.2.0`. Do not change release metadata during planning.
- Prior audit baseline: 68 Python test executions, eight repository validators and 11 dialog DOM-model assertions passed. These checks did not detect the five reproduced findings.
- The manifest contains 114 behavioral scenarios and 606 invariants. That inventory is not a fresh all-scenario model run. Historical five-product evaluation keeps its original provenance.
- F01 was validated by intercepting the deletion call, without deleting data. F03 used actual interface logic with controlled DOM/HTTP responses. F04/F05 used in-memory records/mocks. These prove the stated defects, not fresh browser, production or live-install behavior.
- Recheck the affected source before each fix. Keep future observed results distinct from the baseline and the intended results below.

## Protected boundaries

1. Preserve R0–R8/R9 scoped acceptance and the accepted Persian/font evidence. Do not restart unrelated visual approval or request repeat screenshots without a new concrete defect.
2. Keep one primary design proposal, sequential dark review and conditional secondary language/layout. Preserve approved typography, palette, spacing, semantic icons and the canonical `DESIGN.md` authority.
3. Preserve owner/tenant authorization, private drafts, atomic publication, history, rollback, truthful save states and server-side concurrency checks.
4. Do not modify raw evaluation inputs or historical results to make a check pass. Keep deliberately faulty test fixtures distinct from production guidance.
5. Keep existing dependencies and supported hosts unless a fix demonstrates a material need. Do not install/update the host or a specialist while testing its checker.
6. Use a single implementation writer. Source/diff/test review is required; independent review is reported only if actually performed and authorized.
7. Keep generated packages, test data, scans and operational logs outside product source. Durable acceptance summaries belong in the existing roadmap/evidence structure.

## R10.1: Safe release packaging

**Finding F01 — High.** [The packager](../scripts/package_release.py), `main()`, passes `ROOT / args.output` to `shutil.rmtree` before validating source resources. Intercepted calls for `.`, `..` and `skills` targeted the checkout, its parent and Skill sources. The warnings in [INSTALL.md](../INSTALL.md) and [CONTRIBUTING.md](../CONTRIBUTING.md) do not enforce safety.

**Change boundary:** package output validation/staging, targeted new packager tests, relevant installation/contribution wording and the existing [validation workflow](../.github/workflows/validate-skill.yml). Preserve archive layout, version checks, source symlink refusal and checksums. Do not clean up existing user directories as part of the fix.

**Implementation tasks:**

- Define and enforce a fresh dedicated output contract. Resolve paths before side effects; reject the repository root, ancestors, source/metadata directories and unsafe symlink/junction aliases. Never use a force option to bypass protected-target rules.
- Refuse reuse of nonempty/unowned output. If repeat generation is supported, limit replacement to proven packager-owned output with an explicit preservation/recovery contract.
- Validate required inputs and matching versions before replacing any output; build in isolated staging and expose completed artifacts only after success. Keep existing data intact on validation, copy, ZIP or write failure; clean only this invocation's owned temporary artifacts.
- Add the focused test command to existing CI. Update documented usage only after its behavior is implemented and verified.

**Required scenarios / observable results:**

- Relative/absolute repository, ancestor and source paths are rejected before deletion or writes. Tests use disposable fixture roots and intercepted side effects, never dangerous targets in the real checkout.
- Supported Windows path aliases and symlinks/junctions cannot bypass containment. Record unavailable platform checks explicitly; do not call a skipped host case verified.
- Existing nonempty output and sentinel files survive rejection. Missing/mismatched source versions and injected copy/archive failure preserve prior output and source bytes.
- A new dedicated output succeeds; both archives retain expected member layout/version, CRC integrity and matching checksums.

**Exit:** all negative preservation checks and the successful package check pass; no broad recursive deletion remains reachable through the documented output argument. Record the exact supported replacement policy and tested platforms.

## R10.1 verification record (2026-10-07)

Local acceptance by the engineering lead on `codex/r10-remediation`, based on merged plan `4f13176284a1d3588497a653099a9dde006b8374`. This is scoped implementation acceptance, not integration or publication. The [roadmap](../ROADMAP.md#r10-audit-remediation) remains the only current status tracker.

**Accepted behavior:** no replacement policy exists: every existing output is refused, even an empty directory. Only fresh external destinations or the existing CI convention of a fresh top-level `dist` are allowed, under an already-existing parent. Inputs and version agreement are preflighted; builds stage in invocation-owned temporary siblings. Cleanup never receives the caller's output directory. Symlinks/reparse points and Windows device/stream/spelling aliases are refused. See [supported hierarchy and concurrency limits](../INSTALL.md#packaging-safety-and-limits).

**Impact/security review:** the CLI output argument and source metadata cross filesystem boundaries; source files, old artifacts and unrelated owner files are protected assets. Native callers are the two existing workflow jobs; each has its own fresh checkout, so refusal of a reused `dist` does not break their documented flow. ZIP/member names, fixed timestamps, embedded versions and checksum format remain compatible. There is no current local Graphify graph, so callers, config, source and test assertions were traced directly. No independent agent review is claimed; a separate lead diff/security review found and closed the mixed-separator Windows device-path bypass before acceptance. No new dependency or installed-Skill change was needed.

**Reproductions and checks:**

- The new `test_existing_output_is_rejected_before_any_recursive_delete` failed against the audited packager at its intercepted `shutil.rmtree(out)` call; no real output deletion was allowed. It passes against the fix. The mixed-separator Windows alias regression also failed on the first candidate and passes after normalization.
- Windows / Python 3.12.14: `python -B -m unittest discover -s scripts -p "test_*.py"` ran 84 tests: 82 passed, two native-symlink tests skipped because the host lacks symlink creation privilege. The Windows junction and path-alias cases passed. Test execution needed normal host permissions after the sandbox denied access to a newly created disposable temp fixture.
- Existing offline Linux container / Python 3.11: `python -B scripts/test_package_release.py -v` ran 16 tests: 14 passed, the two Windows-only tests skipped. Both actual symlink cases passed. The preinstalled image `python:3.11-slim`, identity `sha256:da047cb8f9d1d98e5c070f5300ba9f7274e33b8fc0e5be5ed88740aed1b95ba9`, ran without network, downloads or writable source mounts. These complementary runs cover all 16 test methods; they do not claim every filesystem/OS is certified.
- Fault scenarios cover copy, archive entry write, checksum write, staging permission and final rename errors; prior packages and source snapshots remain unchanged. A destination created during build is preserved. Missing inputs, mismatched/malformed versions and unsafe plugin names fail before staging.
- Fresh final-source packaging outside the repository produced the 88-member Skill ZIP and 95-member plugin ZIP. Both passed CRC, exact source-member byte comparisons and SHA256SUMS checks; both unpacked Skill versions and plugin metadata remain `3.2.0`. These are local candidates, not published releases or installed copies.
- `node scripts/test_runtime_dialogs.mjs`: 11 DOM-model assertions passed, not browser QA. `python -B scripts/validate_release.py`, the 17-test roadmap policy suite and `git diff --check` passed. The new packager suite is wired into the existing validation workflow; remote CI is deliberately not run/passed as part of this local-only checkpoint.

**Reviewed source identities:** normalized Git blob `cb09383354a4cf30668e1565f0e184af886aecaa` for `scripts/package_release.py`; `3c7dc20add7edddc5fc78160e0397a6f22fdbc0e` for `scripts/test_package_release.py`. No claim is made that the four remaining R10 findings are fixed. Hostile concurrent source/ancestor mutation remains outside the trusted-local packaging contract; final workstream CI, delivery scans, integration and local update remain gated by completion of R10.2–R10.5.

## R10.2: Resource route integrity

**Finding F02 — High.** The audit checked 60 literal parent-relative resource references and found 19 missing targets in seven installed modules. Paths use `../shared/` or `../accessibility.md` from a nested product module instead of reaching the actual reference directory.

Affected modules and observed broken-reference counts:

| Module under `skills/ui-ux-skill/references/products/` | Count |
| --- | --- |
| [web-application/interaction-access.md](../skills/ui-ux-skill/references/products/web-application/interaction-access.md) | 6 |
| [web-application/navigation-state.md](../skills/ui-ux-skill/references/products/web-application/navigation-state.md) | 2 |
| [web-application/workflows-data.md](../skills/ui-ux-skill/references/products/web-application/workflows-data.md) | 2 |
| [website/accessibility-localization-qa.md](../skills/ui-ux-skill/references/products/website/accessibility-localization-qa.md) | 3 |
| [website/conversion-trust.md](../skills/ui-ux-skill/references/products/website/conversion-trust.md) | 2 |
| [website/media-performance.md](../skills/ui-ux-skill/references/products/website/media-performance.md) | 2 |
| [website/structure-navigation.md](../skills/ui-ux-skill/references/products/website/structure-navigation.md) | 2 |

**Change boundary:** these routes, a bounded resource-integrity validator/regression test and its existing CI/package integration. Reuse [product](../scripts/validate_product_routes.py) and [shared-rule](../scripts/validate_shared_rules.py) validation where practical; do not rewrite product guidance.

**Implementation tasks:**

- Correct all confirmed relative paths without changing the behavioral rules or preloading unrelated modules.
- Check actual instruction resource routes, including applicable Markdown links and inline-code read/load references. Define resolution relative to the declaring file or explicitly named Skill root; distinguish external URLs, hypothetical product paths, examples and generated destinations from packaged resources.
- Apply the same integrity check to source and the unpacked Skill roots in both release formats. Keep the validator independent of the original checkout so omitted package resources cannot be masked.
- Add negative tests for wrong nesting depth and missing resources; retain a valid nested-path case and exclusions for documented non-resource examples. Wire checks into existing CI.

**Exit:** all 19 references resolve; intentionally broken source and incomplete consumer packages fail with actionable file/path diagnostics. Applicable source/package routing checks pass. A structural pass is not a claim that a fresh model exercised every route.

## R10.2 verification record (2026-10-07)

Local engineering-lead acceptance on `codex/r10-2-resource-routes`, based on R10.1 merge `14d78cbde20fae7b327cc06cf255bfbe08265dd0`. R10.1 was integrated through [PR #35](https://github.com/pooyahayati/UI-UX-Skill/pull/35); its exact-head and [post-merge checks](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37588008949) passed, with publication skipped. This record accepts R10.2 locally, not its remote CI, merge, publication or installation.

**Accepted scope:** only the 19 incorrect path prefixes in the seven listed modules changed; their product guidance and behavioral contracts remain unchanged. The new [resource checker](../scripts/validate_resource_routes.py) reads the supplied package's own Markdown and three existing route registries. It never substitutes repository resources for an incomplete consumer. Resolution rules, exact exclusions and parser limits are documented in [Contributing](../CONTRIBUTING.md#packaged-resource-routing-checks). Existing policy validators still own registry schemas and behavioral requirements. No dependency, version, raw evaluation input, historical result, product runtime or installed Skill changed.

**Reproductions and checks:**

- Before repair, the new checker reported exactly 19 missing targets and its real-source regression failed. After repair, source validation passes. Negative fixtures reject wrong nesting, absent files/registries, malformed registry entries, external/empty registry targets, path escapes, unreadable files and failed scans. Explicit owner-relative links cannot silently fall back to root-relative paths.
- Windows / Python 3.12.14: the full `python -B -m unittest discover -s scripts -p "test_*.py"` suite ran 98 tests: 95 passed and three native-symlink cases skipped for unavailable host privilege. The focused new suite has 14 methods. In the existing offline Linux / Python 3.11 container all 14 passed, including the real symlink case; R10.1's two symlink methods already passed its recorded Linux run. No runtime/image/dependency was installed or downloaded.
- The consumer regression builds and actually extracts both package formats, validates each root, then removes a required consumer resource and observes failure while the original source stays intact. A valid first root cannot mask an invalid second root.
- Fresh local candidate packaging produced the 88-member Skill ZIP and 95-member plugin ZIP. CRC, member-by-member source bytes, SHA256SUMS and both extracted consumer route checks passed; versions remain `3.2.0`. Artifacts are outside source in the workspace's `local-audit-planning-state/r10-2-candidate`, not published or installed.
- Release, Product, Shared, Design System, specialist-registry, evaluation-fixture, historical real-world, Material-sample and new resource validators passed. Historical result structural validation passed without changing provenance; this does not fix F04. The 11 dialog DOM-model assertions passed, not browser QA. `git diff --check` and roadmap policy checks passed.
- Existing validation CI now runs source resource regressions/checks, and both validation/release workflows check actual extracted consumer roots before delivery. R10.2 remote CI has not run because this branch has not been pushed. The official local Skill quick-validator could not start because the available Python lacks `yaml`; no dependency was installed to hide that limitation. Unchanged `SKILL.md` metadata retains R10.1's successful remote official-validation evidence, not a fresh R10.2 remote result.

**Review and limits:** main-agent source/config/diff review traced package layout and both workflow callers; no independent-agent review is claimed. No current Graphify graph was available, so direct tracing was used. This is bounded offline resource-integrity evidence, not full CommonMark parsing, remote URL/anchor verification, new rendered QA or fresh model execution of 114 scenarios. The three remaining findings retain their original status and exit criteria.

**Reviewed source identities:** normalized Git blobs `5079f743645ef89982b04f0032649342937e33af` for `scripts/validate_resource_routes.py` and `7837ec5c6b6671361658c407f06eeac0ac6fef4c` for `scripts/test_resource_routes.py`. Later integration requires actual CI evidence; release and local installation/update remain held until final R10 acceptance.

## R10.3: Stale-draft recovery

**Finding F03 — Medium.** In [the appearance fixture](../evals/fixtures/runtime-appearance/app.js), `reload()` retains the saved draft's old `baseRevision`; the Save handler sends it again. With published revision 2 and draft base 1, reloading and saving still produces `BASE_CONFLICT`. The [server](../scripts/runtime_appearance.py) correctly rejects that stale write, but the interface has no complete reconciliation path.

**Requirement:** [runtime governance](../skills/ui-ux-skill/references/runtime-ui-governance.md) requires reconciliation rather than silently overwriting concurrent changes. This fix concerns the synthetic executable fixture, not a new production admin engine.

**Change boundary:** fixture interface/state and focused interface tests; touch server behavior only where needed for safe reconciliation. Extend [runtime regressions](../scripts/test_runtime_appearance.py), retaining the existing authorization, migration, history and [dialog](../scripts/test_runtime_dialogs.mjs) tests.

**Implementation tasks:**

- Detect a moved published base, preserve saved and unsaved intended edits, and show the current/draft difference with an explicit recovery action.
- Reapply reviewed choices to a freshly observed base; do not silently change `baseRevision` and publish a whole stale snapshot over another owner's changes. Where the original base/difference is unavailable, explain the limit and require an explicit review rather than infer a merge.
- Preserve server compare-and-write protection at save and publish. If publication moves again during review, return another recoverable conflict without losing inputs.
- Cover rollback while a private draft exists. Cancel leaves draft/publication unchanged; discard/reset remain deliberate alternatives, not the only recovery path.
- Keep actual persistence/result messages truthful on failure and retry. Use the existing fixture's controls and styling; no broad visual redesign.

**Required scenarios / observable results:**

- Two owners create drafts; one publishes; the other encounters conflict, reloads, reviews/reconciles, saves and publishes successfully without overwriting unselected newer fields.
- Unsaved edits survive a conflict; cancellation preserves private/public state. Another publication during reconciliation is safely rejected and recoverable.
- Rollback with an existing draft follows the same recovery contract. Cross-tenant/unauthorized attempts remain denied; private drafts never become public through preview or reload.
- Exercise the real interface flow in a browser as well as deterministic state/HTTP checks; verify keyboard/focus and action availability. A DOM-model pass alone cannot close the browser evidence requirement.

**Exit:** the complete conflict-to-recovery workflow passes, not just the rejection branch. Record source revision, actor sequence and observed persisted state. An unavailable required browser check leaves that acceptance pending without reopening unrelated font tests.

## R10.3 verification record (2026-10-07)

Local engineering-lead acceptance on `codex/r10-3-draft-recovery`, based on R10.2 merge `ab20b755ef26ec6441f87ce92b58ae7a69234036`. [PR #36](https://github.com/pooyahayati/UI-UX-Skill/pull/36) passed [exact-head CI](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37590680903) and [post-merge CI](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37590814869), including the official Skill validator; publication was skipped. That closes the previous R10.2 remote-check limitation, not a claim that local PyYAML was installed.

**Accepted behavior:** reload/rollback preserve current saved and unsaved inputs and their original base; a stale base or own-draft revision offers explicit reconciliation. The dialog reads current published/private state and requires a choice for every differing setting. It does not infer intent from a historical base. Saving uses the observed published and private-draft revisions, preserves current unselected fields, and remains private until separate publication. Cancel makes no write. Conflicts and unknown write outcomes preserve original inputs and require refreshed review before another recovery save. An acknowledged save remains accurately reported if the subsequent preview/history refresh fails. Discard now confirms the deliberate loss of local inputs; reset remains a separate deliberate alternative.

**Impact and protected boundaries:** actual browser handlers, one native dialog, focused tests, existing validation CI and fixture documentation only. No server/API/schema/authentication/CSS/token/dependency change. The two-owner and same-owner draft checks retain server compare-and-write protection. Config values are rendered with text/DOM APIs, never executable markup. Existing tenant/actor/CSRF enforcement remains authoritative; public readers never consume private drafts. Risk is treated as cross-module stateful recovery despite the classifier's keyword-only Tier 1 floor; the existing R10.3 plan and criteria were reused. No current Graphify graph exists, so callers, endpoint bodies, persistence guards, rendering and tests were traced directly. The router's unrelated WordPress fixture signals and truncated global scenario inventory did not activate another product route or weaken this bounded analysis.

**Reproduction and automated evidence:**

- The new actual-handler regression failed against the pre-fix source: reload changed unsaved palette `plum` back to saved `forest`. It passes after the fix. The original stale-base loop is also guarded by disabled ordinary save/publication and a tested explicit fresh-base recovery.
- `node scripts/test_runtime_recovery.mjs`: 11 scenarios passed using shipped handlers with a modeled DOM/HTTP boundary. Covers cancellation, mandatory choices, unselected newer fields, a second publication, same-owner draft movement, unknown connection outcome, degraded storage, no-difference review, published-reader refresh retaining the edit base, and acknowledged save with preview failure.
- `node scripts/test_runtime_dialogs.mjs`: 11 existing keyboard assertions passed. Windows / Python 3.12.14 full discovery ran 99 tests: 96 passed; three existing native-symlink cases skipped for host privilege. Those unchanged methods have complementary Linux evidence in R10.1/R10.2; no fresh Linux claim is made here. The added real-HTTP test verifies rejection/preservation, reviewed save and publish after another base move, private-draft isolation, history and the untouched other tenant.
- Nine repository validators passed: release, product routes, shared rules, design system, specialist registry, evaluation fixtures, historical real-world evaluation, authored Material sample and resource routes. The historical result validator passed structurally; F04 remains open. Roadmap policy and whitespace checks passed. No raw fixture input, historical result, release version or installed Skill was rewritten.

**Actual browser acceptance:** `scripts/test_runtime_recovery_browser.mjs` passed against the real Python/SQLite loopback service in installed Chrome `154.0.8037.93`, driven by the preinstalled Playwright runtime. Two isolated synthetic-owner contexts used the UI, not mocked save/publication responses. Owner A saved `forest`, then changed locally to `plum`; the peer published spacing 24 (revision 1). A's reload and cancel preserved saved/local state. During A's review the peer published body size 18 (revision 2); A's attempted recovery was rejected without changing its draft. Refreshed explicit review kept current spacing/body size and A's palette, saved privately, then published revision 3. A subsequently saved spacing 12 and left body size 20 unsaved; rollback to version 0 created revision 4 while preserving both forms of work. Reviewed recovery/publish created revision 5 with only selected local fields. History retained versions 0–5; tenant B was unchanged. A further explicit dark-theme test published revision 6 solely within the disposable store.

Rendered checks covered English/LTR light desktop (1280×720), mobile (390×844), and dark mobile with body size 20/gap 12; native initial focus, Tab/Shift+Tab wrap, Escape and focus return, reachable actions, no horizontal dialog overflow and no browser script errors passed. Screenshots were inspected and retained outside source under `local-audit-planning-state/r10-3-browser` (`recovery-desktop.png`, `recovery-mobile.png`, `recovery-final.png`, `recovery-dark-mobile.png`). The in-app browser tool failed to initialize; the existing browser runtime provided the actual-browser evidence without installing software. The first browser harness attempt failed because it did not open the pre-existing collapsed recovery section; the corrected user-like navigation passed. Test browser/server and disposable database were cleaned up; no real owner data was used.

**Scope review/limits:** one writer and main-agent review; no independent agent claimed. UI route: targeted `web-application`, with its navigation-state, workflows-data and interaction-access modules; Shared forms, feedback, state/recovery, destructive-action, accessibility and responsive contracts informed review. Existing runtime governance was retained; no new foundation, Product Pack, Material activation, language variant or font approval was needed. Security review checked the retained trusted boundary and race/denial/preservation evidence; no new permissions or host installation. Actual screen-reader, other browsers/devices, zoom/forced-colors and Persian/RTL variants were not exercised; this English synthetic fixture does not certify them. Full browser navigation still risks unsaved input after the existing unload warning; offline draft persistence is not added. No fresh all-scenario model evaluation or production security certification is claimed.

**Reviewed identities:** normalized Git blobs `bf2d847dc98f04f0adb8b5c7717e2883dad78520` for `evals/fixtures/runtime-appearance/app.js`, `c2851dbaffcb07c8f07f5c037280bebac7d92d50` for `scripts/test_runtime_recovery.mjs`, and `5bd9b44ca9c0879af4a6c0fd76f32a9efb5ef75a` for `scripts/test_runtime_recovery_browser.mjs`. CI now runs the dependency-free recovery model suite alongside existing real-HTTP tests. The optional real-browser runner uses existing installations only and is not an automatic CI dependency/install step. R10.3 remote CI, push and merge are not claimed; publication/local installation remain held until final R10 acceptance.

## R10.4: Consistent evaluation verdicts

**Finding F04 — Medium.** [Result validation](../scripts/validate_eval_result.py) accepts a case marked `pass` with an invariant marked `fail`, then reports `Fail=0 Partial=0`. An in-memory report covering the full manifest reproduced this with `--require-all`. The tool need not establish evidence truth to detect a contradiction in its own input.

**Change boundary:** validator, [result schema](../evals/result.schema.json) where needed, focused new validator tests and concise [evaluation documentation](../evals/README.md). Compare with [the existing real-world validator](../scripts/validate_real_world_evaluation.py); do not rewrite historical results or reinterpret their original coverage.

**Implementation tasks:**

- Define/document a single verdict-consistency rule: `pass` cannot contain failed, partial or untested required invariants; any failed required invariant cannot be hidden by a successful case summary. Define partial/untestable combinations explicitly and preserve justified conservative case-level failures.
- Reject contradictory, duplicate or unknown invariant records instead of letting set conversion hide ambiguity. Reuse manifest identities rather than creating a separate list.
- Keep structural validity separate from acceptance. A valid recorded failure is useful data; report it accurately rather than automatically treating every non-passing report as malformed.
- Add an explicit acceptance-gate mode only if a real caller needs it, retaining compatible structural-validation behavior. Align schema, CLI help, summaries and CI invocation with the chosen contract.

**Required scenarios / observable results:**

- Overall pass plus invariant fail is rejected; repeat for partial/untestable required invariants. Summary counts cannot report a contradictory clean outcome.
- Consistent pass, fail, partial and not-testable reports behave according to the documented rules; legitimate failure reports remain recordable.
- Missing/duplicate/unknown cases and invariant entries are diagnosed. `--require-all` still controls completeness; a historical subset is not falsely promoted to a complete current run.
- The unchanged historical result remains valid under its documented structural/provenance contract, or a real incompatibility is surfaced without rewriting evidence to hide it.

**Exit:** the reproduced false-clean report is rejected, accepted reports have coherent verdicts/counts, and the existing historical-evaluation checks remain honest and compatible.

## R10.4 verification record (2026-10-07)

Local engineering-lead acceptance on `codex/r10-4-eval-verdicts`, based on R10.3 merge `d813e3357bc2eb37c0e5459cab008a73dde5bb25`. R10.3 was integrated through [PR #37](https://github.com/pooyahayati/UI-UX-Skill/pull/37) after [exact-head CI](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37599603020) passed; its [post-merge workflow](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37599735421) also passed and `Publish release` was skipped. This accepts R10.4 locally, not its push, remote checks or integration.

**Accepted contract:** [the documented verdict table](../evals/README.md#verdict-consistency) is enforced by one shared result validator. Every required manifest invariant is recorded exactly once. Case pass requires all required outcomes to pass; any failed invariant requires case fail. Partial cannot hide failed or entirely untested requirements. All-untested cases remain not-testable. Nonblank case notes permit conservative failure, or partial with all requirements passed; the checker cannot judge whether the explanation is true. Unknown/duplicate records, ambiguous JSON object fields, malformed shapes and read/parse errors fail with diagnostics. The existing historical acceptance gate reuses this consistency rule while retaining its additional evidence/provenance/no-failure requirements; generic recording still permits a coherent failure with exit code 0. No new acceptance flag, dependency or duplicate identity registry was needed. The JSON schema remains the shape contract and explicitly delegates manifest/cross-record rules to the script.

**Reproduction and verification:**

- Before implementation, `test_full_manifest_false_clean_regression` failed against the merged baseline: a synthetic complete manifest report containing case pass/invariant fail returned exit 0 and `Fail=0 Partial=0`. The same actual CLI regression passes after repair by requiring rejection and no successful summary. No historical file was edited to reproduce it.
- The 13-method focused suite passes. It includes the 64 combinations of two required invariant outcomes and four case verdicts, conservative decisions/notes, partial and untested cases, missing/duplicate/unknown records, malformed types/enums/encoding, duplicate JSON fields, absent files, completeness, accurate four-verdict counts, input immutability and unchanged historical-subset compatibility. In-memory mutations exercise the actual historical validator: contradictions and duplicates fail, and its stricter acceptance gate still rejects a structurally valid failure.
- Windows / Python 3.12.14 full `python -B -m unittest discover -s scripts -p "test_*.py"`: 112 tests, 109 passed and three native-symlink tests skipped for unavailable host privilege. Those unchanged methods retain prior R10.1/R10.2 Linux evidence; this is not a fresh Linux run. Focused tests were rerun after the final shared-parser review change.
- Nine repository validators passed: release, product routes, shared rules, design system, specialist registry, evaluation fixtures, historical real-world evaluation, Material sample and resource routes. The actual historical result summary is `Cases=5/114 Pass=5 Fail=0 Partial=0 Not-testable=0`; `--require-all` correctly rejects this subset. Neither count represents fresh model execution.
- Existing 11 keyboard DOM assertions and 11 recovery DOM/HTTP scenarios passed. Roadmap policy and `git diff --check` passed. New focused tests are wired into the existing validation workflow; remote R10.4 CI has not run because this branch is not pushed. Version, Skill sources, raw inputs and historical JSON remain unchanged.

**Review and limits:** single-writer source/diff/input-boundary review, not independent-agent review. The protected assets are truthful verdict reporting and preserved evidence; input strings are data, never executed or fetched, and validation is read-only. Installed security guidance informed duplicate/type/error-path checks; scoped Head acceptance retains existing workflow/permissions rather than introducing web controls into an offline CLI. The first freshness retry returned an HTTP error; authenticated read-only preparation then verified Head `1.5.0` at `0509f53d274e63ae47077dfd4656310281f9bd05` and security guidance `0.6.12` at `a06bc63b3f8b829c14b0bbf53d99fefc39d58092`, with no installation/update. The existing instruction binding was compatible; unrelated cached project rationale was not used as evidence for this change.

No local Graphify graph exists; callers, manifest/schema, shared validation, historical gate and CI were traced directly. Router discovery truncated the large case inventory; tests parse the complete manifest, and full fixture validation covers its structure. Incidental WordPress fixtures and a negated UI term do not place this offline evaluator inside a WordPress/UI implementation boundary. Repository purity reports only the pre-existing missing local-exclude setup, with no forbidden tracked/staged files. No new browser/owner approval is relevant to these offline validation changes. No external JSON Schema engine is installed locally; schema syntax/shape was reviewed, while semantic enforcement is verified by the stdlib tests, not claimed as schema-engine certification. Official Skill metadata validation passed in R10.3 post-merge CI and the Skill entrypoint is unchanged, not freshly revalidated by an unavailable local `yaml` dependency. Release/security-artifact scans, final integrated R10 acceptance and local installation remain deferred to the final authorized delivery boundary.

**Reviewed identities:** normalized Git blobs `c0cd55c1ab45e15842187aad1c79accb458ff417` for `scripts/validate_eval_result.py`, `7050894ba488422649b3c41f8be340255c0b0dce` for `scripts/test_eval_result.py`, and `3d9c6077cd8b9c4171a0da8444166c76905f0b5a` for `scripts/validate_real_world_evaluation.py`. R10.5 remains unimplemented. No new issue/milestone was created; the existing R10 roadmap/acceptance record and predecessor PR retain traceability.

## R10.5: Specialist package integrity

**Finding F05 — Medium.** [The specialist checker](../scripts/validate_specialists.py) compares only local/upstream `SKILL.md` text before emitting `CURRENT`. A controlled installation with a matching entrypoint but a missing referenced resource still passed. This does not establish that the owner's real installation is corrupt.

**Change boundary:** checker, focused new tests and accurately scoped [installation](../INSTALL.md) / [specialist-routing](../skills/ui-ux-skill/references/specialist-routing.md) guidance. Reuse the [registry](../skills/ui-ux-skill/specialists.json); do not add/vend specialists, install packages, pin future routing to a stale release or overwrite Head-managed integration.

**Implementation tasks:**

- Resolve the selected stable release/default-branch source to an immutable commit for one check. Build a bounded manifest for the actual Skill package, not merely the entrypoint or every unrelated repository file.
- Compare required package paths and bytes; identify missing, modified, unsupported or unverified resources. Follow an explicit policy for managed integration/local additions without claiming modified upstream files match.
- Separate entrypoint identity, installed-package integrity and upstream freshness. Emit a whole-package current verdict only when its required checks actually succeeded; network/permission failures remain unverified, not current.
- Require an actual inspection target for strict installed/current enforcement; do not silently succeed with strict flags and no inspected root. Define multi-root results without letting one current copy certify every installation.
- Do not execute downloaded code or install/update during checking. Use safe bounded remote reads, immutable identities and isolated in-memory/temp fixtures; include traversal/symlink and request-failure handling where the chosen manifest mechanism introduces them.

**Required scenarios / observable results:**

- Matching entrypoint plus missing/stale reference, script or bundled required asset is not accepted as current. An intact matching package is accepted.
- Upstream resource-only change with unchanged `SKILL.md` is detected. Moving branch/tag state cannot mix resources from different commits during one check.
- Unavailable/rate-limited/malformed upstream data, permission-denied local reads, no strict inspection target and multiple installation roots produce truthful bounded results.
- Legitimate Head integration is preserved and classified according to the documented policy. All tests leave the actual installed Skill untouched; live upstream availability is reported separately from deterministic test success.

**Exit:** incomplete/stale packages cannot receive a whole-package current verdict; scope and limitations are explicit, and all five findings satisfy the integrated gate below.

## R10.5 verification and integrated local acceptance (2026-10-07)

Local engineering-lead acceptance on `codex/r10-5-specialist-integrity`, based on R10.4 merge `e88693ed15ccf4ce850fe79e39bdcd6692618d67`. [PR #38](https://github.com/pooyahayati/UI-UX-Skill/pull/38) passed [exact-head checks](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37602004111) and [post-merge checks](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37602163431); `Publish release` was skipped. After remote merge succeeded, a stalled local fetch was stopped by its verified process identity and retried with a bounded transport timeout; the next branch was fast-forwarded to the verified merge before implementation. No merge was repeated and no owner work was reset.

**Accepted scope:** the existing CLI now delegates immutable manifest and local-byte comparison to [specialist_integrity.py](../scripts/specialist_integrity.py). The registry remains the identity/source/package-root authority, with no pins, new specialists or vendored resources. One release/default-branch resolution produces an immutable commit, then only tree/blob identities are used; nested package siblings are not compared. Entrypoint identity, resource completeness and source freshness are separate observations. Binary assets and raw line endings participate in Git blob identity. Exact-match strict checks cover every explicitly selected root; missing targets, missing resources and unverified checks cannot pass. Head additions/edits remain untouched and explicitly uncertified rather than stripped to manufacture a match. See [installation semantics and limits](../INSTALL.md#specialist-package-integrity).

**Regression and compatibility evidence:**

- The new `test_matching_entrypoint_missing_resource_is_not_current` failed against the merged pre-fix checker: a synthetic install with identical `SKILL.md` but absent `references/rule.md` returned exit 0 and `CURRENT`. The fixed checker rejects that same case. Tests use disposable roots/mocked upstream responses, never the real installation for fault injection.
- The focused suite contains 19 test methods. It covers intact packages; missing/modified entrypoint, reference, script and binary asset; resource-only upstream change; stable-release/default-branch fallback; one immutable resolution; nested package scope; missing strict target; multiple roots; preserved Head additions/modified entrypoints; caches; permission failure; native symlink refusal; path/type/case collisions; tree/response/file/total limits; truncated/malformed responses; entrypoint digest mismatch; timeout/partial response/rate limit; no redirects/credential destination escape; and read-only snapshots. Windows passes 18 with one unavailable native-symlink privilege skip; Linux passes all 19, including a real symlink. Final local-entrypoint bound was verified with focused reruns after the combined suite.
- Combined Windows / Python 3.12.14 run: **131 tests, 127 passed, four native-symlink privilege skips**. Combined offline Linux / Python 3.11 run: **131 tests, 129 passed, two Windows-only skips**. These complementary runs exercise every method, not universal OS/filesystem certification. The existing `python:3.11-slim` image `sha256:da047cb8f9d1d98e5c070f5300ba9f7274e33b8fc0e5be5ed88740aed1b95ba9` used no network or download, a read-only source mount and disposable container storage.
- Nine repository validators passed (release, product routes, shared rules, design system, specialist registry, eval fixtures, historical real-world, authored Material sample, resource routes). Historical result validation remains `Cases=5/114 Pass=5 Fail=0 Partial=0 Not-testable=0`, not a new 114-case model evaluation. Existing 11 dialog keyboard assertions and 11 actual-handler recovery model scenarios passed. Roadmap policy and whitespace checks passed. CI now invokes the focused specialist suite; the scheduled upstream workflow also watches the new helper/test, and the release validator requires the helper to exist.
- An authenticated **read-only live check** of the real `persian-writing` installation returned `CURRENT entrypoint=MATCH`: 49 tracked package files matched stable `v1.4.0`, commit `28d61f4c1c11b366ea016e56c1977c0ce7210af0`. This is observed freshness at that resolution, not a future pin or an installation operation. Tests did not execute fetched specialist code or write installed files.
- Fresh local candidate archives in the external workspace directory `local-audit-planning-state/r10-5-candidate` contain 88 Skill members and 95 plugin members. CRC, exact member sets/bytes against final packaged sources, `SHA256SUMS`, embedded `3.2.0` versions and resource validation of both actual unpacked consumers passed. They are not published artifacts and were not installed.

**Integrated five-finding review:** R10.1 output preservation/safe packaging, R10.2 source/consumer resource routing, R10.3 stale-draft recovery, R10.4 coherent result recording and R10.5 package identity each retain a demonstrated pre-fix failure and passing regression. The full combined suite passes with complementary platform evidence. R10.3 actual-browser recovery acceptance remains bound to unchanged runtime source; no duplicate browser/font/owner test was requested for this offline checker change. Earlier historical/model evidence, raw fixtures, R0–R8/R9 acceptance, runtime data/permission contracts and release metadata remain unchanged. The only packaged guidance edit explains the checker boundary and preserves higher-level authorization/integration rules.

**Security/maintainability review and limits:** one writer and lead source/diff review; no independent agent is claimed. Security guidance informed trusted-source URL construction, immutable identities, bounded reads, no redirects, path/reparse refusal and explicit unverified states. The installed Head/security bindings were checked read-only and reused without installation. The assets protected are owner installation/customization, API credentials and truthful integrity reporting; no arbitrary URL, downloaded program or installer is executed. Git blob hashing checks byte identity, not malware safety, instruction compatibility or executable-mode portability. Untracked Git/Python caches are outside the documented comparison. Trusted stable local hierarchies are required: concurrent hostile file/ancestor replacement is not snapshot-isolated. Upstream movement after resolution requires a new check. Limits and unsupported resources fail closed rather than narrowing a successful claim.

No current Graphify graph exists; registry/CLI/HTTP/tree/local-read/CI callers were traced directly. Repository purity has no forbidden tracked/staged artifacts and only the existing missing-local-exclude warning. The installed security guide's cached unrelated project rationale was not used as acceptance evidence. R10.4 remote official Skill validation passed; local official quick validation still lacks `yaml`, and no dependency was installed. R10.5 remote CI, final integration, final release scans/version decision/publication and verified local update have **not** occurred. Local repairs/combined acceptance are complete, but those delivery outcomes remain pending and must not be inferred from this record.

**Reviewed source identities:** normalized Git blobs `6daa81eccd151cd1d29d4fa3ec9fd6b09b77bcce` for `scripts/validate_specialists.py`, `5ea1dba9e4d8bb7372c1b27cd6031b7bad9b81c8` for `scripts/specialist_integrity.py`, and `26de276dc1cbab2bc2ffdc8177529d176e576470` for `scripts/test_specialists.py`. Existing R10 roadmap/acceptance documents remain the workstream ledger; no extra issue/milestone or competing roadmap was created.

## Integrated acceptance and delivery boundary

Run focused regressions during each package; run the combined affected suite at final review. Extend existing CI only with checks justified by these fixes, not an additional benchmark/automation system.

Existing command anchors (run from the repository root with the available Python/Node executables):

```text
python -B -m unittest discover -s scripts -p "test_*.py"
node scripts/test_runtime_dialogs.mjs
python -B scripts/validate_release.py
python -B scripts/validate_product_routes.py
python -B scripts/validate_shared_rules.py
python -B scripts/validate_design_system.py
python -B scripts/validate_specialists.py
python -B scripts/validate_eval_fixtures.py
python -B scripts/validate_real_world_evaluation.py
python -B scripts/validate_eval_result.py evals/real-world/result.json
python -B scripts/validate_material_sample.py
git diff --check
```

Add the new package/resource/interface/evaluation/specialist regression commands to the acceptance record when implemented; these command anchors do not already cover the new defects. Run packaging only after R10.1 acceptance, using its verified fresh-output contract and an isolated external destination. Check both unpacked consumer roots, archive integrity, versions and checksums.

For changed Skill instructions, use only relevant raw-input behavioral cases under the [evaluation guide](../evals/README.md). A source-route check does not replace any claimed agent behavior; do not fabricate a full 114-case run. Keep independent model, browser, live network, structural and owner evidence separate.

Before R10 completion, confirm:

- Each finding has a defect regression that would fail against the audited source and passes against the fixed candidate, plus its protected-state/compatibility evidence.
- New checks are actually invoked by the existing validation workflow; all required combined checks pass on the reviewed revision, or the affected package remains pending with a concrete limitation.
- Resource consumers are valid in source and both package formats; the complete stale-draft UI recovery is observed; verdict/package-integrity failure paths cannot masquerade as success.
- There are no unexplained changes to release metadata, raw fixtures, historical evidence, product scope or installed Skills. Recheck R0–R8/R9 tracker compatibility and the separate R10 count/active/next state.
- The lead records dated scope acceptance and remaining limits. Completion means the five repairs are verified; integration, publication and local installation are separate outcomes.

If publication is later authorized, perform the relevant current local source/artifact security scans required by the active engineering workflow, verify final CI and consumer artifacts, then choose/update release metadata deliberately. Do not call a candidate released/installed before verifying that actual operation. No new release number is selected by this plan.

## Start and resume protocol

**Final delivery authorization (2026-10-07):** after all five local repairs and the combined acceptance gate, the owner explicitly requested documentation review, merge, a new release and local update. This supersedes the intermediate publication/install hold above. Compatible patch `3.2.1` is selected; final CI, native source/extracted-package scans, published artifact verification and integration-preserving installation remain required. Earlier dated records retain their then-current pending states; current outcomes belong in `ROADMAP.md`.

1. Use `codex/audit-remediation-roadmap` for the local planning handoff. Inspect dirty files and main divergence before starting; preserve any owner edits. Use a scoped `codex/` implementation branch at kickoff if the plan branch has been integrated.
2. On an implementation instruction, mark only R10.1 `In progress`; record the actual owner, baseline, scope and checks. Start with its non-destructive failing regression, not a package run pointed at existing folders.
3. Complete one package at a time in the roadmap's order. If source evidence changes the diagnosis or a fix needs broader authority, update the affected plan and surface that decision rather than expanding silently.
4. At each handoff update the canonical tracker/count/active/next fields together. Link dated evidence identifying source/test revision, actual command/result, protected-state checks, limits and reviewer acceptance. Keep planned tests distinct from completed ones.
5. Record local/committed/pushed/PR/CI/merged/released/installed state only when observed. Use `Not started`, `In progress`, `Blocked`, `Completed` or `Reopened`; an unstarted prerequisite alone is not a blocker.

Recovery is scoped: preserve the prior committed baseline and user changes; use a reviewed change reversal only when authorized, never a destructive reset. Package tests operate on owned disposable roots; runtime tests use isolated stores, never a real owner's appearance data. Failed checks stop the affected package, not unrelated previously accepted work.
