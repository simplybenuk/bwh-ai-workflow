#!/usr/bin/env python3
"""Check host manifests for a consistent BWH Agent Toolkit package identity."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IDENTIFIER = "bwh-ai-workflow"
DISPLAY_NAME = "BWH Agent Toolkit"
VERSION = "0.2.0"
REPOSITORY = "https://github.com/simplybenuk/bwh-ai-workflow"
LICENSE = "MIT"


def main() -> int:
    errors: list[str] = []
    manifest_paths = [
        ROOT / ".codex-plugin/plugin.json",
        ROOT / ".claude-plugin/plugin.json",
        ROOT / ".cursor-plugin/plugin.json",
    ]
    manifests = []
    for path in manifest_paths:
        try:
            manifest = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            errors.append(f"{path.relative_to(ROOT)}: {error}")
            continue
        manifests.append((path, manifest))
        if manifest.get("name") != IDENTIFIER:
            errors.append(f"{path.relative_to(ROOT)}: identifier changed")
        if manifest.get("version") != VERSION:
            errors.append(f"{path.relative_to(ROOT)}: version must be {VERSION}")
        if manifest.get("repository") != REPOSITORY:
            errors.append(f"{path.relative_to(ROOT)}: repository mismatch")
        if manifest.get("license") != LICENSE:
            errors.append(f"{path.relative_to(ROOT)}: licence must be {LICENSE}")
        if manifest.get("skills") != "./skills/":
            errors.append(f"{path.relative_to(ROOT)}: skills path must be ./skills/")
        if not (ROOT / manifest.get("skills", "missing")).is_dir():
            errors.append(f"{path.relative_to(ROOT)}: skills path does not resolve")
        display_name = manifest.get("displayName") or manifest.get("interface", {}).get("displayName")
        if display_name != DISPLAY_NAME:
            errors.append(f"{path.relative_to(ROOT)}: display name mismatch")
        if DISPLAY_NAME not in manifest.get("description", ""):
            errors.append(f"{path.relative_to(ROOT)}: description omits public name")

    marketplace_paths = [ROOT / ".agents/plugins/marketplace.json", ROOT / ".claude-plugin/marketplace.json"]
    for path in marketplace_paths:
        try:
            marketplace = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            errors.append(f"{path.relative_to(ROOT)}: {error}")
            continue
        if marketplace.get("name") != IDENTIFIER:
            errors.append(f"{path.relative_to(ROOT)}: identifier changed")
        plugin_names = [plugin.get("name") for plugin in marketplace.get("plugins", [])]
        if plugin_names != [IDENTIFIER]:
            errors.append(f"{path.relative_to(ROOT)}: plugin identifier mismatch")
        rendered = json.dumps(marketplace)
        if DISPLAY_NAME not in rendered:
            errors.append(f"{path.relative_to(ROOT)}: public display name missing")

    licence_path = ROOT / "LICENSE"
    try:
        licence_text = licence_path.read_text(encoding="utf-8")
    except OSError as error:
        errors.append(f"LICENSE: {error}")
    else:
        if not licence_text.startswith("MIT License\n"):
            errors.append("LICENSE: expected MIT licence text")
        if "Copyright (c) 2026 Simply Ben" not in licence_text:
            errors.append("LICENSE: expected toolkit copyright notice")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Package manifests valid for Codex, Claude Code, and Cursor")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
