# Behavioral Eval Result

## Candidate

- Skill version: 3.1.1
- Host: Codex / Claude Code / Claude.ai
- Model:
- Date:
- Tester:
- Fixture commit/reference:

## Results

| Case | Trigger | Result | Evidence / notes |
| --- | --- | --- | --- |
| existing-safe-improvement | explicit / implicit | Pass / Partial / Fail / Not testable | |
| visual-regression-redesign | explicit / implicit | Pass / Partial / Fail / Not testable | |
| owner-runtime-governance | explicit / implicit | Pass / Partial / Fail / Not testable | |
| personalization-precedence | explicit / implicit | Pass / Partial / Fail / Not testable | |
| data-trust | explicit / implicit | Pass / Partial / Fail / Not testable | |
| rtl-localization | explicit / implicit | Pass / Partial / Fail / Not testable | |
| realtime-operations | explicit / implicit | Pass / Partial / Fail / Not testable | |
| backend-non-trigger | explicit / implicit | Pass / Partial / Fail / Not testable | |
| auth-boundary | explicit / implicit | Pass / Partial / Fail / Not testable | |
| arbitrary-code-config | explicit / implicit | Pass / Partial / Fail / Not testable | |

## Critical release gates

- [ ] Business logic preserved
- [ ] Working-tree safety preserved
- [ ] Authorization/security boundaries preserved
- [ ] No arbitrary executable runtime customization introduced
- [ ] Owner/user configuration precedence correct
- [ ] Invalid/missing runtime configuration has a safe fallback
- [ ] Stored preferences reconcile safely when constraints change
- [ ] Identity-redesign boundary respected
- [ ] Visual-validation claims have rendered evidence or explicit limitations
- [ ] Trigger boundary behaves as expected

## Regressions

List behavior worse than the previous release.

## Decision

- Release candidate accepted / rejected:
- Blocking issues:
- Follow-up issues:


## Stage 6 five-product evaluation

Record these representative product cases when validating a v3 candidate:

| Product | Case | Result | Evidence / limitations |
| --- | --- | --- | --- |
| Dashboard | real-world-dashboard-evaluation | Pass / Partial / Fail / Not testable | |
| Website | real-world-website-evaluation | Pass / Partial / Fail / Not testable | |
| Web Application | real-world-web-app-evaluation | Pass / Partial / Fail / Not testable | |
| Mobile Application | real-world-mobile-evaluation | Pass / Partial / Fail / Not testable | |
| WordPress Plugin | real-world-wordpress-evaluation | Pass / Partial / Fail / Not testable | |

For every case, distinguish source-based evidence from rendered/browser/device evidence.

Do not mark rendered/device checks as complete when they were not performed.
