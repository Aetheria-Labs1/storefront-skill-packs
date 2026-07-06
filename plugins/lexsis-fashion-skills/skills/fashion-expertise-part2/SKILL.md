---
name: fashion-expertise-part2
description: Fashion pages sell **aspiration and identity**, not fabric specs. The page IS the lookbook. Every section should answer **"who will I become wearing this?"** (Part 2 of 2)
---

## Hero Patterns

### Full-Bleed Editorial Hero

```html
<section class="relative h-screen flex items-center">
  <img src="/hero-on-model.jpg" alt="Editorial hero" class="absolute inset-0 w-full h-full object-cover" />
  <div class="absolute inset-0 bg-black/30"></div>
  
  <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
    <div class="max-w-2xl">
      <p class="text-xs uppercase tracking-widest text-white/80 mb-4">Organic Cotton</p>
      <h1 class="text-white font-light leading-none mb-6" 
          style="font-size: clamp(3rem, 8vw, 7rem);">
        The Relaxed Tee
      </h1>
      <p class="text-lg text-white/90 mb-8">Soft, pre-washed, made to last.</p>
      <button class="bg-white text-black px-8 py-4 text-sm font-medium uppercase tracking-wide hover:bg-gray-100 transition">
        Shop Now
      </button>
    </div>
  </div>
</section>
```

---

### Split Lookbook Hero

```html
<section class="min-h-screen bg-white">
  <div class="grid grid-cols-1 lg:grid-cols-2 min-h-screen">
    
    <!-- Left: Image -->
    <div class="relative h-[60vh] lg:h-screen">
      <img src="/lookbook-split.jpg" alt="Lookbook" class="absolute inset-0 w-full h-full object-cover" />
    </div>

    <!-- Right: Text -->
    <div class="flex items-center justify-center p-8 lg:p-16">
      <div class="max-w-md">
        <p class="text-xs uppercase tracking-widest text-gray-500 mb-4">Spring 2026</p>
        <h1 class="text-5xl sm:text-6xl font-light mb-6">Made for Movement</h1>
        <p class="text-base text-gray-600 mb-8 leading-relaxed">
          Relaxed silhouettes. Premium materials. Designed in Los Angeles for the way you live.
        </p>
        <a href="/collection" class="inline-block border-b-2 border-black text-sm uppercase tracking-wide pb-1 hover:opacity-70 transition">
          Explore Collection
        </a>
      </div>
    </div>

  </div>
</section>
```

---

## Lookbook Grid (Asymmetric)

**Editorial-style asymmetric grid with CSS Grid:**

```html
<section class="py-24 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-4xl font-light mb-12">3 Ways to Wear It</h2>
    
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
      <!-- Large hero tile (2x2) -->
      <div class="col-span-2 row-span-2 relative aspect-[3/4] overflow-hidden group">
        <img src="/styled-1.jpg" alt="Casual look" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
      </div>

      <!-- Medium tile (1x2) -->
      <div class="col-span-1 row-span-2 relative aspect-[3/4] overflow-hidden group">
        <img src="/styled-2.jpg" alt="Layered look" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
      </div>

      <!-- Small tile (1x1) -->
      <div class="col-span-1 row-span-1 relative aspect-square overflow-hidden group">
        <img src="/styled-3.jpg" alt="Dressed up" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
      </div>

      <!-- Small tile (1x1) -->
      <div class="col-span-1 row-span-1 relative aspect-square overflow-hidden group">
        <img src="/styled-4.jpg" alt="Detail shot" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
      </div>
    </div>
  </div>
</section>
```

**Grid size mapping:**
- Large: `col-span-2 row-span-2` (2x2)
- Medium: `col-span-1 row-span-2` (1x2)
- Small: `col-span-1 row-span-1` (1x1)

**Hover effects** (via CSS):
- `group-hover:scale-105` — Zoom
- `group-hover:brightness-110` — Shimmer
- Ken Burns: `transition-transform duration-700`

---

## Social Proof / Reviews

**UGC-first, with customer measurements:**

