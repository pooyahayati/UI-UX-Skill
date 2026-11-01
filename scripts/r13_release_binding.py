"""Exact R13 VERSION-only release compatibility; never fresh behavioral evidence."""
import json
from pathlib import Path
from release_version_binding import content_digest, tree_digest, version_digest

ROOT = Path(__file__).resolve().parents[1]
FROM_VERSION = "3.6.0"
TO_VERSION = "3.6.1"
BEFORE = "c88607b8b2eccc7a93fdfb17a51905897adbcc8acb269486e8a996ceee724692"
RECORDS = {"evals/ui-foundations/r13-result.json",
           "evals/wordpress-settings/r13-stage4-behavior.json", "evals/r13-source.json"}
ACCEPTED_RECORDS = {
    "evals/r13-source.json": "6609c3f3fc9b7a60446ecb1963702b18c619b18e9effae164afe52c8cbf23937",
    "evals/ui-foundations/r13-result.json": "c6e7de84edbfbd83a97cf2d975a5b226564987734f6893ca2d7993dbe4542d44",
    "evals/wordpress-settings/r13-stage4-behavior.json": "3124278f6da720cd63cc4195e54c1c880067e13357c640ee04933a4aeb062690",
}


def r13_release_predecessor(actual, binding=None, *, root=ROOT, result=None, record=None):
    if binding is None:
        binding = json.loads((root / "evals/r13-release-version.json").read_text(encoding="utf-8"))
    keys = {"schema_version", "scope", "normalization", "decision", "recorded_version",
            "release_version", "version_change", "candidate_before_sha256",
            "candidate_after_sha256", "records", "notes"}
    if (not isinstance(binding, dict) or set(binding) != keys
            or binding.get("schema_version") != 1 or binding.get("scope") != "r13-release-version-only"
            or binding.get("normalization") != "git-lf"
            or binding.get("decision") != "docs/releases/3.6.1.md#authority"
            or binding.get("recorded_version") != FROM_VERSION or binding.get("release_version") != TO_VERSION
            or binding.get("candidate_before_sha256") != BEFORE
            or binding.get("version_change") != {"path": "VERSION",
                "previous_sha256": version_digest(FROM_VERSION), "sha256": version_digest(TO_VERSION)}
            or binding.get("records") != ACCEPTED_RECORDS
            or not isinstance(binding.get("notes"), str) or not binding["notes"].strip()):
        raise ValueError("Invalid R13 release-only identity or scope")
    if (not isinstance(actual, dict) or actual.get("VERSION") != version_digest(TO_VERSION)
            or tree_digest(actual) != binding["candidate_after_sha256"]):
        raise ValueError("R13 release source identity changed")
    previous = {**actual, "VERSION": version_digest(FROM_VERSION)}
    if tree_digest(previous) != BEFORE:
        raise ValueError("R13 release changes more than VERSION")
    for path in RECORDS:
        original = json.loads((root / path).read_text(encoding="utf-8"))
        if content_digest(original) != binding["records"][path]:
            raise ValueError("Retained R13 record changed: " + path)
        if path != "evals/r13-source.json" and original.get("candidate") != {"files": previous, "sha256": BEFORE}:
            raise ValueError("R13 release does not succeed the accepted candidate")
    if result is not None or record is not None:
        if record not in RECORDS - {"evals/r13-source.json"} or content_digest(result) != binding["records"][record]:
            raise ValueError("R13 release cannot qualify another or modified evaluation")
    return previous
