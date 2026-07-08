# Lexsis AI — Core Skills

AI-powered Shopify storefront builder. 2 agents + 6 commands for page generation, CRO optimization, and publishing.

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

## Skills

- **storefront-engine** — Core orchestrator for page generation workflows
- **browser-analyze** — Use @Browser to analyze competitor pages, extract design tokens, and run CRO audits

## Commands

- **generate** — Generate a complete Shopify storefront page — auto-detects page type (landing, PDP, collection, homepage, editorial, listicle, bundle) and applies conversion-optimized patterns
- **optimize** — CRO-optimize an existing page — analyzes conversion weaknesses and applies fixes (redesign sections, add trust signals, fix CTAs, improve mobile UX)
- **remix** — Rebuild a competitor page or ad creative adapted to your brand — extracts structure and conversion patterns, regenerates with your products and design tokens
- **experiment** — Set up A/B tests, personalization variants, and monitor experiment results — hypothesis-driven testing with statistical significance tracking
- **cart** — Configure the Cart V2 drawer — add upsells, progress bars, conditional rules, announcement banners, and checkout customization
- **publish** — QA check and publish a page — validates structure, verifies islands, checks mobile rendering, then publishes live or to Shopify

## Knowledge Reference

All domain knowledge lives in `skills/storefront-engine/reference/`. Read the relevant file when you need it:

- `generation-protocol.md` (knowledge)
- `cro-research.md` (knowledge)
- `storefront-craft.md` (knowledge)
- `workflow-orchestration.md` (knowledge)
- `conversion-psychology.md` (knowledge)
- `visual-craft.md` (knowledge)
- `island-patterns.md` (knowledge)
- `qa-recipe.md` (knowledge)
- `page-generation.md` (operational)
- `design-assets.md` (operational)
- `publishing.md` (operational)
- `page-editing.md` (operational)
- `analytics.md` (operational)
- `generate-pdp.md` (operational)
- `generate-landing-page.md` (operational)
- `generate-homepage.md` (operational)
- `generate-collection.md` (operational)
- `generate-listicle.md` (operational)
- `generate-bundle-page.md` (operational)
- `generate-editorial.md` (operational)
- `ad-to-page.md` (operational)
- `page-redesign.md` (operational)
- `competitor-remix.md` (operational)
- `personalization-variant.md` (operational)
- `ab-test-variant.md` (operational)
- `section-library.md` (operational)
- `cart-composition.md` (operational)
- `cart-v2-management.md` (operational)
