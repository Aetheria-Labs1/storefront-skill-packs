#!/usr/bin/env python3
"""Validate the Codex plugin manifest, skills, metadata, and MCP configuration."""
import json
import re
import sys
from pathlib import Path

ROOT = Path("codex")
MANIFEST = ROOT / ".codex-plugin" / "plugin.json"
MCP_CONFIG = ROOT / ".mcp.json"
SKILLS_ROOT = ROOT / "skills"

CANONICAL_SKILLS = {
    "storefront-engine",
    "browser-analyze",
    "analyze-page",
    "cart",
    "experiment",
    "extract-island",
    "generate",
    "optimize",
    "plan-page",
    "publish",
    "remix",
    "search-docs",
}
EXPECTED_SKILLS = CANONICAL_SKILLS
WORKFLOW_ASSERTIONS = {
    "generate": ("validate_vibe_page", "publish_vibe_page", "Codex Browser", "explicitly approves"),
    "publish": ("draft: true", "explicit user approval"),
    "browser-analyze": ("extract_brand_design", "Fallback"),
    "experiment": ("create_ab_test", "statistical"),
    "cart": ("Cart V2", "update_cart_config"),
}


def fail(message):
    print(f"::error::{message}")
    raise SystemExit(1)


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"Could not parse {path}: {error}")


def frontmatter(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        fail(f"{path} is missing YAML frontmatter")
    try:
        closing = next(index for index, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        fail(f"{path} is missing closing YAML frontmatter")
    fields = {}
    for line in lines[1:closing]:
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.+)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip().strip('"')
    return fields


manifest = load_json(MANIFEST)
for field in ("name", "version", "description", "author", "skills", "mcpServers", "interface"):
    if not manifest.get(field):
        fail(f"Codex manifest missing {field}")
if manifest["name"] != "lexsis-storefront-skills":
    fail("Codex manifest name must be lexsis-storefront-skills")
if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", manifest["version"]):
    fail("Codex manifest version must be semver")
if manifest["skills"] != "./skills/" or manifest["mcpServers"] != "./.mcp.json":
    fail("Codex manifest must point to bundled skills and MCP config")
if not manifest["author"].get("name"):
    fail("Codex manifest author.name is required")
interface = manifest["interface"]
for field in ("displayName", "shortDescription", "longDescription", "developerName", "category", "capabilities", "websiteURL", "defaultPrompt"):
    if not interface.get(field):
        fail(f"Codex manifest interface missing {field}")
if len(interface["defaultPrompt"]) > 3 or any(len(prompt) > 128 for prompt in interface["defaultPrompt"]):
    fail("Codex manifest defaultPrompt must contain at most three prompts of 128 characters or fewer")

mcp_config = load_json(MCP_CONFIG)
server = mcp_config.get("mcpServers", {}).get("lexsis-ai")
if not server or server.get("type") != "http" or server.get("url") != "https://mcp.trylexsis.com/mcp":
    fail("Codex MCP config must define lexsis-ai as the expected HTTPS server")

skill_paths = sorted(SKILLS_ROOT.glob("*/SKILL.md"))
skill_names = set()
for skill_path in skill_paths:
    directory_name = skill_path.parent.name
    fields = frontmatter(skill_path)
    if fields.get("name") != directory_name:
        fail(f"{skill_path} name must match its directory")
    if not fields.get("description"):
        fail(f"{skill_path} is missing a single-line description")
    if directory_name in skill_names:
        fail(f"Duplicate Codex skill name: {directory_name}")
    skill_names.add(directory_name)

    metadata = skill_path.parent / "agents" / "openai.yaml"
    if not metadata.exists():
        fail(f"{skill_path} is missing agents/openai.yaml")
    metadata_text = metadata.read_text(encoding="utf-8")
    if 'value: "lexsis-ai"' not in metadata_text:
        fail(f"{metadata} must declare the lexsis-ai MCP dependency")
    explicit_only = "allow_implicit_invocation: false" in metadata_text
    if explicit_only:
        fail(f"{metadata} must allow implicit invocation for skill {directory_name}")

if skill_names != EXPECTED_SKILLS:
    missing = sorted(EXPECTED_SKILLS - skill_names)
    extra = sorted(skill_names - EXPECTED_SKILLS)
    fail(f"Codex skill set mismatch; missing={missing}, extra={extra}")

for skill_name, required_terms in WORKFLOW_ASSERTIONS.items():
    contents = (SKILLS_ROOT / skill_name / "SKILL.md").read_text(encoding="utf-8")
    missing_terms = [term for term in required_terms if term not in contents]
    if missing_terms:
        fail(f"{skill_name} is missing workflow safeguards: {missing_terms}")

print(f"Codex plugin valid: {len(skill_names)} skills and 257 shared references")
