#!/usr/bin/env python3
"""Sync island schemas from storefront-components build output to OSS reference dir.

Usage:
    python3 scripts/sync-island-schemas.py <path-to-island-schemas.json>

Reads the compiled island-schemas.json (47 islands) and writes a schema.json
for each island into plugins/lexsis-storefront-skills/skills/storefront-engine/reference/islands/{kebab-name}/
"""
import json
import re
import sys
from pathlib import Path

ISLANDS_DIR = Path("plugins/lexsis-storefront-skills/skills/storefront-engine/reference/islands")


def pascal_to_kebab(name: str) -> str:
    """BuyBox → buy-box, AnnouncementBar → announcement-bar"""
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1-\2", name)
    s = re.sub(r"([a-z\d])([A-Z])", r"\1-\2", s)
    return s.lower()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/sync-island-schemas.py <island-schemas.json>")
        sys.exit(1)

    schemas_path = Path(sys.argv[1])
    if not schemas_path.exists():
        print(f"Error: {schemas_path} not found")
        sys.exit(1)

    schemas = json.loads(schemas_path.read_text())
    print(f"Loaded {len(schemas)} island schemas")

    created = 0
    updated = 0

    for island_name, schema in schemas.items():
        kebab = pascal_to_kebab(island_name)
        island_dir = ISLANDS_DIR / kebab
        island_dir.mkdir(parents=True, exist_ok=True)

        schema_file = island_dir / "schema.json"
        if schema_file.exists():
            updated += 1
        else:
            created += 1

        schema_file.write_text(json.dumps(schema, indent=2) + "\n")

    print(f"Done: {created} created, {updated} updated")
    print(f"Total: {created + updated} schema.json files in {ISLANDS_DIR}")


if __name__ == "__main__":
    main()
