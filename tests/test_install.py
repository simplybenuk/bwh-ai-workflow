from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from install import HOST_HOMES, InstallError, install  # noqa: E402


def run(*args: str) -> None:
    subprocess.run(list(args), check=True, capture_output=True)


def commit(source: Path, message: str) -> str:
    run("git", "-C", str(source), "add", ".")
    run("git", "-C", str(source), "-c", "user.name=Test", "-c", "user.email=test@example.com", "commit", "-qm", message)
    return subprocess.check_output(["git", "-C", str(source), "rev-parse", "HEAD"], text=True).strip()


def fixture_catalog() -> dict:
    return {
        "schema_version": 1,
        "toolkit": {"identifier": "bwh-ai-workflow", "display_name": "BWH Agent Toolkit", "version": "0.2.0"},
        "hosts": {
            "codex": {"validation_status": "pending"},
            "claude-code": {"validation_status": "pending"},
            "cursor": {"validation_status": "pending"},
        },
        "profiles": {
            "workflow": ["bwh-one"],
            "engineering": ["bwh-two"],
            "authoring": [],
            "full": ["bwh-one", "bwh-two"],
        },
        "skills": [
            {"name": "bwh-one", "directory": "skills/bwh-one", "status": "active", "profiles": ["workflow"], "dependencies": [], "shared_contracts": True, "origin": "core"},
            {"name": "bwh-two", "directory": "skills/bwh-two", "status": "active", "profiles": ["engineering"], "dependencies": [], "shared_contracts": False, "origin": "core"},
        ],
    }


def make_source(path: Path) -> str:
    (path / "skills/bwh-one/references").mkdir(parents=True)
    (path / "skills/bwh-one/scripts").mkdir()
    (path / "skills/bwh-two").mkdir(parents=True)
    (path / "contracts").mkdir()
    (path / "skills/bwh-one/SKILL.md").write_text(
        "---\nname: bwh-one\ndescription: One.\n---\n\nRead [details](references/details.md) and [the contract](../../contracts/base.md).\n",
        encoding="utf-8",
    )
    (path / "skills/bwh-one/references/details.md").write_text("Details.\n", encoding="utf-8")
    helper = path / "skills/bwh-one/scripts/run.sh"
    helper.write_text("#!/bin/sh\nprintf executable\n", encoding="utf-8")
    helper.chmod(0o755)
    (path / "skills/bwh-two/SKILL.md").write_text("---\nname: bwh-two\ndescription: Two.\n---\n\nTwo.\n", encoding="utf-8")
    (path / "contracts/base.md").write_text("Base.\n", encoding="utf-8")
    (path / ".gitignore").write_text("*.ignored\n", encoding="utf-8")
    (path / "catalog.json").write_text(json.dumps(fixture_catalog()), encoding="utf-8")
    run("git", "init", "-q", str(path))
    return commit(path, "fixture")


