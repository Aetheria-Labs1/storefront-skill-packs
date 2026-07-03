---
description: Optimize a page for TikTok ad traffic — mobile-first, fast scroll, video-native patterns
allowed-tools: mcp__lexsis-ai__*
---

# /optimize-tiktok-landing

Optimize a page for TikTok ad traffic — mobile-first, fast scroll, video-native patterns

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

### tiktok-traffic

# TikTok & Short-Form Video → Landing Page — Storefront Design Intelligence
> When to load: Page is being generated for TikTok ad traffic, Instagram Reels traffic, YouTube Shorts traffic, or any short-form video platform.
## Philosophy
**3-second hook or death.** Visitors from TikTok were interrupted mid-scroll. They weren't searching — they were swiping entertainment. Your page has 3 seconds before the back button.
## Mobile-Only Reality
**Every decision flows from mobile-first constraints:**
## Section Sequence (TikTok Formula)
**6-8 sections MAX. Each section = one decision closer to purchase.**
## Hero Patterns
### Pattern 1: Video-First Hero
## Video Integration
**VideoPlayer island placement hierarchy:**
## The TikTok Native Aesthetic
**Raw beats polished.** UGC-style content outperforms studio photography 2-3x for TikTok traffic. Make it feel creator-made.
## Social Proof (TikTok-Style)
**Format principle:** Make it look screenshotted from TikTok/Instagram comments, not designed by marketing.
## CTA Strategy
**Single CTA, repeated everywhere.** Do not confuse with multiple competing actions. One primary CTA on entire page.
## Urgency (When to Use It)
**TikTok traffic = impulse audience.** They arrived mid-scroll, not mid-search. Urgency triggers work exceptionally well.
## Content Rules
**Maximum lengths:**
- Headline: 5 words (4 ideal)
- Subline: 12 words (8-10 ideal)
- Review quote: 80 characters
- FAQ answer: 40 words
- CTA button: 4 words
## Anti-Patterns (TikTok Landing Page Killers)
### 1. Long Pages (>8 Sections)
## Complete Blueprint
### Full 6-Section TikTok Landing Page (VibePage JSON)

### animation-system

# Animation System — Vibe-Code Reference
CSS-only and vanilla JS animations for storefront pages. No framer-motion, no React — pure CSS keyframes + IntersectionObserver for scroll triggers.
## When to Animate vs Not
**Animate:**
- Hero headline on premium/editorial/bold brands
- Section entrances on scroll (fade-up, slide-in)
- Background gradients on dark/vibrant brands
- Stats/numbers counting up
- Floating decorative elements
## Section CSS: Keyframe Animations
Place in section `css` field. Scoped per section.
## Scroll-Triggered Reveal (Section JS)
Use section `js` field. IntersectionObserver fires animation on scroll.
## Headline Effects (CSS-only)
### Word-by-Word Fade
## Background Animations
### Gradient Shift (hero/CTA backgrounds)
## Micro-Interactions (Tailwind transitions)
### Button Hover
```html
<button class="transition-all duration-200 hover:scale-[1.02] hover:shadow-lg active:scale-[0.98]" style="background:var(--lx-accent-color)">
  Shop Now
</button>
```
## Brand Tone → Animation Mapping
| Tone | Level | Recommended |
|---|---|---|
| Luxury/Premium | Subtle, slow | Fade-in-up (0.8s), text-reveal, gradient-text |
| Playful/Bold | Energetic | Stagger, scale-in, floating elements, gradient-shift |
| Clinical/Minimal | Near-zero | Simple fade (0.4s) only |
| Editorial | Refined | Word-by-word, slide-left/right, underline-draw |
| Earthy/Organic | Gentle | Slow fade (1s), parallax, float |
| Tech/DTC | Snappy | Fast stagger (0.08s delay), scale-in |
## Performance Rules
1. Only animate `transform` and `opacity` — never `width`, `height`, `margin`
2. Add `will-change: transform` to heavily animated elements
3. Max 10 keyframe animations per page
4. Accessibility — always include:
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```
5. Scroll observers: `{ passive: true }` and `threshold: 0.15`

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


