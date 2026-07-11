# Lexsis AI — Storefront Skills

> Native AI workflows for building high-converting Shopify storefronts with Claude Code and OpenAI Codex.

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

## Install (OpenAI Codex)

Run these commands in your terminal:

```bash
# 1. Register the Lexsis marketplace (one-time)
codex plugin marketplace add Aetheria-Labs1/storefront-skills --ref main

# 2. Install the storefront plugin
codex plugin add lexsis-storefront-skills@lexsis-storefront
```

Start a new Codex task after installation. Complete the `lexsis-ai` OAuth prompt when Codex requests access to the bundled MCP server.

Codex selects skills automatically from your request. You can also invoke any workflow directly with `$skill-name`, for example `$generate`, `$browser-analyze`, or `$cart`. Plugin-defined slash commands such as `/generate` are Claude-only.

Verify or update the installation:

```bash
# Show installed plugin and version
codex plugin list

# Fetch marketplace updates, then reinstall the latest plugin version
codex plugin marketplace upgrade lexsis-storefront
codex plugin add lexsis-storefront-skills@lexsis-storefront
```

Codex Browser is optional. URL analysis and draft QA use it when available; otherwise skills fall back to Lexsis server-side design extraction.

## Install (Other Platforms)

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
| `$storefront-engine` | Route broad, multi-step storefront requests to the right workflow |
| `$browser-analyze` | Audit a storefront URL using Codex Browser when available |
| `$analyze-page` | Turn page evidence into a reproducible design and CRO brief |
| `$cart` | Configure Cart V2 composition, upsells, and behavior |
| `$experiment` | Set up A/B tests and personalization variants |
| `$extract-island` | Convert a page component into a reusable island layout |
| `$generate` | Generate a Shopify page with planning, validation, and draft-first publishing |
| `$optimize` | Improve an existing page for conversion |
| `$plan-page` | Create a page blueprint before generation |
| `$publish` | Validate, preview, and publish with explicit live approval |
| `$remix` | Adapt competitor or ad patterns to a brand |
| `$search-docs` | Search Lexsis workflows, island schemas, and reference material |

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

Core plugin auto-configures the Lexsis AI MCP server.

- **Codex:** complete OAuth when prompted. No manual MCP configuration is required.
- **Claude Code:** get an API key at [app.trylexsis.com/settings/api-key](https://app.trylexsis.com/settings/api-key), then add it to the `lexsis-ai` MCP server's `Authorization` header in Claude Code settings.

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
