from __future__ import annotations

import copy
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_catalog import load_catalog, validate_catalog  # noqa: E402


class CatalogTests(unittest.TestCase):
    def setUp(self) -> None:
        self.catalog = load_catalog(ROOT / "catalog.json")

    def errors(self, mutate) -> list[str]:
        catalog = copy.deepcopy(self.catalog)
        mutate(catalog)
        return validate_catalog(catalog, ROOT, check_paths=False)

    def test_repository_catalog_is_valid(self) -> None:
        self.assertEqual(validate_catalog(self.catalog, ROOT), [])

    def test_non_object_catalog_and_skill_entries_are_rejected(self) -> None:
        self.assertIn("catalog root must be an object", validate_catalog([], ROOT))
        errors = self.errors(lambda value: value["skills"].append("not-an-object"))
        self.assertTrue(any("must be an object" in error for error in errors))

    def test_every_skill_field_is_required(self) -> None:
        for field in ("name", "directory", "status", "profiles", "dependencies", "shared_contracts", "origin"):
            with self.subTest(field=field):
                errors = self.errors(lambda value, field=field: value["skills"][0].pop(field))
                self.assertTrue(any("missing required fields" in error and field in error for error in errors))

    def test_hosts_require_known_object_entries_and_statuses(self) -> None:
        errors = self.errors(lambda value: value["hosts"].__setitem__("codex", "pending"))
        self.assertTrue(any("metadata must be an object" in error for error in errors))
        errors = self.errors(lambda value: value["hosts"]["cursor"].__setitem__("validation_status", "maybe"))
        self.assertTrue(any("invalid validation metadata" in error for error in errors))
        errors = self.errors(lambda value: value["hosts"].pop("claude-code"))
        self.assertTrue(any("must define exactly" in error for error in errors))

    def test_duplicate_names_are_rejected(self) -> None:
        errors = self.errors(lambda value: value["skills"].append(copy.deepcopy(value["skills"][0])))
        self.assertTrue(any("duplicate skill names" in error for error in errors))

    def test_missing_path_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            errors = validate_catalog(self.catalog, Path(directory))
        self.assertTrue(any("missing" in error for error in errors))

    def test_unknown_dependency_is_rejected(self) -> None:
        errors = self.errors(lambda value: value["skills"][0]["dependencies"].append("bwh-unknown"))
        self.assertTrue(any("unknown dependencies" in error for error in errors))

    def test_dependency_cycle_is_rejected(self) -> None:
        def mutate(value):
            value["skills"][0]["dependencies"] = [value["skills"][1]["name"]]
            value["skills"][1]["dependencies"] = [value["skills"][0]["name"]]
        self.assertTrue(any("dependency cycle" in error for error in self.errors(mutate)))

    def test_invalid_profile_membership_is_rejected(self) -> None:
        errors = self.errors(lambda value: value["profiles"]["workflow"].append("bwh-unknown"))
        self.assertTrue(any("unknown skills" in error for error in errors))

    def test_derived_origin_requires_complete_provenance(self) -> None:
        def remove(value):
            value["skills"][8].pop("provenance")
        self.assertTrue(any("derived skills require provenance" in error for error in self.errors(remove)))
        def incomplete(value):
            value["skills"][8]["provenance"].pop("license")
        self.assertTrue(any("incomplete provenance" in error for error in self.errors(incomplete)))


if __name__ == "__main__":
    unittest.main()
