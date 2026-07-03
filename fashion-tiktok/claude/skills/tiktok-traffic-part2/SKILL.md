---
name: tiktok-traffic-part2
description: Storefront Design Intelligence (Part 2 of 2)
---

## Content Rules

**Maximum lengths:**
- Headline: 5 words (4 ideal)
- Subline: 12 words (8-10 ideal)
- Review quote: 80 characters
- FAQ answer: 40 words
- CTA button: 4 words

**Fragment sentences OK:** "Clearer skin. Faster results." > "Get clearer skin with faster results."

**Line breaks for emphasis:**
```html
<h1>Transform Your Skin<br/>In Just 7 Days</h1>
```
Not: `<h1>Transform Your Skin In Just 7 Days</h1>`

**Emojis:** OK in eyebrows ("✨ As Seen On TikTok"), trust indicators ("⚡ Free Shipping"), casual reviews. NOT in headlines or CTAs.

**Casual > formal:**
- "this actually works" > "clinically proven results"
- "ordered 3 more" > "highly recommend"
- "didn't believe it but wow" > "exceeded expectations"

**Active voice, present tense:** "Get results in 7 days" > "Results can be seen within a week"

### Good vs Bad Examples

**Hero headline (GOOD):**
- "Clearer Skin\nIn 7 Days"
- "The Viral TikTok Blender"
- "10,000 Sold Yesterday"

**Hero headline (BAD):**
- "Discover Our Revolutionary Skincare Solution"
- "Premium Quality You Can Trust"
- "Join Thousands of Happy Customers"

**Subline (GOOD):**
- "Or your money back. No questions."
- "Same routine. Different results."
- "Ships today if you order now."

**Subline (BAD):**
- "We use only the finest ingredients sourced from around the world."
- "Our commitment to quality is unmatched in the industry."

**Review (GOOD):**
- "okay this is actually insane 😭"
- "why did nobody tell me about this??"
- "already ordered 3 more for friends"

**Review (BAD):**
- "I am very satisfied with this purchase and would recommend it to others."
- "Great product, fast shipping, excellent customer service."

**CTA (GOOD):**
- "Get Mine — 40% Off"
- "Try It Risk-Free"
- "Shop Now — Only 12 Left"

**CTA (BAD):**
- "Learn More About Our Products"
- "Explore Our Collection"
- "Add To Cart"

## Anti-Patterns (TikTok Landing Page Killers)

### 1. Long Pages (>8 Sections)

**Why it kills:** TikTok traffic bounces fast. Every section is a chance to lose them. The "tell them everything" approach destroys conversion.

**Fix:** Cut ruthlessly. 6-8 sections max. If a section doesn't directly drive purchase intent, delete it.

### 2. Corporate/Polished Tone

**Why it kills:** Cognitive dissonance. They came from casual UGC, landed on corporate marketing. Feels like bait-and-switch.

**Fix:** Write like a creator, not a brand. Casual language, fragments, lowercase, emojis, authenticity over polish.

### 3. Desktop-First Design

**Why it kills:** 95% mobile traffic. Desktop-optimized layouts look broken, feel slow, require too much scrolling on mobile.

**Fix:** Design for 375px width. Single column. Large touch targets. Test on actual device, not Chrome DevTools.

### 4. Long Copy Anywhere

**Why it kills:** TikTok trained them for 15-second chunks. Paragraphs feel like homework.

**Fix:** Max 12 words per text block. Use line breaks. Replace paragraphs with bullet fragments.

### 5. Multiple Competing CTAs

**Why it kills:** Decision paralysis. "Shop All", "Learn More", "Watch Video", "Read Reviews" — they'll click none.

**Fix:** One CTA, repeated. Same button text throughout entire page.

### 6. No Video

**Why it kills:** They came from video, expect video. Static images feel outdated, less trustworthy.

**Fix:** Video in hero or immediately after. Product demo, before/after, or UGC testimonial. 15-30s max.

### 7. Polished Studio Photography

**Why it kills:** UGC aesthetic wins on TikTok. Professional photos feel like "ads", trigger skepticism.

**Fix:** Casual lifestyle shots. Phone-photo quality. Customer photos over brand photos. Screenshot aesthetic for reviews.

### 8. Formal Testimonials