class InstallTests(unittest.TestCase):
    def test_all_profiles_dry_run_for_each_host(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            make_source(source)
            for host in HOST_HOMES:
                for profile in ("workflow", "engineering", "authoring", "full"):
                    result = install(source, target, host, profile, dry_run=True)
                    self.assertEqual(result["profile"], profile)

    def test_fresh_install_preserves_unrelated_skill_and_writes_v2_lock(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            revision = make_source(source)
            unrelated = target / ".agents/skills/personal/SKILL.md"
            unrelated.parent.mkdir(parents=True)
            unrelated.write_text("personal\n", encoding="utf-8")
            install(source, target, "codex", "workflow")
            lock = json.loads((target / ".agents/bwh-ai-workflow.lock").read_text())
            self.assertEqual(lock["format_version"], 2)
            self.assertEqual(lock["revision"], revision)
            self.assertEqual(lock["source"], str(source.resolve()))
            self.assertEqual(lock["installed_skills"], ["bwh-one"])
            self.assertEqual(unrelated.read_text(), "personal\n")

    def test_tracked_executable_mode_is_preserved_and_helper_runs(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            make_source(source)
            install(source, target, "codex", "workflow")
            helper = target / ".agents/skills/bwh-one/scripts/run.sh"
            self.assertEqual(helper.stat().st_mode & 0o777, 0o755)
            output = subprocess.check_output([str(helper)], text=True)
            self.assertEqual(output, "executable")

    def test_local_modification_blocks_update_and_preserves_lock(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            make_source(source)
            install(source, target, "codex", "workflow")
            lock_path = target / ".agents/bwh-ai-workflow.lock"
            prior_lock = lock_path.read_bytes()
            skill = target / ".agents/skills/bwh-one/SKILL.md"
            skill.write_text("local edit\n", encoding="utf-8")
            with self.assertRaises(InstallError):
                install(source, target, "codex", "workflow")
            self.assertEqual(lock_path.read_bytes(), prior_lock)
            self.assertEqual(skill.read_text(), "local edit\n")

    def test_profile_change_prunes_only_unchanged_managed_files(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            make_source(source)
            install(source, target, "codex", "full")
            self.assertTrue((target / ".agents/skills/bwh-two/SKILL.md").is_file())
            install(source, target, "codex", "workflow")
            self.assertFalse((target / ".agents/skills/bwh-two/SKILL.md").exists())

    def test_version_one_lock_migrates_only_after_success(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            old_revision = make_source(source)
            target_skill = target / ".agents/skills/bwh-one/SKILL.md"
            target_skill.parent.mkdir(parents=True)
            target_skill.write_bytes((source / "skills/bwh-one/SKILL.md").read_bytes())
            target_reference = target / ".agents/skills/bwh-one/references/details.md"
            target_reference.parent.mkdir(parents=True)
            target_reference.write_bytes((source / "skills/bwh-one/references/details.md").read_bytes())
            target_contract = target / ".agents/contracts/base.md"
            target_contract.parent.mkdir(parents=True)
            target_contract.write_bytes((source / "contracts/base.md").read_bytes())
            lock_path = target / ".agents/bwh-ai-workflow.lock"
            lock_path.write_text(f"source: fixture\nrevision: {old_revision}\ninstalled_at: old\nhost: codex\ninstalled_paths: .agents/skills/bwh-*, .agents/contracts/\n", encoding="utf-8")
            (source / "skills/bwh-one/SKILL.md").write_text("---\nname: bwh-one\ndescription: One.\n---\n\nNew.\n", encoding="utf-8")
            commit(source, "new")
            install(source, target, "codex", "workflow")
            self.assertEqual(json.loads(lock_path.read_text())["format_version"], 2)
            self.assertIn("New.", target_skill.read_text())

    def test_failed_installed_validation_restores_files_and_old_lock(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            make_source(source)
            install(source, target, "codex", "workflow")
            lock_path = target / ".agents/bwh-ai-workflow.lock"
            skill_path = target / ".agents/skills/bwh-one/SKILL.md"
            prior_lock, prior_skill = lock_path.read_bytes(), skill_path.read_bytes()
            with patch("install.validate_installed", side_effect=InstallError("fixture validation failure")):
                with self.assertRaisesRegex(InstallError, "fixture validation failure"):
                    install(source, target, "codex", "full")
            self.assertEqual(lock_path.read_bytes(), prior_lock)
            self.assertEqual(skill_path.read_bytes(), prior_skill)
            self.assertFalse((target / ".agents/skills/bwh-two/SKILL.md").exists())

    def test_dirty_source_is_rejected_without_writing_a_lock(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            make_source(source)
            (source / "contracts/base.md").write_text("dirty\n", encoding="utf-8")
            with self.assertRaisesRegex(InstallError, "uncommitted changes"):
                install(source, target, "codex", "workflow")
            self.assertFalse((target / ".agents/bwh-ai-workflow.lock").exists())

    def test_escape_path_in_v2_lock_is_rejected_without_target_writes(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            make_source(source)
            install(source, target, "codex", "workflow")
            lock_path = target / ".agents/bwh-ai-workflow.lock"
            lock = json.loads(lock_path.read_text())
            lock["managed_files"][".agents/skills/../../outside.txt"] = "0" * 64
            lock_path.write_text(json.dumps(lock), encoding="utf-8")
            malicious_lock = lock_path.read_bytes()
            outside = target / "outside.txt"
            outside.write_text("keep\n", encoding="utf-8")
            with self.assertRaisesRegex(InstallError, "normalized|unsafe"):
                install(source, target, "codex", "workflow")
            self.assertEqual(outside.read_text(), "keep\n")
            self.assertEqual(lock_path.read_bytes(), malicious_lock)

    def test_invalid_v2_lock_fields_digests_and_host_are_rejected(self) -> None:
        mutations = {
            "missing": lambda lock: lock.pop("source"),
            "unknown": lambda lock: lock.__setitem__("surprise", True),
            "digest": lambda lock: lock["managed_files"].__setitem__(next(iter(lock["managed_files"])), "bad"),
            "host": lambda lock: lock.__setitem__("host", "cursor"),
            "wrong-home": lambda lock: lock["managed_files"].__setitem__(".claude/contracts/base.md", "0" * 64),
        }
        for label, mutate in mutations.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
                source, target = Path(source_directory), Path(target_directory)
                make_source(source)
                install(source, target, "codex", "workflow")
                lock_path = target / ".agents/bwh-ai-workflow.lock"
                lock = json.loads(lock_path.read_text())
                mutate(lock)
                lock_path.write_text(json.dumps(lock), encoding="utf-8")
                prior = lock_path.read_bytes()
                with self.assertRaises(InstallError):
                    install(source, target, "codex", "workflow")
                self.assertEqual(lock_path.read_bytes(), prior)

    def test_install_reads_only_tracked_blobs_and_ignores_ignored_files(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            revision = make_source(source)
            ignored = source / "skills/bwh-one/secret.ignored"
            ignored.write_text("not installed\n", encoding="utf-8")
            install(source, target, "codex", "workflow")
            installed = target / ".agents/skills/bwh-one/SKILL.md"
            expected = subprocess.check_output(["git", "-C", str(source), "show", f"{revision}:skills/bwh-one/SKILL.md"])
            self.assertEqual(installed.read_bytes(), expected)
            self.assertFalse((target / ".agents/skills/bwh-one/secret.ignored").exists())

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks unavailable")
    def test_tracked_symlink_is_rejected_without_following_target(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            make_source(source)
            outside = source.parent / f"{source.name}-outside.txt"
            outside.write_text("outside\n", encoding="utf-8")
            try:
                os.symlink(outside, source / "skills/bwh-one/references/external.md")
                commit(source, "symlink")
                with self.assertRaisesRegex(InstallError, "symlink"):
                    install(source, target, "codex", "workflow")
                self.assertFalse((target / ".agents/bwh-ai-workflow.lock").exists())
                self.assertFalse((target / ".agents/skills/bwh-one/references/external.md").exists())
            finally:
                outside.unlink(missing_ok=True)

    def test_remote_origin_is_recorded_instead_of_temporary_clone_path(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            make_source(source)
            run("git", "-C", str(source), "remote", "add", "origin", "https://example.com/bwh-ai-workflow.git")
            install(source, target, "codex", "workflow")
            lock = json.loads((target / ".agents/bwh-ai-workflow.lock").read_text())
            self.assertEqual(lock["source"], "https://example.com/bwh-ai-workflow.git")

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks unavailable")
    def test_managed_file_staging_symlink_cannot_write_outside_or_change_install(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            make_source(source)
            install(source, target, "codex", "workflow")
            lock_path = target / ".agents/bwh-ai-workflow.lock"
            skill_path = target / ".agents/skills/bwh-one/SKILL.md"
            prior_lock, prior_skill = lock_path.read_bytes(), skill_path.read_bytes()
            outside = target / "outside.txt"
            outside.write_text("keep\n", encoding="utf-8")
            os.symlink(outside, skill_path.with_name(".SKILL.md.bwh-new"))
            skill = source / "skills/bwh-one/SKILL.md"
            skill.write_text(skill.read_text() + "\nChanged.\n", encoding="utf-8")
            commit(source, "changed")
            with self.assertRaisesRegex(InstallError, "staging path already exists"):
                install(source, target, "codex", "workflow")
            self.assertEqual(outside.read_text(), "keep\n")
            self.assertEqual(skill_path.read_bytes(), prior_skill)
            self.assertEqual(lock_path.read_bytes(), prior_lock)

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks unavailable")
    def test_lock_staging_symlink_cannot_write_outside_or_change_install(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            make_source(source)
            install(source, target, "codex", "workflow")
            lock_path = target / ".agents/bwh-ai-workflow.lock"
            skill_path = target / ".agents/skills/bwh-one/SKILL.md"
            prior_lock, prior_skill = lock_path.read_bytes(), skill_path.read_bytes()
            outside = target / "outside.txt"
            outside.write_text("keep\n", encoding="utf-8")
            os.symlink(outside, lock_path.with_name(".bwh-ai-workflow.lock.new"))
            with self.assertRaisesRegex(InstallError, "staging path already exists"):
                install(source, target, "codex", "workflow")
            self.assertEqual(outside.read_text(), "keep\n")
            self.assertEqual(skill_path.read_bytes(), prior_skill)
            self.assertEqual(lock_path.read_bytes(), prior_lock)

    def test_v2_lock_can_prune_skill_removed_from_new_catalog(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            make_source(source)
            install(source, target, "codex", "full")
            catalog = json.loads((source / "catalog.json").read_text())
            catalog["skills"] = [skill for skill in catalog["skills"] if skill["name"] != "bwh-two"]
            catalog["profiles"]["engineering"] = []
            catalog["profiles"]["full"] = ["bwh-one"]
            (source / "catalog.json").write_text(json.dumps(catalog), encoding="utf-8")
            (source / "skills/bwh-two/SKILL.md").unlink()
            (source / "skills/bwh-two").rmdir()
            commit(source, "remove two")
            install(source, target, "codex", "workflow")
            self.assertFalse((target / ".agents/skills/bwh-two/SKILL.md").exists())

    def test_v2_lock_preserves_locally_edited_skill_removed_from_new_catalog(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            make_source(source)
            install(source, target, "codex", "full")
            lock_path = target / ".agents/bwh-ai-workflow.lock"
            prior_lock = lock_path.read_bytes()
            installed = target / ".agents/skills/bwh-two/SKILL.md"
            installed.write_text("local edit\n", encoding="utf-8")
            catalog = json.loads((source / "catalog.json").read_text())
            catalog["skills"] = [skill for skill in catalog["skills"] if skill["name"] != "bwh-two"]
            catalog["profiles"]["engineering"] = []
            catalog["profiles"]["full"] = ["bwh-one"]
            (source / "catalog.json").write_text(json.dumps(catalog), encoding="utf-8")
            (source / "skills/bwh-two/SKILL.md").unlink()
            (source / "skills/bwh-two").rmdir()
            commit(source, "remove two")
            with self.assertRaisesRegex(InstallError, "locally modified managed file excluded"):
                install(source, target, "codex", "workflow")
            self.assertEqual(installed.read_text(), "local edit\n")
            self.assertEqual(lock_path.read_bytes(), prior_lock)

    def test_v1_tag_conflict_leaves_original_lock_untouched(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            old_revision = make_source(source)
            run("git", "-C", str(source), "tag", "v0.1.0", old_revision)
            target_skill = target / ".agents/skills/bwh-one/SKILL.md"
            target_skill.parent.mkdir(parents=True)
            target_skill.write_bytes((source / "skills/bwh-one/SKILL.md").read_bytes())
            target_reference = target / ".agents/skills/bwh-one/references/details.md"
            target_reference.parent.mkdir(parents=True)
            target_reference.write_bytes((source / "skills/bwh-one/references/details.md").read_bytes())
            target_contract = target / ".agents/contracts/base.md"
            target_contract.parent.mkdir(parents=True)
            target_contract.write_bytes((source / "contracts/base.md").read_bytes())
            lock_path = target / ".agents/bwh-ai-workflow.lock"
            lock_path.write_text("source: fixture\nrevision: v0.1.0\ninstalled_at: old\nhost: codex\ninstalled_paths: .agents/skills/bwh-*, .agents/contracts/\n", encoding="utf-8")
            prior_lock = lock_path.read_bytes()
            target_skill.write_text("local edit\n", encoding="utf-8")
            with self.assertRaisesRegex(InstallError, "locally modified"):
                install(source, target, "codex", "workflow")
            self.assertEqual(lock_path.read_bytes(), prior_lock)

    def test_v1_migration_prunes_removed_skill_proven_at_recorded_revision(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            old_revision = make_source(source)
            for name in ("bwh-one", "bwh-two"):
                source_root = source / "skills" / name
                target_root = target / ".agents/skills" / name
                for source_file in source_root.rglob("*"):
                    if source_file.is_file():
                        target_file = target_root / source_file.relative_to(source_root)
                        target_file.parent.mkdir(parents=True, exist_ok=True)
                        target_file.write_bytes(source_file.read_bytes())
            target_contract = target / ".agents/contracts/base.md"
            target_contract.parent.mkdir(parents=True)
            target_contract.write_bytes((source / "contracts/base.md").read_bytes())
            lock_path = target / ".agents/bwh-ai-workflow.lock"
            lock_path.write_text(f"source: fixture\nrevision: {old_revision}\ninstalled_at: old\nhost: codex\ninstalled_paths: .agents/skills/bwh-*, .agents/contracts/\n", encoding="utf-8")
            catalog = json.loads((source / "catalog.json").read_text())
            catalog["skills"] = [skill for skill in catalog["skills"] if skill["name"] != "bwh-two"]
            catalog["profiles"]["engineering"] = []
            catalog["profiles"]["full"] = ["bwh-one"]
            (source / "catalog.json").write_text(json.dumps(catalog), encoding="utf-8")
            (source / "skills/bwh-two/SKILL.md").unlink()
            (source / "skills/bwh-two").rmdir()
            commit(source, "remove two")
            install(source, target, "codex", "workflow")
            self.assertFalse((target / ".agents/skills/bwh-two/SKILL.md").exists())
            self.assertEqual(json.loads(lock_path.read_text())["format_version"], 2)

    def test_frontmatter_name_mismatch_rolls_back_without_lock(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            make_source(source)
            skill = source / "skills/bwh-one/SKILL.md"
            skill.write_text(skill.read_text().replace("name: bwh-one", "name: wrong"), encoding="utf-8")
            commit(source, "wrong name")
            with self.assertRaisesRegex(InstallError, "does not match"):
                install(source, target, "codex", "workflow")
            self.assertFalse((target / ".agents/bwh-ai-workflow.lock").exists())

    def test_missing_relative_markdown_reference_rolls_back_without_lock(self) -> None:
        with tempfile.TemporaryDirectory() as source_directory, tempfile.TemporaryDirectory() as target_directory:
            source, target = Path(source_directory), Path(target_directory)
            make_source(source)
            skill = source / "skills/bwh-one/SKILL.md"
            skill.write_text(skill.read_text() + "\n[Missing](references/missing.md)\n", encoding="utf-8")
            commit(source, "missing reference")
            with self.assertRaisesRegex(InstallError, "unresolved.*Markdown reference"):
                install(source, target, "codex", "workflow")
            self.assertFalse((target / ".agents/bwh-ai-workflow.lock").exists())


if __name__ == "__main__":
    unittest.main()
