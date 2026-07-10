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
git clone https://github.com/Aetheria-Labs1/storefront-skills.git
cp -r storefront-skills/codex/skills/* .agents/skills/
cp storefront-skills/codex/AGENTS.md .
```
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
| `lexsis-storefront-skills` | **Core** | 28 skills + 7 commands + 2 agents + MCP config |
| `lexsis-beauty-skills` | Vertical | Beauty/skincare patterns |
| `lexsis-supplements-skills` | Vertical | Supplement/wellness patterns |
| `lexsis-fashion-skills` | Vertical | Fashion/apparel patterns |
| `lexsis-food-skills` | Vertical | Food/beverage DTC patterns |
| `lexsis-home-skills` | Vertical | Home goods/decor patterns |
| `lexsis-luxury-skills` | Vertical | Luxury/premium patterns |

> Traffic source skills (Meta, Google, TikTok) shipping separately — coming soon.

## Commands (after installing core)

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

Add a new vertical:
1. Create skill: `plugins/lexsis-{name}-skills/skills/{name}-expertise/SKILL.md`
2. Add plugin.json: `plugins/lexsis-{name}-skills/.claude-plugin/plugin.json`
3. PR it

## License

MIT — [LICENSE](./LICENSE)

---

Built with [Lexsis AI](https://trylexsis.com)
