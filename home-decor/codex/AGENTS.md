# Home & Decor — Room Context Pages

Build context-rich landing pages for furniture, decor, candles, and textiles brands.

## MCP Server

Connect the Lexsis AI MCP server for full tool access:

```json
{
  "mcpServers": {
    "lexsis-ai": {
      "type": "http",
      "url": "https://mcp.trylexsis.com/mcp",
      "headers": { "Authorization": "Bearer <your-api-key>" }
    }
  }
}
```

## Available Skills

- **storefront-craft** (knowledge) — Start Here
- **workflow-orchestration** (knowledge) — Execution Engine
- **conversion-psychology** (knowledge) — Storefront Design Intelligence
- **home-expertise** (knowledge) — Storefront Design Intelligence
- **google-traffic** (knowledge) — Storefront Design Intelligence
- **visual-craft** (knowledge) — Typography, Spacing, Color & Polish
- **premium-patterns** (knowledge) — High-Converting Section Templates
- **design-enrichment** (knowledge) — AI Image Generation & Compositing
- **island-patterns** (knowledge) — Wrapper HTML & Combination Recipes
- **page-generation** (operational) — Storefront Page Generation
- **design-assets** (operational) — Design Assets & Brand Management
- **publishing** (operational) — Storefront Publishing & Lifecycle
- **page-editing** (operational) — Storefront Page Editing
- **analytics** (operational) — Storefront Analytics & Experiments

## Commands

- `generate-home-page` — Generate a home/decor page with room context photography and material storytelling
- `create-room-context-assets` — Generate lifestyle room shots and dimension-aware product composites
