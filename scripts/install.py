#!/usr/bin/env python3
"""Install a catalog profile into a project without overwriting local edits."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import posixpath
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

from validate_catalog import load_catalog, validate_catalog


HOST_HOMES = {"codex": ".agents", "claude-code": ".claude", "cursor": ".cursor"}
LOCK_NAME = "bwh-ai-workflow.lock"
LOCK_FIELDS = {
    "format_version", "package_id", "source", "revision", "installed_at", "host",
    "install_scope", "profile", "installed_skills", "installed_contracts",
    "catalog_schema_version", "managed_files",
}
SHA256_PATTERN = re.compile(r"[0-9a-f]{64}")
COMMIT_PATTERN = re.compile(r"[0-9a-f]{40}")
SKILL_NAME_PATTERN = re.compile(r"bwh-[a-z0-9]+(?:-[a-z0-9]+)*")
MARKDOWN_LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


class InstallError(RuntimeError):
    pass


def run_git(root: Path, *args: str, text: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        capture_output=True,
        text=text,
    )


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_digest(path: Path) -> str:
    return digest(path.read_bytes())


def source_revision(root: Path) -> str:
    status = run_git(root, "status", "--porcelain", "--untracked-files=all", text=True)
    if status.returncode != 0:
        raise InstallError("source must be a Git checkout at a pinned revision")
    if status.stdout:
        raise InstallError("source checkout has uncommitted changes; install from a clean pinned revision")
    result = run_git(root, "rev-parse", "--verify", "HEAD", text=True)
    revision = result.stdout.strip()
    if result.returncode != 0 or not COMMIT_PATTERN.fullmatch(revision):
        raise InstallError("source checkout has no pinned commit")
    return revision


def source_identity(root: Path) -> str:
    result = run_git(root, "config", "--get", "remote.origin.url", text=True)
    origin = result.stdout.strip()
    return origin if result.returncode == 0 and origin else str(root.resolve())


def parse_v1_lock(text: str) -> dict:
    values: dict[str, str] = {}
    for line in text.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip()
    if not values.get("source") or not values.get("revision"):
        raise InstallError("version 1 lock is missing source or revision")
    return {"format_version": 1, **values}


def normalized_managed_path(value: object, agent_home: str, kinds: set[str], label: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value:
        raise InstallError(f"{label} must be a non-empty relative POSIX path")
    path = PurePosixPath(value)
    if path.is_absolute() or str(path) != value or posixpath.normpath(value) != value:
        raise InstallError(f"{label} is not a normalized relative POSIX path: {value!r}")
    if any(part in {"", ".", ".."} for part in path.parts):
        raise InstallError(f"{label} contains an unsafe segment: {value!r}")
    home_parts = PurePosixPath(agent_home).parts
    if path.parts[: len(home_parts)] != home_parts or len(path.parts) <= len(home_parts):
        raise InstallError(f"{label} is outside {agent_home}: {value!r}")
    if path.parts[len(home_parts)] not in kinds:
        raise InstallError(f"{label} is outside the allowed managed directories: {value!r}")
    return value


def validate_v2_lock(lock: object, expected_host: str, agent_home: str, catalog: dict) -> dict:
    if not isinstance(lock, dict):
        raise InstallError("version 2 lock must be a JSON object")
    missing = sorted(LOCK_FIELDS - set(lock))
    unknown = sorted(set(lock) - LOCK_FIELDS)
    if missing:
        raise InstallError("version 2 lock is missing fields: " + ", ".join(missing))
    if unknown:
        raise InstallError("version 2 lock has unknown fields: " + ", ".join(unknown))
    if lock["format_version"] != 2 or lock["package_id"] != "bwh-ai-workflow":
        raise InstallError("version 2 lock has an invalid format or package identifier")
    for field in ("source", "installed_at"):
        if not isinstance(lock[field], str) or not lock[field]:
            raise InstallError(f"version 2 lock field {field} must be a non-empty string")
    if not isinstance(lock["revision"], str) or not COMMIT_PATTERN.fullmatch(lock["revision"]):
        raise InstallError("version 2 lock revision must be a full Git commit SHA")
    if lock["host"] != expected_host:
        raise InstallError(f"version 2 lock host {lock['host']!r} does not match {expected_host!r}")
    if lock["install_scope"] != "project":
        raise InstallError("version 2 lock install_scope must be project")
    if lock["profile"] not in catalog["profiles"]:
        raise InstallError(f"version 2 lock has unknown profile {lock['profile']!r}")
    if not isinstance(lock["catalog_schema_version"], int) or lock["catalog_schema_version"] < 1:
        raise InstallError("version 2 lock catalog_schema_version must be a positive integer")

    installed_skills = lock["installed_skills"]
    if (
        not isinstance(installed_skills, list)
        or any(not isinstance(name, str) or not SKILL_NAME_PATTERN.fullmatch(name) for name in installed_skills)
        or len(set(installed_skills)) != len(installed_skills)
    ):
        raise InstallError("version 2 lock installed_skills must contain unique valid BWH skill names")
    contracts = lock["installed_contracts"]
    if not isinstance(contracts, list) or any(not isinstance(path, str) for path in contracts) or len(set(contracts)) != len(contracts):
        raise InstallError("version 2 lock installed_contracts must be a unique path array")
    for path in contracts:
        normalized_managed_path(path, agent_home, {"contracts"}, "installed contract path")

    managed = lock["managed_files"]
    if not isinstance(managed, dict):
        raise InstallError("version 2 lock managed_files must be an object")
    for path, recorded_digest in managed.items():
        normalized_managed_path(path, agent_home, {"skills", "contracts"}, "managed file path")
        if not isinstance(recorded_digest, str) or not SHA256_PATTERN.fullmatch(recorded_digest):
            raise InstallError(f"version 2 lock has an invalid digest for {path!r}")
        relative = PurePosixPath(path).relative_to(PurePosixPath(agent_home))
        if relative.parts[0] == "skills" and (len(relative.parts) < 3 or relative.parts[1] not in installed_skills):
            raise InstallError(f"managed skill path is not covered by installed_skills: {path!r}")
    if any(path not in managed for path in contracts):
        raise InstallError("every installed contract path must also appear in managed_files")
    return lock


def read_lock(path: Path, expected_host: str, agent_home: str, catalog: dict) -> dict | None:
    if not path.exists():
        return None
    if path.is_symlink():
        raise InstallError(f"lock path must not be a symlink: {path}")
    text = path.read_text(encoding="utf-8")
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        return parse_v1_lock(text)
    if not isinstance(value, dict) or value.get("format_version") != 2:
        version = value.get("format_version") if isinstance(value, dict) else None
        raise InstallError(f"unsupported lock format: {version!r}")
    return validate_v2_lock(value, expected_host, agent_home, catalog)


def resolve_skills(catalog: dict, profile: str) -> list[str]:
    profiles = catalog["profiles"]
    if profile not in profiles:
        raise InstallError(f"unknown profile {profile!r}; choose from {', '.join(sorted(profiles))}")
    by_name = {skill["name"]: skill for skill in catalog["skills"]}
    resolved: list[str] = []

    def add(name: str) -> None:
        for dependency in by_name[name]["dependencies"]:
            add(dependency)
        if name not in resolved:
            resolved.append(name)

    for name in profiles[profile]:
        add(name)
    return resolved


def git_tree_files(source: Path, revision: str, roots: list[str]) -> dict[str, tuple[bytes, int]]:
    result = run_git(source, "ls-tree", "-r", "-z", "--full-tree", revision, "--", *roots)
    if result.returncode != 0:
        raise InstallError("could not enumerate the pinned Git tree")
    files: dict[str, tuple[bytes, int]] = {}
    for entry in result.stdout.split(b"\0"):
        if not entry:
            continue
        metadata, raw_path = entry.split(b"\t", 1)
        mode, object_type, _object_id = metadata.decode("ascii").split(" ", 2)
        repository_path = raw_path.decode("utf-8")
        if object_type != "blob":
            raise InstallError(f"unsupported Git tree entry type for {repository_path}: {object_type}")
        if mode == "120000":
            raise InstallError(f"symlink entries are not supported in managed sources: {repository_path}")
        if mode not in {"100644", "100755"}:
            raise InstallError(f"unsupported Git file mode for {repository_path}: {mode}")
        blob = run_git(source, "show", f"{revision}:{repository_path}")
        if blob.returncode != 0:
            raise InstallError(f"could not read pinned Git blob: {repository_path}")
        files[repository_path] = (blob.stdout, 0o755 if mode == "100755" else 0o644)
    return files


def desired_files(source: Path, revision: str, agent_home: str, skills: list[str], catalog: dict) -> dict[str, tuple[bytes, int]]:
    by_name = {skill["name"]: skill for skill in catalog["skills"]}
    roots = [by_name[name]["directory"] for name in skills]
    if any(by_name[name]["shared_contracts"] for name in skills):
        roots.append("contracts")
    if not roots:
        return {}
    tree = git_tree_files(source, revision, roots)
    files: dict[str, tuple[bytes, int]] = {}
    for repository_path, payload in tree.items():
        path = PurePosixPath(repository_path)
        if path.parts[0] == "skills" and len(path.parts) >= 3 and path.parts[1] in skills:
            installed = PurePosixPath(agent_home, "skills", *path.parts[1:])
        elif path.parts[0] == "contracts" and len(path.parts) >= 2:
            installed = PurePosixPath(agent_home, *path.parts)
        else:
            raise InstallError(f"pinned Git tree returned an unexpected path: {repository_path}")
        relative = str(installed)
        normalized_managed_path(relative, agent_home, {"skills", "contracts"}, "source file path")
        files[relative] = payload
    for name in skills:
        required = f"{agent_home}/skills/{name}/SKILL.md"
        if required not in files:
            raise InstallError(f"pinned Git tree is missing {by_name[name]['directory']}/SKILL.md")
    return files


def resolve_recorded_revision(source: Path, revision: object) -> str:
    if not isinstance(revision, str) or not revision:
        raise InstallError("version 1 lock revision must be a commit SHA or tag")
    result = run_git(source, "rev-parse", "--verify", f"{revision}^{{commit}}", text=True)
    resolved = result.stdout.strip()
    if result.returncode != 0 or not COMMIT_PATTERN.fullmatch(resolved):
        raise InstallError(f"version 1 lock revision cannot be resolved: {revision!r}")
    return resolved


def old_blob_digest(source: Path, revision: str, installed_path: str, agent_home: str) -> str | None:
    normalized_managed_path(installed_path, agent_home, {"skills", "contracts"}, "legacy managed path")
    relative = PurePosixPath(installed_path).relative_to(PurePosixPath(agent_home))
    repository_path = PurePosixPath(*relative.parts)
    result = run_git(source, "show", f"{revision}:{repository_path}")
    return digest(result.stdout) if result.returncode == 0 else None


def safe_target_path(target: Path, relative: str, agent_home: str) -> Path:
    normalized_managed_path(relative, agent_home, {"skills", "contracts"}, "target path")
    path = target.joinpath(*PurePosixPath(relative).parts)
    current = target
    for part in PurePosixPath(relative).parts:
        current = current / part
        if current.is_symlink():
            raise InstallError(f"managed target path must not contain a symlink: {relative}")
    try:
        path.resolve(strict=False).relative_to(target)
    except ValueError as error:
        raise InstallError(f"managed target path escapes the project: {relative}") from error
    return path


def reject_legacy_staging_path(path: Path, staging_name: str) -> None:
    staging = path.with_name(staging_name)
    if staging.exists() or staging.is_symlink():
        raise InstallError(f"staging path already exists and must be inspected: {staging}")


def atomic_replace_bytes(path: Path, data: bytes, prefix: str, mode: int) -> None:
    descriptor, temporary_name = tempfile.mkstemp(dir=path.parent, prefix=prefix)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            os.fchmod(handle.fileno(), mode)
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def legacy_managed_files(source: Path, target: Path, agent_home: str, lock: dict) -> dict[str, str]:
    managed: dict[str, str] = {}
    revision = resolve_recorded_revision(source, lock["revision"])
    candidates: list[Path] = []
    skills_root = safe_target_path(target, f"{agent_home}/skills", agent_home)
    if skills_root.is_dir():
        for root in skills_root.iterdir():
            if root.is_symlink():
                raise InstallError(f"legacy skill path must not be a symlink: {root}")
            if root.is_dir() and SKILL_NAME_PATTERN.fullmatch(root.name):
                candidates.extend(path for path in root.rglob("*") if path.is_file() and not path.is_symlink())
    contract_root = safe_target_path(target, f"{agent_home}/contracts", agent_home)
    if contract_root.is_dir():
        candidates.extend(path for path in contract_root.rglob("*") if path.is_file() and not path.is_symlink())
    for path in candidates:
        relative = path.relative_to(target).as_posix()
        old_digest = old_blob_digest(source, revision, relative, agent_home)
        if old_digest is not None:
            managed[relative] = old_digest
    return managed


def markdown_reference_target(markdown_file: Path, raw_target: str) -> Path | None:
    value = raw_target.strip()
    if value.startswith("<") and value.endswith(">"):
        value = value[1:-1]
    elif " " in value:
        value = value.split(" ", 1)[0]
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    return markdown_file.parent / unquote(parsed.path)


def validate_installed(target: Path, agent_home: str, skills: list[str], contract_paths: list[str]) -> None:
    for name in skills:
        skill_root = safe_target_path(target, f"{agent_home}/skills/{name}", agent_home)
        skill_file = skill_root / "SKILL.md"
        if not skill_file.is_file() or skill_file.is_symlink():
            raise InstallError(f"installed skill is missing {skill_file}")
        text = skill_file.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            raise InstallError(f"invalid frontmatter in {skill_file}")
        parts = text.split("---\n", 2)
        if len(parts) != 3:
            raise InstallError(f"invalid frontmatter in {skill_file}")
        frontmatter = parts[1]
        fields = {}
        for line in frontmatter.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                fields[key.strip()] = value.strip()
        if len(frontmatter.splitlines()) != 2 or list(fields) != ["name", "description"]:
            raise InstallError(f"frontmatter must contain only name and description in {skill_file}")
        if fields["name"] != name:
            raise InstallError(f"frontmatter name {fields['name']!r} does not match installed skill {name!r}")
        for markdown_file in skill_root.rglob("*.md"):
            if markdown_file.is_symlink():
                raise InstallError(f"installed Markdown file must not be a symlink: {markdown_file}")
            markdown = markdown_file.read_text(encoding="utf-8")
            for raw_target in MARKDOWN_LINK_PATTERN.findall(markdown):
                reference = markdown_reference_target(markdown_file, raw_target)
                if reference is not None:
                    try:
                        resolved_reference = reference.resolve(strict=True)
                        resolved_reference.relative_to(target)
                    except (FileNotFoundError, OSError, ValueError):
                        relative_markdown = markdown_file.relative_to(target)
                        raise InstallError(f"unresolved or escaping Markdown reference in {relative_markdown}: {raw_target}")
    for relative in contract_paths:
        if not safe_target_path(target, relative, agent_home).is_file():
            raise InstallError(f"installed contract is missing {relative}")


def install(source: Path, target: Path, host: str, profile: str, dry_run: bool = False) -> dict:
    source = source.resolve()
    target = target.resolve()
    catalog = load_catalog(source / "catalog.json")
    errors = validate_catalog(catalog, source)
    if errors:
        raise InstallError("source catalog is invalid: " + "; ".join(errors))
    revision = source_revision(source)
    if host not in HOST_HOMES:
        raise InstallError(f"unknown host {host!r}; choose from {', '.join(sorted(HOST_HOMES))}")
    agent_home = HOST_HOMES[host]
    agent_root = target.joinpath(*PurePosixPath(agent_home).parts)
    if agent_root.is_symlink():
        raise InstallError(f"agent home must not be a symlink: {agent_root}")
    lock_path = agent_root / LOCK_NAME
    old_lock = read_lock(lock_path, host, agent_home, catalog)
    skills = resolve_skills(catalog, profile)
    desired = desired_files(source, revision, agent_home, skills, catalog)

    if old_lock and old_lock["format_version"] == 2:
        old_managed = dict(old_lock["managed_files"])
    elif old_lock:
        old_managed = legacy_managed_files(source, target, agent_home, old_lock)
    else:
        old_managed = {}

    conflicts: list[str] = []
    for relative, (data, _mode) in desired.items():
        path = safe_target_path(target, relative, agent_home)
        if not path.exists():
            continue
        current = file_digest(path)
        old = old_managed.get(relative)
        if old is None and current != digest(data):
            conflicts.append(f"unmanaged target exists: {relative}")
        elif old is not None and current != old:
            conflicts.append(f"locally modified managed file: {relative}")

    removals: list[str] = []
    for relative, recorded_digest in old_managed.items():
        if relative in desired:
            continue
        path = safe_target_path(target, relative, agent_home)
        if not path.exists():
            continue
        if file_digest(path) != recorded_digest:
            conflicts.append(f"locally modified managed file excluded by profile: {relative}")
        else:
            removals.append(relative)
    if conflicts:
        raise InstallError("installation stopped to preserve local files:\n- " + "\n- ".join(conflicts))

    contract_paths = sorted(path for path in desired if path.startswith(f"{agent_home}/contracts/"))
    lock = {
        "format_version": 2,
        "package_id": "bwh-ai-workflow",
        "source": source_identity(source),
        "revision": revision,
        "installed_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "host": host,
        "install_scope": "project",
        "profile": profile,
        "installed_skills": skills,
        "installed_contracts": contract_paths,
        "catalog_schema_version": catalog["schema_version"],
        "managed_files": {relative: digest(data) for relative, (data, _mode) in sorted(desired.items())},
    }
    validate_v2_lock(lock, host, agent_home, catalog)
    result = {"profile": profile, "skills": skills, "writes": sorted(desired), "removals": sorted(removals), "lock": str(lock_path)}
    if dry_run:
        return result

    for relative in desired:
        path = safe_target_path(target, relative, agent_home)
        reject_legacy_staging_path(path, f".{path.name}.bwh-new")
    reject_legacy_staging_path(lock_path, f".{LOCK_NAME}.new")

    backup_root = Path(tempfile.mkdtemp(prefix="bwh-install-backup-"))
    touched = sorted(set(desired) | set(removals))
    existed: set[str] = set()
    try:
        for relative in touched:
            path = safe_target_path(target, relative, agent_home)
            if path.is_file():
                backup = backup_root.joinpath(*PurePosixPath(relative).parts)
                backup.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, backup)
                existed.add(relative)
        for relative, (data, mode) in desired.items():
            path = safe_target_path(target, relative, agent_home)
            path.parent.mkdir(parents=True, exist_ok=True)
            atomic_replace_bytes(path, data, f".{path.name}.bwh-new-", mode)
        for relative in removals:
            safe_target_path(target, relative, agent_home).unlink()
        validate_installed(target, agent_home, skills, contract_paths)
        lock_path.parent.mkdir(parents=True, exist_ok=True)
        atomic_replace_bytes(lock_path, (json.dumps(lock, indent=2) + "\n").encode("utf-8"), f".{LOCK_NAME}.new-", 0o600)
    except Exception:
        for relative in touched:
            path = safe_target_path(target, relative, agent_home)
            backup = backup_root.joinpath(*PurePosixPath(relative).parts)
            if relative in existed:
                path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(backup, path)
            elif path.exists():
                path.unlink()
        raise
    finally:
        shutil.rmtree(backup_root)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--host", required=True, choices=sorted(HOST_HOMES))
    parser.add_argument("--profile", default="workflow")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        result = install(args.source, args.target, args.host, args.profile, args.dry_run)
    except (InstallError, OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
