---
name: tiktok-traffic-part1
description: Storefront Design Intelligence (Part 1 of 2)
---

# TikTok & Short-Form Video → Landing Page — Storefront Design Intelligence

> When to load: Page is being generated for TikTok ad traffic, Instagram Reels traffic, YouTube Shorts traffic, or any short-form video platform.

## Philosophy

**3-second hook or death.** Visitors from TikTok were interrupted mid-scroll. They weren't searching — they were swiping entertainment. Your page has 3 seconds before the back button.

**Speed > explanation. Proof > promises. Action > education.**

**Raw authenticity wins.** UGC screenshots beat professional photography. Short punchy fragments beat polished copy. Casual lowercase beats corporate tone. The page should feel creator-made, not brand-designed.

**Mobile-ONLY reality.** 95%+ mobile traffic. Design for 375px width. Desktop is an afterthought.

## Mobile-Only Reality

**Every decision flows from mobile-first constraints:**

- **Single column everything** — no side-by-side layouts
- **48px+ tap targets** — thumb-zone CTAs within 120px of bottom edge
- **Short viewport sections** — each section = one mobile screen max (~600px vertical)
- **No hover states** — all interactions tap/swipe only
- **Swipeable carousels** — not click-through galleries

**Viewport target:** iPhone SE (375×667px) to iPhone 14 Pro Max (430×932px). Design for the smaller end.

**Tailwind patterns:**
```html
<!-- Full-width mobile tap target -->
<button class="w-full min-h-[56px] px-6 py-4 text-lg font-bold">
  Get Mine — 40% Off
</button>

<!-- Single column layout -->
<div class="flex flex-col gap-6 px-4">
  <!-- All content stacks vertically -->
</div>

<!-- Mobile-first spacing -->
<section class="py-12 px-4 md:py-16 md:px-6">
  <!-- 48px mobile, 64px desktop -->
</section>
```

## Section Sequence (TikTok Formula)

**6-8 sections MAX. Each section = one decision closer to purchase.**

1. **Hero** (3-second hook) — Video, bold claim, or before/after visual
2. **Social proof strip** — Stars + "as seen on TikTok" (immediate validation)
3. **Problem/Solution** — Visual agitation (before/after, lifestyle contrast)
4. **Product showcase** — BuyBox island, simple and fast
5. **Reviews** — UGC-style screenshots, casual testimonials
6. **CTA** — Final push with urgency/scarcity
7. *Optional:* **FAQ** (max 4 questions, expandable)
8. *Optional:* **Newsletter** (only if email-first funnel)

**Why short:** Average TikTok landing page session = 23 seconds. Highest bounce rate of any platform. If they're still scrolling after 6 sections, they're already convinced. More sections = more chances to lose them.

**What to cut:** Feature grids, company story, mission statements, detailed specs, multiple testimonial sections. Every section must directly drive purchase intent.

## Hero Patterns

### Pattern 1: Video-First Hero

**When to use:** Product demo video exists, or ad itself was a video demonstration.

```html
<section class="relative min-h-[70vh] bg-black flex items-center justify-center overflow-hidden">
  <!-- VideoPlayer island (autoplay, muted, loop) -->
  <div data-island="VideoPlayer" 
       data-props='{"src":"VIDEO_URL","autoplay":true,"muted":true,"loop":true,"poster":"POSTER_URL","aspectRatio":"9:16"}'
       class="absolute inset-0 w-full h-full">
  </div>
  
  <!-- Content overlay -->
  <div class="relative z-10 text-center px-4 max-w-md mx-auto">
    <h1 class="text-[clamp(2rem,8vw,2.75rem)] font-extrabold tracking-tight leading-[1.1] text-white mb-4">
      Watch It Work
    </h1>
    <p class="text-[clamp(1rem,4vw,1.125rem)] font-medium leading-relaxed text-neutral-300 mb-8">
      Real results in 60 seconds
    </p>
    <button class="w-full min-h-[56px] px-8 py-4 bg-[var(--lx-accent-color)] text-white font-bold text-lg rounded-lg">
      Get Mine — 40% Off
    </button>
  </div>
</section>
```

**Video spec:** 15-30s max. Show product in use, not talking heads. Vertical (9:16) or square (1:1). Autoplay, muted, loop.

### Pattern 2: Bold Text Punch

**When to use:** Strong claim, high-contrast offer, no video asset.

