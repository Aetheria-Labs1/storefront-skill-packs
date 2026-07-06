# Lexsis AI — Core Skills

Foundation knowledge + all operational workflows. Install this first — works for any vertical.

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
- **animation-system** (knowledge) — Vibe-Code Reference
- **design-enrichment** (knowledge) — AI Image Generation & Compositing
- **premium-patterns** (knowledge) — High-Converting Section Templates
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
- **brand-setup** (operational) — First-Time Brand Setup
- **section-library** (operational) — Quick Section Insert

## Commands

- `generate-page` — Generate a complete Shopify landing page — auto-detects vertical and applies best patterns
- `optimize-page` — Analyze and optimize an existing page for better conversions
- `create-assets` — Generate brand-matched visual assets — search library first, generate if needed
- `run-experiment` — Set up an A/B test with a variant page and monitor results
- `generate-pdp` — Generate a product detail page optimized for conversions
- `generate-homepage` — Generate a brand homepage with navigation and collections
- `generate-collection` — Generate a collection/category page with filterable product grid
- `generate-bundle` — Generate a bundle builder page with discount tiers
- `generate-editorial` — Generate a magazine-style editorial page with shoppable products
- `generate-listicle` — Generate an SEO-optimized comparison/listicle page
- `convert-ad` — Convert an ad creative into a message-matched landing page
- `redesign-page` — Redesign an existing page while preserving SEO and performance
- `remix-competitor` — Rebuild a competitor page adapted to your brand
- `personalize-page` — Generate persona-specific variants of an existing page
- `ab-test` — Create a hypothesis-driven A/B test variant and set up experiment
- `setup-brand` — First-time brand configuration — extract design from URL, set up kit and theme
- `add-section` — Quick-insert a section into an existing page from the section library
