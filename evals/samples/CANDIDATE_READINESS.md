# R8 candidate preparation review

Latest reconciliation: [2026-10-06 checkpoint](#current-finalization-checkpoint--2026-10-06).

Date: 2026-10-05. Owner/reviewer: engineering lead, one implementation writer.
Disposition: preparation progressing; whole-candidate acceptance not granted.

## Authority and sequencing

The owner requested advancing to the next stage while R7 evidence remained
unverified. Independent packaging, regression and raw-case preparation proceed;
R7 acceptance and final R8 readiness are not inferred from that request. No new
release, installed skill update, font installation or production action.
The formal roadmap dependency guard remains unchanged.

## Current source and artifact binding

Worktree `worktrees/material-roadmap`, branch
`codex/r7-integrated-quality-completion`; HEAD and cached origin/main are
`2e62e9b4cb0a8d7d77a172dbc1a913f544d20e7f`, zero ahead/behind against that
cached ref. The candidate is dirty/uncommitted; original dirty checkout remains
untouched. No R8 source commit, remote branch, PR, issue/milestone, candidate CI,
merge or release exists for this preparation. Live upstream was not fetched.
No Graphify generation/freshness is claimed; direct package-source relationships
are the relevant impact map for this bounded preparation.

Exact locally built working-source candidates (not Git-normalized release bytes):

| Artifact | SHA256 | Members | Result |
| --- | --- | --- | --- |
| Portable Skill ZIP | `da05ea774a1c8f86ed432ab01451336afd88e4d08c64abfca49972ad16fde44d` | 75 | CRC, exact source inventory/bytes and reproducibility pass |
| Plugin ZIP | `1a8e2712dc944bc22a850def25f17a70397c5cb8deda4255a585bc641d6bb1bc` | 82 | CRC, exact source inventory/bytes and reproducibility pass |

Both contain all 75 canonical Skill resources, including DESIGN.md template,
current typography, QA and owner font-upload guidance. Root/Skill/plugin version
is 3.1.1. Two fresh output directories were verified absent before the unchanged
packager ran; nothing was overwritten/deleted. Actual second-build ZIP bytes
match the first. No ZIP was installed or uploaded. Subsequent eval/roadmap review
changes do not enter these ZIPs; no packaged Skill resource has changed since
the builds. A later changed packaged resource requires rebuilding/rebinding.

Operational verification script, per-resource digests, ZIPs and runs are under
the external workspace `.roadmap-ops/r8-readiness-20261005/`, not Git. The source
and package facts above are the portable review summary, not a synthetic receipt.

## Verification actually performed

- Release metadata, product routing/isolation, shared rules, design system and
  specialist registry validators pass. Registry validation is not installed
  freshness or independent specialist use.
- 11 roadmap-policy tests, four handbook migration tests, seven input-preparation
  tests, three authored-asset tests and 20 runtime configuration/store/HTTP tests
  pass. Those are entrypoint counts, not unique scenario/model quality coverage.
  Scoped temporary-directory tests used an authorized isolated elevated run due
  to the known sandbox directory-access issue; tests/source were not weakened.
- After two new raw cases were added, the expanded seven-test preparation suite
  passes exact copied input/prompt binding, original preservation and rejection
  of existing-output overwrite. These checks do not run an AI evaluator.
- Fixture validation now reports 88 definitions/17 fixtures. Historical recorded
  five-product results/schema validate separately; neither result represents
  newly executed candidate model/browser/device coverage.
- Official quick validation was attempted and failed to import `yaml`; it is
  unavailable, not passed. No PyYAML or other dependency was installed.
- Read-only preparation manager reports WARN with no blocked/selected specialist:
  Head v1.4.0 and installed UI v3.1.1 current, no update. Unselected security/API
  inventory checks had network-related warnings; they were not used to claim
  specialist currentness or a security review. No additional specialist added.

## Behavioral coverage and scoped execution

Existing raw cases already cover professional discovery, reference uncertainty,
handbook migration, sequential approval, incremental decisions, delegation
fallback, appearance lifecycle, icons and product isolation. Do not duplicate
them merely to increase case count. Prior bounded independent results remain
historical and source-scoped, not a full new R8 conformance run.

New raw cases are `runtime-appearance-persian-font-upload` and
`runtime-appearance-preserve-approved-font`. They exercise new Persian-font
foundation/upload planning and preserve a settled alternate brand font during
a narrow extension. The owner subsequently authorized fresh independent
execution. One fresh evaluator completed both planning requests from a frozen
75-resource snapshot and raw briefs, without invariants/answer keys/reviews.
The lead read the generated recommendations, initial handbook, implementation
plans and handbook delta separately: 2 cases / 10 scoped invariants pass.
See the [font forward review](FONT_FORWARD_REVIEW.md) for actual observations,
source/input bindings and shared-session limits. No behavioral failure warrants
another Skill correction. Generated artifacts remain outside Git.
This is planning behavior, not font-upload implementation or rendered-font
proof. It is not an execution result for all 88 cases or five product routes.

The lead also reviewed the four changed packaged resources (QA checklist,
language/typography reference, runtime governance and handbook template).
They preserve product-language scope, accepted fonts, planning versus actual
implementation status and the single runtime contract. All 75 canonical
resources still match the verified package/snapshot digests. This bounded source
review does not establish whole-candidate security, CI or formal R8 acceptance.

## Owner-supplied font image

The owner supplied an image of the new Persian revision's selected h1 and Styles
panel, plus the root font declaration. Visible evidence shows Vazirmatn as the
requested shared family, local Regular @font-face and font-synthesis:none.
The page reports ordinary/bold loading. This supports declared source/style
and readiness evidence only; the image does not show Rendered Fonts, actual
glyph identity/weight or original QF04 samples. No QF04 pass is inferred.
The original image is preserved operationally as owner-font-styles.png; it is
not a public repository attachment or authorization to change the approved UI.

## Remaining acceptance gates

- Required R7 actual-font/native-confirm and representative visual/access checks.
- Broader candidate behavioral acceptance beyond the two new font-planning cases.
- Final whole-candidate review and any source-normalized package rebuild.
- Official quick validation on a capable authorized runtime or candidate CI.
- Candidate-bound native scan, current CI and authorized delivery verification
  when integration/publication is requested. No scan is claimed for this snapshot.

Do not enter R9 or mark R7/R8 completed from these preparatory successes.

## Fresh continuation and final-source preparation — 2026-10-05

The owner explicitly requested completion and passing integration of R7/R8,
then resumed after stopping Computer Use with Escape. No new release remains
authorized. A live read-only GitHub refresh/fetch confirmed the same HEAD and
origin/main `2e62e9b4cb0a8d7d77a172dbc1a913f544d20e7f`, zero ahead/behind;
no open PR was returned. The local working candidate is still uncommitted.
Existing v3.1.1 release identity/assets were inspected, not mutated.

Fresh independent five-route planning execution is now separately accepted in
[ROUTE_FORWARD_REVIEW.md](ROUTE_FORWARD_REVIEW.md). Three evaluator sessions,
five requests and actual lead review are not all 88 cases or application QA.
All 75 frozen Skill resources still match current source and the previously
verified ZIPs. Both exact archives again pass inventories/CRC/byte comparison
and the two builds remain byte-identical. Version remains 3.1.1.

The unchanged native Trivy executable was checked against the current official
stable release, both 0.75.0. An actual secret scan of the extracted candidate
plugin tree passed with zero findings and no coverage warnings. A separate
comparison verified all 82 scanned members exactly match the verified plugin
ZIP, which includes the complete portable Skill resource set. Private report
SHA256 is `da30acbda8e825a14e7abbb169ef6f8d1087de39807cccea6daf29a301b7293d`;
scan and binding live under `.roadmap-ops/r8-final-20261005/`, outside Git.
Reading the restricted scan report required an authorized elevated check; its
permissions were not loosened. This covers working-source package bytes, not
the entire repository or a future Git-normalized candidate. Dependency/image/
infrastructure scans were not represented as run: the package ships text/assets,
not supported bundled dependency runtimes or affected infrastructure.

Fresh regression: 11 roadmap, four handbook migration, seven raw-input, three
authored-asset and 20 runtime tests passed (45 entrypoint tests). Release metadata,
product routes, shared rules, design system, specialists and 88-case/17-fixture
validators passed. Historical five-product schema validation also passed but is
not the new execution. Sandbox temporary-directory access failed first; an
isolated existing test run with the required access passed without source/test
weakening or dependency installation. Official quick_validate still fails to
import yaml; no PyYAML was installed and no candidate CI is claimed. Repository
purity found no tracked/staged forbidden files; only the optional local-exclude
configuration warning remains. Whitespace review passed.

R7 recovery has partial original-Persian rendered-font evidence, but original
native confirmation and remaining representative checks are not closed. On the
resumed attempt, the safety reviewer refused further Windows inspection because
of the prior Escape stop. Explicit scoped permission to reactivate browser
control was requested; no alternative browser/automation bypass was attempted.
Unaffected R8 preparation continued. No stage gate is waived: there is no R7/R8
completion, source commit/push/PR/current CI/merge, release or R9 kickoff here.

## Current finalization checkpoint — 2026-10-06

The owner requested finalizing both stages after three manually successful tests.
The [integrated review](INTEGRATED_QUALITY_REVIEW.md#owner-manual-review--2026-10-06)
now records their exact supplied artifacts and distinguishes reported execution
from visible screenshot scope. No same-test repetition or implied design approval.

Fresh 45 entrypoint tests and protected metadata/routing/shared/design/specialist/
fixture/historical-result validators pass. The known Windows temporary-directory
permission failure was recovered with an explicitly authorized isolated rerun;
no fixture/test/security change. JavaScript syntax and whitespace review pass.
Purity finds no tracked/staged forbidden artifacts; local-exclude WARN remains.

On this date, the existing exact two-build package verifier was rerun against
current working source and existing archives into a new external report. Both
ZIP inventories, CRCs, member bytes and repeat-build byte equality pass; all 75
Skill resources match. Hashes remain da05ea77...fde44d (portable) and
1a8e2712...bb1bc (plugin), with full identities above. No rebuild, installation,
upload or Git-normalized-byte claim is inferred. Planning-return reuse is limited
to unchanged packaged resources and the existing separately reviewed cases.

Live authorized fetch and open-PR inspection confirm baseline main
2e62e9b4cb0a8d7d77a172dbc1a913f544d20e7f and no open PR at that observation.
Local official validation again fails to import yaml; it is not a pass. Freshness
manager obtains Head/UI source records but fails an unrelated due inventory
archive transfer; no full preflight/compatibility acceptance is manufactured.
No PyYAML installation, dependency addition or installed-Skill change occurred.

R7 original-font metadata, qualified representative capture/access and overlay
keyboard acceptance remain unresolved. The owner-reported original native
save/cancel/accept check is attributed manual evidence, with the final completion
state independently visible, not an automated native-dialog recovery claim.
Candidate CI/security/delivery must be tied to the actual reviewed commit when
run. A draft review PR does not remove the dependent R7/R8 acceptance gates.
