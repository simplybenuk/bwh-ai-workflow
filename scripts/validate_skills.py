#!/usr/bin/env python3
"""Run portable static checks over every catalogued skill."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from validate_catalog import load_catalog, validate_catalog


LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
LEAKAGE_PATTERNS = {
    "host home": re.compile(r"(?:\.cursor|\.claude|\.agents)(?:/|\\|\b)", re.IGNORECASE),
    "host instruction filename": re.compile(r"\b(?:CLAUDE|AGENTS)\.md\b"),
    "host invocation": re.compile(r"(?:^|[\s`])(?:\$bwh-|/bwh-)", re.IGNORECASE | re.MULTILINE),
    "agent vendor": re.compile(r"\b(?:Codex|Claude Code|Cursor)\b"),
    "named model": re.compile(r"\b(?:GPT-[0-9][\w.-]*|Claude-[0-9][\w.-]*|Opus|Sonnet)\b", re.IGNORECASE),
}
ROUTED_RELATIVE_PREFIXES = ("agents/",)


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str] | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        return None
    fields: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields, parts[2]


def link_target(markdown_file: Path, raw_target: str) -> Path | None:
    value = raw_target.strip()
    if value.startswith("<") and value.endswith(">"):
        value = value[1:-1]
    elif " " in value:
        value = value.split(" ", 1)[0]
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    return markdown_file.parent / unquote(parsed.path)


def validate_skills(root: Path, catalog: dict) -> list[str]:
    errors = [f"catalog: {error}" for error in validate_catalog(catalog, root)]
    try:
        resolved_root = root.resolve()
    except OSError:
        resolved_root = root
    for skill in catalog.get("skills", []):
        if not isinstance(skill, dict) or not isinstance(skill.get("name"), str) or not isinstance(skill.get("directory"), str):
            continue
        name = skill["name"]
        skill_root = root / skill["directory"]
        skill_file = skill_root / "SKILL.md"
        if not skill_file.is_file():
            continue
        parsed = parse_frontmatter(skill_file)
        if parsed is None:
            errors.append(f"{name}: SKILL.md has invalid frontmatter delimiters")
        else:
            fields, _body = parsed
            frontmatter_text = skill_file.read_text(encoding="utf-8").split("---\n", 2)[1]
            if len(frontmatter_text.splitlines()) != 2 or list(fields) != ["name", "description"]:
                errors.append(f"{name}: frontmatter must contain exactly name and description")
            if fields.get("name") != name or skill_root.name != name:
                errors.append(f"{name}: folder, catalog, and frontmatter names must match")
            if not fields.get("description"):
                errors.append(f"{name}: description must not be empty")

        for markdown_file in sorted(skill_root.rglob("*.md")):
            relative_to_skill = markdown_file.relative_to(skill_root).as_posix()
            text = markdown_file.read_text(encoding="utf-8")
            for raw_target in LINK_PATTERN.findall(text):
                target = link_target(markdown_file, raw_target)
                if target is None:
                    continue
                try:
                    resolved = target.resolve(strict=True)
                    resolved.relative_to(resolved_root)
                except (FileNotFoundError, OSError, ValueError):
                    errors.append(f"{name}: unresolved or escaping Markdown reference in {relative_to_skill}: {raw_target}")
            if relative_to_skill.startswith(ROUTED_RELATIVE_PREFIXES):
                continue
            body = parse_frontmatter(markdown_file)
            portable_text = body[1] if markdown_file.name == "SKILL.md" and body else text
            for label, pattern in LEAKAGE_PATTERNS.items():
                match = pattern.search(portable_text)
                if match:
                    errors.append(f"{name}: {label} leakage in {relative_to_skill}: {match.group(0)}")

        scripts_root = skill_root / "scripts"
        if scripts_root.is_dir():
            for helper in sorted(path for path in scripts_root.rglob("*") if path.is_file()):
                relative = helper.relative_to(root)
                data = helper.read_bytes()
                if not data.startswith(b"#!"):
                    errors.append(f"{relative}: executable helper must declare an interpreter with a shebang")
                if not os.access(helper, os.X_OK):
                    errors.append(f"{relative}: executable helper is not marked executable")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        catalog = load_catalog(args.root / "catalog.json")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    errors = validate_skills(args.root, catalog)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Portable skill validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
