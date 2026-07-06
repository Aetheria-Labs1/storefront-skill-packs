# Lexsis AI Skill Packs

Distributable AI skill packs for building Shopify landing pages. Customers install these alongside the [Lexsis AI MCP server](https://mcp.trylexsis.com) to get expert-guided AI page building.

## How It Works

```
Source Skills (services/storefront-blueprint-mcp/skills/)
        ↓ build pipeline
Pack Manifests (manifests/*.json)
        ↓ platform emitters
dist/{pack}/
  ├── claude/    → Claude Code (.claude/skills/ + .claude/commands/)
  ├── codex/     → OpenAI Codex (.agents/skills/)
  ├── cursor/    → Cursor (.cursor/rules/)
  ├── gpt/       → Custom GPT (knowledge + instructions)
  └── mcp/       → MCP connection config (all clients)
```

## Available Packs

| Pack | Skills | Description |
|------|--------|-------------|
| `starter` | 9 | Foundation — works for any vertical/traffic source |
| `beauty-meta-ads` | 13 | Beauty/skincare brands running Meta ads |

## Build

```bash
npm install
npm run build          # Build all packs
npm run build starter  # Build one pack
npm run validate       # Check output constraints
```

## Adding a New Pack

1. Create `manifests/{pack-id}.json` with skill references
2. Run `npm run build`
3. Output appears in `dist/{pack-id}/`

## Manifest Format

```json
{
  "id": "pack-id",
  "name": "Display Name",
  "version": "1.0.0",
  "description": "One-line description",
  "skills": {
    "knowledge": [{ "source": "skills/file.md", "name": "output-name" }],
    "operational": [{ "source": "codex-skills/dir/SKILL.md", "name": "output-name" }]
  },
  "commands": [{ "name": "cmd-name", "description": "...", "loads": ["skill1", "skill2"] }]
}
```

Source paths relative to `services/storefront-blueprint-mcp/`.
