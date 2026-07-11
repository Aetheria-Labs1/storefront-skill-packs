# Lexsis AI — Codex Skills

AI-powered Shopify storefront workflows for Codex. Plugin includes 32 skills, Lexsis AI MCP configuration, 257 shared reference files, and optional Codex Browser integration.

## Invocation

Codex selects focused skills from task descriptions. Invoke one explicitly with `$skill-name` when needed. Plugin-defined slash commands such as `/generate` are not available in Codex.

## Automatic Skills

- `storefront-engine` — Route broad, multi-step storefront requests.
- `browser-analyze` — Extract design and CRO evidence from a reference URL.
- `analyze-page` — Create a reproducible page-design brief.
- `cro-analyzer` — Return a structured CRO blueprint for an ecommerce URL.
- `page-builder` — Build and validate a storefront draft from a brief or CRO blueprint.
- `generate`, `optimize`, `remix`, `plan-page`, `cart`, `experiment`, `publish` — Core storefront workflows.
- `extract-island`, `search-docs` — Component extraction and Lexsis knowledge lookup.

## Explicit Workflow Aliases

Use these with `$` to choose a narrow entry point: `generate-page`, `optimize-page`, `create-assets`, `run-experiment`, `generate-pdp`, `generate-homepage`, `generate-collection`, `generate-bundle`, `generate-editorial`, `generate-listicle`, `convert-ad`, `redesign-page`, `remix-competitor`, `personalize-page`, `ab-test`, `setup-brand`, `add-section`, and `setup-cart`.

## MCP and Browser

The plugin configures `lexsis-ai` at `https://mcp.trylexsis.com/mcp`. Use its tools for storefront data, assets, validation, and publishing; complete OAuth when Codex requests it.

Use Codex Browser for live reference-page analysis and draft visual QA when available. If Browser is unavailable, use Lexsis `extract_brand_design` and state that DOM, interaction, and mobile viewport checks were unavailable.

## Safety

- Check credits before any paid asset generation, image editing, page mutation, or publish operation.
- Validate page data before writing or publishing.
- Publish drafts first. Require explicit user approval before a live publish.
- Preview a section update before committing it. Confirm destructive removal or replacement.

## Reference Knowledge

Shared knowledge lives under `skills/storefront-engine/reference/`. Read only relevant files. Island documentation contains contracts, schemas, and layout JSON; use those exact schemas instead of inventing island props.
