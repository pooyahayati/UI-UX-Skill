"""Release-document policy checks, not proof of agent or UI behavior."""
from __future__ import annotations

import re
from datetime import date as calendar_date

HISTORICAL_STAGES = (
    "Stage 1 — Website Product Pack",
    "Stage 2 — WordPress Plugin Product Pack",
    "Stage 3 — Dashboard Product Pack",
    "Stage 4 — Shared Product UI Rules",
    "Stage 5 — Design System Hardening",
    "Stage 6 — Real-World Product Evaluation",
)
CORRECTION_SCOPE = {
    "design foundation",
    "the living handbook",
    "visual approval",
    "safe parametric appearance management",
}
STATES = {"Not started", "In progress", "Blocked", "Completed", "Reopened"}
DEPENDENCIES = {
    "R0": set(), "R1": {"R0"}, "R2": {"R1"}, "R3": {"R1", "R2"},
    "R4": {"R2", "R3"}, "R5": {"R2", "R4"}, "R6": {"R5"},
    "R7": {"R1", "R3", "R6"}, "R8": {f"R{i}" for i in range(8)},
}


def section(text: str, heading: str) -> str:
    match = re.search(rf"^## {re.escape(heading)}\s*$", text, re.M)
    if not match:
        return ""
    end = re.search(r"^## ", text[match.end():], re.M)
    return text[match.end():match.end() + end.start()] if end else text[match.end():]


def validate_policy(readme: str, roadmap: str) -> list[str]:
    errors: list[str] = []
    for heading in HISTORICAL_STAGES:
        block = section(roadmap, heading)
        if "**Status:** Completed" not in block:
            errors.append(f"{heading} must remain Completed")
    history = section(roadmap, HISTORICAL_STAGES[-1])
    for term in ("in-session source-based behavioral evaluation", "did not independently execute",
                 "not represented as completed checks"):
        if term not in history:
            errors.append(f"Historical evaluation limitations must remain: {term}")

    freeze = section(roadmap, "Feature Freeze — 3.1.0 Stabilization")
    for term in (
        "**Status:** Active with limited correction exception",
        "**Correction exception:** Authorized for R0–R8 only.",
        "**Outside this exception:** Stabilization maintenance only.",
        "new Product Types", "new major capability families", "persian-writing",
        "deduplication", "context isolation", "additional external design specialists",
    ):
        if term not in freeze:
            errors.append(f"ROADMAP stabilization policy missing: {term}")
    scope = re.search(r"^Allowed correction scope:\s*\n((?:\s*\n)?(?:- [^\n]+\n)+)", freeze, re.M)
    items = [] if not scope else re.findall(r"^- (.+?)[;.]?\s*$", scope[1], re.M)
    if len(items) != len(CORRECTION_SCOPE) or set(items) != CORRECTION_SCOPE:
        errors.append("Authorized correction scope must contain exactly the four agreed areas")
    if "## Future Product Types" in roadmap:
        errors.append("ROADMAP must not advertise future Product Types during stabilization")
    policy = section(readme, "Feature freeze")
    for term in ("Limited correction exception: R0–R8 only.", "Outside this exception",
                 "no new Product Types", "additional external design specialists",
                 "general-purpose page builder", "[Roadmap](ROADMAP.md)"):
        if term not in policy:
            errors.append(f"README stabilization policy missing: {term}")

    # Restrict parsing to the canonical tracker; do not count stage IDs in prose.
    tracker = re.search(r"^### Correction stage tracker\s*\n(.*?)(?=^### |^## |\Z)",
                        roadmap, re.M | re.S)
    rows = [] if not tracker else re.findall(r"^\| (R\d+) \| (.+)\|\s*$", tracker[1], re.M)
    if [row[0] for row in rows] != [f"R{i}" for i in range(9)]:
        errors.append("Correction tracker must contain R0–R8 exactly once and in order")
    completed = 0
    active = []
    statuses = {}
    for stage, tail in rows:
        fields = [value.strip() for value in tail.split("|")]
        if len(fields) != 6:
            errors.append(f"{stage}: tracker must have seven columns")
            continue
        _, status, _, owner, date, evidence = fields
        statuses[stage] = status
        if status not in STATES:
            errors.append(f"{stage}: invalid stage status {status!r}")
        if not owner or owner in {"TBD", "Not recorded"}:
            errors.append(f"{stage}: accountable owner is required")
        if status in {"In progress", "Blocked", "Reopened"}:
            active.append(stage)
        if status == "Completed":
            completed += 1
            try:
                valid_date = bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", date)) and bool(calendar_date.fromisoformat(date))
            except ValueError:
                valid_date = False
            if not valid_date or not re.search(r"\[[^\]]+\]\([^)]+\)", evidence):
                errors.append(f"{stage}: completion needs a dated evidence link")
    for stage, status in statuses.items():
        if status not in {"Completed", "In progress"}:
            continue
        required = DEPENDENCIES.get(stage, set())
        if stage == "R7" and status == "In progress":
            required = {"R1", "R3"}  # Language/theme work precedes final R6 integration.
        if any(statuses.get(dep) != "Completed" for dep in required):
            errors.append(f"{stage}: prerequisites must be Completed before {status}")
    count = re.search(r"^\- Implementation: \*\*([^*]+)\*\*; \*\*(\d+) of 9 correction stages completed\*\*\.", roadmap, re.M)
    if not count or int(count[2]) != completed:
        errors.append("Implementation completed count must agree with the canonical tracker")
    elif count[1] != ("Completed" if completed == 9 else "In progress"):
        errors.append("Implementation state must reflect the authorized correction workstream")
    current = re.search(r"^\- Active implementation stage: \*\*(None|R\d+)\*\*\.", roadmap, re.M)
    if not current or active != ([] if current[1] == "None" else [current[1]]):
        errors.append("Active implementation stage must agree with the canonical tracker")
    remaining = [stage for stage in DEPENDENCIES if statuses.get(stage) != "Completed" and stage not in active]
    next_stage = re.search(r"^\- Next implementation stage: \*\*(None|R\d+)\b", roadmap, re.M)
    if not next_stage or next_stage[1] != (remaining[0] if remaining else "None"):
        errors.append("Next implementation stage must agree with the canonical tracker")
    return errors