**Why it kills:** "I am very satisfied" doesn't match how people actually talk. Feels scripted, fake.

**Fix:** Short punchy quotes. Casual language. "this actually works 😭" > "highly recommend this product."

### 9. Gradients/Decorative Elements

**Why it kills:** Visual noise on mobile. Slow-loading. Distracts from content. Feels 2015.

**Fix:** Solid backgrounds. Pure white or pure black. Bold accent colors for CTAs only. Clean, fast, focused.

### 10. Slow-Loading Assets

**Why it kills:** 3-second attention span. If page takes >2s to load, they're gone.

**Fix:** Optimize images (<200KB each). Lazy-load below-fold content. Inline critical CSS. Test on 3G.

### 11. Hiding Price

**Why it kills:** TikTok traffic is comparison-shopping mentally. Hidden price = "click to reveal" friction = bounce.

**Fix:** Show price in hero or immediately after. BuyBox island placement in sections 3-4, not 6-7.

### 12. No Social Proof Above Fold

**Why it kills:** Trust is the barrier. They don't know your brand. Without immediate social proof, they assume it's a scam.

**Fix:** Star rating + count in hero section. "4.9★ from 14,847 reviews" or "127K orders this month" above fold.

## Complete Blueprint

### Full 6-Section TikTok Landing Page (VibePage JSON)

