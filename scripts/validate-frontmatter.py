#!/usr/bin/env python3
"""Validate command .md files have YAML frontmatter with description.

Commands (slash commands) MUST have frontmatter — they are user-facing.
Reference/knowledge skills are checked as warnings only (many are plain markdown).
"""
import sys
from pathlib import Path

failed = False
warned = 0

# Commands are required to have frontmatter
command_files = list(Path("plugins").glob("*/commands/*.md"))

# Reference skills are warned only
reference_files = list(Path("plugins").glob("*/skills/**/*.md"))

def check_frontmatter(md, required=True):
    global failed, warned
    content = md.read_text(encoding="utf-8")
    lines = content.split("\n")

    if not lines or lines[0].strip() != "---":
        if required:
            print(f"::error file={md}::Missing frontmatter (no opening ---)")
            failed = True
        else:
            warned += 1
        return

    closing = -1
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == "---":
            closing = i
            break

    if closing == -1:
        if required:
            print(f"::error file={md}::Missing frontmatter (no closing ---)")
            failed = True
        else:
            warned += 1
        return

    frontmatter = "\n".join(lines[1:closing])
    if "description:" not in frontmatter:
        if required:
            print(f"::error file={md}::Frontmatter missing 'description' field")
            failed = True
        else:
            warned += 1
    else:
        print(f"  {md.name}: OK")

for md in command_files:
    check_frontmatter(md, required=True)

for md in reference_files:
    check_frontmatter(md, required=False)

if warned:
    print(f"::warning::{warned} reference files missing frontmatter (non-blocking)")

if failed:
    sys.exit(1)

print(f"All {len(command_files)} command files have valid frontmatter")
