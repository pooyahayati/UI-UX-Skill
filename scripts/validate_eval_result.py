#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
cases_manifest = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
VALID = ("pass", "partial", "fail", "not-testable")


def verdict_consistent(item: dict, outcomes: set[str]) -> bool:
    """Required outcomes set the floor; notes justify conservative case verdicts."""
    verdict = item.get("result")
    if verdict == "pass":
        return outcomes == {"pass"}
    if verdict == "not-testable":
        return outcomes == {"not-testable"}
    reason = isinstance(item.get("notes"), str) and bool(item["notes"].strip())
    if verdict == "fail":
        return "fail" in outcomes or reason
    if verdict == "partial":
        return ("fail" not in outcomes and outcomes != {"not-testable"}
                and (outcomes != {"pass"} or reason))
    return False


def validate_result(result: object, *, manifest: dict = cases_manifest,
                    require_all: bool = False) -> list[str]:
    """Validate structure and coherence, not evidence truth or release acceptance."""
    errors: list[str] = []
    if not isinstance(result, dict):
        return ["Result must be an object"]
    expected = {case["id"]: case for case in manifest["cases"]}

    if result.get("skillVersion") != manifest.get("version"):
        errors.append("skillVersion does not match eval manifest")
    for field in ("host", "model", "date"):
        if not isinstance(result.get(field), str) or not result[field].strip():
            errors.append(f"{field} must be a nonempty string")
    for field in ("fixtureCommit", "notes"):
        if field in result and not isinstance(result[field], str):
            errors.append(f"{field} must be a string")
    cases = result.get("cases")
    if not isinstance(cases, list) or not cases:
        return errors + ["cases must be a nonempty array"]

    seen: set[str] = set()
    for index, item in enumerate(cases):
        if not isinstance(item, dict):
            errors.append(f"cases[{index}] must be an object")
            continue
        case_id = item.get("id")
        if not isinstance(case_id, str) or case_id not in expected:
            errors.append(f"Unknown case id: {case_id}")
            continue
        if case_id in seen:
            errors.append(f"Duplicate result case: {case_id}")
        seen.add(case_id)
        if item.get("triggerMode") not in ("explicit", "implicit"):
            errors.append(f"{case_id}: invalid triggerMode")
        if item.get("result") not in VALID:
            errors.append(f"{case_id}: invalid result")
        if "notes" in item and not isinstance(item["notes"], str):
            errors.append(f"{case_id}: notes must be a string")
        if "evidence" in item and (not isinstance(item["evidence"], list)
                                  or not all(isinstance(x, str) for x in item["evidence"])):
            errors.append(f"{case_id}: evidence must be an array of strings")

        expected_invariants = expected[case_id]["invariants"]
        recorded = item.get("invariants")
        if not isinstance(recorded, list) or not recorded:
            errors.append(f"{case_id}: invariants must be a nonempty array")
            continue
        recorded_text: set[str] = set()
        outcomes: set[str] = set()
        invariant_errors = len(errors)
        for inv in recorded:
            if not isinstance(inv, dict):
                errors.append(f"{case_id}: invariant must be an object")
                continue
            text = inv.get("text")
            if not isinstance(text, str) or text not in expected_invariants:
                errors.append(f"{case_id}: unknown invariant: {text}")
            elif text in recorded_text:
                errors.append(f"{case_id}: duplicate invariant: {text}")
            else:
                recorded_text.add(text)
            if inv.get("result") not in VALID:
                errors.append(f"{case_id}: invalid invariant result: {text}")
            else:
                outcomes.add(inv["result"])
            if "evidence" in inv and not isinstance(inv["evidence"], str):
                errors.append(f"{case_id}: invariant evidence must be a string: {text}")
        for inv in expected_invariants:
            if inv not in recorded_text:
                errors.append(f"{case_id}: missing invariant result: {inv}")
        if len(errors) == invariant_errors and item.get("result") in VALID:
            if not verdict_consistent(item, outcomes):
                errors.append(f"{case_id}: inconsistent case result {item['result']!r} "
                              f"for required invariant outcomes {sorted(outcomes)}; "
                              "see evals/README.md#verdict-consistency")

    if require_all:
        missing = sorted(set(expected) - seen)
        if missing:
            errors.append(f"Missing case results: {', '.join(missing)}")
    return errors


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    """Do not silently overwrite contradictory JSON object fields."""
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"Duplicate JSON field: {key}")
        value[key] = item
    return value


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate recorded eval structure and verdict consistency, not acceptance or evidence truth.")
    parser.add_argument("result")
    parser.add_argument("--require-all", action="store_true",
                        help="Require every current manifest case; does not require passing outcomes.")
    args = parser.parse_args()
    try:
        result = json.loads(Path(args.result).read_text(encoding="utf-8"), object_pairs_hook=unique_object)
        errors = validate_result(result, require_all=args.require_all)
    except (OSError, ValueError) as exc:
        errors = [f"Cannot read result: {exc}"]

    if errors:
        print("Behavioral eval result validation failed:")
        for item in errors:
            print(f"- {item}")
        sys.exit(1)

    counts = {verdict: sum(x["result"] == verdict for x in result["cases"]) for verdict in VALID}
    print("Behavioral eval result is structurally valid and internally consistent (not acceptance). "
          f"Cases={len(result['cases'])}/{len(cases_manifest['cases'])} "
          f"Pass={counts['pass']} Fail={counts['fail']} Partial={counts['partial']} "
          f"Not-testable={counts['not-testable']}")
    failures = [x["id"] for x in result["cases"] if x["result"] == "fail"]
    if failures:
        print("Failed cases:", ", ".join(failures))

if __name__ == "__main__":
    main()
