#!/usr/bin/env python3
"""Check cross-platform sync (informational only, non-blocking)."""
from pathlib import Path

ref_dir = Path("plugins/lexsis-storefront-skills/skills/storefront-engine/reference")
codex_dir = Path("codex/skills/storefront-engine/reference")

if not ref_dir.exists():
    print("No reference dir found — skipping sync check")
    exit(0)

ref_files = [f.name for f in ref_dir.glob("*.md")]
missing = []

for name in ref_files:
    if not (codex_dir / name).exists():
        missing.append(name)

if missing:
    print(f"::warning::Cross-platform sync: {len(missing)} files in reference/ not in codex/")
    for name in missing[:10]:
        print(f"  - {name}")
    if len(missing) > 10:
        print(f"  ... and {len(missing) - 10} more")
else:
    print(f"All {len(ref_files)} reference files synced to codex/")
