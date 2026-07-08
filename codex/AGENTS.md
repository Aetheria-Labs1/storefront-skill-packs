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

## Available Skills

- **generation-protocol** (knowledge) — How Pages Are Built
- **cro-research** (knowledge) — 2026 Landing Page Best Practices
- **storefront-craft** (knowledge) — Start Here
- **workflow-orchestration** (knowledge) — Execution Engine
- **conversion-psychology** (knowledge) — Storefront Design Intelligence
- **visual-craft** (knowledge) — Typography, Spacing, Color & Polish
- **island-patterns** (knowledge) — Wrapper HTML & Combination Recipes
- **qa-recipe** (knowledge) — QA Recipe
- **page-generation** (operational) — Storefront Page Generation
- **design-assets** (operational) — Design Assets & Brand Management
- **publishing** (operational) — Storefront Publishing & Lifecycle
- **page-editing** (operational) — Storefront Page Editing
- **analytics** (operational) — Storefront Analytics & Experiments
- **generate-pdp** (operational) — Product Detail Page (PDP) Generation
- **generate-landing-page** (operational) — Campaign / Ad Landing Page Generation
- **generate-homepage** (operational) — Brand Homepage Generation
- **generate-collection** (operational) — Collection / Category Page Generation
- **generate-listicle** (operational) — SEO Listicle / Comparison Page Generation
- **generate-bundle-page** (operational) — Bundle Builder Page Generation
- **generate-editorial** (operational) — Editorial / Magazine-Style Page Generation
- **ad-to-page** (operational) — Ad Creative to Landing Page
- **page-redesign** (operational) — Page Redesign (Modernize/Refresh Existing Page)
- **competitor-remix** (operational) — Competitor Remix (Rebuild from Reference URL)
- **personalization-variant** (operational) — Personalization Variant (Persona-Specific Page Versions)
- **ab-test-variant** (operational) — A/B Test Variant (Hypothesis-Driven Experiment)
- **section-library** (operational) — Quick Section Insert
- **cart-composition** (operational) — DrawerShell + Atomic Islands
- **cart-v2-management** (operational) — MCP Workflow

## Commands

- `generate` — Generate a complete Shopify storefront page — auto-detects page type (landing, PDP, collection, homepage, editorial, listicle, bundle) and applies conversion-optimized patterns
- `optimize` — CRO-optimize an existing page — analyzes conversion weaknesses and applies fixes (redesign sections, add trust signals, fix CTAs, improve mobile UX)
- `remix` — Rebuild a competitor page or ad creative adapted to your brand — extracts structure and conversion patterns, regenerates with your products and design tokens
- `experiment` — Set up A/B tests, personalization variants, and monitor experiment results — hypothesis-driven testing with statistical significance tracking
- `cart` — Configure the Cart V2 drawer — add upsells, progress bars, conditional rules, announcement banners, and checkout customization
- `publish` — QA check and publish a page — validates structure, verifies islands, checks mobile rendering, then publishes live or to Shopify
