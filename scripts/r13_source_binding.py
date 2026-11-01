"""Bounded R13 source succession; historical acceptance is never current evidence."""
import json
from behavior_evaluation import ROOT, canonical, digest, snapshot, tree_digest
from release_version_binding import version_digest

ROUTING = {"references/products/wordpress-plugin.md", "references/products/wordpress/components.md"}
THEME = {"SKILL.md", "references/design-foundation-workflow.md", "references/design-handbook.md",
         "assets/templates/DESIGN.md", "references/material-foundations.md", "references/material-samples.md",
         "references/discovery-and-profile.md", "references/interactive-motion.md", "references/shadcn-ui.md",
         "references/material-design.md", "references/material-components.md"}


def r13_predecessor(actual=None, binding=None):
    """Verify every current file, then expose the exact released historical view."""
    if actual is None: actual = snapshot(ROOT / "skills/ui-ux-skill")
    if actual.get("VERSION") == version_digest("3.7.0"):
        from r14_source_binding import r14_predecessor
        actual = r14_predecessor(actual)
    if actual.get("VERSION") == version_digest("3.6.1"):
        from r13_release_binding import r13_release_predecessor
        actual = r13_release_predecessor(actual)
    if binding is None: binding = json.loads((ROOT / "evals/r13-source.json").read_text(encoding="utf-8"))
    original = json.loads((ROOT / "evals/wordpress-settings/r12-behavior-results.json").read_text(encoding="utf-8"))
    released = {**original["candidate"]["files"], "VERSION": version_digest("3.6.0")}
    parents = {name: digest(canonical(ROOT / name)) for name in
               ("evals/r12-release-version.json", "evals/ui-foundations/r12-result.json", "evals/wordpress-settings/r12-behavior-results.json")}
    allowed = ROUTING if binding.get("stage") == "R13.3" else ROUTING | THEME if binding.get("stage") == "R13.4" else set()
    if (binding.get("schema_version") != 1 or binding.get("decision") != "docs/R13_EXECUTION.md#authority"
            or binding.get("normalization") != "git-lf" or binding.get("parents") != parents
            or binding.get("parent_sha256") != tree_digest(released)
            or binding.get("parent_sha256") != "971eef071c2a05e5554dc98f1fb4eaee5fc54b2cf50f837a36b0402a1de033cd"
            or not allowed or set(binding.get("changes", {})) != allowed):
        raise ValueError("R13 source scope or exact historical parent changed")
    expected = dict(released)
    for name, change in binding["changes"].items():
        if change.get("previous_sha256") != released[name] or change.get("sha256") == released[name]:
            raise ValueError("R13 source change does not bind its parent: " + name)
        expected[name] = change.get("sha256")
    if actual != expected or binding.get("candidate_sha256") != tree_digest(actual):
        raise ValueError("R13 current source identity changed or exceeds correction scope")
    return released


def retained_r12_version_case(result, case, root=ROOT):
    """Only an exact retained R12 row may reuse its already accepted VERSION bridge."""
    source = root / "evals/ui-foundations/r12-result.json"
    link = result.get("retainedR12VersionOnly")
    if not isinstance(link, dict) or link != {"record": "evals/ui-foundations/r12-result.json", "sha256": digest(canonical(source))}:
        return False
    original = json.loads(source.read_text(encoding="utf-8"))
    from release_version_binding import content_digest
    release = json.loads((root / "evals/r12-release-version.json").read_text(encoding="utf-8"))
    if release["records"][link["record"]] != content_digest(original): return False
    return (result.get("candidate") == original["candidate"] and result.get("skillVersion") == "3.6.0"
            and any(case == row for row in original["cases"]))
