# R11 execution evidence

The [roadmap](../ROADMAP.md#r11-audit-remediation) is the live status ledger. Acceptance criteria remain in the [R11 plan](R11_AUDIT_REMEDIATION.md). The owner's 2026-10-16 instruction authorizes the three implementations in order, merge, a new release and this Skill's managed local update.

## Baseline and boundaries

- Branch: `codex/r11-remediation`, starting at merged `ec5293a2190fd5ff332c84545a5a6e14bacd4e0e`; pre-existing planning changes retained.
- Direct source impact analysis: UI handlers -> pure draft model -> revision-checked PHP save -> browser/model tests -> fixture evidence integrity; canonical Skill subtree -> packager -> consumer verification; raw evaluation cases -> preparation -> independent outputs -> reviewer/CI checks. No authoritative Graphify evidence is claimed.
- Tier 2: cross-boundary behavior and release; synthetic WordPress data only. Existing request authorization, secret masking, compare-and-swap, historical evidence and accepted design decisions remain protected.
- No new application dependency or production deployment. Temporary browsers, scan reports and packages remain outside product source. Final release requires native security scanning and actual downloaded-artifact verification.
- Preflight used installed engineering Head 1.7.1; its output needed UTF-8 on Windows. The unrelated locally modified security specialist is preserved, not automatically updated. Its applicable guidance remains subject to the Head's scope: no new authentication, scanner, dependency or broad hardening work.

## R11.1

Accepted 2026-10-16 after source review, deterministic regressions and real-admin execution. No PHP contract, storage, permission, dependency, palette or typography change was needed.

| Acceptance | Evidence |
| --- | --- |
| WP-A1 | `node evals/wordpress-settings/test_conflict.cjs` first failed on the original handlers: expected `https://peer.example.test`, received `https://old.example.test`. The corrected handlers pass; real two-admin saves retain the peer endpoint and intended credential action. |
| WP-A2 | `test_model.cjs` covers untouched fields, independent same-section edits and identical changes; actual-handler/browser checks retain an unrelated title draft. |
| WP-A3 | Per-field review exposes newer endpoint/enabled values and requires explicit overlapping-field choices. Existing title-replacement browser regression passes. Hidden credentials require an explicit action because presence alone cannot establish that a peer did not replace a secret. |
| WP-A4 | Actual-handler and real-admin tests cover cancellation without writes and a second peer revision after review. Local input remains; another conflict is required. Keep/replace/remove model and existing real-admin tests pass. |
| WP-A5 | Existing browser rejection, duplicate-click, edit-during-save, lost-response, reset, capability and nonce checks still pass. No secret is rendered in the conflict summary. |
| WP-A6 | 21 recorded browser observations pass on WordPress 7.1.3 and 6.8 / PHP 8.3.35 / Edge 155.0.4283.45. English conflict dialogs inspected at 1440/390px on both hosts; Persian at 390px. Tab containment, Escape, focus return and horizontal-overflow assertions pass. |

- Actual output: [successor browser record](../evals/wordpress-settings/evidence/r11-browser-results.json); exact [fixture delta](../evals/wordpress-settings/r11-fixture-delta.json), including the unchanged historical parent.
- Rendered review: [Persian narrow](../evals/wordpress-settings/evidence/r11-conflict-current-fa-390.png), [English narrow/current](../evals/wordpress-settings/evidence/r11-conflict-current-en-390.png), [English narrow/minimum](../evals/wordpress-settings/evidence/r11-conflict-minimum-en-390.png). Text, controls and choices fit; no new design/font approval is claimed or requested.
- `python -B evals/wordpress-settings/test_contracts.py`: 14 passing tests, including successor scope/parent rejection and historical evidence preservation. The browser runner and exact live fixture are bound to the successor record. Original WPS results/images are untouched.
- Limits: synthetic owned installations, modelled HTTP in the deterministic handler test, desktop-emulated narrow viewports; not real-device or assistive-technology certification. The existing 200% CSS stress check is not native browser zoom.

## R11.2

Accepted 2026-10-16 after R11.1. The independent completeness regression first failed with `Standalone distribution must include the full license notice`, then passed against corrected source.

| Acceptance | Evidence |
| --- | --- |
| PK-A1–A2 | Canonical `skills/ui-ux-skill/LICENSE` matches the full root notice. Actual candidate ZIPs contain it: standalone 92 files, plugin 99. A separately copied direct-install subtree and independently extracted ZIP roots pass resource validation without Head injection. |
| PK-A3 | Package preflight rejects missing, empty, truncated and altered notices before staging. Consumer tests reject removed/empty/truncated/wrong-attribution archive notices even after recomputing their checksums. The reviewed notice identity prevents matching truncated source copies from redefining success. |
| PK-A4 | Both actual candidate ZIPs pass CRC, checksum, exact members, canonical-source bytes and embedded-version checks; extracted resources resolve. Skill source additions are restricted by the exact [license delta](../evals/wordpress-settings/r11-license-delta.json); no historical source/evaluation record was rewritten. |
| PK-A5 | Packaging suite: 18 tests, 16 passed / two native-symlink skips on Windows. Existing junction/path, refusal and failure-preservation checks pass. Dedicated integrity suite: 15 passed. Linux CI still must execute the native symlink cases before integration. |

Commands: `python -B scripts/test_package_release.py`, `python -B evals/wordpress-settings/test_contracts.py`, `scripts/package_release.py --output <fresh-external-dir>`, `evals/wordpress-settings/verify_packages.py --directory <actual-output>` and `validate_resource_routes.py --skill-root <each-extracted-or-staged-root>`. CI now invokes actual-ZIP consumer verification; the main-push installer smoke also compares the installed notice.

These are unreleased candidate artifacts carrying the then-current 3.5.0 metadata, not replacements for published 3.5.0 assets. Final-version packages and published downloads require their own delivery verification. No active local installation changed.

## R11.3

Accepted 2026-10-16 after R11.2. The lead read every actual response and scored all 27 selected criteria: 13 cases passed, no failed/partial/unavailable required outcome. No decision defect requiring a Skill-guidance change was observed in this selected run. The five unselected raw prompts remain unexecuted, not inferred passes.

| Acceptance | Evidence |
| --- | --- |
| EV-A1 | The [selection manifest](../evals/ui-foundations/manifest.json) covers all six decision families. `prepare_eval_run.py <id> --suite ui-foundations --output <fresh-external-dir>` creates exact raw prompt + candidate input under `evaluator/`, with reviewer-only `RUN.json` outside it. All 13 prepared trees were rechecked after execution. |
| EV-A2 | [Actual outputs and result](../evals/ui-foundations/result.json) retain host/model/date, per-case evaluator identity, raw/preparation/output hashes, whole-candidate content identity, consumed-source mapping and local external-resource hashes. Retained outputs were compared with the original agent-written files, not reconstructed from review notes. |
| EV-A3 | Fresh `fork_turns=none` agents `/root/r11_<case-id>` ran one case each. The lead separately reviewed decisions against the withheld criteria. All 27 criteria have concrete evidence; `--suite ui-foundations --accept` passes. This is independent evaluator context, not a different model family or independent human certification. |
| EV-A4 | 15 deterministic tests pass: exact input separation, answer-file leakage, changed raw/candidate/rubric, reused context, missing/changed output/evidence, candidate identity, source dependencies, duplicate/contradictory/incomplete records and coherent failure versus acceptance. An incorrect path in the new synthetic dependency test was corrected before acceptance; the original failure remains in the run history. |
| EV-A5 | Existing CI now runs preparation/record regression tests and the selected saved-record acceptance gate. No live model call or service cost is introduced. Consumed-source changes invalidate mapped cases; shared routing/version changes invalidate all selected cases. CI execution itself remains an integration gate below. |
| EV-A6 | Historical five-product, WPS and source-only shadcn/motion records remain unchanged. The old five-product version is not rewritten: an exact-content [compatibility sidecar](../evals/real-world/compatibility.json) records only current structural compatibility. Unbound version mismatches and inconsistent results still fail. |

Invocation: each fresh agent was told to read its own prepared `evaluator/skill/SKILL.md` and raw `evaluator/PROMPT.txt`, follow only routed candidate resources (plus required Persian specialization), avoid parent repository/sibling cases/reviewer `RUN.json`/prior outputs, and write a complete English response plus a separate actual-read list. No product repository was supplied; browsing, installation, product writes and nested agents were excluded. The wrapper contained no expected decisions. Windows' launcher initially hit an unrelated locked drive; narrowly scoped read-only escalation resolved the file-access problem without changing host drives.

The candidate is version 3.5.1 with normalized Skill-tree digest `3f84dc6f0512a344cbc469c806c33f82a1d22b8102104686775c5bfcb402a37d`. Model: inherited `gpt-6-astra`, verified from parent turn metadata; host: Codex desktop on Windows. All selected runs occurred on 2026-10-16. Candidate guidance remained fixed throughout. `readPaths` are agent-reported; `sourcePaths` additionally include common routing/version dependencies. External Persian-writing hashes identify the local resources read, not a new upstream freshness check.

Limits: input separation is instructional plus file-integrity checking, not an OS sandbox; hashes cannot prove semantic truth or read history. These are text decisions, not rendered Motion/Animate UI tests, real-device/assistive-technology certification or owner visual approval. The run is 13 of 18 raw shadcn/motion prompts, not the 114-case general inventory. No new runtime adapter or animation dependency is shipped.

## Combined closeout

The full resource regression exposed an old synthetic packager fixture with a placeholder license. It now supplies the real complete notice; the original broken-resource tests remain intact and pass. This reconciles R11.2 with an existing consumer test without weakening notice validation.

Source review confirmed unchanged PHP storage/authorization/CAS, no package dependencies added, preserved historical evidence, bounded fixture changes, and explicit separation of historical compatibility from fresh behavioral acceptance. README, INSTALL, CHANGELOG, roadmap and evaluation instructions were checked for changed claims. Authorized publication/install evidence will be recorded separately in [release 3.5.1](releases/3.5.1.md); implementation acceptance alone is not published delivery.