```html
<section class="py-24 bg-gray-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-4xl font-light mb-4">What Customers Are Wearing</h2>
    <p class="text-base text-gray-600 mb-12">Real people, real fit feedback.</p>

    <div data-island="ReviewCarousel" data-props='{
      "displayMode": "ugc_gallery",
      "items": [
        {
          "customerName": "Alex M.",
          "customerStats": "5'\''8\", 145lbs, size M",
          "rating": 5,
          "reviewText": "Perfect fit. True to size. Fabric is so soft—ordering more colors.",
          "customerPhoto": "/ugc-customer-1.jpg",
          "verifiedPurchase": true,
          "sizeRating": "true_to_size",
          "styleTags": ["casual", "everyday"]
        },
        {
          "customerName": "Sarah J.",
          "customerStats": "5'\''6\", 130lbs, size S",
          "rating": 5,
          "reviewText": "Love the relaxed fit. Great for layering.",
          "customerPhoto": "/ugc-customer-2.jpg",
          "verifiedPurchase": true,
          "sizeRating": "true_to_size"
        }
      ],
      "filters": ["sizeRating", "styleTags"],
      "sortBy": "photosFirst"
    }'></div>

    <!-- Size Rating Summary -->
    <div class="mt-12 max-w-md mx-auto">
      <p class="text-sm font-medium mb-4">Fit Rating</p>
      <div class="space-y-2">
        <div class="flex items-center gap-3">
          <span class="text-xs text-gray-600 w-24">Runs Small</span>
          <div class="flex-1 bg-gray-200 h-2 rounded-full">
            <div class="bg-gray-800 h-2 rounded-full" style="width: 10%;"></div>
          </div>
          <span class="text-xs text-gray-600">10%</span>
        </div>
        <div class="flex items-center gap-3">
          <span class="text-xs text-gray-600 w-24">True to Size</span>
          <div class="flex-1 bg-gray-200 h-2 rounded-full">
            <div class="bg-gray-800 h-2 rounded-full" style="width: 85%;"></div>
          </div>
          <span class="text-xs text-gray-600">85%</span>
        </div>
        <div class="flex items-center gap-3">
          <span class="text-xs text-gray-600 w-24">Runs Large</span>
          <div class="flex-1 bg-gray-200 h-2 rounded-full">
            <div class="bg-gray-800 h-2 rounded-full" style="width: 5%;"></div>
          </div>
          <span class="text-xs text-gray-600">5%</span>
        </div>
      </div>
    </div>
  </div>
</section>
```

**WHY**: Customer body stats + photos = trust. Aggregate fit data reduces returns.

---

## Anti-Patterns (Fashion Page Killers)

### 1. Product-on-white-only (No Lifestyle)
**Bad**: Only flat-lay white-background shots.  
**Fix**: Lead with on-model editorial. Flat-lays secondary.

### 2. Stock Photos
**Bad**: Generic stock models.  
**Fix**: Custom or AI-generated brand-consistent imagery.

### 3. Centered Symmetric Layouts
**Bad**: Every section centered, equal columns.  
**Fix**: Asymmetric grids, off-center text, varied sizes.

### 4. Too Much Text
**Bad**: Long paragraphs explaining product story.  
**Fix**: 1-3 word headlines. Let imagery carry narrative.

### 5. Corporate Typography
**Bad**: Arial, same size everywhere.  
**Fix**: Dramatic size contrast. Ultra-light heroes (300 weight).

### 6. Equal-Column Product Grids
**Bad**: 4-column grid, all same size.  
**Fix**: Asymmetric lookbook grids. Mixed sizes.

### 7. Generic "Shop Now" CTAs
**Bad**: Every CTA says "Shop Now."  
**Fix**: "Shop [Collection]", "Add to Bag", "View Lookbook."

### 8. Ignoring Mobile Aspect Ratios
**Bad**: 16:9 landscape heroes that crop poorly.  
**Fix**: Portrait aspect ratios (3:4, 4:5). Test mobile.

### 9. Size Chart as Afterthought
**Bad**: Size chart buried in footer.  
**Fix**: SizeGuide island link prominent near BuyBox.

### 10. No Model Measurements
**Bad**: Product photos with no fit context.  
**Fix**: Always include: "Model is 5'10", wearing M."

