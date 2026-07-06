---
description: First-time brand configuration — extract design from URL, set up kit and theme
allowed-tools: mcp__lexsis-ai__*
---

# /setup-brand

First-time brand configuration — extract design from URL, set up kit and theme

## Prerequisites

Connect the Lexsis AI MCP server:
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

## Loaded Knowledge

### visual-craft

# Visual Craft — Typography, Spacing, Color & Polish
Techniques for making vibe-code pages look premium. Load when polishing visual quality.
## Typography Hierarchy
### Fluid Sizing (clamp)
## Spacing Rhythm
### Section Padding
## Color Usage
### Accent Application
## Image Treatment
### Rounded + Shadow (product cards)
## Micro-Interactions
### Button States
## Glass Morphism
```html
<div class="backdrop-blur-md rounded-2xl p-6 border border-white/20" style="background:rgba(255,255,255,0.1)">
  Frosted glass card
</div>
```
## Grain/Noise Texture
```css
.grain::before {
  content: '';
  position: absolute;
  inset: 0;
  opacity: 0.03;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  pointer-events: none;
}
```
## Responsive Patterns
### Grid Collapse

## Workflow

# First-Time Brand Setup

Bootstrap a new workspace — verify connectivity, extract brand identity, configure the kit and theme, and verify everything renders correctly with `--lx-*` CSS variables.

## When to Use

- New merchant onboarding (no brand kit exists yet)
- Reconnecting or reconfiguring an existing store
- Extracting brand identity from an existing website URL
- Resetting brand kit after a rebrand

## Prerequisites

- Shopify store credentials (domain + access token) OR an existing connected store
- A reference URL to extract brand design from (merchant's live site, competitor, or mood board)
- Workspace must be provisioned (the MCP session implies this)

## Flow

### 1. Check workspace exists

```
get_workspace_details
```

- Confirms workspace ID, plan tier, and session validity
- If workspace missing or invalid: abort with clear error

### 2. Check store connection

```
get_connected_stores
```

- If store already connected: proceed to step 3
- If no store: store provisioning happens via Shopify OAuth (outside MCP) — instruct user to connect store first

### 3. Collect reference URL

Ask user for their store URL or an existing site URL for design extraction:
- "What URL should I extract your brand design from? (Your Shopify store, existing website, or a reference site you like)"

### 4. Extract brand design from URL

```
extract_brand_design({ url })
```

- Pulls: primary/secondary/accent colors, font families, spacing scale, logo URL, imagery style, tone of voice
- Works on any public URL (Shopify store, competitor, portfolio site)
- If extraction fails: fall back to manual input (ask for colors, fonts, logo URL)

### 5. Check existing brand kit

```
get_brand_kit
```

- If kit exists and user wants to override: proceed with update
- If kit exists and user wants to keep: skip to step 7
- If no kit: create new from extracted values

### 6. Present extracted values for confirmation

Show user the extracted brand values and ask for confirmation/adjustment:

```
Extracted brand identity:
- Primary color: #4F46E5
- Secondary color: #10B981
- Accent color: #F59E0B
- Heading font: Playfair Display
- Body font: Inter
- Logo URL: https://...
- Border radius: 8px
- Voice/tone: Premium, confident

Does this look right? Any adjustments?
```

Wait for user confirmation before proceeding.

### 7. Update brand kit

Update brand kit with confirmed values via the Golem API (brand kit is managed there, not via MCP tool directly). The MCP session carries the auth context.

### 8. Apply to default theme

```
list_themes
```

Then:

```
update_theme({
  colors: { primary, secondary, accent, background, surface, text },
  typography: { heading_font, body_font, scale_ratio },
  spacing: { base_unit, section_padding },
  borders: { radius, style },
  logo_url,
  favicon_url
})
```

- All `--lx-*` CSS variables must be populated
- Fonts must be valid Google Fonts families or system font stacks

### 9. Verify design library access

```
search_design_library({ query: "brand" })
```

- Confirm assets (logo, favicon, OG image) are accessible
- If missing: prompt user to upload or use `import_asset`

### 10. Verify product catalog synced

```
list_products({ limit: 5 })
```

- Confirm products synced from Shopify
- If empty: warn user that product-based sections won't render

### 11. Generate test section to verify brand rendering

Create a simple hero section using the brand colors, fonts, and logo:

```html
<section class="py-16 md:py-24 px-4" style="background-color: var(--lx-bg-color)">
  <div class="max-w-6xl mx-auto text-center">
    <img src="{logo_url}" alt="{brand_name}" class="h-12 mx-auto mb-8" />
    <h1 class="text-4xl md:text-5xl font-bold mb-4" style="font-family: var(--lx-font-heading); color: var(--lx-text-color)">
      Your Brand, Beautifully Rendered
    </h1>
    <p class="text-lg mb-8" style="font-family: var(--lx-font-body); color: var(--lx-text-muted)">
      This is a test section to verify your brand kit renders correctly.
    </p>
    <a href="#" class="inline-block px-8 py-3 rounded-lg text-white font-semibold" style="background-color: var(--lx-accent-color)">
      Test CTA Button
    </a>
  </div>
</section>
```

Publish as draft:

```
publish_vibe_page({ ... draft: true })
```

Visually verify:
- Fonts loading correctly (not system fallback)?
- Brand colors applied (not default purple)?
- Logo rendering (not 404/broken)?
- CTA button has proper contrast?

### 12. Confirm to user

"Brand configured. Ready to generate pages."

## Decision Points

| Scenario | Action |
|---|---|
| Store not connected | Instruct user to complete Shopify OAuth first |
| Brand kit already exists | Ask: override, merge, or keep existing? |
| URL extraction fails | Fall back to manual input (ask for colors, fonts, logo) |
| No products synced yet | Warn user; product sections will show placeholders |
| Multiple themes needed | Create default first, additional via separate `update_theme` calls |
| Colors fail contrast check | Suggest adjusted shade that passes WCAG AA |

## Quality Checks

- All `--lx-*` CSS variables populated (no fallback `unset` values):
  - `--lx-accent-color`, `--lx-accent-color-hover`
  - `--lx-text-color`, `--lx-text-muted`
  - `--lx-bg-color`, `--lx-bg-surface`, `--lx-surface-alt`
  - `--lx-border-color`
  - `--lx-font-heading`, `--lx-font-body`
- Logo URL accessible (not 404, correct MIME type)
- Fonts from Google Fonts or brand CDN (valid URL)
- Color contrast WCAG AA: 4.5:1 for normal text, 3:1 for large text
- If extracted colors fail contrast: suggest adjustment with passing alternative
- At least one product visible in catalog
- Test section renders without validation errors

## Deprecated Tools (DO NOT USE)

| Removed | Replacement |
|---------|-------------|
| `get_theme_json` | `get_brand_kit` (includes theme data) |
| `provision_store` | Handle via Shopify OAuth onboarding, not MCP |


