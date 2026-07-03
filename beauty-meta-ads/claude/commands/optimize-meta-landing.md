---
description: Optimize an existing landing page for Meta ad traffic conversion
allowed-tools: mcp__lexsis-ai__*
---

# /optimize-meta-landing

Optimize an existing landing page for Meta ad traffic conversion

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

### conversion-psychology

# Conversion Psychology — Storefront Design Intelligence
> When to load: ALWAYS. Read before generating any ecommerce page.
## The Conversion Stack (AIDA → Sections)
Map the AIDA framework to section order. Each stage requires specific psychology and placement.
## Above-the-Fold Rules
What MUST be visible without scroll (< 900px viewport height). Violating this kills 40%+ of conversions.
## Price Psychology Patterns
### Anchoring (strikethrough + current)
## Social Proof Hierarchy
Rank order by persuasive power (highest to lowest). Use this sequence in sections.
## Urgency & Scarcity
Three types. Each requires different implementation and psychology.
## Cognitive Load Management
Max 3 choices per section. More options = decision paralysis = abandonment.
## Trust Escalation Ladder
Move visitors from low-commitment → high-commitment actions. Don't ask for the sale immediately.
## CTA Psychology
Button copy is conversion science. Every word matters.
## Visual Hierarchy for Conversion
Eye-flow patterns direct attention to CTAs.
## Anti-Patterns (Conversion Killers)
| ❌ | Why | ✅ |
|----|-----|-----|
| Generic headlines ("Welcome to Our Store") | No hook, no benefit | "Get [Specific Benefit] in [Timeframe]" |
| Hidden prices ("Contact for Pricing") | Friction, distrust | Show price upfront (even if high) |
| Walls of text (5-paragraph descriptions) | Cognitive overload | Bullet points, max 3 benefits |
| Too many CTAs (3+ above fold) | Decision paralysis | 1 primary CTA, 1 optional secondary |
| Tiny mobile buttons (40px tap target) | Poor UX, missed clicks | 48px minimum (py-3 or py-4) |
| Auto-playing video with sound | Annoys users | Muted autoplay, click to unmute |
| No trust signals above fold | Credibility gap | Add star rating or customer count near CTA |
| Fake urgency (evergreen countdown) | Trust erosion | Real sale end dates or remove timer |
| Cluttered forms (8-field email capture) | Abandonment | Email only with `data-island="EmailCapture"` |
| Slow load times (5+ second hero load) | Bounce rate spike | Optimize images, lazy-load below fold |
| No mobile optimization (desktop-only) | Poor mobile UX | Responsive spacing, clamp() font sizes |
| Unclear value prop ("We're the best") | Generic, meaningless | "Save 10 hours/week with automated [task]" |
| No risk reversal (no guarantee) | Fear of loss | Risk reversal section before final CTA |
| Dead-end pages (no next step) | Lost momentum | Every section ends with CTA or link |
| Inconsistent branding (5 button styles) | Unprofessional | Consistent colors via CSS vars |
## Complete Page Recipes
### Recipe 1: Lead Gen (Email Capture)

### meta-traffic

