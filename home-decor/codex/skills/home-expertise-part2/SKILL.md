---
name: home-expertise-part2
description: Storefront Design Intelligence (Part 2 of 2)
---

## Social Proof

**Photo reviews showing the product in REAL customer homes** (not staged). This is the most trusted content in the home vertical — buyers want to see the product after delivery, in imperfect lighting, in real rooms.

```html
<section class="py-20 px-6 lg:px-16" style="background:var(--lx-bg-surface)">
  <div class="max-w-7xl mx-auto">
    <div class="text-center mb-12">
      <h2 style="font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:400;color:var(--lx-text-color)">
        In Your Homes
      </h2>
      <p class="mt-3 text-sm" style="color:var(--lx-text-muted)">
        Real rooms, real reviews
      </p>
    </div>

    <div data-island="ReviewCarousel" data-props='{
      "reviews": [
        {
          "id": "r1",
          "author": "Jessica M.",
          "location": "Portland, OR",
          "rating": 5,
          "title": "Exactly what we needed",
          "text": "Perfect size for our open-plan kitchen. The oak warms up the whole space. We've had it for 6 months and it still looks brand new despite daily use with two kids.",
          "images": ["ASSET[customer-room-jessica.jpg]", "ASSET[customer-detail-jessica.jpg]"],
          "metadata": {"room": "Kitchen/Dining", "style": "Modern Farmhouse"},
          "verifiedPurchase": true,
          "date": "2026-05-12"
        },
        {
          "id": "r2",
          "author": "David L.",
          "location": "Austin, TX",
          "rating": 5,
          "title": "Worth every penny",
          "text": "We deliberated for weeks before buying. No regrets. The finish is bulletproof, seats 8 comfortably, and the craftsmanship is obvious. It's the anchor of our dining room.",
          "images": ["ASSET[customer-room-david.jpg]", "ASSET[customer-room-david-2.jpg]"],
          "metadata": {"room": "Dining Room", "style": "Transitional"},
          "verifiedPurchase": true,
          "date": "2026-04-28"
        },
        {
          "id": "r3",
          "author": "Priya S.",
          "location": "Seattle, WA",
          "rating": 5,
          "title": "Finally, a table that fits our space",
          "text": "We have a narrow dining room and most tables are either too wide or too small. This is the Goldilocks table — 72\" is perfect. The delivery team was incredibly careful and professional.",
          "images": ["ASSET[customer-room-priya.jpg]"],
          "metadata": {"room": "Dining Room", "style": "Mid-Century"},
          "verifiedPurchase": true,
          "date": "2026-03-15"
        }
      ],
      "showPhotosOnly": false,
      "slidesToShow": 1,
      "autoplay": false
    }'></div>
  </div>
</section>
```

---

## Photography

**Room context is non-negotiable.** Do not show furniture floating in a white void — it reads as cheap, despite the price point.

### Required shot types (in order of priority):
1. **Room-wide hero** — product as focal point in a fully styled room (rug, lighting, accessories, wall art)
2. **Scale reference** — product with a person seated/standing nearby (or known-size objects like books, plates)
3. **Detail shots** — joinery, grain, hardware, finish (macro lens, natural light)
4. **Alternate angles** — room from 2-3 different viewpoints
5. **In-use shots** — table set for a meal, candle lit, textiles draped/styled
6. **Material close-ups** — ImageZoom-ready macros of wood grain, fabric weave, ceramic glaze

### Asset keyword patterns:
- `room-wide-hero`, `room-angle-2`, `room-kitchen-view`
- `detail-leg-joinery`, `detail-oak-grain`, `detail-hardware`
- `scale-person-seated`, `scale-room-context`
- `styled-dining-table-set`, `styled-breakfast-nook`
- `customer-room-[name]`, `customer-detail-[name]`

### Anti-pattern:
Never use product photos with:
- Pure white backgrounds (reads as e-commerce commodity, not heirloom furniture)
- No scale reference (can't tell if it's 4 feet or 8 feet)
- Harsh studio lighting (looks artificial)
- Empty rooms (reads as "before" photo, not aspirational)

---

## Anti-Patterns

### 12 Home Page Killers