```html
<section class="relative min-h-[65vh] bg-gradient-to-br from-purple-600 to-purple-800 flex items-center justify-center px-4 py-16">
  <div class="text-center max-w-md mx-auto">
    <h1 class="text-[clamp(2.5rem,10vw,3.5rem)] font-black tracking-tighter leading-[0.95] text-white mb-6">
      Clearer Skin<br/>In 7 Days
    </h1>
    <p class="text-[clamp(1.125rem,4.5vw,1.25rem)] font-semibold leading-tight text-purple-200 mb-8">
      Or your money back. No questions.
    </p>
    <button class="w-full min-h-[56px] px-8 py-4 bg-white text-purple-700 font-bold text-lg rounded-lg">
      Try It Risk-Free
    </button>
  </div>
</section>
```

**Text rules:** Max 4 words per line. Line breaks (`<br/>`) for emphasis. No sentences — fragments only. Dark background always.

### Pattern 3: Before/After Hero

**When to use:** Transformation product (skincare, fitness, home, fashion).

```html
<section class="relative min-h-[75vh] bg-white flex items-center justify-center px-4 py-12">
  <div class="max-w-lg mx-auto text-center">
    <!-- Eyebrow -->
    <div class="text-sm font-bold tracking-wider uppercase text-purple-600 mb-3">
      Real Customer • 14 Days
    </div>
    
    <!-- Headline -->
    <h1 class="text-[clamp(1.75rem,7vw,2.25rem)] font-extrabold tracking-tight leading-[1.15] text-black mb-8">
      Same Routine.<br/>Different Results.
    </h1>
    
    <!-- BeforeAfter island -->
    <div data-island="BeforeAfter" 
         data-props='{"before":"BEFORE_URL","after":"AFTER_URL","beforeLabel":"BEFORE","afterLabel":"14 DAYS"}'
         class="mb-8 rounded-2xl overflow-hidden">
    </div>
    
    <button class="w-full min-h-[56px] px-8 py-4 bg-black text-white font-bold text-lg rounded-lg">
      Get Started
    </button>
  </div>
</section>
```

**Image spec:** Same angle, same lighting, clear difference. Labels: "BEFORE" and specific timeframe ("14 DAYS"), not generic "AFTER".

### Pattern 4: UGC Screenshot Hero

**When to use:** Viral review/comment exists, or mimicking TikTok native feel.

```html
<section class="relative min-h-[60vh] bg-neutral-50 flex items-center justify-center px-4 py-12">
  <div class="max-w-md mx-auto text-center">
    <!-- Screenshot mockup -->
    <div class="mb-8 relative">
      <img src="SCREENSHOT_URL" alt="TikTok comment screenshot" class="rounded-2xl shadow-2xl mx-auto max-w-[320px]"/>
    </div>
    
    <!-- Headline (quoted comment) -->
    <h1 class="text-[clamp(1.5rem,6vw,2rem)] font-bold tracking-tight leading-snug text-black italic mb-4">
      "I was skeptical but this actually works? 😭"
    </h1>
    
    <!-- Attribution -->
    <p class="text-[clamp(0.875rem,3.5vw,1rem)] font-medium text-neutral-600 mb-8">
      — @sarah.wellness, 847K views
    </p>
    
    <button class="w-full min-h-[56px] px-8 py-4 bg-black text-white font-bold text-lg rounded-lg">
      Shop the Viral Product
    </button>
  </div>
</section>
```

**Screenshot aesthetic:** Phone UI chrome visible, Instagram/TikTok comment format, engagement numbers, casual language with emojis.

## Video Integration

**VideoPlayer island placement hierarchy:**

1. **Hero VideoPlayer** — Product in action, autoplay muted
2. **Before/After video** — Time-lapse transformation (15s max)
3. **Review video** — Customer testimonial (vertical selfie format)

**Autoplay rules:** Hero = autoplay. Anywhere else = click-to-play (mobile bandwidth).

**HTML pattern for VideoPlayer island:**

```html
<div class="relative aspect-[9/16] max-w-[375px] mx-auto rounded-2xl overflow-hidden">
  <div data-island="VideoPlayer" 
       data-props='{
         "src": "VIDEO_URL",
         "autoplay": true,
         "muted": true,
         "loop": true,
         "controls": false,
         "poster": "THUMBNAIL_URL",
         "aspectRatio": "9:16"
       }'>
  </div>
</div>
```

