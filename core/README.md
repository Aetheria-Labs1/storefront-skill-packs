# Lexsis AI — Core Skills

Foundation knowledge + all operational workflows. Install this first — works for any vertical.

## What's Included

### Knowledge Skills (work standalone — no MCP required)
- **generation-protocol** — expert domain knowledge
- **cro-research** — expert domain knowledge
- **storefront-craft** — expert domain knowledge
- **workflow-orchestration** — expert domain knowledge
- **conversion-psychology** — expert domain knowledge
- **visual-craft** — expert domain knowledge
- **animation-system** — expert domain knowledge
- **design-enrichment** — expert domain knowledge
- **premium-patterns** — expert domain knowledge
- **island-patterns** — expert domain knowledge
- **qa-recipe** — expert domain knowledge

### Operational Skills (enhanced with Lexsis AI MCP)
- **page-generation** — workflow automation
- **design-assets** — workflow automation
- **publishing** — workflow automation
- **page-editing** — workflow automation
- **analytics** — workflow automation
- **generate-pdp** — workflow automation
- **generate-landing-page** — workflow automation
- **generate-homepage** — workflow automation
- **generate-collection** — workflow automation
- **generate-listicle** — workflow automation
- **generate-bundle-page** — workflow automation
- **generate-editorial** — workflow automation
- **ad-to-page** — workflow automation
- **page-redesign** — workflow automation
- **competitor-remix** — workflow automation
- **personalization-variant** — workflow automation
- **ab-test-variant** — workflow automation
- **brand-setup** — workflow automation
- **section-library** — workflow automation

### Commands
- `/generate-page` — Generate a complete Shopify landing page — auto-detects vertical and applies best patterns
- `/optimize-page` — Analyze and optimize an existing page for better conversions
- `/create-assets` — Generate brand-matched visual assets — search library first, generate if needed
- `/run-experiment` — Set up an A/B test with a variant page and monitor results
- `/generate-pdp` — Generate a product detail page optimized for conversions
- `/generate-homepage` — Generate a brand homepage with navigation and collections
- `/generate-collection` — Generate a collection/category page with filterable product grid
- `/generate-bundle` — Generate a bundle builder page with discount tiers
- `/generate-editorial` — Generate a magazine-style editorial page with shoppable products
- `/generate-listicle` — Generate an SEO-optimized comparison/listicle page
- `/convert-ad` — Convert an ad creative into a message-matched landing page
- `/redesign-page` — Redesign an existing page while preserving SEO and performance
- `/remix-competitor` — Rebuild a competitor page adapted to your brand
- `/personalize-page` — Generate persona-specific variants of an existing page
- `/ab-test` — Create a hypothesis-driven A/B test variant and set up experiment
- `/setup-brand` — First-time brand configuration — extract design from URL, set up kit and theme
- `/add-section` — Quick-insert a section into an existing page from the section library

## Installation

### Quick Install (auto-detects your platform)

```bash
chmod +x install.sh && ./install.sh
```

### Manual Install

<details>
<summary><strong>Claude Code</strong></summary>

1. Copy `claude/skills/` into your project's `.claude/skills/`
2. Copy `claude/commands/` into your project's `.claude/commands/`
3. Add MCP config from `mcp/mcp.json` to your `.mcp.json`

```bash
cp -r claude/skills/* .claude/skills/
cp -r claude/commands/* .claude/commands/
# Then merge mcp/mcp.json into your .mcp.json
```
</details>

<details>
<summary><strong>OpenAI Codex</strong></summary>

1. Copy `codex/skills/` into your project's `.agents/skills/`
2. Copy `codex/AGENTS.md` to your project root (or merge with existing)

```bash
cp -r codex/skills/* .agents/skills/
cp codex/AGENTS.md .
```
</details>

<details>
<summary><strong>Cursor</strong></summary>

1. Copy `cursor/rules/` into your project's `.cursor/rules/`

```bash
mkdir -p .cursor/rules
cp -r cursor/rules/* .cursor/rules/
```
</details>

<details>
<summary><strong>Custom GPT</strong></summary>

1. Open `gpt/instructions.md` — paste into your GPT's Instructions field
2. Upload `gpt/knowledge.md` as a Knowledge file in GPT configuration
</details>

## Connect Lexsis AI MCP Server

For full tool access (image generation, page publishing, analytics), connect the MCP server:

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

Get your API key at [trylexsis.com/settings/api-keys](https://trylexsis.com/settings/api-keys)

## Usage

Once installed, use these commands in your AI assistant:

### `/generate-page`
Generate a complete Shopify landing page — auto-detects vertical and applies best patterns

### `/optimize-page`
Analyze and optimize an existing page for better conversions

### `/create-assets`
Generate brand-matched visual assets — search library first, generate if needed

### `/run-experiment`
Set up an A/B test with a variant page and monitor results

### `/generate-pdp`
Generate a product detail page optimized for conversions

### `/generate-homepage`
Generate a brand homepage with navigation and collections

### `/generate-collection`
Generate a collection/category page with filterable product grid

### `/generate-bundle`
Generate a bundle builder page with discount tiers

### `/generate-editorial`
Generate a magazine-style editorial page with shoppable products

### `/generate-listicle`
Generate an SEO-optimized comparison/listicle page

### `/convert-ad`
Convert an ad creative into a message-matched landing page

### `/redesign-page`
Redesign an existing page while preserving SEO and performance

### `/remix-competitor`
Rebuild a competitor page adapted to your brand

### `/personalize-page`
Generate persona-specific variants of an existing page

### `/ab-test`
Create a hypothesis-driven A/B test variant and set up experiment

### `/setup-brand`
First-time brand configuration — extract design from URL, set up kit and theme

### `/add-section`
Quick-insert a section into an existing page from the section library


---

Built with [Lexsis AI](https://trylexsis.com) — AI-powered Shopify Landing Page Builder