# Meta Ads → Landing Page — Storefront Design Intelligence
> **When to load**: Page generated from Meta (Facebook/Instagram) ad creative.  
> **Auto-loads as**: `vibe://skills/traffic-source-meta`
## The #1 Rule: Message Match
Meta traffic arrives **interrupted** — they were scrolling feed, not searching. The #1 conversion killer is message discontinuity between ad and landing page.
## Mobile-First Reality
**85%+ of Meta ad traffic is mobile.** Every design decision must pass the "thumb-zone test."
## Section Sequence (The Meta Formula)
This is the **proven sequence for cold Meta traffic** (no brand familiarity, interrupted state):
## Hero Patterns for Meta Traffic
### Pattern 1: Social Proof Hero
**Best for**: High-review-count products
## Trust Stacking (Critical for Cold Traffic)
Meta traffic has **ZERO brand familiarity**. Trust must be immediate, overwhelming, and specific.
## Social Proof (UGC > Polished)
Meta traffic trusts **authentic > polished**.
## CTA Strategy (Single Goal, Repeat 3x)
### The Rule: One Conversion Goal
All CTAs point to the same action.
## Urgency for Meta Traffic (Use Sparingly)
### When to Use Urgency
✅ Real sale with deadline  
✅ Limited inventory (< 50 units)  
✅ Launch window  
✅ Seasonal cutoff
## Mobile Patterns
### Container Padding
```html
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <!-- Content -->
</div>
```
## Anti-Patterns (Meta Killers)
### ❌ Message Mismatch
**What**: Ad says "40% off" → page doesn't mention sale  
**Fix**: Ad headline = page headline
## Complete VibePage Blueprint: Product Launch (New Product)
```json
{
  "head": {
    "title": "GripFlow™ Yoga Mat — The Mat That Won't Slip",
    "description": "Join 47,000+ yogis who solved their slipping problem. 60-day guarantee.",
    "fonts": [
      "https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap"
    ]
  },
  "theme_css": ":root { --lx-accent-color: #4F46E5; --lx-text-color: #111827; --lx-text-muted: #6B7280; --lx-bg-color: #FFFFFF; --lx-bg-surface: #F9FAFB; --lx-border-color: #E5E7EB; --lx-font-heading: 'Inter', system-ui, sans-serif; --lx-font-body: 'Inter', system-ui, sans-serif; }",
  "sections": [
    {
      "id": "hero",
      "html": "<section class=\"relative min-h-[85vh] flex items-center px-4\" style=\"background:white\"><div class=\"max-w-2xl mx-auto text-center space-y-6\"><p class=\"text-sm font-semibold uppercase tracking-wide\" style=\"color:var(--lx-accent-color)\">Rated #1 Yoga Mat of 2025</p><div class=\"flex justify-center items-center gap-2\"><div class=\"flex\"><svg class=\"w-6 h-6\" style=\"fill:gold\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z\"/></svg><svg class=\"w-6 h-6\" style=\"fill:gold\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z\"/></svg><svg class=\"w-6 h-6\" style=\"fill:gold\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z\"/></svg><svg class=\"w-6 h-6\" style=\"fill:gold\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z\"/></svg><svg class=\"w-6 h-6\" style=\"fill:gold\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z\"/></svg></div><span class=\"text-lg font-bold\" style=\"color:var(--lx-text-color)\">4.9/5 stars (12,847 reviews)</span></div><h1 class=\"font-extrabold leading-[1.1]\" style=\"font-family:var(--lx-font-heading);font-size:clamp(2.25rem,7vw,4rem);letter-spacing:-0.03em\">The mat that finally grips</h1><p style=\"font-size:clamp(1.125rem,3vw,1.5rem);color:#4B5563\">Join 47,000+ yogis who solved their slipping problem</p><div class=\"flex flex-col sm:flex-row gap-4 justify-center\"><button class=\"px-8 py-4 rounded-lg font-semibold\" style=\"background:var(--lx-accent-color);color:white\">Get yours now</button></div><img src=\"{{product_image_url}}\" alt=\"GripFlow Mat\" class=\"w-full max-w-lg mx-auto rounded-lg\"/><div class=\"flex flex-wrap justify-center gap-6 text-sm pt-4\"><span class=\"flex items-center gap-2\"><svg class=\"w-5 h-5\" style=\"color:var(--lx-accent-color)\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z\"/></svg><span>47,000+ customers</span></span><span class=\"flex items-center gap-2\"><svg class=\"w-5 h-5\" style=\"color:var(--lx-accent-color)\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z\"/></svg><span>60-day money-back guarantee</span></span></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "trust-strip",
      "html": "<section class=\"py-8 border-b\" style=\"background:var(--lx-bg-surface);border-color:var(--lx-border-color)\"><div class=\"max-w-7xl mx-auto px-4\"><div class=\"grid grid-cols-2 md:grid-cols-4 gap-6 text-center\"><div class=\"space-y-1\"><svg class=\"w-8 h-8 mx-auto\" style=\"color:var(--lx-accent-color)\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z\"/></svg><p class=\"font-semibold\" style=\"color:var(--lx-text-color)\">60-Day Guarantee</p><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">Love it or return it</p></div><div class=\"space-y-1\"><svg class=\"w-8 h-8 mx-auto\" style=\"color:var(--lx-accent-color)\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\"><path d=\"M9 17a2 2 0 11-4 0 2 2 0 014 0zM19 17a2 2 0 11-4 0 2 2 0 014 0z\"/><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M13 16V6a1 1 0 00-1-1H4a1 1 0 00-1 1v10a1 1 0 001 1h1m8-1a1 1 0 01-1 1H9m4-1V8a1 1 0 011-1h2.586a1 1 0 01.707.293l3.414 3.414a1 1 0 01.293.707V16a1 1 0 01-1 1h-1m-6-1a1 1 0 001 1h1M5 17a2 2 0 104 0m-4 0a2 2 0 114 0m6 0a2 2 0 104 0m-4 0a2 2 0 114 0\"/></svg><p class=\"font-semibold\" style=\"color:var(--lx-text-color)\">Free Shipping</p><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">On all US orders</p></div><div class=\"space-y-1\"><svg class=\"w-8 h-8 mx-auto\" style=\"color:var(--lx-accent-color)\" viewBox=\"0 0 24 24\" fill=\"gold\"><path d=\"M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z\"/></svg><p class=\"font-semibold\" style=\"color:var(--lx-text-color)\">12,847 5-Star Reviews</p><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">Rated Excellent</p></div><div class=\"space-y-1\"><svg class=\"w-8 h-8 mx-auto\" style=\"color:var(--lx-accent-color)\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z\"/></svg><p class=\"font-semibold\" style=\"color:var(--lx-text-color)\">Featured in Yoga Journal</p><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">Best Mat 2025</p></div></div></div></section>",
      "css": "",
      "js": ""
    }
  ],
  "islands": [
    {
      "type": "StickyBar",
      "props": {
        "trigger_scroll": "50vh",
        "cta_text": "Get my GripFlow mat",
        "price": "$79",
        "trust_badge": "60-day guarantee • Free shipping"
      }
    }
  ]
}
```
## TL;DR — The Meta Landing Page Checklist
✅ **Message match**: Ad headline → page headline  
✅ **Mobile-first**: `clamp()` for text/spacing, 44px tap targets  
✅ **Trust immediately**: Star rating + review count in hero  
✅ **Single CTA goal**: All buttons → same action  
✅ **CTA 3x minimum**: Hero, post-social-proof, sticky bar  
✅ **UGC > polished** (Facebook) OR **editorial > UGC** (Instagram)  