**Video types that convert:**

- **Product demo** (15s) — Show use case, result, benefit. No talking.
- **Unboxing reaction** — Authentic excitement. "First impressions" format.
- **Before/After transformation** — Time-lapse or side-by-side.
- **Creator testimonial** — Casual to camera, <30s, specific claim.

**What to avoid:** Corporate explainer videos, founder stories, brand films, anything >45s.

## The TikTok Native Aesthetic

**Raw beats polished.** UGC-style content outperforms studio photography 2-3x for TikTok traffic. Make it feel creator-made.

### Visual Principles

**Colors:**
- Pure white (`#ffffff`) or pure black (`#000000`) backgrounds — no off-whites, no gradients (except in CTAs)
- Bold accent colors — purple-600, pink-500, amber-500, emerald-500
- High contrast always — mobile readability in bright sunlight

**Typography:**
- Bold sans-serif only — Inter, DM Sans, Poppins (weight 700-900)
- No decorative fonts, no serifs, no script
- Large sizes — `clamp(1.75rem, 7vw, 2.5rem)` minimum for headlines
- Tight letter-spacing — `-0.02em` to `-0.04em`

**Content format:**
- Short punchy fragments, not sentences
- Line breaks for emphasis
- Emojis OK in eyebrows and trust indicators
- ALL CAPS for urgency elements (sparingly)

**Imagery:**
- Phone-screenshot quality > professional photography
- Casual lifestyle shots > studio product shots
- Selfie-style reviews > corporate headshots
- UGC videos > brand videos

### Concrete Tailwind Classes (TikTok Aesthetic)

**Headlines (punchy, bold, high-contrast):**
```html
<h2 class="text-[clamp(2rem,8vw,2.75rem)] font-extrabold tracking-tight leading-[1.1] text-black">
  Transform Your Skin
</h2>
```

**Sublines (supporting, readable, medium weight):**
```html
<p class="text-[clamp(1rem,4vw,1.125rem)] font-medium leading-relaxed text-neutral-600">
  Real results in 7 days
</p>
```

**Eyebrows (category/proof, uppercase, accent color):**
```html
<div class="text-sm font-bold tracking-wider uppercase text-purple-600">
  ✨ As Seen On TikTok
</div>
```

**Review text (casual, quoted, italic):**
```html
<blockquote class="text-[clamp(1rem,4vw,1.125rem)] font-semibold leading-relaxed text-black italic">
  "okay this is actually insane 😭"
</blockquote>
```

## Social Proof (TikTok-Style)

**Format principle:** Make it look screenshotted from TikTok/Instagram comments, not designed by marketing.

### Pattern 1: Screenshot Aesthetic Reviews

```html
<section class="py-12 px-4 bg-white">
  <div class="max-w-md mx-auto">
    <!-- ReviewCarousel island -->
    <div data-island="ReviewCarousel" 
         data-props='{
           "reviews": [
             {"text": "okay i was NOT expecting this to work but here we are 😭", "name": "Sarah M.", "handle": "@sarah.wellness", "rating": 5, "platform": "tiktok"},
             {"text": "why did nobody tell me about this sooner??", "name": "Mike Chen", "handle": "@mikesfitness", "rating": 5, "platform": "instagram"},
             {"text": "literally changed my skin", "name": "Emma", "rating": 5, "platform": "tiktok"}
           ],
           "autoplay": true,
           "interval": 4000
         }'>
    </div>
  </div>
</section>
```

**Copy rules:** Lowercase, casual punctuation, emojis, no formal language. "this actually works" > "I'm very satisfied with this product."

### Pattern 2: Star Rating with Huge Count

```html
<section class="py-8 px-4 bg-neutral-50">
  <div class="max-w-md mx-auto flex flex-col gap-6">
    <!-- Large star rating -->
    <div class="text-center">
      <div class="text-6xl font-black text-black mb-2">4.9</div>
      <div class="text-3xl text-amber-400 mb-2">★★★★★</div>
      <div class="text-sm font-medium text-neutral-600">14,847 reviews</div>
    </div>
    
    <!-- Orders stat -->
    <div class="text-center border-t border-neutral-200 pt-6">
      <div class="text-4xl font-black text-black mb-1">127K+</div>
      <div class="text-base font-semibold text-neutral-800">Orders This Month</div>
      <div class="text-sm text-neutral-500">As seen on TikTok</div>
    </div>
  </div>
</section>
```

