# Real-World Product Evaluation

Stage 6 evaluates one representative project for each primary Product Type:

1. Dashboard
2. Website
3. Web Application
4. Mobile Application
5. WordPress Plugin

## Evaluation layers

### Repository / source-based behavioral evaluation

This layer is recorded in `result.json`.

It verifies:

- product classification;
- Product Pack/local-pack selection;
- Shared Rule scope;
- Design System module scope;
- issue detection;
- safety/authorization/data-integrity boundaries;
- unnecessary-rule avoidance;
- evidence discipline.

The recorded 2026-10-02 run used ChatGPT / GPT-5.6 Sol in this working session.

### Render/device limitation

This connector workflow does not provide an independent browser/device execution environment for these five fixtures.

Therefore the evaluation does **not** claim:

- browser-rendered visual quality;
- real device VoiceOver/TalkBack behavior;
- real wp-admin rendering;
- measured performance;
- independent fresh-session reproducibility.

Passing the evidence-discipline invariants requires explicitly reporting those limitations.

A later independent Codex/Claude/browser run can be added without changing the Stage 6 architecture.

## Release rule

The Stage 6 gate requires:

- exactly five real-world product cases;
- all five Product Types covered exactly once;
- no unexplained `fail`;
- evidence for every invariant;
- fixture existence;
- route/pack/module expectations;
- explicit limitation reporting.

