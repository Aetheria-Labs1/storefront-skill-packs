# Food & Beverage — DTC Landing Pages

Build sensory-driven landing pages for food, coffee, snacks, and meal kit DTC brands.

## What's Included

### Knowledge Skills (work standalone — no MCP required)
- **storefront-craft** — expert domain knowledge
- **workflow-orchestration** — expert domain knowledge
- **conversion-psychology** — expert domain knowledge
- **food-expertise** — expert domain knowledge
- **meta-traffic** — expert domain knowledge
- **visual-craft** — expert domain knowledge
- **premium-patterns** — expert domain knowledge
- **island-patterns** — expert domain knowledge

### Operational Skills (enhanced with Lexsis AI MCP)
- **page-generation** — workflow automation
- **design-assets** — workflow automation
- **publishing** — workflow automation
- **page-editing** — workflow automation
- **analytics** — workflow automation

### Commands
- `/generate-food-page` — Generate a food/beverage landing page with sensory photography and warm palettes
- `/optimize-food-subscription` — Optimize a food brand page for subscription conversion — trial offers, frequency selection

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

### `/generate-food-page`
Generate a food/beverage landing page with sensory photography and warm palettes

### `/optimize-food-subscription`
Optimize a food brand page for subscription conversion — trial offers, frequency selection


---

Built with [Lexsis AI](https://trylexsis.com) — AI-powered Shopify Landing Page Builder
