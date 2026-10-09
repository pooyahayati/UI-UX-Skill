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
R9_SCOPE = {
    "optional Material activation and routing",
    "product-personalized foundations and curated research",
    "scoped component guidance and stack-fit assessment",
    "sequential responsive samples and handbook integration",
    "appearance controls through existing runtime contracts",
    "bounded behavioral/rendered evaluation and candidate readiness",
}
R9_DEPENDENCIES = {
    "R9.1": set(), "R9.2": {"R9.1"}, "R9.3": {"R9.2"},
    "R9.4": {"R9.2", "R9.3"}, "R9.5": {"R9.4"},
    "R9.6": {f"R9.{i}" for i in range(1, 6)},
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
    """Validate the preserved historical checkpoint and public README navigation."""
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
        "**Outside this exception:** Stabilization maintenance only, except for the separately named R9 exception below.",
        "new Product Types", "new major capability families", "persian-writing",
        "deduplication", "context isolation", "additional external design specialists",
    ):
        if term not in freeze:
            errors.append(f"ROADMAP stabilization policy missing: {term}")
    scope = re.search(r"^Allowed correction scope:\s*\n((?:\s*\n)?(?:- [^\n]+\n)+)", freeze, re.M)
    items = [] if not scope else re.findall(r"^- (.+?)[;.]?\s*$", scope[1], re.M)
    if len(items) != len(CORRECTION_SCOPE) or set(items) != CORRECTION_SCOPE:
        errors.append("Authorized correction scope must contain exactly the four agreed areas")
    r9_scope = re.search(r"^Allowed R9 scope:\s*\n((?:\s*\n)?(?:- [^\n]+\n)+)", freeze, re.M)
    r9_items = [] if not r9_scope else re.findall(r"^- (.+?)[;.]?\s*$", r9_scope[1], re.M)
    if len(r9_items) != len(R9_SCOPE) or set(r9_items) != R9_SCOPE:
        errors.append("Separate R9 scope must contain exactly the six agreed areas")
    for term in ("**Separate R9 exception:** Optional Material Design only.",
                 "**R9 kickoff:** Authorized local R9.1 implementation on 2026-10-06 after accepted R7/R8.",
                 "Outside the two named exceptions, stabilization maintenance only.",
                 "earlier delivery permission is not silently inherited"):
        if term not in freeze:
            errors.append(f"Separate R9 stabilization policy missing: {term}")
    if "## Future Product Types" in roadmap:
        errors.append("ROADMAP must not advertise future Product Types during stabilization")
    # Detailed authority/scope is owned and validated above in ROADMAP, not
    # duplicated in the public product introduction.
    policy = section(readme, "Project status")
    for term in ("stability", "[Roadmap](ROADMAP.md)", "[Contributing](CONTRIBUTING.md)"):
        if term not in policy:
            errors.append(f"README project-status navigation missing: {term}")
    if section(readme, "Feature freeze") or re.search(r"\bR\d+(?:\.\d+)?\b", policy):
        errors.append("README must keep internal stage/authority details in ROADMAP")

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
    errors.extend(validate_r9_progress(roadmap, statuses))
    return errors


def validate_current_roadmap(roadmap: str) -> list[str]:
    """Validate the live WPS ledger separately from closed historical stages."""
    errors = []
    current = section(roadmap, "Current state")
    summary = {}
    for key, value in re.findall(r"^\| ([^|]+) \| ([^|]+) \|\s*$", current, re.M):
        if key in summary:
            errors.append(f"Duplicate current-state field: {key}")
        summary[key] = value.strip()
    tracker = section(roadmap, "WordPress settings extension (WPS)")
    rows = re.findall(r"^\| (WPS-\d+) \| (.+)\|\s*$", tracker, re.M)
    expected = [f"WPS-{i}" for i in range(7)]
    if [name for name, _ in rows] != expected:
        errors.append("WPS tracker must contain WPS-0–WPS-6 exactly once and in order")
    statuses = {}
    link = r"\[[^\]]+\]\([^)]+\)"
    for name, tail in rows:
        fields = [value.strip() for value in tail.split("|")]
        if len(fields) != 4:
            errors.append(f"{name}: tracker must have five columns")
            continue
        _, status, prerequisite, evidence = fields
        statuses[name] = status
        if status not in STATES:
            errors.append(f"{name}: invalid status {status!r}")
        required = ("Owner instruction to execute WPS" if name == "WPS-0"
                    else f"Accepted WPS-{int(name[4:]) - 1}")
        if required not in prerequisite:
            errors.append(f"{name}: missing execution prerequisite")
        if status != "Not started" and not re.search(link, evidence):
            errors.append(f"{name}: started package needs an execution/evidence link")
        if status == "Completed":
            visible = re.sub(r"\]\([^)]+\)", "]", evidence)
            dates = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", visible)
            try:
                dated = bool(dates) and all(calendar_date.fromisoformat(value) for value in dates)
            except ValueError:
                dated = False
            if not dated:
                errors.append(f"{name}: completion needs valid dated acceptance evidence")
    for index, name in enumerate(expected):
        if statuses.get(name, "Not started") != "Not started":
            if any(statuses.get(previous) != "Completed" for previous in expected[:index]):
                errors.append(f"{name}: prerequisite packages must be Completed")
    completed = sum(value == "Completed" for value in statuses.values())
    active = [name for name in expected if statuses.get(name) in {"In progress", "Blocked", "Reopened"}]
    remaining = [name for name in expected if statuses.get(name) != "Completed" and name not in active]
    if summary.get("Completed WPS packages") != f"{completed} of 7":
        errors.append("WPS completed count must agree with the tracker")
    if len(active) > 1 or summary.get("Active WPS package") != (active[0] if active else "None"):
        errors.append("Active WPS package must match the single active tracker row")
    if summary.get("Next WPS package") != (remaining[0] if remaining else "None"):
        errors.append("Next WPS package must agree with the tracker")
    authority = summary.get("Execution authority", "")
    if not authority:
        errors.append("WPS execution authority must be recorded")
    elif any(value != "Not started" for value in statuses.values()):
        if "Awaiting" in authority or not re.search(link, authority):
            errors.append("Started WPS work requires linked owner execution authority")
    if not summary.get("Accountable role"):
        errors.append("WPS accountable role must be recorded")
    history = section(roadmap, "Completed history")
    if "docs/archive/ROADMAP-2026-10-09.md" not in history:
        errors.append("Completed history must link to the preserved checkpoint")
    for term in ("completed R0–R8 and R9 exceptions are not new authority",
                 "Completion does not authorize push/merge, publication, installation or deployment"):
        if term not in section(roadmap, "Scope and acceptance rules"):
            errors.append(f"Current roadmap authority boundary missing: {term}")
    return errors


