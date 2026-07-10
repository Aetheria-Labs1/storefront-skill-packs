#!/usr/bin/env python3
"""Validate all plugin.json files have required fields."""
import json
import sys
from pathlib import Path

REQUIRED = ["name", "description", "version"]
failed = False

for pj in Path("plugins").glob("*/.claude-plugin/plugin.json"):
    try:
        data = json.loads(pj.read_text())
    except json.JSONDecodeError as e:
        print(f"::error file={pj}::Invalid JSON: {e}")
        failed = True
        continue

    missing = [f for f in REQUIRED if f not in data]
    if missing:
        print(f"::error file={pj}::Missing fields: {', '.join(missing)}")
        failed = True
    elif "author" not in data or "name" not in data.get("author", {}):
        print(f"::error file={pj}::Missing author.name")
        failed = True
    else:
        print(f"  {pj.parent.parent.name}: OK")

if failed:
    sys.exit(1)

print("All plugin.json files valid")
