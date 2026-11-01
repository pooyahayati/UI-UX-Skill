"""Exact R14 source succession and narrowly retained R13 VERSION compatibility."""
import json
from behavior_evaluation import ROOT, canonical, digest, snapshot, tree_digest
from release_version_binding import content_digest, version_digest

PARENT = "e35cec2a8c25de1fd56800efb7f95bb724685abab1d9794519710b7e2a555f8c"
CRITIQUE = {"references/existing-product-audit.md", "references/visual-regression.md"}
ICONS = {"references/implementation-strategies.md", "references/interactive-motion.md"}
PARENTS = {"evals/r13-source.json", "evals/r13-release-version.json",
           "evals/ui-foundations/r13-result.json", "evals/wordpress-settings/r13-stage4-behavior.json"}
PARENT_RECORDS = {
    "evals/r13-release-version.json": "dd7a125c4785dd10eeebf6b80a4522c27b0aa5b2eb85269f9852cca3affccf4e",
    "evals/r13-source.json": "a45f100a58879c984faa9ecaf3056b115976532ac383c5299a19e66635a4e9dd",
    "evals/ui-foundations/r13-result.json": "b74915fae9fcecf80e5aca2657a49e1e565812f89e42f92a2470f469abcaee38",
    "evals/wordpress-settings/r13-stage4-behavior.json": "ea546eb8f1168355fdebf6a97aaaea60622bc8ce4d5b043d0679048db48e5d06",
}


def r14_predecessor(actual=None, binding=None, *, root=ROOT):
    """Verify the entire descendant and expose the exact released 3.6.1 tree."""
    if actual is None:
        actual = snapshot(root / "skills/ui-ux-skill")
    if actual.get("VERSION") == version_digest("3.7.0"):
        from r14_release_binding import r14_release_predecessor
        actual = r14_release_predecessor(actual, root=root)
    if binding is None:
        binding = json.loads((root / "evals/r14-source.json").read_text(encoding="utf-8"))
    original = json.loads((root / "evals/ui-foundations/r13-result.json").read_text(encoding="utf-8"))
    released = {**original["candidate"]["files"], "VERSION": version_digest("3.6.1")}
    parents = {name: digest(canonical(root / name)) for name in PARENTS}
    allowed = CRITIQUE if binding.get("stage") == "R14.2" else CRITIQUE | ICONS if binding.get("stage") == "R14.3" else set()
    if (binding.get("schema_version") != 1 or binding.get("normalization") != "git-lf"
            or binding.get("decision") != "docs/R14_EXECUTION.md#authority"
            or binding.get("parents") != PARENT_RECORDS or parents != PARENT_RECORDS or tree_digest(released) != PARENT
            or binding.get("parent_sha256") != PARENT or not allowed
            or set(binding.get("changes", {})) != allowed):
        raise ValueError("R14 source scope or exact released parent changed")
    expected = dict(released)
    for name, change in binding["changes"].items():
        if change.get("previous_sha256") != released[name] or change.get("sha256") == released[name]:
            raise ValueError("R14 change does not bind its actual parent: " + name)
        expected[name] = change.get("sha256")
    if actual != expected or binding.get("candidate_sha256") != tree_digest(actual):
        raise ValueError("R14 current source identity changed or exceeds scoped corrections")
    return released


def retained_r13_version_case(result, case, root=ROOT):
    """Only exact retained R13 rows may cross their original VERSION-only bump."""
    name = "evals/ui-foundations/r13-result.json"
    original = json.loads((root / name).read_text(encoding="utf-8"))
    from r13_release_binding import ACCEPTED_RECORDS, r13_release_predecessor
    if content_digest(original) != ACCEPTED_RECORDS[name]:
        return False
    if result.get("retainedR13VersionOnly") != {"record": name, "sha256": digest(canonical(root / name))}:
        return False
    released = {**original["candidate"]["files"], "VERSION": version_digest("3.6.1")}
    r13_release_predecessor(released, root=root)
    return any(case == row for row in original["cases"])
