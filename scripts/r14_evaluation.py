"""Integrity of reviewed R14 artifacts; this does not grade model answers."""
import json
import re
from pathlib import Path
from behavior_evaluation import ROOT, canonical, digest, tree_digest
from release_version_binding import content_digest
from r14_source_binding import r14_predecessor

ACCEPTED = {
    "evals/r14/stage2-results.json": "5e89f371b2564aa15a0f12ce19edc98379c3ee6381ef94cc4806d2c69626e5da",
    "evals/r14/stage3-results.json": "49def1428c3a73e898d50b0e6650c410ed292af1dda48f2691fbe71d1af7c327",
    "evals/r14/evidence/icon-runtime.json": "f6f9ff49ea76f32b484213222f746f3827fdf4a36fb487a4c67032b22bc1a478",
}
RUNTIME_IDS = {"STATIC", "NORMAL", "INTERRUPT", "REDUCED-LIVE", "PERSONAL-OFF",
               "PRIVATE-UNSUPPORTED", "SAVE-REOPEN-PUBLISH", "INVALID-DENIED", "RESET-ROLLBACK",
               "CONFIG-FAILURE", "OWNER-OFF", "MOBILE", "CLEANUP", "PROVIDER-FAILURE", "PAYLOAD"}


def artifact(base, name):
    path = base / name
    if not isinstance(name, str) or path.is_symlink() or not path.resolve().is_relative_to(base.resolve()):
        raise ValueError("Artifact escapes its evidence directory")
    return path


def errors(name, result, *, root=ROOT):
    try:
        if name not in ACCEPTED or content_digest(result) != ACCEPTED[name]:
            return ["Reviewed R14 record identity changed"]
        base = root / "evals/r14"
        if name.endswith("icon-runtime.json"):
            rows = result["observations"]
            if len(rows) != len(RUNTIME_IDS) or {r["id"] for r in rows} != RUNTIME_IDS:
                return ["Runtime observation inventory changed"]
            for row in rows:
                if row["status"] != "passed" or not row["details"]:
                    return ["Runtime observation is not passing"]
            for path, sha in result["source"].items():
                if digest(artifact(root, path).read_bytes().replace(b"\r\n", b"\n")) != sha:
                    return ["Runtime producer/input changed: " + path]
            for path, sha in result["artifacts"].items():
                if digest(artifact(base / "evidence", path).read_bytes()) != sha:
                    return ["Runtime image changed: " + path]
            return []
        stage = result["stage"]
        expected = {"C01-baseline", "C02-baseline", "C01-candidate", "C02-candidate", "B03", "B04"} if stage == "R14.2" else {"I01", "I02"}
        rows = result["cases"]
        if {r["id"] for r in rows} != expected or len(rows) != len(expected) or len({r["evaluator"] for r in rows}) != len(rows):
            return ["Missing/duplicate case or independent evaluator"]
        binding = json.loads((root / ("evals/r14-stage2-source.json" if stage == "R14.2" else "evals/r14-source.json")).read_text())
        r14_predecessor(result["candidate"]["files"], binding, root=root)
        for row in rows:
            if row["candidate"]["sha256"] != tree_digest(row["candidate"]["files"]):
                return ["Malformed per-run candidate"]
            if digest(canonical(artifact(base, row["output"]))) != row["output_sha256"]:
                return ["Actual output changed: " + row["id"]]
            if "image" in row and digest(artifact(base, row["image"]).read_bytes()) != row["image_sha256"]:
                return ["Actual comparison image changed"]
            ident = row.get("request", row["id"])
            source = root / ("evals/wordpress-settings/R12_CASES.md" if ident.startswith("B") else "evals/r14/CASES.md")
            match = re.search(r"^## " + ident + r"[^\n]*\n(.*?)(?=^## |\Z)", source.read_text(encoding="utf-8"), re.M | re.S)
            if not match or digest((match[1].strip()+"\n").encode()) != row["prompt_sha256"]:
                return ["Raw request changed: " + ident]
        return []
    except (OSError, ValueError, KeyError, TypeError) as error:
        return ["Invalid R14 evidence: " + str(error)]
