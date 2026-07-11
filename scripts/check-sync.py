#!/usr/bin/env python3
"""Require core reference parity between Claude and Codex packages."""
import filecmp
import sys
from pathlib import Path

ref_dir = Path("plugins/lexsis-storefront-skills/skills/storefront-engine/reference")
codex_dir = Path("codex/skills/storefront-engine/reference")

if not ref_dir.exists() or not codex_dir.exists():
    print("::error::Missing Claude or Codex reference directory")
    sys.exit(1)

ref_files = sorted(path.relative_to(ref_dir) for path in ref_dir.rglob("*") if path.is_file())
codex_files = sorted(path.relative_to(codex_dir) for path in codex_dir.rglob("*") if path.is_file())
missing = [path for path in ref_files if path not in codex_files]
extra = [path for path in codex_files if path not in ref_files]
mismatched = [
    path for path in ref_files
    if path in codex_files and not filecmp.cmp(ref_dir / path, codex_dir / path, shallow=False)
]

if missing or extra or mismatched:
    for label, paths in (("missing", missing), ("extra", extra), ("content mismatch", mismatched)):
        if paths:
            print(f"::error::Codex reference {label}: {len(paths)}")
            for path in paths[:10]:
                print(f"  - {path}")
            if len(paths) > 10:
                print(f"  ... and {len(paths) - 10} more")
    sys.exit(1)

print(f"All {len(ref_files)} reference files are byte-identical in codex/")
