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

Started after R11.2 acceptance. Prepare a bounded independent behavior suite using existing raw inputs; freeze the selected cases, reviewer criteria and candidate Skill before evaluation.
