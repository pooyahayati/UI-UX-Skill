# R15 evidence

`r14-runtime-source/` preserves all seven original producer/input files named in
the unchanged R14 runtime report. Each copy was checked against that report's
existing LF-normalized SHA-256 before R15 runtime edits. The historical validator
explicitly uses this source root; altered/missing historical files still fail.
It does not present that report as acceptance of the current specimen.

R15's new runtime report and dedicated gate bind the current source and required
recovery scenarios. The old report, images, portable Skill, provider pin and
source/version binding records remain unchanged. No production capability is claimed.

## Current acceptance

[Runtime report](evidence/runtime.json) and [mobile capture](evidence/mobile.png):
17 observation groups, including four real cached-navigation cycles and fresh
HTTP/network failures with recovery. All seven producer/input hashes, provider
identity and artifact hashes are bound to this report; there is no blanket hash
waiver or relabelled historical result.

Run `python scripts/r15_evaluation.py` and `python scripts/test_r15_runtime.py`
from the repository root for retained-evidence integrity. Run
`node scripts/test_icon_lifecycle.mjs` for controlled asynchronous/cleanup cases
(set `PYTHON` when the Python executable is not `python3`). A new browser execution
uses the existing [runner prerequisites](../fixtures/icon-morph/README.md#reproduction).
Recorded evidence checks are not a fresh browser run or independent model evaluation.
