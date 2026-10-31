"""Exact R12 release metadata successor; never a model rerun or source waiver."""
from __future__ import annotations

import hashlib
import json
import re


RECORDS = {
    "evals/ui-foundations/r12-result.json",
    "evals/wordpress-settings/r12-behavior-results.json",
}
FROM_VERSION = "3.5.1"
TO_VERSION = "3.6.0"


def content_digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=False).encode()).hexdigest()


def tree_digest(files):
    return hashlib.sha256(json.dumps(files, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def version_digest(version):
    return hashlib.sha256((version + "\n").encode()).hexdigest()


def release_predecessor(result, actual, binding, *, record, current_version):
    """Return the old source view only for two exact retained R12 records.

    The caller still validates every prompt, preparation, output and consumed
    source against this view. Both recorded candidate identities remain intact.
    """
    keys = {"schema_version", "normalization", "scope", "decision", "recorded_version",
            "release_version", "version_change", "candidate_before_sha256",
            "candidate_after_sha256", "records", "notes"}
    if (not isinstance(binding, dict) or set(binding) != keys
            or binding.get("schema_version") != 1 or binding.get("normalization") != "git-lf"
            or binding.get("scope") != "r12-release-version-only"
            or binding.get("decision") != "docs/releases/3.6.0.md#authority"
            or binding.get("recorded_version") != FROM_VERSION
            or binding.get("release_version") != TO_VERSION or current_version != TO_VERSION
            or not isinstance(binding.get("records"), dict) or set(binding["records"]) != RECORDS
            or any(not re.fullmatch(r"[a-f0-9]{64}", str(value)) for value in binding["records"].values())
            or record not in RECORDS or not isinstance(result, dict)
            or binding["records"].get(record) != content_digest(result)
            or not isinstance(binding.get("notes"), str) or not binding["notes"].strip()
            or binding.get("version_change") != {
                "path": "VERSION", "previous_sha256": version_digest(FROM_VERSION),
                "sha256": version_digest(TO_VERSION)}):
        raise ValueError("Invalid R12 release-version-only identity, scope or retained record")
    if (not isinstance(actual, dict) or not actual
            or any(not isinstance(name, str) or not re.fullmatch(r"[a-f0-9]{64}", str(value))
                   for name, value in actual.items())
            or actual.get("VERSION") != version_digest(TO_VERSION)
            or binding.get("candidate_after_sha256") != tree_digest(actual)):
        raise ValueError("Release source identity or VERSION content changed")
    previous = {**actual, "VERSION": version_digest(FROM_VERSION)}
    if binding.get("candidate_before_sha256") != tree_digest(previous):
        raise ValueError("Release predecessor source identity changed")
    # R12's fresh S04 run and WPS run share this complete candidate. Historical
    # per-case candidates in the UI suite remain independently validated.
    if record == "evals/ui-foundations/r12-result.json":
        rows = result.get("cases", [])
        selected = [row for row in rows if isinstance(row, dict) and row.get("id") == "S04"] if isinstance(rows, list) else []
        parent = selected[0].get("candidate") if len(selected) == 1 else None
        if result.get("skillVersion") != FROM_VERSION:
            raise ValueError("Retained UI record version changed")
    else:
        parent = result.get("candidate")
    if parent != {"files": previous, "sha256": tree_digest(previous)}:
        raise ValueError("Release does not succeed the exact retained R12 candidate")
    return previous