1. **No room context** — product floating in white void. NEVER.
2. **Missing dimensions above the fold** — buyers can't proceed without H×W×D.
3. **Tiny product images** — home buyers zoom obsessively. Use ImageZoom islands.
4. **Cold color palette** — stark white (#FFF), cool grays, blue accents. Reads as clinical/office, not home.
5. **Generic product photography** — no styling, no accessories, no life.
6. **Buried shipping/assembly info** — surprise fees or assembly requirements kill conversions.
7. **No material story** — "solid oak" means nothing without origin, finish, durability.
8. **No customer room photos** — staged rooms are aspirational, customer rooms build trust.
9. **Mobile-hostile specs** — dimensions in a dense paragraph instead of scannable list.
10. **No cross-sells** — buyers want to see the full room, not just one piece.
11. **Flat typography** — home is tactile. Use warm serifs, generous spacing, hierarchy.
12. **No scale reference** — table could be 4 feet or 12 feet. Show a person or known-size object.

### Warning Signs in Blueprint Prompts:
- "Minimalist design" → often means cold/sparse. Home needs warmth.
- "Lots of whitespace" → yes, but warm off-white (#FAFAF8), not stark.
- "Product gallery" → must specify room context shots, not just product-on-white.
- "Clean and modern" → risk of sterile. Clarify "warm modern" or "organic modern."

---

## Complete Blueprint Example

**Full VibePage JSON for Furniture PDP (Dining Table)**

```json
{
  "head": {
    "title": "The Everyday Table — Solid White Oak | [Brand Name]",
    "description": "Hand-crafted dining table in solid white oak. 72\" × 36\" × 30\". Seats 6-8. Mortise-and-tenon joinery. Natural oil finish. White-glove delivery in 4-6 weeks.",
    "og_image": "ASSET[og-everyday-table.jpg]"
  },
  "theme_css": ":root{--lx-bg-color:#FAFAF8;--lx-bg-surface:#F7F5F2;--lx-text-color:#2C2C2C;--lx-text-muted:#6B6B6B;--lx-border-color:#E8E6E1;--lx-accent-color:#8B7355;--lx-font-heading:'Fraunces',Georgia,serif;--lx-font-body:'Avenir Next',-apple-system,sans-serif}",
  "sections": [
    {
      "id": "hero",
      "html": "<section class=\"relative min-h-[85vh]\"><img src=\"ASSET[dining-room-wide-hero.jpg]\" alt=\"The Everyday Table in sunlit dining room\" class=\"absolute inset-0 w-full h-full object-cover\" loading=\"eager\"/><div class=\"absolute inset-0 bg-gradient-to-r from-white/80 via-white/40 to-transparent\"></div><div class=\"relative z-10 flex items-center min-h-[85vh] px-6 lg:px-16\"><div class=\"max-w-lg space-y-5\"><p class=\"text-xs uppercase tracking-[0.12em]\" style=\"color:var(--lx-text-muted)\">Solid White Oak</p><h1 style=\"font-family:var(--lx-font-heading);font-size:clamp(2rem,4vw,3rem);font-weight:400;line-height:1.15;color:var(--lx-text-color)\">The Everyday Table</h1><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">72\" × 36\" × 30\" • Seats 6-8 • No assembly required</p><div class=\"flex gap-4 items-center\"><span class=\"text-2xl font-medium\" style=\"color:var(--lx-text-color)\">$1,850</span><a href=\"#details\" class=\"inline-block text-sm font-medium border-b pb-1 transition-colors hover:opacity-70\" style=\"color:var(--lx-text-color);border-color:var(--lx-border-color)\">View Details →</a></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "quick-specs",
      "html": "<section class=\"py-12 px-6 lg:px-16\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-4xl mx-auto grid grid-cols-2 lg:grid-cols-4 gap-6 text-center\"><div><p class=\"text-xs uppercase tracking-wide\" style=\"color:var(--lx-text-muted)\">Dimensions</p><p class=\"text-sm font-medium mt-1\" style=\"color:var(--lx-text-color)\">72\" × 36\" × 30\"</p></div><div><p class=\"text-xs uppercase tracking-wide\" style=\"color:var(--lx-text-muted)\">Material</p><p class=\"text-sm font-medium mt-1\" style=\"color:var(--lx-text-color)\">Solid White Oak</p></div><div><p class=\"text-xs uppercase tracking-wide\" style=\"color:var(--lx-text-muted)\">Finish</p><p class=\"text-sm font-medium mt-1\" style=\"color:var(--lx-text-color)\">Natural Oil</p></div><div><p class=\"text-xs uppercase tracking-wide\" style=\"color:var(--lx-text-muted)\">Delivery</p><p class=\"text-sm font-medium mt-1\" style=\"color:var(--lx-text-color)\">4-6 Weeks</p></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "product-gallery",
      "html": "<section class=\"py-16 px-6 lg:px-16\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-6xl mx-auto\"><div data-island=\"ProductGallery\" data-props='{\"images\":[{\"src\":\"ASSET[table-room-wide.jpg]\",\"alt\":\"Dining table in styled room\",\"type\":\"room\"},{\"src\":\"ASSET[table-detail-leg.jpg]\",\"alt\":\"Oak leg joinery close-up\",\"type\":\"detail\"},{\"src\":\"ASSET[table-scale-person.jpg]\",\"alt\":\"Table with person seated\",\"type\":\"scale\"},{\"src\":\"ASSET[table-room-angle2.jpg]\",\"alt\":\"Dining room from kitchen view\",\"type\":\"room\"},{\"src\":\"ASSET[table-detail-grain.jpg]\",\"alt\":\"Oak grain macro\",\"type\":\"detail\"}],\"thumbnailPosition\":\"left\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "dimensions-tabs",
      "html": "<section class=\"py-16 px-6 lg:px-16\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-4xl mx-auto\"><div data-island=\"Tabs\" data-props='{\"tabs\":[{\"id\":\"dimensions\",\"label\":\"Dimensions\",\"content\":\"<div class=\\\"space-y-4\\\"><h3 class=\\\"text-lg font-medium mb-3\\\">Dimensions</h3><ul class=\\\"space-y-2 text-sm\\\" style=\\\"color:var(--lx-text-muted)\\\"><li><strong>Height:</strong> 30 inches</li><li><strong>Width:</strong> 72 inches</li><li><strong>Depth:</strong> 36 inches</li><li><strong>Weight:</strong> 145 lbs</li><li><strong>Clearance:</strong> 24\\\" recommended</li><li><strong>Assembly:</strong> None — delivered fully assembled</li></ul></div>\"},{\"id\":\"materials\",\"label\":\"Materials\",\"content\":\"<div class=\\\"space-y-4\\\"><h3 class=\\\"text-lg font-medium mb-3\\\">Materials</h3><p class=\\\"text-sm\\\" style=\\\"color:var(--lx-text-muted)\\\">Solid white oak from Vermont. Natural oil finish. Stainless steel leveling feet.</p></div>\"},{\"id\":\"care\",\"label\":\"Care\",\"content\":\"<div class=\\\"space-y-4\\\"><h3 class=\\\"text-lg font-medium mb-3\\\">Care</h3><p class=\\\"text-sm\\\" style=\\\"color:var(--lx-text-muted)\\\">Wipe with damp cloth. Re-oil annually.</p></div>\"},{\"id\":\"shipping\",\"label\":\"Shipping\",\"content\":\"<div class=\\\"space-y-4\\\"><h3 class=\\\"text-lg font-medium mb-3\\\">Shipping</h3><p class=\\\"text-sm\\\" style=\\\"color:var(--lx-text-muted)\\\">White-glove delivery in 4-6 weeks.</p></div>\"}],\"defaultTab\":\"dimensions\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "material-story",
      "html": "<section class=\"py-20 px-6 lg:px-16\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-6xl mx-auto\"><div class=\"text-center mb-12\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:400;color:var(--lx-text-color)\">Crafted to Last Generations</h2></div><div class=\"grid grid-cols-1 lg:grid-cols-12 gap-4\"><div class=\"lg:col-span-7 lg:row-span-2 relative overflow-hidden rounded-lg\"><img src=\"ASSET[oak-forest.jpg]\" alt=\"Vermont oak forest\" class=\"w-full h-full object-cover min-h-[400px]\"/></div><div class=\"lg:col-span-5 p-8 rounded-lg\" style=\"background:var(--lx-bg-surface)\"><h3 class=\"text-lg font-medium mb-3\">Sustainably Sourced</h3><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">FSC-certified Vermont oak.</p></div><div class=\"lg:col-span-5 relative overflow-hidden rounded-lg\"><div data-island=\"ImageZoom\" data-props='{\"src\":\"ASSET[mortise-tenon.jpg]\",\"alt\":\"Joinery detail\",\"zoomLevel\":2.5}'></div></div><div class=\"lg:col-span-7 p-8 rounded-lg\" style=\"background:var(--lx-bg-surface)\"><h3 class=\"text-lg font-medium mb-3\">Natural Oil Finish</h3><p class=\"text-sm\" style=\"color:var(--lx-text-muted)\">Matte, warm, repairable.</p></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "room-gallery",
      "html": "<section class=\"py-20 px-6 lg:px-16\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-7xl mx-auto\"><div class=\"text-center mb-12\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:400\">Styled Six Ways</h2></div><div class=\"grid grid-cols-4 lg:grid-cols-8 gap-4\"><div class=\"col-span-4 row-span-2 relative overflow-hidden rounded-lg group\"><img src=\"ASSET[table-farmhouse.jpg]\" alt=\"Modern farmhouse\" class=\"w-full h-full object-cover min-h-[500px] transition-transform duration-500 group-hover:scale-105\"/><div class=\"absolute bottom-0 left-0 right-0 p-6 bg-gradient-to-t from-black/60 to-transparent\"><p class=\"text-white text-sm font-medium\">Modern Farmhouse</p></div></div><div class=\"col-span-2 lg:col-span-4 relative overflow-hidden rounded-lg group\"><img src=\"ASSET[table-midcentury.jpg]\" alt=\"Mid-century\" class=\"w-full h-full object-cover min-h-[240px] transition-transform duration-500 group-hover:scale-105\"/></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "cross-sell",
      "html": "<section class=\"py-16 px-6 lg:px-16\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-7xl mx-auto\"><div data-island=\"ProductCarousel\" data-props='{\"title\":\"Complete the Room\",\"products\":[{\"id\":\"bench-01\",\"name\":\"Matching Bench\",\"price\":\"$485\",\"image\":\"ASSET[bench.jpg]\"},{\"id\":\"chair-01\",\"name\":\"Oak Dining Chair\",\"price\":\"$295\",\"image\":\"ASSET[chair.jpg]\"}],\"slidesToShow\":3}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "before-after",
      "html": "<section class=\"py-20 px-6 lg:px-16\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-5xl mx-auto\"><div class=\"text-center mb-8\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:400\">Room Transformations</h2></div><div data-island=\"BeforeAfter\" data-props='{\"beforeImage\":\"ASSET[before-dining.jpg]\",\"afterImage\":\"ASSET[after-dining.jpg]\",\"caption\":\"Sarah's dining room with The Everyday Table\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "reviews",
      "html": "<section class=\"py-20 px-6 lg:px-16\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-7xl mx-auto\"><div class=\"text-center mb-12\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(1.75rem,3vw,2.25rem);font-weight:400\">In Your Homes</h2></div><div data-island=\"ReviewCarousel\" data-props='{\"reviews\":[{\"id\":\"r1\",\"author\":\"Jessica M.\",\"rating\":5,\"text\":\"Perfect for our open-plan kitchen.\",\"images\":[\"ASSET[customer-1.jpg]\"],\"verifiedPurchase\":true}],\"slidesToShow\":1}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "faq",
      "html": "<section class=\"py-16 px-6 lg:px-16\" style=\"background:var(--lx-bg-color)\"><div class=\"max-w-3xl mx-auto\"><h2 class=\"text-center mb-8\" style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,2.5vw,2rem);font-weight:400\">Frequently Asked Questions</h2><div data-island=\"FAQ\" data-props='{\"items\":[{\"question\":\"Is assembly required?\",\"answer\":\"No. The table is delivered fully assembled.\"},{\"question\":\"Can I customize the size?\",\"answer\":\"Yes. Contact us for a quote on custom dimensions.\"},{\"question\":\"What's your return policy?\",\"answer\":\"30-day returns. We'll arrange pickup and issue a full refund.\"}]}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "cta-footer",
      "html": "<section class=\"py-20 px-6 lg:px-16 text-center\" style=\"background:var(--lx-bg-surface)\"><div class=\"max-w-xl mx-auto\"><h2 style=\"font-family:var(--lx-font-heading);font-size:clamp(1.5rem,2.5vw,2rem);font-weight:400;color:var(--lx-text-color)\">Get Design Tips in Your Inbox</h2><p class=\"mt-3 text-sm\" style=\"color:var(--lx-text-muted)\">Room styling ideas, new releases, and exclusive offers</p><div class=\"mt-6\"><div data-island=\"EmailCapture\" data-props='{\"placeholder\":\"Your email\",\"buttonText\":\"Subscribe\",\"successMessage\":\"Thanks! Check your inbox.\"}'></div></div></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

---

## Summary

Home & lifestyle pages succeed when they **transport the buyer into the space** — not just show them a product. Every section should answer: "What will this look like in my home? How will it feel? Will it fit? Is it worth the price?" Context, scale, material story, and real customer rooms are the four pillars. Skip any of them and conversions collapse.
