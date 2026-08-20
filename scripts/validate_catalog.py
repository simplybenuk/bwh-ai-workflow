#!/usr/bin/env python3
"""Validate the BWH Agent Toolkit catalog and its local skill paths."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path, PurePosixPath


ALLOWED_STATUSES = {"active", "pilot", "retired"}
ALLOWED_ORIGINS = {"core", "derived"}
ALLOWED_HOST_STATUSES = {"pending", "supported", "failed"}
EXPECTED_HOSTS = {"codex", "claude-code", "cursor"}
REQUIRED_TOP_LEVEL = {"schema_version", "toolkit", "hosts", "profiles", "skills"}
REQUIRED_TOOLKIT = {"identifier", "display_name", "version"}
REQUIRED_SKILL = {"name", "directory", "status", "profiles", "dependencies", "shared_contracts", "origin"}
REQUIRED_PROVENANCE = {"repository", "revision", "license", "attribution", "paths", "adaptations"}
NAME_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
REVISION_PATTERN = re.compile(r"[0-9a-f]{40}")


def load_catalog(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError("catalog root must be a JSON object")
    return value


def string_list(value: object) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) and item for item in value)


def normalized_directory(value: object, name: str) -> bool:
    if not isinstance(value, str) or "\\" in value:
        return False
    path = PurePosixPath(value)
    return not path.is_absolute() and str(path) == value and path.parts == ("skills", name)


def validate_catalog(catalog: object, root: Path, check_paths: bool = True) -> list[str]:
    errors: list[str] = []
    if not isinstance(catalog, dict):
        return ["catalog root must be an object"]
    missing_top = sorted(REQUIRED_TOP_LEVEL - set(catalog))
    if missing_top:
        errors.append("catalog is missing fields: " + ", ".join(missing_top))
    if catalog.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    toolkit = catalog.get("toolkit")
    if not isinstance(toolkit, dict):
        errors.append("toolkit must be an object")
        toolkit = {}
    missing_toolkit = sorted(REQUIRED_TOOLKIT - set(toolkit))
    if missing_toolkit:
        errors.append("toolkit is missing fields: " + ", ".join(missing_toolkit))
    if toolkit.get("identifier") != "bwh-ai-workflow":
        errors.append("toolkit.identifier must remain bwh-ai-workflow")
    if toolkit.get("display_name") != "BWH Agent Toolkit":
        errors.append("toolkit.display_name must be BWH Agent Toolkit")
    if not isinstance(toolkit.get("version"), str) or not toolkit.get("version"):
        errors.append("toolkit.version must be a non-empty string")

    hosts = catalog.get("hosts")
    if not isinstance(hosts, dict):
        errors.append("hosts must be an object")
        hosts = {}
    if set(hosts) != EXPECTED_HOSTS:
        errors.append("hosts must define exactly codex, claude-code, and cursor")
    for host, metadata in hosts.items():
        if not isinstance(metadata, dict):
            errors.append(f"host {host}: metadata must be an object")
        elif set(metadata) != {"validation_status"} or metadata.get("validation_status") not in ALLOWED_HOST_STATUSES:
            errors.append(f"host {host}: invalid validation metadata")

    profiles = catalog.get("profiles")
    skills = catalog.get("skills")
    if not isinstance(profiles, dict) or not profiles:
        errors.append("profiles must be a non-empty object")
        profiles = {}
    if not isinstance(skills, list):
        errors.append("skills must be an array")
        skills = []

    object_skills: list[dict] = []
    for index, skill in enumerate(skills):
        if not isinstance(skill, dict):
            errors.append(f"skill entry {index}: must be an object")
        else:
            object_skills.append(skill)
    names = [skill.get("name") for skill in object_skills if isinstance(skill.get("name"), str)]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        errors.append(f"duplicate skill names: {', '.join(duplicates)}")
    known = set(names)
    by_name = {skill["name"]: skill for skill in object_skills if isinstance(skill.get("name"), str)}

    for index, skill in enumerate(object_skills):
        label = skill.get("name") if isinstance(skill.get("name"), str) else f"skill entry {index}"
        missing = sorted(REQUIRED_SKILL - set(skill))
        if missing:
            errors.append(f"{label}: missing required fields: {', '.join(missing)}")
        name = skill.get("name")
        if not isinstance(name, str) or not NAME_PATTERN.fullmatch(name):
            errors.append(f"{label}: invalid skill name")
            continue
        directory = skill.get("directory")
        if not normalized_directory(directory, name):
            errors.append(f"{name}: directory must be the normalized path skills/{name}")
        elif check_paths and not (root / directory / "SKILL.md").is_file():
            errors.append(f"{name}: missing {directory}/SKILL.md")
        status = skill.get("status")
        if status not in ALLOWED_STATUSES:
            errors.append(f"{name}: invalid status {status!r}")
        origin = skill.get("origin")
        if origin not in ALLOWED_ORIGINS:
            errors.append(f"{name}: origin must be core or derived")
        if not isinstance(skill.get("shared_contracts"), bool):
            errors.append(f"{name}: shared_contracts must be a boolean")

        declared_profiles = skill.get("profiles")
        if not string_list(declared_profiles):
            errors.append(f"{name}: profiles must be an array of non-empty strings")
            declared_profiles = []
        unknown_profiles = sorted(set(declared_profiles) - set(profiles))
        if unknown_profiles:
            errors.append(f"{name}: unknown profiles: {', '.join(unknown_profiles)}")
        if status == "active" and not declared_profiles:
            errors.append(f"{name}: active skills need at least one profile")

        dependencies = skill.get("dependencies")
        if not string_list(dependencies):
            errors.append(f"{name}: dependencies must be an array of non-empty strings")
            dependencies = []
        unknown_dependencies = sorted(set(dependencies) - known)
        if unknown_dependencies:
            errors.append(f"{name}: unknown dependencies: {', '.join(unknown_dependencies)}")

        provenance = skill.get("provenance")
        if origin == "derived" and provenance is None:
            errors.append(f"{name}: derived skills require provenance")
        if provenance is not None:
            if not isinstance(provenance, dict):
                errors.append(f"{name}: provenance must be an object")
            else:
                missing_provenance = sorted(REQUIRED_PROVENANCE - set(provenance))
                if missing_provenance:
                    errors.append(f"{name}: incomplete provenance: {', '.join(missing_provenance)}")
                for field in ("repository", "license", "attribution"):
                    if not isinstance(provenance.get(field), str) or not provenance.get(field):
                        errors.append(f"{name}: provenance {field} must be a non-empty string")
                revision = provenance.get("revision")
                if not isinstance(revision, str) or not REVISION_PATTERN.fullmatch(revision):
                    errors.append(f"{name}: provenance revision must be a full commit SHA")
                for field in ("paths", "adaptations"):
                    if not string_list(provenance.get(field)) or not provenance.get(field):
                        errors.append(f"{name}: provenance {field} must be a non-empty string array")

    for profile, members in profiles.items():
        if not isinstance(profile, str) or not profile:
            errors.append("profile names must be non-empty strings")
            continue
        if not string_list(members) and members != []:
            errors.append(f"profile {profile}: membership must be a string array")
            continue
        unknown = sorted(set(members) - known)
        if unknown:
            errors.append(f"profile {profile}: unknown skills: {', '.join(unknown)}")
        duplicate_members = sorted({name for name in members if members.count(name) > 1})
        if duplicate_members:
            errors.append(f"profile {profile}: duplicate skills: {', '.join(duplicate_members)}")
        for name in members:
            skill = by_name.get(name)
            if skill and skill.get("status") != "active":
                errors.append(f"profile {profile}: {name} is not active")
            if skill and profile != "full" and profile not in skill.get("profiles", []):
                errors.append(f"profile {profile}: {name} does not declare membership")

    expected_full = set().union(*(set(members) for name, members in profiles.items() if name != "full" and (string_list(members) or members == [])))
    full_members = profiles.get("full", [])
    if not isinstance(full_members, list) or set(full_members) != expected_full:
        errors.append("profile full must be the union of all other profiles")

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(name: str) -> None:
        if name in visiting:
            errors.append(f"dependency cycle includes {name}")
            return
        if name in visited or name not in by_name:
            return
        visiting.add(name)
        dependencies = by_name[name].get("dependencies", [])
        if isinstance(dependencies, list):
            for dependency in dependencies:
                if isinstance(dependency, str):
                    visit(dependency)
        visiting.remove(name)
        visited.add(name)

    for name in known:
        visit(name)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("catalog", nargs="?", type=Path, default=Path(__file__).resolve().parents[1] / "catalog.json")
    parser.add_argument("--skip-paths", action="store_true")
    args = parser.parse_args()
    try:
        catalog = load_catalog(args.catalog)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    root = args.catalog.resolve().parent
    errors = validate_catalog(catalog, root, not args.skip_paths)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Catalog valid: {args.catalog}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
