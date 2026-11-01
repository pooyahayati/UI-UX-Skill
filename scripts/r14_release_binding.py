"""Exact accepted R14 VERSION-only successor, never a fresh evaluation."""
import json
from pathlib import Path
from release_version_binding import content_digest, tree_digest, version_digest
from r14_evaluation import ACCEPTED

ROOT=Path(__file__).resolve().parents[1]
BEFORE="8067331adcf001b8a25a149572ed65996984d4d2a5dc57b7d65244541e5434c7"
RECORDS={**ACCEPTED,
 "evals/ui-foundations/r14-result.json":"dd1d78b0270b6ac0f70f7554ec25f09b360165b1c9a050ed0bb21c9820dbb21e",
 "evals/r14-source.json":"def8b6c1b0544e3447d8ed2d05c3560cc8e0216f4a8e985eeba5be13530610f4"}

def r14_release_predecessor(actual,binding=None,*,root=ROOT,result=None,record=None):
    if binding is None:
        binding=json.loads((root/"evals/r14-release-version.json").read_text(encoding="utf-8"))
    keys={"schema_version","scope","normalization","decision","recorded_version","release_version",
          "version_change","candidate_before_sha256","candidate_after_sha256","records","notes"}
    if (not isinstance(binding,dict) or set(binding)!=keys or binding.get("schema_version")!=1
        or binding.get("scope")!="r14-release-version-only" or binding.get("normalization")!="git-lf"
        or binding.get("decision")!="docs/releases/3.7.0.md#authority"
        or binding.get("recorded_version")!="3.6.1" or binding.get("release_version")!="3.7.0"
        or binding.get("candidate_before_sha256")!=BEFORE or binding.get("records")!=RECORDS
        or binding.get("version_change")!={"path":"VERSION","previous_sha256":version_digest("3.6.1"),"sha256":version_digest("3.7.0")}
        or not isinstance(binding.get("notes"),str) or not binding["notes"].strip()):
        raise ValueError("Invalid R14 release-only identity or scope")
    if not isinstance(actual,dict) or actual.get("VERSION")!=version_digest("3.7.0") or tree_digest(actual)!=binding["candidate_after_sha256"]:
        raise ValueError("R14 release source identity changed")
    previous={**actual,"VERSION":version_digest("3.6.1")}
    if tree_digest(previous)!=BEFORE:raise ValueError("R14 release changes more than VERSION")
    for name,expected in RECORDS.items():
        original=json.loads((root/name).read_text(encoding="utf-8"))
        if content_digest(original)!=expected:raise ValueError("Accepted R14 record changed: "+name)
    if result is not None or record is not None:
        if record!="evals/ui-foundations/r14-result.json" or content_digest(result)!=RECORDS[record]:
            raise ValueError("R14 release cannot qualify another or modified evaluation")
    return previous
