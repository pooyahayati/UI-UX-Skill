"""R11 raw-input preparation and record checks; not model execution or evidence truth."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

from package_release import copy_tree, source_files, validate_output

ROOT = Path(__file__).resolve().parents[1]
SUITE = "ui-foundations"
COMMON_PATHS = {"SKILL.md", "VERSION", "product-types.json", "references/product-routing.md"}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(path: Path) -> bytes:
    data = path.read_bytes()
    return data.replace(b"\r\n", b"\n") if path.suffix in {"", ".md", ".json", ".yaml", ".yml", ".txt", ".svg"} else data


def snapshot(skill: Path) -> dict:
    return {p.relative_to(skill).as_posix(): digest(canonical(p)) for p in sorted(source_files(skill))}


def tree_digest(files: dict) -> str:
    return digest(json.dumps(files, sort_keys=True, separators=(",", ":")).encode())


def manifest(root: Path = ROOT) -> dict:
    from validate_eval_result import unique_object
    selected = json.loads((root / "evals/ui-foundations/manifest.json").read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    raw = {}
    for source in ("shadcn", "motion"):
        text = (root / "evals" / source / "CASES.md").read_text(encoding="utf-8")
        for match in re.finditer(r"^## ([SM]\d{2})[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S):
            if match[1] in raw:
                raise ValueError("Duplicate raw case")
            raw[match[1]] = match[2].strip() + "\n"
    cases = []
    for row in selected["cases"]:
        if row["id"] not in raw or row["id"] in {c["id"] for c in cases}:
            raise ValueError("Unknown or duplicate selected case")
        if not row.get("invariants") or len(set(row["invariants"])) != len(row["invariants"]) or not all(isinstance(x, str) and x.strip() for x in row["invariants"]):
            raise ValueError("Missing/duplicate reviewer criteria")
        cases.append({**row, "prompt": raw[row["id"]]})
    if selected.get("schema_version") != 1 or set(raw) != {r["id"] for r in cases} | set(selected["unexecuted"]) or set(selected["unexecuted"]) & {r["id"] for r in cases}:
        raise ValueError("Selected/unexecuted coverage must partition the raw inventory")
    return {"version": (root / "VERSION").read_text().strip(), "cases": cases, "unexecuted": selected["unexecuted"]}


def run_record(case: dict, files: dict) -> dict:
    return {"suite": SUITE, "caseId": case["id"], "inputSha256": digest(case["prompt"].encode()),
            "candidateSha256": tree_digest(files), "invariants": case["invariants"],
            "boundary": "Only evaluator/ is model input. RUN.json is reviewer-only. Preparation does not run a model."}


def run_bytes(run: dict) -> bytes:
    return (json.dumps(run, indent=2) + "\n").encode()


def preparation_errors(output: Path, root: Path = ROOT) -> list[str]:
    """Require exact raw text + candidate; refuse added reviewer/output material."""
    try:
        from validate_eval_result import unique_object
        run = json.loads((output / "RUN.json").read_text(encoding="utf-8"), object_pairs_hook=unique_object)
        case = next(c for c in manifest(root)["cases"] if c["id"] == run["caseId"])
        evaluator = output / "evaluator"
        expected = snapshot(root / "skills/ui-ux-skill")
        allowed = {"PROMPT.txt"} | {"skill/" + p for p in expected}
        paths = {p.relative_to(evaluator).as_posix() for p in source_files(evaluator)}
        if (paths != allowed or snapshot(evaluator / "skill") != expected
                or canonical(evaluator / "PROMPT.txt") != case["prompt"].encode()
                or run != run_record(case, expected)):
            return ["Prepared input, candidate or reviewer isolation mismatch"]
        return []
    except (OSError, ValueError, KeyError, StopIteration, TypeError) as error:
        return ["Invalid preparation: " + str(error)]


def prepare(case_id: str, output: Path, root: Path = ROOT) -> Path:
    case = next((c for c in manifest(root)["cases"] if c["id"] == case_id), None)
    if case is None:
        raise ValueError("Unknown selected case: " + case_id)
    output = validate_output(root.resolve(), output)
    files = snapshot(root / "skills/ui-ux-skill")
    output.mkdir()
    evaluator = output / "evaluator"
    evaluator.mkdir()
    copy_tree(root / "skills/ui-ux-skill", evaluator / "skill")
    (evaluator / "PROMPT.txt").write_text(case["prompt"], encoding="utf-8")
    (output / "RUN.json").write_bytes(run_bytes(run_record(case, files)))
    errors = preparation_errors(output, root)
    if errors:
        raise ValueError("; ".join(errors))
    return output


def validate_record(result: object, directory: Path, *, root: Path = ROOT,
                    accept: bool = False, require_all: bool = False) -> list[str]:
    from validate_eval_result import validate_result
    current = manifest(root)
    errors = validate_result(result, manifest=current, require_all=accept or require_all)
    if not isinstance(result, dict):
        return errors
    candidate = result.get("candidate", {})
    supplied = candidate.get("files", {}) if isinstance(candidate, dict) else {}
    actual = snapshot(root / "skills/ui-ux-skill")
    if (not isinstance(supplied, dict) or not supplied or set(supplied) != set(actual)
            or candidate.get("sha256") != tree_digest(supplied)
            or not all(re.fullmatch(r"[a-f0-9]{64}", str(v)) for v in supplied.values())):
        errors.append("Missing/malformed candidate identity or changed resource inventory")
        supplied = {} if not isinstance(supplied, dict) else supplied
    if result.get("unexecuted") != current["unexecuted"] or result.get("suite") != SUITE:
        errors.append("Missing/changed suite coverage boundary")
    expected = {c["id"]: c for c in current["cases"]}
    evaluators = set()
    for case in result.get("cases", []) if isinstance(result.get("cases"), list) else []:
        if not isinstance(case, dict) or not isinstance(case.get("id"), str) or case["id"] not in expected:
            continue
        case_id = case["id"]
        if case.get("inputSha256") != digest(expected[case_id]["prompt"].encode()):
            errors.append(case_id + ": stale raw input")
        if case.get("preparationSha256") != digest(run_bytes(run_record(expected[case_id], supplied))):
            errors.append(case_id + ": stale preparation/rubric binding")
        # Shared routing inputs plus the declared case-specific dependency/read set.
        # Changes to consumed sources invalidate those cases, not unrelated outputs.
        paths = case.get("sourcePaths")
        if (not isinstance(paths, list) or not all(isinstance(p, str) for p in paths)
                or len(paths) != len(set(paths)) or not COMMON_PATHS.issubset(paths)):
            errors.append(case_id + ": missing/duplicate source dependency set")
        else:
            for name in paths:
                if name not in supplied or supplied.get(name) != actual.get(name):
                    errors.append(case_id + ": stale/missing consumed source " + name)
        if not isinstance(case.get("evaluatorId"), str) or not case["evaluatorId"].strip():
            errors.append(case_id + ": missing independent evaluator identity")
        elif case["evaluatorId"] in evaluators:
            errors.append(case_id + ": reused evaluator context")
        else:
            evaluators.add(case["evaluatorId"])
        try:
            output = canonical(directory / "outputs" / (case_id + ".md"))
            if not output.strip() or case.get("outputSha256") != digest(output):
                errors.append(case_id + ": missing/changed actual output")
        except OSError:
            errors.append(case_id + ": missing actual output")
        invariants = case.get("invariants", [])
        if (not case.get("evidence") or not isinstance(case["evidence"], list)
                or not all(isinstance(e, str) and e.strip() for e in case["evidence"])
                or not isinstance(invariants, list)
                or any(not str(inv.get("evidence", "")).strip() for inv in invariants if isinstance(inv, dict))):
            errors.append(case_id + ": missing reviewer evidence")
        if accept and case.get("result") != "pass":
            errors.append(case_id + ": required acceptance is not passing")
    return errors
