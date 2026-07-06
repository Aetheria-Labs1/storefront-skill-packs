# Lexsis AI — Storefront Skill Packs

> AI skills for building high-converting Shopify landing pages with any coding assistant.

```
┌─────────────────────────────────────────────────────┐
│  Your AI (Claude, Codex, Cursor, GPT)               │
│    ├── core/          → generation workflows        │
│    ├── verticals/     → industry expertise          │
│    ├── traffic-sources/ → ad platform patterns      │
│    └── MCP Server     → tools (publish, assets)     │
└─────────────────────────────────────────────────────┘
```

## Quick Start

```bash
# 1. Clone
git clone https://github.com/Aetheria-Labs1/storefront-skill-packs.git
cd storefront-skill-packs

# 2. Install core (required — works for any industry)
cd core && chmod +x install.sh && ./install.sh

# 3. Add your industry (optional — pick one)
cd ../verticals/beauty && ./install.sh

# 4. Add your traffic source (optional — pick one)
cd ../../traffic-sources/meta-ads && ./install.sh
```

That's it. Your AI assistant now knows how to build Shopify landing pages.

## Structure

```
storefront-skill-packs/
├── core/                    ← Install first (30 skills, all workflows)
├── verticals/               ← Pick your industry
│   ├── beauty/
│   ├── supplements/
│   ├── fashion/
│   ├── food-dtc/
│   ├── home-decor/
│   └── luxury/
├── traffic-sources/         ← Pick your ad platform
│   ├── meta-ads/
│   ├── google-ads/
│   └── tiktok-ads/
└── mcp/                     ← MCP server configs (all platforms)
```

## What's in Each Layer

### Core (required)

Everything needed to generate any page type:

| Type | Skills | Examples |
|------|--------|---------|
| Knowledge | 11 | CRO research, conversion psychology, design patterns, island system |
| Operational | 19 | Generate PDP, landing page, homepage, collection, editorial, bundle, listicle |
| Workflows | 5 | Ad-to-page, redesign, competitor remix, personalization, A/B test |
| Utilities | 3 | Brand setup, section library, design assets |

### Verticals (pick one or more)

Industry-specific knowledge — section patterns, copy tone, product display, conversion tactics:

| Vertical | Focus |
|----------|-------|
| `beauty` | Ingredients, before/after, routine builders, shade finders |
| `supplements` | Clinical data, dosage info, subscription, trust signals |
| `fashion` | Size guides, lookbooks, model specs, style pairing |
| `food-dtc` | Flavor profiles, subscription boxes, recipe integration |
| `home-decor` | Room scenes, measurement guides, material specs |
| `luxury` | Editorial restraint, heritage storytelling, exclusivity |

### Traffic Sources (pick one or more)

Ad platform-specific landing page optimization:

| Source | Optimization |
|--------|-------------|
| `meta-ads` | Warm traffic, social proof heavy, video-native, lookalike audiences |
| `google-ads` | Intent-driven, feature-first, comparison-ready, keyword match |
| `tiktok-ads` | Scroll-stopping, UGC-style, fast cuts, youth-optimized |

## Manual Installation

<details>
<summary><strong>Claude Code</strong></summary>

```bash
# From any pack (core/, verticals/beauty/, traffic-sources/meta-ads/)
cp -r claude/skills/* /path/to/project/.claude/skills/
cp -r claude/commands/* /path/to/project/.claude/commands/  # core only
```

</details>

<details>
<summary><strong>OpenAI Codex</strong></summary>

```bash
cp -r codex/skills/* /path/to/project/.agents/skills/
cp codex/AGENTS.md /path/to/project/   # core only
```

</details>

<details>
<summary><strong>Cursor</strong></summary>

```bash
mkdir -p /path/to/project/.cursor/rules
cp -r cursor/rules/* /path/to/project/.cursor/rules/
```

</details>

<details>
<summary><strong>Custom GPT</strong></summary>

1. Paste `gpt/instructions.md` → GPT Instructions field
2. Upload `gpt/knowledge.md` → GPT Knowledge file

</details>

## MCP Server Setup

Connect the Lexsis AI MCP server for full tool access (image generation, publishing, analytics):

```json
{
  "mcpServers": {
    "lexsis-ai": {
      "type": "http",
      "url": "https://mcp.trylexsis.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

Get your API key: [trylexsis.com/settings/api-keys](https://trylexsis.com/settings/api-keys)

Pre-built configs for each platform are in the `mcp/` directory.

## Visual Verification (Recommended)

Skills instruct the AI to screenshot pages after generating them. Install [Playwright MCP](https://playwright.dev/docs/getting-started-mcp) for automatic visual QA:

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

## How Generation Works

All skills follow a two-phase approach:

```
Phase 0: Context     → get_workspace + get_brand_kit + get_design_md
Phase 1: Assets      → search_design_library → generate_asset (if needed)
Phase 2A: HTML       → Pure HTML + Tailwind (fast iteration, no islands)
Phase 2B: Islands    → Map commerce components (BuyBox, Cart, Reviews)
Phase 3: Validate    → validate_vibe_page
Phase 4: Publish     → publish_vibe_page → screenshot → verify
```

Phase 2A renders instantly in any browser. Phase 2B adds interactive commerce via React islands that hydrate client-side.

## Available Commands (after installing core)

| Command | What It Does |
|---------|-------------|
| `/generate-pdp` | Product detail page (BuyBox, gallery, reviews) |
| `/generate-landing-page` | Campaign landing (message match, zero nav) |
| `/generate-homepage` | Brand homepage (nav, collections, story) |
| `/generate-collection` | Product grid with filters |
| `/generate-listicle` | SEO comparison/top-10 page |
| `/generate-bundle` | Bundle builder with discount tiers |
| `/generate-editorial` | Magazine-style shoppable content |
| `/convert-ad` | Ad creative → landing page |
| `/redesign-page` | Modernize existing page |
| `/remix-competitor` | Adapt competitor design to your brand |
| `/personalize-page` | Per-persona variants |
| `/ab-test` | Hypothesis-driven split test |
| `/setup-brand` | First-time brand configuration |
| `/add-section` | Quick-insert section into existing page |

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for how to add new verticals or traffic sources.

## License

MIT — see [LICENSE](./LICENSE)

---

Built with [Lexsis AI](https://trylexsis.com) — AI-Powered Shopify Landing Page Builder
