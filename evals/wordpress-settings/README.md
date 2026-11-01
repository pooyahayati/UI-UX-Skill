# WordPress settings evaluation

## R13 current evidence

The [R13 execution record](../../docs/R13_EXECUTION.md) separates error-ownership
runtime checks, evidence-validator mutations and independent guidance responses.
The [roadmap](../../ROADMAP.md#r13-audit-remediation) is the live acceptance ledger.

- [Error ownership](evidence/r13/validation/r13-validation-results.json): nine
  real-admin observations across both declared hosts and narrow Persian RTL.
- [Discovery/workspace](evidence/r13/discovery/r12-browser-results.json) and
  [legacy regression](evidence/r13/regression/r13-regression-results.json): fresh
  R13 fixture runs using the unchanged existing runners. The legacy raw report is
  retained next to its labelled metadata wrapper. Guide hashes remain the actual
  runtime-run inputs; later prose corrections are covered by model responses.
- [Stage-three responses](r13-stage3-behavior.json) and
  [stage-four responses](r13-stage4-behavior.json): isolated raw requests, exact
  candidate/output bindings and lead review. [Additional raw cases](R13_CASES.md)
  cover operational-only routing and the distinct theme gates.
- [Fixture successor](r13-fixture-delta.json) changes only App error ownership;
  original WPS/R11/R12 reports and images remain historical, unchanged.

```sh
python -B -X utf8 evals/wordpress-settings/test_contracts.py
python -B -X utf8 evals/wordpress-settings/test_r13_evidence.py
python -B -X utf8 evals/wordpress-settings/test_r13_behavior.py
node evals/wordpress-settings/test_validation.cjs
```

Full-report acceptance checks completion, scope, omissions, real-browser methods,
source/runner identity, supported host/control compatibility and the required
capture matrix. The legacy producer has its own schema; it cannot be promoted to
a complete discovery report. CI validates saved evidence, not live model/browser
behavior or owner approval.

## Historical R12 evidence

The [R12 execution record](../../docs/R12_EXECUTION.md) separates Skill decisions,
rendered synthetic-host checks and independent task observation. No customer
approval, human usability benchmark or production rollout is implied.

| Evidence | Scope |
| --- | --- |
| [Raw requests](R12_CASES.md) · [reviewed responses](r12-behavior-results.json) | Five fresh-context design decisions; actual outputs in `r12-outputs/`, ten lead-reviewed criteria. |
| [Raw administrator task](R12_TASK.md) · [actual UI report](r12-task/report.md) · [source-bound review](r12-task-result.json) | Fresh evaluator found/corrected settings from the interface, retained drafts and verified reload persistence; limitations and one automation wrong turn are explicit. |
| [Discovery/workspace runtime](evidence/r12-browser-results.json) | Eleven real-admin observations, exact source/runner and screenshot bindings, WordPress 6.8/7.1.3. |
| [Legacy regression runtime](evidence/r12-regression-results.json) | Twenty-one fresh observations from the unchanged runner, including two-admin conflict and permission/nonce/secret recovery. |
| [Exact-parent successor](r12-source-fixture-delta.json) | Only three portable guides and five fixture paths; WPS/R11 parent records remain unchanged. |
| [Refreshed S04](../ui-foundations/outputs/S04-r12.md) · [suite successor](../ui-foundations/r12-result.json) | One fresh affected response; twelve unchanged historical responses keep their original bindings. |

Selected R12 captures: [settings desktop](evidence/r12-discovery-current-fa-1440.png),
[settings narrow](evidence/r12-discovery-current-fa-390.png),
[reports desktop](evidence/r12-workspace-current-fa-1440.png),
[details narrow](evidence/r12-workspace-detail-current-fa-390.png).
Dark mode and a fully English host were not exercised; English plugin content
inside the supported host is a separate compatibility check.

```sh
python -B -X utf8 evals/wordpress-settings/test_contracts.py
python -B -X utf8 evals/wordpress-settings/test_r12_behavior.py
node evals/wordpress-settings/test_discovery.cjs
```

These commands protect retained evidence/invariants. They do not replace fresh
model or browser execution when the bound behavior changes.

## Historical WPS evidence

Raw inputs are in [briefs](../fixtures/wordpress-settings/briefs.json); required
outcomes are in the [plan](../../docs/WORDPRESS_SETTINGS_ROADMAP.md#planned-acceptance-scenarios).
The [execution record](EXECUTION.md) keeps actual evidence and limitations.

Protected Skill content is bound to [the pre-edit baseline](baseline.json). Hashes
use canonical UTF-8 Git content (CRLF normalized to LF), so a checkout line-ending
conversion is not a behavioral change. Version-only release metadata is separate.

Dedicated structural/regression command: `python -B -X utf8 evals/wordpress-settings/test_contracts.py`.
Real-admin specimen/browser commands are documented in the [runnable fixture](../fixtures/wordpress-settings/README.md).
The structural gate does not prove model decisions, rendering or WordPress runtime
behavior. No new independent agent/session is authorized by these artifacts.

[RESULTS.json](RESULTS.json) binds the nineteen accepted outcomes to their methods,
candidate content hashes and package comparison. [Source review](SOURCE_REVIEW.md)
and [actual browser observations](evidence/browser-results.json) remain distinct.

Selected real-admin captures: [simple desktop](evidence/persian-simple-1440.png),
[simple narrow](evidence/persian-simple-390.png), [multi-topic desktop](evidence/persian-multi-1440.png),
[multi-topic narrow](evidence/persian-multi-390.png), [reset dialog](evidence/persian-reset-dialog-390.png),
and [200% owned-surface CSS zoom stress](evidence/persian-zoom-200.png).
These are synthetic engineering evidence, not production design approval.

Release evidence: [local candidate checks](RELEASE_CANDIDATE.json) and
[actual published v3.4.0 downloads](RELEASE_PUBLISHED.json). Their archive hashes
are kept separate; canonical content, versions and source/tag binding were verified.