## Workflow

# Storefront Page Editing

Edit existing pages using section-level operations.

## Edit Flow

1. `list_pages` — find target page
2. `get_page` — read current page structure + HTML
3. Make changes (one of the operations below)
4. `validate_vibe_page` — verify changes are valid
5. Page auto-versions on each mutation

## Operations

### Update/Replace a Section

```
update_page_section(page_id, section_id, { html, css, settings })
```
- Can replace HTML entirely or patch specific parts
- Auto-bumps page version
- Use for: changing copy, swapping images, restyling

### Add a New Section

```
update_page_section(page_id, null, { html, css, settings, position })
```
- Position: "before:{section_id}" or "after:{section_id}" or index number
- Must include full section HTML

### Remove a Section

```
remove_page_section(page_id, section_id)
```
- Irreversible — confirm with user first
- Auto-bumps version

### Reorder Sections

```
move_page_section(page_id, section_id, new_position)
```
- Position is 0-indexed
- All other sections shift accordingly

## Best Practices

- Always `get_page` first to understand current structure
- Reference section IDs from the page data (don't guess)
- After editing, run `validate_vibe_page` before telling user it's done
- For multi-section changes, batch them (each call bumps version)
- Preserve existing CSS variables and island configurations
- Don't break mobile responsiveness when editing desktop layout


# Storefront Analytics & Experiments

Access page performance data and manage A/B experiments.

## Analytics Tools

### Page-Level Deep Dive
```
get_page_analytics(page_id)
```
Returns: CVR, bounce rate, time on page, traffic sources, device split, top-performing sections.

### Time Series Trends
```
get_analytics_timeseries({ metric: "conversions", period: "daily", range: "30d" })
```
Returns: daily/weekly trends for hits, conversions, revenue, AOV.

### Revenue Attribution
```
get_attribution({ page_id? })
```
Returns: ROAS by channel, revenue per page, top campaigns driving conversions.

## A/B Testing Flow

### 1. Create Experiment
```
create_ab_test({
  page_id: "...",
  variants: [{ blueprint_id: "...", weight: 50 }, { blueprint_id: "...", weight: 50 }]
})
```

### 2. Monitor Results
```
get_experiment_results(experiment_id)
```
Returns: CVR per variant, statistical significance (mSPRT), sample sizes, winner recommendation.

### 3. Scale Winner
```
scale_winner(experiment_id, { variant_id: "..." })
```
Scales winning variant to 100% traffic, marks experiment complete.

## Best Practices

- Wait for statistical significance before scaling winner
- Minimum ~1000 visitors per variant for reliable results
- Check device split — a variant may win on mobile but lose on desktop
- Use `get_attribution` to understand which traffic sources convert best
- Compare page analytics before/after changes to measure impact