def validate_r9_progress(roadmap: str, correction_statuses: dict[str, str]) -> list[str]:
    """Keep the extension separate and require real prerequisite/evidence records."""
    errors = []
    tracker = re.search(r"^### R9 package tracker\s*\n(.*?)(?=^### |^## |\Z)",
                        roadmap, re.M | re.S)
    rows = [] if not tracker else re.findall(r"^\| (R9\.\d+) \| (.+)\|\s*$", tracker[1], re.M)
    if [row[0] for row in rows] != list(R9_DEPENDENCIES):
        errors.append("R9 package tracker must contain R9.1–R9.6 exactly once and in order")
    statuses = {}
    for package, tail in rows:
        fields = [value.strip() for value in tail.split("|")]
        if len(fields) != 4:
            errors.append(f"{package}: tracker must have five columns")
            continue
        _, status, _, evidence = fields
        statuses[package] = status
        if status not in STATES:
            errors.append(f"{package}: invalid package status {status!r}")
        if status != "Not started" and not re.search(r"\[[^\]]+\]\([^)]+\)", evidence):
            errors.append(f"{package}: started package needs an execution/evidence link")
        if status == "Completed":
            # A dated anchor target is not a dated acceptance statement.
            visible_evidence = re.sub(r"\]\([^)]+\)", "]", evidence)
            dates = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", visible_evidence)
            try:
                dated = bool(dates) and all(calendar_date.fromisoformat(value) for value in dates)
            except ValueError:
                dated = False
            if not dated:
                errors.append(f"{package}: completion needs valid dated acceptance evidence")
        if status in {"Completed", "In progress", "Blocked", "Reopened"}:
            if any(correction_statuses.get(dep) != "Completed" for dep in ("R7", "R8")):
                errors.append(f"{package}: accepted R7/R8 are required before execution")
    for package, status in statuses.items():
        if status != "Not started" and any(statuses.get(dep) != "Completed"
                                           for dep in R9_DEPENDENCIES.get(package, set())):
            errors.append(f"{package}: prerequisite packages must be Completed")
    if sum(status in {"In progress", "Blocked", "Reopened"} for status in statuses.values()) > 1:
        errors.append("R9 must have at most one active implementation package")
    overall_rows = re.findall(r"^\| R9 \| (.+)\|\s*$", roadmap, re.M)
    if len(overall_rows) != 1:
        errors.append("Separate R9 overall tracker must contain R9 exactly once")
        return errors
    overall = [value.strip() for value in overall_rows[0].split("|")]
    if len(overall) != 6:
        errors.append("R9 overall tracker must have seven columns")
        return errors
    _, state, _, owner, date, evidence = overall
    if state not in STATES or not owner or owner in {"TBD", "Not recorded"}:
        errors.append("R9 overall status and accountable owner must be valid")
    started = any(value != "Not started" for value in statuses.values())
    complete = len(statuses) == 6 and all(value == "Completed" for value in statuses.values())
    if ((state == "Not started" and started) or (state == "Completed" and not complete)
            or (state not in {"Not started", "Completed"} and (not started or complete))):
        errors.append("R9 overall status must agree with its six-package tracker")
    if state == "Completed":
        try:
            dated = bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", date)) and bool(calendar_date.fromisoformat(date))
        except ValueError:
            dated = False
        if not dated or not re.search(r"\[[^\]]+\]\([^)]+\)", evidence):
            errors.append("R9 overall completion needs a dated evidence link")
    return errors
