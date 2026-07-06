# Lexsis AI — Food DTC Vertical

Industry-specific patterns for food/beverage DTC brands. Install alongside core.

## What's Included

### Knowledge Skills (work standalone — no MCP required)
- **food-expertise** — expert domain knowledge

### Operational Skills (enhanced with Lexsis AI MCP)


### Commands


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



---

Built with [Lexsis AI](https://trylexsis.com) — AI-powered Shopify Landing Page Builder
