# WordPress settings execution and acceptance

Current package statuses belong only in the [roadmap](../../ROADMAP.md#wordpress-settings-extension-wps). This record retains decisions, methods and actual evidence, not a competing tracker.

## Execution authorization — 2026-10-10

The owner explicitly authorized completing WPS-0 through WPS-6 and releasing this repository on GitHub: project file edits, necessary commands, tests, fixes, branches, commits, pushes, pull requests and merges. The endpoint includes publication of the verified release. This supersedes the plan-only/no-delivery state recorded on 2026-10-09.

Scope is `pooyahayati/UI-UX-Skill`, through this endpoint or until revised. Empty tool-install/deployment/data clauses grant no fresh authority and revoke no valid earlier authority. Use existing host tools and an isolated synthetic local WordPress test environment; do not affect other projects, real sites or user data. Local Skill installation is not part of this endpoint. One implementation writer; no new agents.

Release preparation may update the existing version manifests, README version/coverage and changelog after WPS acceptance. Select 3.4.0 for the new bounded settings capability; this does not authorize unrelated behavior or CI changes. The native final-source and extracted-artifact security gate remains required before release.

The first exact-candidate CI exposed two existing evaluation release bindings: `evals/cases.json.version` must match root VERSION, and `evals/real-world/result.json.skillVersion` must match that manifest. Release preparation therefore includes only those version fields and the existing explanatory `releaseBinding` text. Original cases, prompts, invariants, verdicts, source-evaluation version, host/model/date and evidence remain unchanged; no historical result is presented as fresh 3.4.0 behavior. No shared validator is changed to bypass the mismatch.

## WPS-0 — 2026-10-10

- Baseline: `4e20b3f5524120a5c2559a8bd525c30e66c43d3c`; branch `codex/wordpress-settings-implementation`. The preceding local roadmap cleanup is preserved and will be integrated with this work.
- Inspected the current plan, source/router, WordPress pack/settings, scoped shared rules and release workflow. Context Router inspection was complete. Head/specialist preparation returned PASS: Vibe 1.5.0 and UI/UX 3.3.0, no installation/update performed.
- Protected Skill resources and the three behavior paths are captured in [baseline](baseline.json). Raw [nineteen scenario inputs](../fixtures/wordpress-settings/briefs.json) precede behavior edits.
- Existing Docker engine, WordPress/PHP 8.3 image, MariaDB 11.4 image, bundled Node/Playwright/Python and native Trivy are available. Test instances will bind only loopback and use synthetic data. No host-tool installation is needed.
- Official version API and release documentation identify WordPress 7.1.3 as current stable; the existing image carries 7.1.2. The specimen will declare 6.8 as its minimum and exercise both 6.8 and 7.1.3 in isolated containers.
- Dedicated stdlib check entry point: `python -B -X utf8 evals/wordpress-settings/test_contracts.py`; it will be added to the existing validation job at WPS-5. Real-admin behavior/captures remain a separate browser test, not inferred from that check.
- Save/storage contracts are preserved in Skill guidance. The synthetic specimen may use its own bounded option and conflict-aware save contract; that is not a migration instruction for real products.
- Lead acceptance: baseline/tooling/raw-input preparation is complete; no WPS behavior edit or runtime pass is claimed by this package.

## WPS-1 — 2026-10-10

Added the new-design/authorized-redesign mandate and settings-only guide route in the two existing WordPress resources, plus the bounded component guide. Simple forms are included; audit/narrow-fix, non-settings, public and hybrid boundaries are explicit. No global entrypoint/registry or other product was edited. Product-route and package-resource validators both passed. Lead acceptance covers the source/routing contract; model/runtime observations follow in WPS-4/5.

## WPS-2 — 2026-10-10

Added option-inventory/task grouping, short-form sections, conditional tabs/disclosure and handbook-based visual criteria. Added initial-load, duplicate/newer-edit, per-section preservation, uncertain-commit and applicable conflict-recovery contracts; shared methodology is linked rather than copied. Resource/shared-rule validation, all 27 roadmap tests and diff whitespace checks passed. Lead acceptance is source-contract acceptance; actual data/visual behavior remains for the specimen.

## WPS-3 — 2026-10-10

Verified official package and selected public control/element references on 2026-10-10. Added a task-based component shortlist, product-derived compatibility checking, built/no-build asset paths, shared styles/dependencies, host-scoped CSS, overlays, translation and preserved Settings API/storage/permission boundaries. Resource and release-document validators passed. No experimental/private/next opt-in APIs or repository-wide dependencies were introduced. Lead acceptance is source/integration guidance; concrete basic-control support on the declared hosts remains a required WPS-4 observation.

## WPS-4 — 2026-10-10

The runnable [specimen](../fixtures/wordpress-settings/README.md) uses existing Docker/Node/browser tools, loopback-only isolated containers and synthetic data. Both simple and multi-topic forms run inside actual `wp-admin`: WordPress 6.8 and 7.1.3, PHP 8.3.35, MariaDB 11.4, Edge 154.0.4258.62; only the specimen plugin is active. Current-host Persian core translation supplies the real RTL admin shell.

`node evals/wordpress-settings/run_browser.cjs` passed eighteen observations (thirteen runtime scenarios plus five layout records), zero JavaScript errors and zero compatibility warnings. Covered successful/rejected/unknown saves, newer edits, duplicate requests, unrelated sections, two-administrator conflict recovery, subscriber read/write denial, nonce denial, synthetic-secret masking/removal and section reset. A late error reopens a collapsed secondary panel. Keyboard checks cover modal Tab containment, Escape and return focus; navigation preserves unsaved work. The additional enlargement check uses 200% CSS zoom on the owned surface, not native browser zoom or assistive technology.

Lead inspected all four final normal/narrow captures and the narrow reset dialog against [DESIGN.md](../fixtures/wordpress-settings/DESIGN.md): widths 1440/390, readable labels/help, ordered headings, scoped save actions, no horizontal overflow, LTR technical values in RTL. Actual rendered custom Vazirmatn was checked through browser font inspection for labels/headings, including regular/bold loads. This is engineering specimen acceptance, not customer approval or universal accessibility certification.

Runtime review found and fixed unstable React child keys that lost open disclosures, inherited component typography that bypassed the Persian font, and deprecated control-style defaults. The public transition flags were inspected on both hosts and explicitly adopted, rather than hiding warnings or introducing experimental controls. Shared product contracts remain unchanged.

## WPS-5 — 2026-10-10

All nineteen required [outcomes](RESULTS.json) are accepted: thirteen real-admin scenarios, five explicitly same-session [source traces](SOURCE_REVIEW.md), and one source/package identity comparison. Runtime evidence is retained in [browser results](evidence/browser-results.json); selected screenshots are in the same directory. Candidate behavior and specimen files are hash-bound. This is not a fresh independent model benchmark.

All eighty-five protected Skill resources match the pre-edit canonical baseline in source and both extracted candidate packages (89 Skill / 96 plugin members). Dedicated Python tests passed 6/6; the shared UI draft model checks passed. A deliberately missing-outcome report exited 1, proving that the new additive CI invocation does not accept absent/contradictory evidence. No existing gate, expectation, trigger, permission or dependency was weakened.

Existing structural validators and modeled runtime keyboard/recovery gates passed. Full unchanged regressions: Linux non-root, offline, 141 tests with 2 platform-specific skips; Windows, 141 tests with 4 platform-specific skips when using a writable no-space temporary directory. The initial Windows run in a spaced temporary directory exposed an existing Markdown-link test limitation (the unescaped absolute-path fixture is not parsed); the shared validator/tests were not modified. Linux exercises the symlink/permission paths unavailable on this Windows host. This limitation is not new WPS behavior or proof of general Markdown parsing.

Lead acceptance: scoped routing, data/runtime behavior and protected-resource isolation criteria are satisfied. Remote CI remains unverified until the exact candidate is pushed and checked.

## WPS-6 — 2026-10-10

Lead reviewed the final settings guidance, bounded component route, retained scenario/visual evidence, additive-only CI diff and prior roadmap cleanup. Public README remains concise; 3.4.0 manifests and changelog describe the settings-only capability without promising a production engine. Historical checkpoints remain archived and separately validated. Fixture bootstrap is explicitly CLI-only/loopback-bound; fixture-local Git attributes preserve shell LF on Windows.

Final candidate packages passed CRC/checksum, complete member/source identity (89 Skill / 96 plugin members), embedded 3.4.0, extracted resource routes and protected baseline checks. [Candidate verification](RELEASE_CANDIDATE.json) records actual local archive hashes; these are not the published download hashes. Dedicated tests passed 8/8 on Windows and non-root Linux after adding evidence-binding and consumer failure-path regressions. Existing 141-regression suite and structural/runtime gates passed within the platform limits recorded above.

Native Trivy 0.75.0 matches the freshly checked upstream stable release. Source and extracted final consumers passed secret scanning, zero findings. The first consumer-wrapper attempt failed while resolving/executing the gate; native diagnostic scanning and a retry pinned to that verified stable version passed. This did not disable scanning, data updates, severity levels or findings checks. Reports remain outside source; extracted-consumer report SHA-256: `9dc5e1d0490de3b09086288b05401bacbb349adf0d383b529832030cac1a86f7`. The final committed source will be scanned again before merge.

The official quick validator could not run in local Python or the existing test image because PyYAML is absent. No host dependency was installed and the validator was not replaced; its existing remote CI step remains a required integration gate. Engineering local acceptance is complete; push/CI/merge/publication are still separate pending delivery observations.

## Integration and publication

PR #43 first candidate `eb09ff62c7512735eddb3585db5ce7dbad1e8333`: CI run `38001706422` correctly rejected the unsynchronized evaluation version. Its WPS gate and all earlier existing gates passed, but later steps were not claimed successful. Synchronized the three release-binding fields described above, reproduced both affected validators locally, and compared all other evaluation content to the pre-edit Git baseline. Added a dedicated hash regression preserving original cases/evidence after stripping only those release fields (9 dedicated tests).

Corrected candidate `c02f6bec4de108c9c4cfe74267e90e56c7420a42` passed [CI 38001992411](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/38001992411), including the dedicated nine-test gate, existing package checks and official OpenAI quick validation. The corrected full Linux suite also passed 141 tests (2 platform skips). Native committed-source secret scan: zero findings, report SHA-256 `517682fdb25c8516f8bb0ba337858a77644a36492960543cb23690eb152c9852`.

[PR #43](https://github.com/pooyahayati/UI-UX-Skill/pull/43) was merged as `32986b62e9d22a291cb41329b2f592201f7bdc7b`. Its Git tree `7b19fe7eb311b7c13aae4fee712b9a2ca2bfce35` exactly matches the checked/scanned candidate. [Release run 38002130047](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/38002130047) passed merged-source validation, official quick validation, exact-commit installer smoke test, packaging and publication.

[v3.4.0](https://github.com/pooyahayati/UI-UX-Skill/releases/tag/v3.4.0) is a published, non-draft, non-prerelease release. Publication timestamp: `2026-10-09T22:59:56Z` (2026-10-10 in Tehran). Release target and remote tag both bind to the merge commit above. Actual downloads, not local builds, passed `verify_packages.py`: checksum manifest, CRC, exact inventories, complete canonical source identity and embedded 3.4.0. Both extracted downloads passed resource routes and the eighty-five-file protected baseline. [Published verification](RELEASE_PUBLISHED.json) records actual asset hashes (96 plugin / 89 Skill members); line endings/archive metadata make local candidate hashes different, without content divergence.

Native Trivy 0.75.0 separately scanned the extracted published downloads with zero findings; report SHA-256 `c1bd9246c53e3a5bcd8d0c1a9b2b7b59195590560803e99d13b8a0991ca8668b`. No original release asset or tag was replaced. Publication evidence is complete; the follow-up documentation commit does not change portable Skill content or retag the release.

No required WPS criterion remains open. Same-session source review, selected browser/keyboard/200% owned-surface CSS stress evidence and historical evaluation limits remain disclosed, not universal conformance. The four project-owned synthetic containers were stopped after acceptance; volumes/data remain recoverable, and other projects were untouched. Local installed Skill VERSION was read as 3.3.0 and was not upgraded: that action is outside this endpoint. No production deployment or real-data migration occurred.
