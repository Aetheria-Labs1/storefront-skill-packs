# Lexsis AI — Storefront Skill Packs

> Expert AI skills for building high-converting Shopify landing pages. Works with Claude Code, OpenAI Codex, Cursor, and Custom GPTs.

## What Are Skill Packs?

Skill packs give your AI coding assistant deep expertise in Shopify landing page design — conversion psychology, vertical-specific patterns, traffic source optimization, and operational workflows. Combined with the [Lexsis AI MCP server](https://mcp.trylexsis.com), your AI can generate, publish, and optimize complete Shopify pages.

## Available Packs

| Pack | Best For | Skills |
|------|----------|--------|
| [**starter**](./starter/) | Any Shopify store — foundation skills | 9 skills, 2 commands |
| [**beauty-meta-ads**](./beauty-meta-ads/) | Beauty/skincare brands running Meta ads | 13 skills, 3 commands |

## Quick Install

```bash
# Clone this repo
git clone https://github.com/lexsis-ai/storefront-skill-packs
cd storefront-skill-packs

# Pick a pack and run the installer
cd starter        # or: beauty-meta-ads
./install.sh      # Auto-detects your platform
```

## Manual Install

### Claude Code

```bash
cd starter
cp -r claude/skills/* /path/to/your/project/.claude/skills/
cp -r claude/commands/* /path/to/your/project/.claude/commands/
```

### OpenAI Codex

```bash
cd starter
cp -r codex/skills/* /path/to/your/project/.agents/skills/
cp codex/AGENTS.md /path/to/your/project/
```

### Cursor

```bash
cd starter
mkdir -p /path/to/your/project/.cursor/rules
cp -r cursor/rules/* /path/to/your/project/.cursor/rules/
```

### Custom GPT

1. Open the pack's `gpt/instructions.md` — paste into your GPT's Instructions field
2. Upload `gpt/knowledge.md` as a Knowledge file

## Connect Lexsis AI MCP Server

Skills work standalone for design guidance. For full power (generate images, publish pages, run A/B tests), connect the MCP server:

```json
{
  "mcpServers": {
    "lexsis-ai": {
      "type": "http",
      "url": "https://mcp.trylexsis.com/mcp",
      "headers": {
        "Authorization": "Bearer <your-api-key>"
      }
    }
  }
}
```

Add this to:
- **Claude Code**: `.mcp.json` in your project root
- **Cursor**: `.cursor/mcp.json`
- **VS Code**: `.vscode/mcp.json`

Get your API key at [trylexsis.com/settings/api-keys](https://trylexsis.com/settings/api-keys)

## What's Inside Each Pack

```
{pack-name}/
├── README.md              # Pack-specific install + usage
├── install.sh             # Auto-installer (detects platform)
├── claude/
│   ├── commands/          # Slash commands (e.g. /generate-beauty-page)
│   └── skills/            # Auto-matched by context
├── codex/
│   ├── skills/            # SKILL.md files
│   └── AGENTS.md          # Root conventions
├── cursor/
│   └── rules/             # .mdc rule files
├── gpt/
│   ├── instructions.md    # Custom GPT instructions
│   └── knowledge.md       # Knowledge file upload
└── mcp/
    ├── mcp.json           # Universal MCP config
    ├── claude-desktop-config.json
    └── vscode-mcp.json
```

## How Skills + MCP Work Together

```
┌─────────────────────────────────────────────────────┐
│  Your AI Assistant (Claude Code / Codex / Cursor)    │
│                                                       │
│  Skills (installed)          MCP Server (connected)   │
│  ├── Conversion psychology   ├── generate_asset       │
│  ├── Vertical expertise      ├── validate_vibe_page   │
│  ├── Traffic source strategy ├── publish_vibe_page    │
│  └── Workflow orchestration  ├── get_brand_kit        │
│                              └── analyze_ad_creative  │
│                                                       │
│  Skills = WHAT to build      MCP = HOW to build it   │
└─────────────────────────────────────────────────────┘
```

---

Built by [Lexsis AI](https://trylexsis.com) — AI-powered Shopify Landing Page Builder
