#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "evals" / "cases.json"
FIXTURES = ROOT / "evals" / "fixtures"

def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare a behavioral-eval fixture and run manifest.")
    parser.add_argument("case_id")
    parser.add_argument("--output", required=True)
    parser.add_argument("--suite", choices=["default", "ui-foundations"], default="default")
    args = parser.parse_args()

    if args.suite == "ui-foundations":
        from behavior_evaluation import prepare
        try:
            print(prepare(args.case_id, Path(args.output)))
        except (OSError, ValueError) as error:
            parser.exit(1, f"Preparation failed: {error}\n")
        return

    manifest = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    case = next((item for item in manifest["cases"] if item["id"] == args.case_id), None)
    if case is None:
        raise SystemExit(f"Unknown case: {args.case_id}")

    out = Path(args.output).resolve()
    if out.exists():
        raise SystemExit(f"Output already exists: {out}")
    out.mkdir(parents=True)

    fixture = case.get("fixture")
    if fixture:
        src = FIXTURES / fixture
        if not src.is_dir():
            raise SystemExit(f"Fixture not found: {src}")
        shutil.copytree(src, out / "fixture")

    run = {
        "skillVersion": manifest["version"],
        "caseId": case["id"],
        "type": case["type"],
        "fixture": fixture,
        "prompt": case["prompt"],
        "invariants": case["invariants"],
        "instructions": [
            "Use a fresh host session where practical.",
            "Record explicit vs implicit Skill triggering.",
            "Do not edit the source fixture directory; work in this prepared copy.",
            "Capture rendered/visual evidence when the case and tools permit it.",
            "Record checks that were not possible rather than claiming them."
        ]
    }
    (out / "RUN.json").write_text(json.dumps(run, indent=2) + "\n", encoding="utf-8")
    (out / "PROMPT.txt").write_text(case["prompt"] + "\n", encoding="utf-8")
    print(out)

if __name__ == "__main__":
    main()