### 11. Overuse of Urgency (Non-Sale)
**Bad**: Countdown timers on regular PDPs.  
**Fix**: Use urgency only for real sales/drops.

### 12. No UGC / Customer Photos
**Bad**: Only professional brand photos in reviews.  
**Fix**: ReviewCarousel with UGC. Prioritize customer photos.

---

## Complete Fashion PDP Blueprint

**Full VibePage JSON for a premium fashion PDP:**

```json
{
  "head": {
    "title": "The Relaxed Tee — Organic Cotton",
    "meta": [
      {"name": "description", "content": "Soft, pre-washed, made to last."}
    ]
  },
  "theme_css": ":root { --lx-accent-color: #0a0a0a; --lx-text-color: #0a0a0a; --lx-text-muted: rgba(0,0,0,0.6); --lx-bg-color: #ffffff; --lx-font-heading: 'Inter', sans-serif; --lx-font-body: 'Inter', sans-serif; }",
  "sections": [
    {
      "id": "hero",
      "html": "<section class=\"relative h-screen flex items-center\"><img src=\"/hero-editorial.jpg\" alt=\"The Relaxed Tee\" class=\"absolute inset-0 w-full h-full object-cover\" /><div class=\"absolute inset-0 bg-black/20\"></div><div class=\"relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full\"><div class=\"max-w-2xl\"><p class=\"text-xs uppercase tracking-widest text-white/80 mb-4\">Organic Cotton</p><h1 class=\"text-white font-light leading-none mb-6\" style=\"font-size: clamp(3rem, 8vw, 7rem);\">The Relaxed Tee</h1><p class=\"text-lg text-white/90 mb-8\">Soft, pre-washed, made to last.</p><a href=\"#product\" class=\"inline-block bg-white text-black px-8 py-4 text-sm font-medium uppercase tracking-wide hover:bg-gray-100 transition\">Shop Now</a></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "product",
      "html": "<section class=\"py-16 bg-white\"><div class=\"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8\"><div class=\"grid grid-cols-1 lg:grid-cols-2 gap-12\"><div><div data-island=\"ProductGallery\" data-props='{\"images\":[{\"url\":\"/hero-editorial.jpg\",\"alt\":\"Model wearing product\"},{\"url\":\"/front-flat.jpg\",\"alt\":\"Front view\"},{\"url\":\"/back-flat.jpg\",\"alt\":\"Back view\"},{\"url\":\"/detail-texture.jpg\",\"alt\":\"Fabric detail\"}],\"layout\":\"editorial\",\"zoom\":true,\"aspectRatio\":\"3:4\"}'></div></div><div class=\"flex flex-col gap-8\"><div><p class=\"text-xs uppercase tracking-widest text-gray-500 mb-3\">Organic Cotton</p><h2 class=\"text-4xl sm:text-5xl font-light mb-4\">The Relaxed Tee</h2><p class=\"text-base text-gray-600 mb-6\">Soft, pre-washed, made to last.</p><p class=\"text-2xl font-semibold mb-8\">$48</p></div><div><p class=\"text-sm font-medium mb-3\">Color</p><div data-island=\"VariantSwatches\" data-props='{\"type\":\"color\",\"display\":\"swatch\",\"size\":\"lg\",\"showLabel\":true}'></div></div><div><div class=\"flex items-center justify-between mb-3\"><p class=\"text-sm font-medium\">Size</p><button class=\"text-sm underline\">Size Guide</button></div><div data-island=\"VariantSwatches\" data-props='{\"type\":\"size\",\"display\":\"button\",\"size\":\"md\"}'></div></div><div data-island=\"BuyBox\" data-props='{\"showPrice\":false,\"showQuantity\":true,\"ctaText\":\"Add to Bag\"}'></div><div class=\"border-t pt-6\"><details class=\"group\"><summary class=\"flex items-center justify-between cursor-pointer text-sm font-medium mb-2\">Material<svg class=\"w-5 h-5 transition-transform group-open:rotate-180\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M19 9l-7 7-7-7\"/></svg></summary><p class=\"text-sm text-gray-600 mt-2\">100% organic cotton. GOTS certified.</p></details></div></div></div></div><div data-island=\"SizeGuide\" data-props='{\"measurements\":[{\"size\":\"XS\",\"chest\":\"32-34\\\"\",\"waist\":\"24-26\\\"\",\"hip\":\"34-36\\\"\"},{\"size\":\"S\",\"chest\":\"34-36\\\"\",\"waist\":\"26-28\\\"\",\"hip\":\"36-38\\\"\"}],\"fitDescription\":\"Relaxed fit. Size down for fitted.\",\"modelStats\":\"Model is 5'10\\\" (178cm), wearing M.\"}'></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "styling",
      "html": "<section class=\"py-24 bg-white\"><div class=\"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8\"><h2 class=\"text-4xl font-light mb-12\">3 Ways to Wear It</h2><div class=\"grid grid-cols-2 lg:grid-cols-4 gap-4\"><div class=\"col-span-2 row-span-2 relative aspect-[3/4] overflow-hidden group\"><img src=\"/styled-1.jpg\" alt=\"Casual\" class=\"w-full h-full object-cover transition-transform duration-700 group-hover:scale-105\" /></div><div class=\"col-span-1 row-span-2 relative aspect-[3/4] overflow-hidden group\"><img src=\"/styled-2.jpg\" alt=\"Layered\" class=\"w-full h-full object-cover transition-transform duration-700 group-hover:scale-105\" /></div><div class=\"col-span-1 row-span-1 relative aspect-square overflow-hidden group\"><img src=\"/styled-3.jpg\" alt=\"Dressed up\" class=\"w-full h-full object-cover transition-transform duration-700 group-hover:scale-105\" /></div></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "cross-sell",
      "html": "<section class=\"py-16 bg-gray-50\"><div class=\"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8\"><h2 class=\"text-3xl font-light mb-8\">Complete the Look</h2><div data-island=\"ProductCarousel\" data-props='{\"products\":[{\"id\":\"prod_123\",\"title\":\"Wide Leg Cargo\",\"price\":\"$98\",\"image\":\"/cargo.jpg\"},{\"id\":\"prod_124\",\"title\":\"Canvas Sneaker\",\"price\":\"$68\",\"image\":\"/sneaker.jpg\"}],\"layout\":\"scroll\",\"ctaStyle\":\"quickAdd\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "reviews",
      "html": "<section class=\"py-24 bg-white\"><div class=\"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8\"><h2 class=\"text-4xl font-light mb-12\">What Customers Are Wearing</h2><div data-island=\"ReviewCarousel\" data-props='{\"displayMode\":\"ugc_gallery\",\"items\":[{\"customerName\":\"Alex M.\",\"customerStats\":\"5'8\\\", 145lbs, size M\",\"rating\":5,\"reviewText\":\"Perfect fit. True to size.\",\"customerPhoto\":\"/ugc-1.jpg\",\"sizeRating\":\"true_to_size\"}],\"sortBy\":\"photosFirst\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "cta",
      "html": "<section class=\"py-16 bg-gray-50\"><div class=\"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center\"><a href=\"#product\" class=\"inline-block bg-black text-white px-12 py-5 text-sm font-medium uppercase tracking-wide hover:bg-gray-800 transition\">Add to Bag</a></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

---

## Summary

Fashion pages are **editorial, image-forward, minimal**. Photography does 80% of the work.

**Core principles:**
1. **Aspiration first** — hero imagery before specs
2. **Whitespace = luxury** — generous spacing (py-16, py-24)
3. **Dramatic typography** — huge heroes, tiny eyebrows
4. **Monochrome + one accent** — let product color pop
5. **Asymmetric layouts** — editorial ≠ symmetry
6. **Minimal copy** — 1-3 word headlines
7. **UGC > professional reviews** — real customers, real fit
8. **Size guide prominent** — reduce returns, model stats
9. **Lookbook grids** — asymmetric CSS Grid, mixed sizes
10. **Sub-vertical tailoring** — streetwear ≠ basics ≠ athleisure

Use HTML+Tailwind. Inject islands via `data-island`. Use CSS vars for theming. Test on mobile. Let imagery lead.
