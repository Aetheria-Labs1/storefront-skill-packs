# Lexsis AI — Storefront Skills

> AI skills for building high-converting Shopify landing pages. One command to install.

## Install (Claude Code)

```bash
# 1. Register marketplace (one-time)
/plugin marketplace add lexsis https://github.com/Aetheria-Labs1/storefront-skills

# 2. Install core skills (required — all page types + workflows)
/plugin install lexsis-storefront-skills@lexsis

# 3. Add your industry vertical (optional)
/plugin install lexsis-beauty-skills@lexsis
```

Done. Skills auto-load, MCP auto-configures, commands available immediately.

## Install (Other Platforms)

<details>
<summary><strong>OpenAI Codex</strong></summary>

```bash
# Register or refresh marketplace
codex plugin marketplace add Aetheria-Labs1/storefront-skills --ref main

# Install Lexsis Codex plugin
codex plugin add lexsis-storefront-skills@lexsis-storefront
```

Codex selects workflows automatically from your request. Invoke one of the 12 workflows with `$generate`, `$browser-analyze`, `$cart`, or another `$skill-name`; custom `/generate` commands are Claude-only.

Codex Browser is optional. URL analysis and draft QA use it when available, otherwise skills fall back to Lexsis server-side design extraction.
</details>

<details>
<summary><strong>Cursor</strong></summary>

```bash
git clone https://github.com/Aetheria-Labs1/storefront-skills.git
mkdir -p .cursor/rules
cp -r storefront-skills/cursor/rules/* .cursor/rules/
```
</details>

<details>
<summary><strong>Custom GPT</strong></summary>

1. Copy `gpt/instructions.md` → paste into GPT Instructions
2. Upload `gpt/knowledge.md` as Knowledge file
</details>

## Available Plugins

| Plugin | Type | What It Adds |
|--------|------|-------------|
| `lexsis-storefront-skills` | **Core** | 12 Codex skills, 10 Claude commands, 257 references, and MCP config |
| `lexsis-beauty-skills` | Vertical | Beauty/skincare patterns |
| `lexsis-supplements-skills` | Vertical | Supplement/wellness patterns |
| `lexsis-fashion-skills` | Vertical | Fashion/apparel patterns |
| `lexsis-food-skills` | Vertical | Food/beverage DTC patterns |
| `lexsis-home-skills` | Vertical | Home goods/decor patterns |
| `lexsis-luxury-skills` | Vertical | Luxury/premium patterns |

> Traffic source skills (Meta, Google, TikTok) shipping separately — coming soon.

## Codex Skills

Codex supports skills rather than plugin-defined slash commands. Use natural language for automatic skill selection, or select one directly with `$skill-name`.

| Skill | What It Does |
|-------|--------------|
| `$generate` | Generate a Shopify page with planning, validation, and draft-first publishing |
| `$browser-analyze` | Audit a storefront URL using Codex Browser when available |
| `$analyze-page` / `$extract-island` | Analyze a reference page or turn a component into a reusable island layout |
| `$cart` | Configure Cart V2 and related islands |
| `$experiment` | Run experiments and create page variants |
| `$optimize`, `$remix`, `$plan-page`, `$publish` | Optimize, adapt, plan, and safely publish pages |

Page-type and specialist workflows such as `generate-pdp.md`, `generate-homepage.md`, `ab-test-variant.md`, and `cart-v2-management.md` remain shared references used by these skills. They are not duplicated as standalone Codex skills.

## Claude Code Commands (after installing core)

| Command | What It Does |
|---------|-------------|
| `/generate` | Generate a Shopify page — auto-detects type (PDP, landing, collection, homepage, editorial, listicle, bundle) |
| `/optimize` | CRO-optimize an existing page — fix CTAs, trust signals, mobile UX |
| `/remix` | Rebuild a competitor page or ad creative adapted to your brand |
| `/experiment` | Set up A/B tests, personalization variants, monitor results |
| `/cart` | Configure Cart V2 drawer — upsells, progress bars, conditional rules |
| `/publish` | QA check and publish a page to Shopify |
| `/search-docs` | Search documentation — islands, skills, conversion patterns, workflows |

## MCP Server

Core plugin auto-configures the Lexsis AI MCP server. You'll need your API key:

1. Get key at [app.trylexsis.com/settings/api-key](https://app.trylexsis.com/settings/api-key)
2. Add to your Claude Code settings under MCP server `lexsis-ai` → headers → Authorization

## Visual Verification

Skills instruct Claude to screenshot pages after generation. Install [Playwright MCP](https://playwright.dev/docs/getting-started-mcp) for automatic visual QA:

```bash
/plugin install playwright@claude-plugins-official
```

Codex workflows use Codex Browser when enabled. Browser is optional; URL analysis falls back to Lexsis server-side extraction when it is unavailable.

## How It Works

```
Skills (this repo)          → teaches AI how to build pages
MCP Server (mcp.trylexsis.com) → provides tools (generate, publish, analyze)
Playwright (optional)       → visual verification via screenshots
```

## Repo Structure

```
storefront-skills/
├── plugins/                         ← Claude Code marketplace plugins
│   ├── lexsis-storefront-skills/    ← Core (required)
│   ├── lexsis-beauty-skills/        ← Vertical add-ons
│   ├── lexsis-supplements-skills/
│   ├── lexsis-fashion-skills/
│   ├── lexsis-food-skills/
│   ├── lexsis-home-skills/
│   └── lexsis-luxury-skills/
├── codex/                           ← OpenAI Codex format
├── cursor/                          ← Cursor rules
└── gpt/                             ← Custom GPT knowledge
```

## Contributing

We welcome contributions! See [CONTRIBUTING.md](./CONTRIBUTING.md) for:
- How to add a new vertical plugin
- How to add a core skill or command
- Skill file structure and conventions
- PR process and local testing

## License

MIT — [LICENSE](./LICENSE)

---

Built with [Lexsis AI](https://trylexsis.com)
