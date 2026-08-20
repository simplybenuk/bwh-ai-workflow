from __future__ import annotations

import copy
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_skills import validate_skills  # noqa: E402


def catalog() -> dict:
    return {
        "schema_version": 1,
        "toolkit": {"identifier": "bwh-ai-workflow", "display_name": "BWH Agent Toolkit", "version": "0.2.0"},
        "hosts": {
            "codex": {"validation_status": "pending"},
            "claude-code": {"validation_status": "pending"},
            "cursor": {"validation_status": "pending"},
        },
        "profiles": {"workflow": ["bwh-one"], "engineering": [], "authoring": [], "full": ["bwh-one"]},
        "skills": [
            {"name": "bwh-one", "directory": "skills/bwh-one", "status": "active", "profiles": ["workflow"], "dependencies": [], "shared_contracts": False, "origin": "core"}
        ],
    }


def write_fixture(root: Path) -> dict:
    skill = root / "skills/bwh-one"
    (skill / "references").mkdir(parents=True)
    (skill / "scripts").mkdir()
    (skill / "SKILL.md").write_text(
        "---\nname: bwh-one\ndescription: One.\n---\n\nRead [details](references/details.md). Lock: `<agent-home>/bwh-ai-workflow.lock`.\n",
        encoding="utf-8",
    )
    (skill / "references/details.md").write_text("Details.\n", encoding="utf-8")
    helper = skill / "scripts/check.sh"
    helper.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
    helper.chmod(0o755)
    return catalog()


class SkillValidationTests(unittest.TestCase):
    def test_valid_portable_skill_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(validate_skills(root, write_fixture(root)), [])

    def test_name_link_and_leakage_failures_are_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture = write_fixture(root)
            skill = root / "skills/bwh-one/SKILL.md"
            skill.write_text(
                "---\nname: wrong\ndescription: One.\n---\n\nUse Cursor at [.cursor](references/missing.md). Run /bwh-test.\n",
                encoding="utf-8",
            )
            errors = validate_skills(root, fixture)
            self.assertTrue(any("names must match" in error for error in errors))
            self.assertTrue(any("unresolved" in error for error in errors))
            self.assertTrue(any("agent vendor leakage" in error for error in errors))
            self.assertTrue(any("host home leakage" in error for error in errors))
            self.assertTrue(any("host invocation leakage" in error for error in errors))

    def test_helper_requires_shebang_and_execute_permission(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture = write_fixture(root)
            helper = root / "skills/bwh-one/scripts/check.sh"
            helper.write_text("exit 0\n", encoding="utf-8")
            helper.chmod(0o644)
            errors = validate_skills(root, fixture)
            self.assertTrue(any("shebang" in error for error in errors))
            self.assertTrue(any("not marked executable" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
