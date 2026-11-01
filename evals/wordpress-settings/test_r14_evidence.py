"""Legacy viewport evidence must fail closed without rewriting historical reports."""
import copy
import unittest

from test_contracts import R12_REGRESSION_IDS, r12_runtime_errors
from test_r13_evidence import read


class LegacyViewportEvidence(unittest.TestCase):
    def reports(self):
        for name in ("evidence/r12-regression-results.json",
                     "evidence/r13/regression/r13-regression-results.json"):
            yield read(name)

    def check(self, report):
        return r12_runtime_errors(report, report["behavior_hashes"], report["fixture_hashes"],
                                  report["runner_sha256"], R12_REGRESSION_IDS)

    def rejected(self, original, mutate, reason):
        report = copy.deepcopy(original)
        mutate(report)
        errors = self.check(report)
        self.assertTrue(any(reason in error for error in errors), errors)

    def test_existing_reports_pass_unchanged(self):
        for report in self.reports():
            self.assertEqual(self.check(report), [])
            self.assertNotIn("compatibility", report)

    def test_each_missing_or_wrong_viewport_is_rejected(self):
        for report in self.reports():
            views = [row for row in report["observations"] if row["id"].startswith("VIEW-")]
            self.rejected(report, lambda r: r.update(observations=[row for row in r["observations"]
                          if not row["id"].startswith("VIEW-")]), "observations")
            for view in views:
                with self.subTest(id=view["id"]):
                    self.rejected(report, lambda r: r["observations"].remove(view), "observations")
                    self.rejected(report, lambda r: next(row for row in r["observations"]
                                  if row["id"] == view["id"]).update(id="VIEW-unknown"), "observations")
                    self.rejected(report, lambda r: r["observations"].append(copy.deepcopy(view)), "observations")
            self.rejected(report, lambda r: r["observations"].append(
                {**views[0], "id": "VIEW-extra"}), "observations")

    def test_viewport_details_reject_malformed_and_contradictory_values(self):
        for report in self.reports():
            for row in report["observations"]:
                if not row["id"].startswith("VIEW-") or row["id"] == "VIEW-zoom-200":
                    continue
                def detail(r):
                    return next(item for item in r["observations"] if item["id"] == row["id"])
                for value in (None, {}, [], {"anything": True}):
                    self.rejected(report, lambda r: detail(r).update(detail=value), "viewport")
                for key, value in (("direction", "ltr"), ("overflow", True), ("overflow", 0),
                                   ("regular", False), ("regular", 1), ("bold", False),
                                   ("font", "Arial, sans-serif"), ("font", None), ("rendered_fonts", {})):
                    with self.subTest(id=row["id"], key=key, value=value):
                        self.rejected(report, lambda r: detail(r)["detail"].update({key: value}), "viewport")
                for key in row["detail"]:
                    self.rejected(report, lambda r: detail(r)["detail"].pop(key), "viewport")

    def test_rendered_font_records_require_actual_custom_glyphs(self):
        for report in self.reports():
            def fonts(r):
                return next(row for row in r["observations"] if row["id"] == "VIEW-multi-390")["detail"]["rendered_fonts"]
            for selector in ("#wps-root h1", "#wps-root label"):
                for value in (None, [], {}, [None], [{"familyName": "Arial", "isCustomFont": True, "glyphCount": 13}],
                              [{"familyName": "Vazirmatn", "isCustomFont": False, "glyphCount": 13}],
                              [{"familyName": "Vazirmatn", "isCustomFont": True, "glyphCount": 0}],
                              [{"familyName": "Vazirmatn", "isCustomFont": 1, "glyphCount": 13}]):
                    self.rejected(report, lambda r: fonts(r).update({selector: value}), "viewport")
                self.rejected(report, lambda r: fonts(r).pop(selector), "viewport")

    def test_zoom_has_its_own_geometry_and_limit_contract(self):
        for report in self.reports():
            def detail(r):
                return next(row for row in r["observations"] if row["id"] == "VIEW-zoom-200")["detail"]
            for key, value in (("zoom", "1"), ("zoom", 2), ("overflow", True), ("overflow", 0),
                               ("limitation", ""), ("limitation", "native browser certification")):
                self.rejected(report, lambda r: detail(r).update({key: value}), "viewport")
            for value in (None, True, "758", 0, -1, 781, 10 ** 1000, float("nan"), float("inf")):
                self.rejected(report, lambda r: detail(r).update(rootWidth=value), "viewport")
            for key in ("zoom", "overflow", "rootWidth", "limitation"):
                self.rejected(report, lambda r: detail(r).pop(key), "viewport")

    def test_other_producers_do_not_accept_stray_viewport_rows(self):
        from test_contracts import R12_DISCOVERY_IDS, R13_VALIDATION_IDS
        for name, ids in (("evidence/r13/discovery/r12-browser-results.json", R12_DISCOVERY_IDS),
                          ("evidence/r13/validation/r13-validation-results.json", R13_VALIDATION_IDS)):
            report = read(name)
            report["observations"].append({"id": "VIEW-extra", "status": "passed",
                                           "method": "real-admin-browser", "detail": {"bogus": True}})
            errors = r12_runtime_errors(report, report["behavior_hashes"], report["fixture_hashes"],
                                        report["runner_sha256"], ids)
            self.assertTrue(any("observations" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