**Display format:** Giant numbers, specific counts (not rounded), "As seen on TikTok" badge language.

### Pattern 3: SocialProofPopup Island

```html
<!-- Placed at page level, triggers immediately -->
<div data-island="SocialProofPopup" 
     data-props='{
       "trigger": "immediate",
       "frequency": 8000,
       "messages": [
         "Sarah from Los Angeles just ordered",
         "Mike from Austin just ordered",
         "Jessica from Miami just ordered"
       ],
       "position": "bottom-left"
     }'>
</div>
```

**Timing:** Appears immediately (no scroll delay), every 8-12 seconds. First name + city format. Max 5 words.

## CTA Strategy

**Single CTA, repeated everywhere.** Do not confuse with multiple competing actions. One primary CTA on entire page.

**Button label hierarchy:**
1. **Benefit + urgency:** "Get Mine — 40% Off" (best)
2. **Direct benefit:** "Try It Risk-Free"
3. **Action + scarcity:** "Shop Now — Limited Stock"
4. **Never:** "Learn More", "Explore Collection", "Read Reviews"

**StickyBar appears immediately:**

```html
<!-- Page-level StickyBar island -->
<div data-island="StickyBar" 
     data-props='{
       "trigger": "immediate",
       "position": "bottom",
       "ctaText": "Get 40% Off Today",
       "showPrice": true,
       "showCountdown": false
     }'>
</div>
```

**All CTAs use consistent styling:**

```html
<button class="w-full min-h-[56px] px-8 py-4 bg-[var(--lx-accent-color)] text-white font-bold text-lg rounded-lg shadow-lg active:scale-95 transition-transform">
  Get Mine — 40% Off
</button>
```

**Never use:** Ghost or outline variants for primary CTA. Link variant only for secondary actions ("No thanks").

**Large tap targets:** 56px height minimum, full-width on mobile.

## Urgency (When to Use It)

**TikTok traffic = impulse audience.** They arrived mid-scroll, not mid-search. Urgency triggers work exceptionally well.

### When to Apply Urgency

- **Flash sale traffic:** CountdownTimer + InventoryIndicator
- **Product launch:** InventoryIndicator + SocialProofPopup
- **Viral product:** SocialProofPopup + "trending" language
- **Always-on:** SocialProofPopup only (least aggressive)

### Pattern 1: CountdownTimer (Real Deadline)

```html
<section class="py-12 px-4 bg-white text-center">
  <h2 class="text-[clamp(1.75rem,7vw,2.25rem)] font-extrabold text-black mb-6">
    40% Off Ends Tonight
  </h2>
  
  <!-- CountdownTimer island -->
  <div data-island="CountdownTimer" 
       data-props='{
         "endTime": "2026-06-28T04:59:59Z",
         "label": "Sale ends in:",
         "style": "compact"
       }'
       class="mb-8">
  </div>
  
  <button class="w-full min-h-[56px] px-8 py-4 bg-black text-white font-bold text-lg rounded-lg max-w-md mx-auto">
    Shop Now
  </button>
</section>
```

**Placement:** Hero section or immediately after. Must be visible without scrolling.

**Copy tone:** Casual, not corporate. "ends tonight" > "LIMITED TIME OFFER". Lowercase feels authentic.

### Pattern 2: InventoryIndicator

```html
<div data-island="InventoryIndicator" 
     data-props='{
       "currentStock": 12,
       "threshold": 20,
       "message": "Only {{count}} left in stock"
     }'
     class="text-center py-4">
</div>
```

**When it works:** Specific low numbers (8-15). "only 12 left" feels real. "only 197 left" feels fake.

**Placement:** Near BuyBox, before final CTA section.

### Pattern 3: SocialProofPopup (Purchase Notifications)

```html
<div data-island="SocialProofPopup" 
     data-props='{
       "trigger": "immediate",
       "frequency": 10000,
       "messages": [
         "3 people viewing this right now",
         "Sarah just ordered from Miami",
         "12 sold in the last hour"
       ]
     }'>
</div>
```

**Tone:** Casual, specific, believable. First names, cities, recent timeframes (<1 hour).

**Authenticity rule:** If you wouldn't text it to a friend, don't show it as social proof.
