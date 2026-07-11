# Lexsis AI — Codex Skills

AI-powered Shopify storefront workflows for Codex. Plugin includes 12 skills, Lexsis AI MCP configuration, 257 shared reference files, and optional Codex Browser integration.

## Invocation

Codex selects focused skills from task descriptions. Invoke one explicitly with `$skill-name` when needed. Plugin-defined slash commands such as `/generate` are not available in Codex.

## Skills

- `storefront-engine` — Route broad, multi-step storefront requests.
- `browser-analyze` — Extract design and CRO evidence from a reference URL.
- `analyze-page` — Create a reproducible page-design brief.
- `cart` — Configure Cart V2 composition and behavior.
- `experiment` — Set up A/B tests and personalization variants.
- `extract-island` — Convert a page component into a reusable island layout.
- `generate` — Generate every supported page type.
- `optimize` — Improve an existing page for conversion.
- `plan-page` — Create a page blueprint before generation.
- `publish` — Validate, preview, and publish with explicit live approval.
- `remix` — Adapt competitor or ad patterns to a brand.
- `search-docs` — Search Lexsis documentation and schemas.

## MCP and Browser

The plugin configures `lexsis-ai` at `https://mcp.trylexsis.com/mcp`. Use its tools for storefront data, assets, validation, and publishing; complete OAuth when Codex requests it.

Use Codex Browser for live reference-page analysis and draft visual QA when available. If Browser is unavailable, use Lexsis `extract_brand_design` and state that DOM, interaction, and mobile viewport checks were unavailable.

## Safety

- Check credits before any paid asset generation, image editing, page mutation, or publish operation.
- Validate page data before writing or publishing.
- Publish drafts first. Require explicit user approval before a live publish.
- Preview a section update before committing it. Confirm destructive removal or replacement.

## Reference Knowledge

Shared knowledge lives under `skills/storefront-engine/reference/`. Page-specific workflows such as `generate-pdp.md`, `generate-homepage.md`, `ab-test-variant.md`, and `cart-v2-management.md` remain references loaded by the 12 skills; they are not separate skills. Island documentation contains contracts, schemas, and layout JSON; use those exact schemas instead of inventing island props.
