# R14 targeted evaluation review

## Visual critique — accepted 2026-11-02

The two images in `evidence/` are identical between each baseline/candidate pair.
Each independent evaluator received only the raw request, its isolated Skill
snapshot and image. It did not receive a rubric, prior answer or expected defect.
`stage2-results.json` binds actual outputs, reads, evaluator IDs and image hashes.
The baseline is released 3.6.1; the candidate changes two existing references.

| Example | Baseline | Candidate and reviewer conclusion |
| --- | --- | --- |
| C01: Persian WordPress settings, 390 px | Preserves the native layout; recommends general findability, save and accessibility checks. | Preserves it too, but identifies a **provisional** disabled-save emphasis question and a falsifiable state/action check. The apparently disabled blue control is visible; actual disabled/busy state and user confusion are not established by this image. Verify those before changing anything. This is a more actionable hypothesis, not a confirmed product bug. |
| C02: English mobile assigned-visit list, 390 px | Finds no evidenced defect and retains the design. | Traces notice → record → action, retains the design and does not treat unused space as a defect. Useful negative control: critique need not manufacture a redesign. |

No fixture UI was changed. No improved task time, user success rate or findability
was measured. CRIT-5's correction-rendering condition was not triggered; these are
guidance/response comparisons, not a before/after product outcome.

The retained criteria address hierarchy in repeated tasks, competing emphasis,
preservation of good baselines and evidence → impact → smallest correction →
falsifiable check. They live in the existing audit and visual-regression references.
No extra QA checklist, questionnaire, score, handbook or agent requirement was
added. Source attribution is retained at the point of use. General house-style
prescriptions and the sources' orchestration were not adopted.

## Affected prior scenarios

Four previous cases consumed the changed references. They were rerun independently:

- S08 preserves customized shadcn/ui, fonts, semantic tokens and portal consumers;
  no regeneration, migration or unsupported browser-success claim.
- M07 preserves a Vue, English-only narrow audit; distinguishes intentional duration
  from render/request latency without installing React, a motion engine or an admin.
- B03 preserves native WordPress settings and the operational-page boundary;
  future interest in Material does not authorize migration or forced cards/search.
- B04 rejects blanket experimental component imports; preserves host-version,
  Settings API, native components and conditional operational DataViews decisions.

The refreshed S08/M07 rows are in `../ui-foundations/r14-stage2-result.json`.
Other rows remain exact historical R13 records, with original outputs and identities.
The explicit source successor and VERSION-only retention are integrity checks,
not new model observations. Review of the actual answers supports CRIT-1–CRIT-4;
the report validator checks provenance, not answer quality.

## Optional providers — accepted 2026-11-02

The ten previously selected foundation cases that consumed implementation/motion
guidance were rerun in fresh isolated contexts: S07/S08 and M01–M07/M10. S01/S02/S04
retain their exact historical R13 answers. The final foundation report binds this
distinction. No previously unselected case is counted as newly executed.

I01 retains the approved family and semantic assignments; Aria is optional discovery,
per-collection licensing is checked, and no catalog/MCP/CLI/runtime dependency is
installed. I02 identifies timer-based false save success, missing control naming
and missing effective motion policy; it keeps the existing service and distinguishes
the inspected exporter from the newer engine. Both explicitly leave runtime checks
unperformed. Their actual responses and reads are in `stage3-results.json`.

The independent answers preserve the WordPress/native host, Vue narrow-audit,
existing dashboard, settled foundations and no-new-admin boundaries. Review found
no need to change the Skill route, defaults, template or workflow.

Separate [runtime evidence](../fixtures/icon-morph/README.md) verifies one bounded
DOM specimen with 15 observation groups and actual payload measurement. This does
not turn the source catalog, every icon family or a future product into a tested
adapter. The unsupported solid/badge path is the specimen's own support boundary.
