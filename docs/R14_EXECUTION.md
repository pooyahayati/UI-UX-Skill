# R14 Execution and Acceptance

## Authority

On 2026-11-02 the owner authorized R14.1 through R14.3, followed by commit/push/PR
integration and merge, a new release, then the local Skill update. This supersedes
the planning-only checkpoint in [the plan](R14_AUDIT_REMEDIATION.md). Keep its
acceptance criteria, existing workflow, product decisions and external-source
boundaries. No unrelated Skill update or production-product migration is authorized.

Use the [roadmap](../ROADMAP.md#r14-bounded-quality-gap-corrections) as the only
live status ledger. Actual checks and bounded results belong below. Release and
installation require their final artifact checks and a recoverable local backup.

## R14.1

The six new viewport-evidence tests were run against the original validator:
the valid-record test passed and five negative test groups failed, reproducing
acceptance of missing/contradictory evidence (and stray VIEW rows in other producers).
The correction uses the exact legacy producer inventory, separate regular/zoom
contracts, strict boolean/font records and bounded finite geometry. It changes no
producer, historical report, screenshot, font or accepted owner decision.

The existing roadmap validator now selects the R14 ledger. Ordered, planning,
active/blocked/reopened, completed, malformed and premature states are covered
without weakening historical checks. CI explicitly runs the viewport regression.

Accepted 2026-11-02: six new evidence tests, five R13 evidence tests, 23 WordPress
contracts, 50 roadmap-policy tests and release metadata validation passed.
The synthetic contract fixture now supplies the required legacy viewport rows;
its old assertions accepting unknown VIEW rows were strengthened to reject them.
Historical reports/images and all Skill source bytes are unchanged. No fresh
browser/owner font test was performed or needed for this validator-only change.

## R14.2

Accepted 2026-11-02 against CRIT-1 through CRIT-5. The changes are confined to
`existing-product-audit.md` and `visual-regression.md`: task-sensitive hierarchy,
preservation of useful baselines and evidence-backed, falsifiable refinement.
The existing audit section is the canonical destination; duplicating these rules
in the QA checklist or adding a parallel guide would broaden evaluation inputs
without a new benefit. Source attribution and the original workflow are preserved.

[Paired critique review](../evals/r14/REVIEW.md) records two fixed rendered examples,
four isolated baseline/candidate answers and four rerun affected scenarios.
The useful difference is a more precise, testable state-emphasis hypothesis in C01,
not a demonstrated user-performance gain or a confirmed defect in that fixture.
C02 correctly preserves the existing design. No product correction was rendered.

The 13-case foundation report passes the existing evidence-integrity validator;
S08/M07 are fresh responses and other cases retain their exact original identities.
Source succession, release-history and WordPress contract checks passed (3, 4, 7
and 23 tests respectively). The review separately accepts actual behavioral scope.

## R14.3

Accepted 2026-11-02 against ICON-1 through ICON-7. Optional Aria discovery and
morphicons state transitions are documented in the existing implementation/motion
references. Only four portable guidance files changed across R14. No provider,
specialist, runtime settings engine or package dependency is installed by the Skill.

The [review](../evals/r14/REVIEW.md#optional-providers--accepted-2026-11-02) accepts
ten independently refreshed affected foundation cases and two raw icon scenarios.
Unchanged S01/S02/S04 retain their R13 identities. Scope, owner controls, actual
licenses, version-specific exporter limitations and truthful outcomes are preserved.

The [bounded runtime specimen](../evals/fixtures/icon-morph/README.md) passed all
15 observation groups in installed Edge 156.0.4314.58 at 390×844. It exercises the
actual pinned 2.0.2 DOM provider with the existing authenticated appearance API;
the original fixture/store and WordPress host are unchanged. Normal/reduced/off,
interruption, keyboard/focus, private preview, save/reopen/publish, reset/rollback,
invalid/denied requests, configuration/provider failure and cleanup were verified.
Solid/badge choices retain static truthful artwork rather than an unsupported morph.

The initial unminified provider exceeded the preselected 16,000-byte gzip budget.
An isolated pinned esbuild build reduced the requested provider route to 9,611
bytes without raising that ceiling. No physical-device/FPS/user-speed claim is made.
The Chrome media-query emulation limitation was isolated; the final Edge test
observes a real active morph and a delivered preference-change event. Assertions
also check final geometry, not only the driver's pre-first-frame progress value.

Three evidence-integrity regression tests and three exact-source succession tests
passed. They reject changed outputs, requests, images, producer inputs and
relabelled reports; CI retains these checks. The final 13-case foundation record
passes the existing integrity gate. Human-readable review and runtime evidence
remain separate from structural validator success.

## Delivery

R14 implementation is accepted. [Release 3.7.0](releases/3.7.0.md) tracks final
combined validation, source/package security, merge/publication and managed local
installation. No earlier response or browser record is relabelled for the version bump.
