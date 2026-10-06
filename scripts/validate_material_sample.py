"""Authored specimen gate/asset consistency, not consent or browser conformance."""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "evals/material/ham-amooz"


def approval_matches(approval: object, identity: dict) -> bool:
    return (isinstance(approval, dict)
            and all(isinstance(approval.get(k), str) and approval[k].strip()
                    for k in ("actor", "source", "date", "scope"))
            and approval.get("identity") == identity)


def validate_metadata(data: dict, sample: Path = SAMPLE) -> list[str]:
    errors = []
    for key in ("sample_revision", "handbook_revision", "default_language", "direction", "theme"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            errors.append(f"missing identity: {key}")
    identity = {k: data.get(k) for k in
                ("sample_revision", "handbook_revision", "default_language", "direction", "theme")}

    def local_file(raw: object) -> bool:
        if not isinstance(raw, str) or not raw:
            return False
        url = urlsplit(raw)
        if url.scheme or url.netloc or url.query or url.fragment:
            return False
        path = (sample / raw).resolve()
        return path.is_relative_to(ROOT / "evals") and path.is_file()

    for field in ("entry", "handbook", "brief", "foundations"):
        if not local_file(data.get(field)):
            errors.append(f"missing/out-of-scope artifact: {field}")
    primary = data.get("approval")
    if primary is not None and not approval_matches(primary, identity):
        errors.append("primary approval is not provenance/revision bound")
    dark = data.get("dark", {})
    if not isinstance(dark, dict):
        return errors + ["invalid dark record"]
    if dark.get("status") == "not-started":
        if any(dark.get(k) is not None for k in ("entry", "parent", "approval")):
            errors.append("unstarted dark has premature artifact/approval")
    elif dark.get("status") in ("proposed", "approved"):
        if not approval_matches(primary, identity) or dark.get("parent") != identity:
            errors.append("dark requires exact approved primary parent")
        if not local_file(dark.get("entry")):
            errors.append("dark artifact missing/out-of-scope")
        dark_identity = dark.get("identity")
        if (not isinstance(dark_identity, dict) or dark_identity.get("theme") != "dark"
                or dark_identity.get("default_language") != identity["default_language"]
                or dark_identity.get("direction") != identity["direction"]
                or not dark_identity.get("sample_revision") or not dark_identity.get("handbook_revision")):
            errors.append("invalid derived dark identity")
        if dark.get("status") == "approved" and not approval_matches(dark.get("approval"), dark_identity):
            errors.append("dark approval is not provenance/revision bound")
        if dark.get("status") == "proposed" and dark.get("approval") is not None:
            errors.append("proposed dark cannot carry approval")
    else:
        errors.append("unknown dark status")
    secondary = data.get("secondary", {})
    if not isinstance(secondary, dict):
        return errors + ["invalid secondary record"]
    if secondary.get("status") == "not-applicable":
        if not local_file(secondary.get("source")):
            errors.append("secondary N/A needs product source")
        if secondary.get("entry") is not None or secondary.get("authorization") is not None:
            errors.append("secondary N/A cannot have an artifact/authorization")
    elif secondary.get("status") == "proposed":
        if dark.get("status") != "approved" or not approval_matches(dark.get("approval"), dark.get("identity")):
            errors.append("secondary requires approved dark")
        if secondary.get("parent") != dark.get("identity"):
            errors.append("secondary parent is stale")
        authority = secondary.get("authorization")
        if (not isinstance(authority, dict) or not all(authority.get(k)
                for k in ("actor", "source", "scope", "date", "language", "direction", "need"))):
            errors.append("secondary needs named scope/need/authority")
        if not local_file(secondary.get("entry")):
            errors.append("secondary artifact missing/out-of-scope")
    else:
        errors.append("unknown secondary status")
    if local_file(data.get("handbook")):
        handbook = (sample / data["handbook"]).read_text(encoding="utf-8")
        if "Sample revision: " + str(data.get("sample_revision")) not in handbook:
            errors.append("sample and handbook sample revision disagree")
        if "Handbook revision: " + str(data.get("handbook_revision")) not in handbook:
            errors.append("sample and handbook revision disagree")
    return errors


if __name__ == "__main__":
    findings = validate_metadata(json.loads((SAMPLE / "sample.json").read_text(encoding="utf-8")))
    if findings:
        raise SystemExit("\n".join(findings))
    print("Authored Material sample metadata valid; approval remains a human evidence decision.")