```json
{
  "head": {
    "title": "The Viral TikTok Blender — 40% Off Today",
    "description": "10,000 sold this week. Smooth, quiet, 30 seconds. As seen on TikTok.",
    "og_image": "PRODUCT_IMAGE_URL"
  },
  "theme_css": ":root { --lx-accent-color: #7c3aed; --lx-text-color: #000000; --lx-text-muted: #6b7280; --lx-bg-color: #ffffff; --lx-bg-surface: #f9fafb; --lx-border-color: #e5e7eb; --lx-font-heading: 'Inter', system-ui, sans-serif; --lx-font-body: 'Inter', system-ui, sans-serif; }",
  "sections": [
    {
      "id": "hero",
      "html": "<section class=\"relative min-h-[70vh] bg-black flex items-center justify-center overflow-hidden\"><div data-island=\"VideoPlayer\" data-props='{\"src\":\"VIDEO_URL\",\"autoplay\":true,\"muted\":true,\"loop\":true,\"poster\":\"POSTER_URL\",\"aspectRatio\":\"9:16\"}' class=\"absolute inset-0 w-full h-full\"></div><div class=\"relative z-10 text-center px-4 max-w-md mx-auto\"><h1 class=\"text-[clamp(2rem,8vw,2.75rem)] font-extrabold tracking-tight leading-[1.1] text-white mb-4\">The Viral Blender<br/>Everyone's Talking About</h1><p class=\"text-[clamp(1rem,4vw,1.125rem)] font-medium leading-relaxed text-neutral-300 mb-8\">Smooth. Quiet. 30 Seconds.</p><button class=\"w-full min-h-[56px] px-8 py-4 bg-purple-600 text-white font-bold text-lg rounded-lg shadow-lg\">Get 40% Off Today</button></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "social-proof",
      "html": "<section class=\"py-8 px-4 bg-neutral-50\"><div class=\"max-w-md mx-auto flex flex-col gap-6\"><div class=\"text-center\"><div class=\"text-6xl font-black text-black mb-2\">4.9</div><div class=\"text-3xl text-amber-400 mb-2\">★★★★★</div><div class=\"text-sm font-medium text-neutral-600\">14,847 reviews</div></div><div class=\"text-center border-t border-neutral-200 pt-6\"><div class=\"text-4xl font-black text-black mb-1\">2.4M</div><div class=\"text-base font-semibold text-neutral-800\">TikTok Views</div><div class=\"text-sm text-neutral-500\">This Week</div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "problem-solution",
      "html": "<section class=\"py-12 px-4 bg-white\"><div class=\"max-w-lg mx-auto\"><h2 class=\"text-[clamp(1.75rem,7vw,2.25rem)] font-extrabold text-center text-black mb-8\">Smoothies That Actually Taste Good</h2><div class=\"grid grid-cols-2 gap-4\"><div class=\"bg-neutral-100 rounded-2xl p-6 text-center\"><div class=\"text-4xl mb-3\">😵</div><div class=\"font-bold text-neutral-800 mb-2\">Other Blenders</div><div class=\"text-sm text-neutral-600\">Chunky. Loud. Takes Forever.</div></div><div class=\"bg-purple-50 rounded-2xl p-6 text-center border-2 border-purple-600\"><div class=\"text-4xl mb-3\">✨</div><div class=\"font-bold text-black mb-2\">With This</div><div class=\"text-sm text-neutral-800\">Smooth. Quiet. 30 Seconds.</div></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "buybox",
      "html": "<section class=\"py-12 px-4 bg-white\"><div class=\"max-w-md mx-auto\"><div class=\"rounded-2xl overflow-hidden shadow-2xl mb-6\"><img src=\"PRODUCT_IMAGE_URL\" alt=\"Product\" class=\"w-full aspect-square object-cover\"/></div><div data-island=\"BuyBox\" data-props='{\"productId\":\"PRODUCT_ID\",\"price\":79,\"salePrice\":47,\"ctaText\":\"Add To Cart — $47 (Was $79)\"}' class=\"mb-6\"></div><div data-island=\"InventoryIndicator\" data-props='{\"currentStock\":12,\"threshold\":20,\"message\":\"Only {{count}} left in stock\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "reviews",
      "html": "<section class=\"py-12 px-4 bg-neutral-50\"><div class=\"max-w-md mx-auto\"><h2 class=\"text-[clamp(1.75rem,7vw,2.25rem)] font-extrabold text-center text-black mb-8\">What People Are Saying</h2><div data-island=\"ReviewCarousel\" data-props='{\"reviews\":[{\"text\":\"this changed my mornings honestly\",\"name\":\"Emma\",\"handle\":\"@emmawellness\",\"rating\":5},{\"text\":\"quieter than my old one?? how\",\"name\":\"Tyler\",\"handle\":\"@tylerscooks\",\"rating\":5},{\"text\":\"bought 2 more as gifts\",\"name\":\"Sarah\",\"handle\":\"@sarahfitness\",\"rating\":5}],\"autoplay\":true,\"interval\":4000}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "final-cta",
      "html": "<section class=\"py-12 px-4 bg-purple-600\"><div class=\"max-w-md mx-auto text-center\"><div data-island=\"CountdownTimer\" data-props='{\"endTime\":\"2026-06-28T04:59:59Z\",\"label\":\"Sale ends in:\",\"style\":\"compact\"}' class=\"mb-6\"></div><h2 class=\"text-[clamp(1.75rem,7vw,2.25rem)] font-extrabold text-white mb-6\">40% Off Ends Tonight</h2><button class=\"w-full min-h-[56px] px-8 py-4 bg-white text-purple-700 font-bold text-lg rounded-lg shadow-lg\">Get Mine Now</button></div></section>",
      "css": "",
      "js": ""
    }
  ],
  "islands": [
    {
      "type": "StickyBar",
      "props": {
        "trigger": "immediate",
        "position": "bottom",
        "ctaText": "Get 40% Off Today",
        "showPrice": true,
        "showCountdown": false
      }
    },
    {
      "type": "SocialProofPopup",
      "props": {
        "trigger": "immediate",
        "frequency": 8000,
        "messages": [
          "Sarah from Los Angeles just ordered",
          "Mike from Austin just ordered",
          "Jessica from Miami just ordered"
        ],
        "position": "bottom-left"
      }
    }
  ]
}
```

**Why this blueprint works:**

1. **Video hook** matches ad creative (continuity, no jarring transition)
2. **Social proof immediate** (4.9★ + 14K reviews + 2.4M TikTok views above fold)
3. **Problem/solution visual** (before/after in 2-column grid, mobile-friendly)
4. **BuyBox at section 4** (mid-page, after trust established, not buried)
5. **UGC reviews** (casual language, screenshot aesthetic, carousel format)
6. **Urgency at end** (countdown + scarcity for final push, not aggressive until they're convinced)
7. **StickyBar + SocialProofPopup** (page-level islands = CTA always accessible, social proof continuous)

**Total page height:** ~4 mobile screens. Fast scroll. Every section drives purchase intent. No friction.

---

**Final principle:** When in doubt, make it shorter, bolder, more casual. TikTok traffic punishes traditional marketing. The page should feel like it was made by a creator who sold out, not a brand trying to go viral.
