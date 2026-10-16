# shadcn/ui scope and source review

Historical source-only checkpoint. The owner's later delivery instruction and
current publication/install evidence are tracked in the [3.5.0 release record](../../docs/releases/3.5.0.md).
The delivery exclusions and version statements below describe this checkpoint,
not the subsequent release.

Date: 2026-10-16. Base: `d20ea89d4d982fbc669abd83af54f35dd0f1b798` (published
3.4.0 line). Authority: [owner-scoped roadmap decision](../../ROADMAP.md#shadcnui-dashboard-default).

This record describes the shadcn-only checkpoint. The later authorized
[interactive motion addition](../motion/REVIEW.md) retains this source delta and
package evidence as historical, then binds its own changes to this exact parent.
Current-source checks include both deltas; these earlier package hashes are not
the current combined candidate hashes.

## Acceptance boundary

This change adds instructions and routes, not an application, generated component
catalog, installed library or external specialist. The default belongs to the
Dashboard Product Pack; explicit choices for other products reach the shared
implementation guide without activating dashboard methodology.

Only two existing portable resources change: the Dashboard Product Pack and
implementation strategies. One new portable resource is added: shadcn-ui.md.
The [source delta](source-delta.json) binds their previous and current normalized
hashes. All other WPS-protected resources remain hash-checked. The original WPS
baseline, browser results, outcome methods and evaluation inputs remain intact.
This new scope is not represented as fresh WPS runtime acceptance.

## Scenario review

Method: same-session logical source tracing of [eight raw prompts](CASES.md).
These are expected paths inspected in the candidate instructions, not recorded
outputs from an independent model, product rendering or owner visual approval.

| Case | Source-traced acceptance condition |
| --- | --- |
| S01 | Dashboard default selects shadcn/ui without repeating a library-choice question; approved Persian/RTL/Vazirmatn and tokens remain; primary responsive review comes first. |
| S02 | Explicit Mantine selection wins; no persuasion or shadcn installation. |
| S03 | Existing Vue stack and audit-only scope win; no library migration or global rediscovery. |
| S04 | WordPress host and native settings controls take precedence over a secondary dashboard default; permissions/storage are preserved. |
| S05 | Explicit shadcn use reaches implementation guidance under Website; no dashboard mode, automatic second language or admin role. |
| S06 | Native platform and narrow scope are identified as constraints; no claim of direct React-component compatibility or runtime migration. |
| S07 | Material style and library choice remain distinct; compatible dashboard default applies; approved tokens/semantic icons map through governed controls and sequential reviews. |
| S08 | Existing generated source and primitive family are inspected; no blind overwrite; supported-style and portal-direction limits require actual affected-surface checks. |

Relevant sources: [Dashboard selection](../../skills/ui-ux-skill/references/products/dashboard.md#default-component-foundation),
[implementation routing](../../skills/ui-ux-skill/references/implementation-strategies.md#shadcnui-component-foundations),
[shared guide](../../skills/ui-ux-skill/references/shadcn-ui.md).
Unchanged product routing, WordPress requirements, handbook and sequential
approval contracts supply the protected constraints; the guide links relevant
implementation rules rather than duplicating those contracts.

## Verification record

Passed locally on Windows:

- Release metadata, roadmap policy, Product/Shared/Design/Specialist registries,
  source-resource routes and existing evaluation-input validation (114 cases,
  22 fixtures); the eight new prompts are a separately scoped source review.
- 68 regression tests across roadmap policy, package safety, resource routing
  and WPS evidence/source contracts: 65 passed, 3 native-symlink cases skipped
  because the host cannot create those links. Simulated reparse checks and
  Windows junction checks passed; skips are not native-symlink evidence.
- Original WPS evaluation data and behavior hashes remain unchanged. Added
  successor regressions reject wrong parent hashes, scope expansion, missing
  changes and incorrect successor content; no global checksum exemption.
- Both generated ZIPs passed checksum, CRC, complete member/source comparison
  and resource checks after independent extraction. Both extracted Skill roots
  passed the current source-delta check.

Local test packages (not published assets): Skill ZIP has 90 files and SHA-256
`0f3ca18ab7e3eab84adb2d59007b7abb321073d94a8b0d4ff4c6e2fd0e890f78`;
plugin ZIP has 97 files and SHA-256
`5b47916853a31a97468d6ee9c4c0a018a42b6884a7714138f5a3c85a9febf781`.

Official Skill quick validation passed (`Skill is valid!`). The bundled Python
lacks PyYAML and the package-host download timed out; the validator was therefore
run with the pure-Python library from the official `yaml/pyyaml` 6.0.3 source tag
in an external temporary directory. No global Python environment or project
dependency was changed. Downloaded source archive SHA-256:
`673e7e7de556542598ab38f43e09e714d028383d8d8a62b3239c4e3541c8227b`.

For source or new package consumers, run:

```sh
python evals/wordpress-settings/test_contracts.py
python evals/wordpress-settings/test_contracts.py --current-source --skill-root <extracted-skill-root>
```

Omitting `--current-source` with `--skill-root` intentionally retains the original
WPS checkpoint check for historical packages. Do not pass it for new consumers
and mistake the expected historical mismatch for a fresh WPS runtime defect.

No independent agent or browser evaluation is claimed. These checks cannot prove
the usability, accessibility, performance or owner approval of a future product.
No release, push/merge or active local-Skill replacement is part of this source
change; VERSION remains the published 3.4.0 baseline with an Unreleased entry.
