# R8 scoped font-planning forward review

Date: 2026-10-05. Disposition: both planning cases accepted by separate lead
review; no whole-candidate or product-runtime acceptance.

## Execution and source boundary

The owner authorized this offered next step. One fresh evaluator,
`/root/r8_font_forward` with `fork_turns:none`, received the candidate Skill and
two named raw briefs, without expected answers, invariants, authored samples,
tests or prior review results. It completed both cases in the same session;
this is independent from the lead, not two mutually independent executions.
No application implementation, installation or publication was authorized.

Operational evidence is retained outside Git under
`.roadmap-ops/r8-readiness-20261005/forward-01/`. `EVALUATION_BINDING.md` records
the input hashes, evaluator assignment and permitted outputs. All 75 Skill
resources in the snapshot and working source matched the package-verification
resource digests before execution. Version remains 3.1.1; this is the dirty
working-source candidate, not a released or source-normalized Git package.

| Case | Raw input | SHA256 |
| --- | --- | --- |
| runtime-appearance-persian-font-upload | PERSIAN_FONT.md | `484b96b208592bb0f8fb593dfb64ca4d6158109d82e6f2bc0c0cc31f48a4273c` |
| runtime-appearance-preserve-approved-font | FONT_EXISTING.md | `62da1316bee55ea57615913a033b3a472dc9848db542871af1a939ee47cfdc77` |

## Artifacts actually reviewed

Under `outputs/persian-font/`: `RECOMMENDATION.md`, `DESIGN.md` and
`APPEARANCE_PLAN.md`. Under `outputs/preserve-font/`: `FONT_UPLOAD_PLAN.md` and
`DESIGN.delta.md`. The lead read the actual artifacts, not just the evaluator's
summary. The initial handbook is a draft for the fictional new product; the
delta does not replace an actual h12 handbook. Generated outputs stay external.
Both READS.md manifests were also read; they report only the active
web-application Product Pack, scope-relevant shared/design modules and required
installed Persian-writing resources. Resource-use claims are evaluator-reported,
not instrumented access traces. Seven final artifact SHA256 bindings are retained
in the external receipt. Automated Persian editorial checks were not executed;
no pass for them or for browser/runtime checks is claimed.

## Separate lead assessment

These are planning-output judgments, not execution results for their proposed
upload, permission, font, browser or accessibility checks.

| Case / invariant | Lead result | Observed artifact behavior |
| --- | --- | --- |
| New / product isolation | Pass | DESIGN product section selects only web-application; Persian RTL is monolingual and phone-first, without native-mobile/dashboard/English expansion. |
| New / professional default and approval | Pass | Recommendation and handbook propose Vazirmatn with rationale; appearance values and revision d1 remain unapproved. |
| New / actual assets and consumers | Pass | Handbook identifies a proposed font source, actual 400/700 and licensing needs, explicitly absent binaries; plan names forms/table plus chart Canvas/SVG redraw and Portal consumers. |
| New / validated selectable uploads | Pass | Plan admits validated tenant-scoped assets into the existing owner catalog using safe IDs, actual content/weight/license validation and bounded parsing; raw code/URLs and OS installation are excluded. |
| New / controlled lifecycle and handbook boundary | Pass | Private candidate, preview, explicit atomic publication, refresh/persistence, retained history, reset, rollback, fallback and failure preservation are planned; handbook is not a live settings database. |
| New / actual acceptance plan, honest evidence | Pass | Future-check table includes authorized lifecycle, denied/cross-tenant access, malformed/oversized assets, missing fonts, relevant consumers and recovery; each is explicitly not performed. |
| Existing / preserve accepted font | Pass | Plan and delta retain supplied h12/BrandFa and its real-weight scenario facts as default/reset source; Vazirmatn is not substituted. |
| Existing / bounded integration | Pass | Upload extends the prepared-font selector through existing authorization/storage/private draft/publication/history/restoration; no new panel or role. |
| Existing / no unrelated rediscovery | Pass | Approved palette, spacing, primary/dark treatments and Persian-only scope stay settled; no framework migration, extra locale or full questionnaire. |
| Existing / planned delta, no fabricated acceptance | Pass | Delta is a proposed merge into the current handbook; synthetic supplied facts are distinguished from missing source/font/runtime inspection and new approval. |

Result: 2 executed planning cases, 10 reviewed invariants pass. No observed
behavioral failure justifies a new candidate-Skill correction in this pass.
Suggested upload formats, byte/count limits, palette and viewport values are
explicit proposals, not verified compatibility or approved product defaults.
Primary review precedes dark review; no extra language is invented.

After recording the result, 11 roadmap-policy tests, release metadata validation,
88-case/17-fixture structural validation and `git diff --check` pass. Source and
snapshot resource hashes were rechecked against the package manifest with no
change. These checks are separate from the two model-planning outcomes above.
Branch remains `codex/r7-integrated-quality-completion`, HEAD and cached
origin/main `2e62e9b4cb0a8d7d77a172dbc1a913f544d20e7f`, zero ahead/behind;
working changes are uncommitted/unpushed. No new PR/CI/merge/release exists.
No live upstream refresh or Graphify generation/freshness is claimed.

## Limits and next gate

This does not execute the other 86 case definitions, refresh historical
five-product coverage, implement font upload, verify real font glyph/weight,
grant owner visual approval, or close R7 QF04/QF05 and representative QA gaps.
It does not establish full R8 conformance, current candidate CI, security scan,
installation, integration or release. Retain the existing dependency gates and
continue from the [candidate readiness review](CANDIDATE_READINESS.md), not from
a claim that all 88 cases passed.
