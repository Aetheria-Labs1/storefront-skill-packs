# Lexsis AI — Storefront Skill Packs

AI skill packs for building high-converting Shopify landing pages. Install alongside the [Lexsis AI MCP server](https://mcp.trylexsis.com) to get expert-guided page generation in any AI coding assistant.

## How It Works

```
Your AI Assistant (Claude, Codex, Cursor, GPT)
     ├── Skills (installed from this repo) → domain knowledge + workflows
     └── MCP Server (mcp.trylexsis.com)   → tools (assets, publish, analytics)
```

Skills teach your AI assistant *how* to build pages. The MCP server provides the *tools* to execute (image generation, page publishing, brand kit access, analytics).

## Available Packs

| Pack | Skills | Best For |
|------|--------|----------|
| **[starter](./starter/)** | 9 | Any vertical — foundation skills |
| **[full-suite](./full-suite/)** | 33 | Everything — all verticals, all workflows, all page types |
| **[beauty-meta-ads](./beauty-meta-ads/)** | 13 | Beauty/skincare brands running Meta ads |
| **[supplements-google](./supplements-google/)** | 13 | Supplement brands running Google ads |
| **[fashion-tiktok](./fashion-tiktok/)** | 13 | Fashion brands running TikTok ads |
| **[food-dtc](./food-dtc/)** | 14 | Food/beverage DTC brands |
| **[home-decor](./home-decor/)** | 13 | Home goods and decor brands |
| **[luxury-brand](./luxury-brand/)** | 13 | Luxury/premium brands |

## Quick Install

Each pack has an auto-detect installer:

```bash
cd full-suite  # or any pack
chmod +x install.sh && ./install.sh
```

## Manual Installation by Platform

### Claude Code

```bash
# From any pack directory (e.g., full-suite/)
cp -r claude/skills/* .claude/skills/
cp -r claude/commands/* .claude/commands/
```

Then add MCP server to your Claude Code settings (`.claude/settings.json` or project `.claude/settings.json`):

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

**Visual verification** (recommended): Install [Playwright MCP](https://playwright.dev/docs/getting-started-mcp) so Claude can screenshot and verify generated pages:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

### OpenAI Codex

```bash
cp -r codex/skills/* .agents/skills/
cp codex/AGENTS.md .
```

Codex has a built-in browser — pages are verified automatically after generation.

### Cursor

```bash
mkdir -p .cursor/rules
cp -r cursor/rules/* .cursor/rules/
```

Add MCP to Cursor settings (Settings > MCP Servers > Add):
- URL: `https://mcp.trylexsis.com/mcp`
- Auth: Bearer token with your API key

### Custom GPT

1. Paste `gpt/instructions.md` into your GPT's **Instructions** field
2. Upload `gpt/knowledge.md` as a **Knowledge** file

## Connect MCP Server

All packs work best with the Lexsis AI MCP server connected:

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

Get your API key: [trylexsis.com/settings/api-keys](https://trylexsis.com/settings/api-keys)

### Available MCP Tools

| Tool | Purpose |
|------|---------|
| `get_workspace_details` | Your workspace context |
| `get_connected_stores` | Shopify store connection |
| `get_brand_kit` | Brand colors, fonts, logo, voice |
| `get_design_md` | Design philosophy and constraints |
| `search_design_library` | Find existing brand assets |
| `generate_asset` | AI image generation |
| `edit_asset` | Image compositing/editing |
| `list_products` | Shopify product catalog |
| `get_navigation` | Store navigation structure |
| `validate_vibe_page` | Validate page before publishing |
| `publish_vibe_page` | Publish to Shopify store |
| `get_page_analytics` | Page performance data |
| `create_ab_test` | Set up A/B experiments |
| `analyze_ad_creative` | Extract ad creative data |
| `match_persona_to_ad` | Map ad to audience persona |
| + 40 more | [Full tool catalog](https://docs.trylexsis.com) |

## Skill Types

### Knowledge Skills (passive context)

Loaded automatically — teach your AI about CRO patterns, verticals, design systems:

| Skill | What It Provides |
|-------|-----------------|
| `generation-protocol` | VibePage schema, CSS variables, two-phase generation, island system |
| `cro-research` | 2026 conversion data — section ordering, mobile patterns, psychology |
| `conversion-psychology` | Behavioral triggers, urgency tactics, social proof placement |
| `craft-guide` | Storefront design principles and quality bar |
| `island-patterns` | Interactive component usage (BuyBox, Cart, Reviews, FAQ) |
| `visual-craft` | Typography, spacing, color theory, animation |
| `vertical-*` | Niche patterns (beauty, supplements, fashion, food, home, luxury) |
| `traffic-source-*` | Channel optimization (Meta warm traffic, Google intent, TikTok scroll-stop) |

### Operational Skills (step-by-step workflows)

Triggered by slash commands — execute page generation:

| Skill | Command | What It Does |
|-------|---------|-------------|
| `generate-pdp` | `/generate-pdp` | Product detail page with BuyBox, gallery, reviews |
| `generate-landing-page` | `/generate-landing-page` | Ad-to-page with message match, zero nav |
| `generate-homepage` | `/generate-homepage` | Brand homepage with nav, collections, story |
| `generate-collection` | `/generate-collection` | Product grid with filters |
| `generate-listicle` | `/generate-listicle` | SEO long-form with embedded commerce |
| `generate-bundle-page` | `/generate-bundle` | Step-based bundle with discount tiers |
| `generate-editorial` | `/generate-editorial` | Magazine-style shoppable content |
| `ad-to-page` | `/convert-ad` | Ad creative to landing page with scent match |
| `page-redesign` | `/redesign-page` | Modernize existing page, preserve SEO |
| `competitor-remix` | `/remix-competitor` | Adapt competitor structure to your brand |
| `personalization-variant` | `/personalize-page` | Per-persona page variants |
| `ab-test-variant` | `/ab-test` | Hypothesis-driven split test setup |
| `brand-setup` | `/setup-brand` | First-time brand kit configuration |
| `section-library` | `/add-section` | Quick-insert sections into existing pages |

## Generation Protocol

All skills follow a two-phase approach for fast iteration:

```
Phase 0: Context (parallel)
  get_workspace_details + get_connected_stores + get_brand_kit + get_design_md

Phase 1: Assets
  search_design_library → generate_asset (only if needed)

Phase 2A: Raw HTML + Tailwind (no islands)
  Generate full page layout — iterates fast, renders in any browser

Phase 2B: Island Mapping
  Replace placeholders with data-island markers + JSON props

Phase 3: Validate
  validate_vibe_page → fix any structural errors

Phase 4: Publish + Visual Verify
  publish_vibe_page → screenshot with browser tool → verify rendering
```

### Why Two-Phase?

- **Phase 2A** produces pure HTML that renders instantly — fast visual feedback loop
- **Phase 2B** wires commerce islands (BuyBox, Cart, Reviews) which need the renderer
- Design decisions stay separate from data-wiring decisions
- Easier to iterate layout without breaking island prop JSON

## Visual Verification

After publishing, skills instruct the AI to screenshot and verify:

| Platform | Method |
|----------|--------|
| Claude Code | [Playwright MCP](https://playwright.dev/docs/getting-started-mcp) — `browser_navigate` + `browser_take_screenshot` |
| Codex | Built-in browser tool |
| Cursor | Opens preview URL via available browser |
| No browser | Provides preview URL for manual check |

## Directory Structure

```
{pack-id}/
  ├── README.md              — Pack-specific documentation
  ├── install.sh             — Auto-detect platform installer
  ├── claude/
  │   ├── commands/*.md      — Slash commands (/generate-pdp, /convert-ad, etc.)
  │   └── skills/*/SKILL.md  — One directory per skill
  ├── codex/
  │   ├── AGENTS.md          — Agent config with MCP setup
  │   └── skills/*/SKILL.md  — One directory per skill
  ├── cursor/
  │   └── rules/*.mdc        — MDC rule files (auto-load + on-demand)
  ├── gpt/
  │   ├── instructions.md    — Custom GPT system prompt
  │   └── knowledge.md       — Custom GPT knowledge upload
  └── mcp/
      ├── mcp.json                   — Universal MCP config (Claude Code, Cursor, VS Code)
      ├── claude-desktop-config.json — Claude Desktop format
      └── vscode-mcp.json           — VS Code MCP format
```

## Building from Source

Skills are authored in the [voc-pipeline](https://github.com/Aetheria-Labs1/voc-pipeline) monorepo:

```
services/storefront-blueprint-mcp/skills/
  ├── _knowledge/*.md    — Knowledge skills
  └── _operational/*.md  — Operational skills
```

Build:

```bash
cd skill-packs
npm install
npm run build          # Build all 8 packs
npm run build starter  # Build single pack
npm run validate       # Check line limits + frontmatter
```

## Adding a New Pack

1. Create `manifests/{pack-id}.json`:

```json
{
  "id": "pack-id",
  "name": "Display Name",
  "version": "1.0.0",
  "description": "One-line description",
  "category": "vertical",
  "skills": {
    "knowledge": [
      { "source": "skills/_knowledge/craft-guide.md", "name": "storefront-craft" }
    ],
    "operational": [
      { "source": "skills/_operational/page-generation.md", "name": "page-generation" }
    ]
  },
  "commands": [
    { "name": "generate-page", "description": "...", "loads": ["storefront-craft", "page-generation"] }
  ]
}
```

2. `npm run build` — output appears in `dist/{pack-id}/`

---

Built with [Lexsis AI](https://trylexsis.com) — AI-Powered Shopify Landing Page Builder
