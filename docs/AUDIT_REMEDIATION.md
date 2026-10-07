# R10: Deep Audit Remediation Plan

Prepared 2026-10-07. This document defines the work and acceptance criteria for five confirmed audit findings. [ROADMAP.md](../ROADMAP.md#r10-audit-remediation) is the single current progress ledger.

## Objective and authority

Remove the five evidenced failure modes with bounded fixes and regression coverage. Preserve the existing design workflow, product scope, historical evidence and installation boundaries. This is stabilization maintenance, not a redesign or a new capability family.

The owner authorized planning and project preparation, then explicitly authorized documentation integration: commit, push, pull request and merge after checks pass. Implementation starts on a subsequent implementation instruction. No code/test/workflow change, version bump, release or installed-Skill update is authorized by this documentation checkpoint.

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

1. Use `codex/audit-remediation-roadmap` for the local planning handoff. Inspect dirty files and main divergence before starting; preserve any owner edits. Use a scoped `codex/` implementation branch at kickoff if the plan branch has been integrated.
2. On an implementation instruction, mark only R10.1 `In progress`; record the actual owner, baseline, scope and checks. Start with its non-destructive failing regression, not a package run pointed at existing folders.
3. Complete one package at a time in the roadmap's order. If source evidence changes the diagnosis or a fix needs broader authority, update the affected plan and surface that decision rather than expanding silently.
4. At each handoff update the canonical tracker/count/active/next fields together. Link dated evidence identifying source/test revision, actual command/result, protected-state checks, limits and reviewer acceptance. Keep planned tests distinct from completed ones.
5. Record local/committed/pushed/PR/CI/merged/released/installed state only when observed. Use `Not started`, `In progress`, `Blocked`, `Completed` or `Reopened`; an unstarted prerequisite alone is not a blocker.

Recovery is scoped: preserve the prior committed baseline and user changes; use a reviewed change reversal only when authorized, never a destructive reset. Package tests operate on owned disposable roots; runtime tests use isolated stores, never a real owner's appearance data. Failed checks stop the affected package, not unrelated previously accepted work.
