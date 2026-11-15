# Playbook 7: UI/UX & Mobile Ergonomics Audit OS
**Version:** 1.0 (2026 Production Standard)  
**Objective:** Systematically audit and optimize the digital user interface and experience of any website, e-commerce store, or SaaS app, focusing on mobile thumb-zone ergonomics, cognitive load reduction, and checkout velocity.

---

## 1. The Expert Mindset: What Amateurs Do vs. What Pros Do

| Amateur Approach | Veteran UI/UX Product Designer Approach |
| :--- | :--- |
| Designs for desktop first, then compresses elements for mobile. | Designs strictly **Mobile-First** (75%+ of modern D2C and B2B top-of-funnel traffic is on handheld devices). |
| Fills the screen with fancy animations, auto-rotating carousels, and popups. | Eliminates cognitive clutter; knows that auto-rotating banners have a $<1\%$ click rate and destroy mobile performance. |
| Places critical action buttons at the top of the mobile screen. | Anchors primary action buttons inside the natural **Thumb Zone** (bottom third of the screen) using sticky footers. |
| Assumes users read every word. | Designs for the **F-Pattern and Z-Pattern scanner**, using visual weight, high-contrast badges, and scannable bullet points. |

---

## 2. Intake Architecture: What Data to Demand Before Starting

1. **Device Breakdown:** Mobile vs. Desktop traffic split (from GA4 or Shopify analytics).
2. **Page Speed & Core Web Vitals:** Google PageSpeed Insights report for Largest Contentful Paint (LCP), Interaction to Next Paint (INP), and Cumulative Layout Shift (CLS).
3. **Screen Recordings / Heatmaps:** Hotjar or Microsoft Clarity session recordings of mobile checkout sessions.
4. **Current Form / Checkout Funnel:** Drop-off rate at each checkout step.

---

## 3. The 4-Phase Execution Framework

### Phase 1: The Mobile "Thumb Zone" & Ergonomics Audit
On mobile devices, 75% of users navigate with one thumb. Audit the interface against the anatomical thumb map:

```
┌─────────────────────────────────────────────────────────┐
│               THE MOBILE THUMB ZONE MAP                 │
├─────────────────────────────────────────────────────────┤
│ [TOP 25%]  HARD TO REACH  ──► Reserve for non-critical  │
│                               logo, breadcrumbs, search │
├─────────────────────────────────────────────────────────┤
│ [MID 40%]  NATURAL REACH  ──► Product images, key copy, │
│                               swatches, benefit bullets │
├─────────────────────────────────────────────────────────┤
│ [BOTTOM 35%] EASY REACH   ──► STICKY "ADD TO CART" /    │
│                               PRIMARY CTA, bottom nav   │
└─────────────────────────────────────────────────────────┘
```
* **The Sticky ATC Standard:** On any product page or booking page, as soon as the user scrolls past the main buy button, a **persistent sticky bottom bar** must slide up containing: Price, Star rating, and a high-contrast "Add to Cart" or "Book Call" button.

### Phase 2: Cognitive Load & Visual Hierarchy
* **The 5-Second Comprehension Test:** If a first-time visitor cannot explain what the product does and why it matters within 5 seconds of landing on mobile, the visual hierarchy has failed.
* **Typographic Scale:**
  - *H1 (Hero):* 32px–38px on mobile (bold, high contrast).
  - *Body Copy:* Minimum 16px (anything smaller causes mobile eye strain and form zoom issues on iOS).
  - *Line Height:* 1.5x body text size for scannability.
* **Color Psychology:** Reserve the brand’s high-contrast accent color (e.g. electric blue, safety orange, emerald green) **exclusively for primary conversion actions**. If buttons, badges, and headings all share the same color, the eye has no clear visual target.

### Phase 3: The Cart Drawer & Frictionless Checkout
* **The Slide-Out Cart Drawer (Never redirect to a separate cart page):**
  - Keeps the user in their browsing flow.
  - *Elements:* Free shipping progress bar (e.g., *"You are $15 away from Free Express Shipping"*), one-click quantity toggles, and direct Apple Pay / Google Pay / Shop Pay buttons.
* **Form Field Pruning:** Every extra form field reduces conversion by 7%.
  - Eliminate redundant address lines.
  - Enable Google Autofill and Apple Pay 1-click checkout.

### Phase 4: Trust Architecture & Micro-Interactions
* **The Security Triangle:** Place security badges (Norton, McAfee, 256-bit SSL), accepted payment icons (Visa, Mastercard, Amex, Klarna, Tabby), and money-back guarantee seals directly below the final checkout button.
* **Zero-Flicker Micro-Interactions:** Subtle feedback on click (button state changes to a loading spinner upon click to prevent double-charging and reassure the user the system is processing).

### Phase 5: The 20 Laws of UX Heuristic Audit Matrix
Audit every digital touchpoint against the 10 most critical heuristic conversion laws:

| UX Law | Psychological Principle | Conversion Implementation |
| :--- | :--- | :--- |
| **1. Jakob’s Law** | Users spend 99% of their digital life on other sites (Amazon, Apple, Shopify). They expect your store to work like the best sites they already use. | Never reinvent standard navigation. Keep cart icon top-right, search bar accessible, logo top-left, and standard Shopify-style checkout flows. |
| **2. Fitts’s Law** | The time to acquire a target is a function of distance and target size. | Make primary mobile CTAs full-width (minimum **48px–56px** tap target height) and pin them to the bottom thumb zone so zero finger stretching is required. |
| **3. Hick’s Law** | Decision time increases exponentially with the number and complexity of choices. | Limit product bundles to **maximum 3 options** (Good, Better, Best). Collapse secondary technical details into clean accordions. |
| **4. Miller’s Law** | Human working memory can only hold $7 \pm 2$ chunks of information at once. | Chunk product specs into scannable **3-item benefit grids** with bold lead-in words. Avoid long multi-paragraph copy blocks. |
| **5. Doherty Threshold** | System response time must be $< 400\text{ms}$ to maintain human flow state and prevent mental drop-off. | Instant Ajax cart drawer slide-out upon Add-to-Cart click. Zero full-page reload lag on variant or swatch selection. |
| **6. Von Restorff Effect** | When multiple similar items are present, the one that visually differs is remembered and chosen. | In 3-tier pricing tables or bundle selectors, give the middle tier ("Best Value") a high-contrast accent border, elevated shadow, and "MOST POPULAR" pill. |
| **7. Zeigarnik Effect** | People remember incomplete or interrupted tasks far better than finished ones. | Install visual progress meters: *"You're only $14 away from unlocking Free Shipping!"* or multi-step checkout indicators (*"Step 2 of 3"*). |
| **8. Peak-End Rule** | People judge an entire experience by how they felt at its peak emotional moment and at its ending. | Transform the Order Confirmation and Thank You page into an emotional high: Founder validation video, unboxing ritual checklist, and 1-click reward add-on. |
| **9. Aesthetic-Usability Effect** | Users perceive aesthetically pleasing, well-spaced design as significantly easier to use and inherently more trustworthy. | Enforce consistent 8px spatial grid systems, clean typographic hierarchy, and generous whitespace. High design elevates pricing power. |
| **10. Goal-Gradient Effect** | People accelerate their efforts as they perceive themselves getting closer to reaching a goal. | Pre-fill checkout progress meters with the first step already marked complete (*"Step 1: Items Reserved ✓"*) to trigger psychological completion drive. |

---

## 4. The Drop-in Agent Prompt (Copy & Paste)

```markdown
You are a Principal UI/UX Architect and Mobile Ergonomics Specialist who has audited and redesigned multi-million-dollar e-commerce stores and high-converting B2B SaaS applications.

I want you to conduct a comprehensive UI/UX & Mobile Ergonomics Audit for:
- Brand / Product: {{BRAND_NAME}}
- Website / Funnel URL: {{WEBSITE_URL}}
- Business Model: [SPECIFY: D2C E-Commerce OR B2B SaaS]
- Primary Conversion Action: [e.g., Add to Cart, Book a Demo, Start Free Trial]

Deliver an exhaustive, actionable heuristic audit following this 4-step framework:

### STEP 1: Mobile Thumb-Zone & Ergonomics Audit
Evaluate the mobile browsing experience:
1. Identify 3 friction points where key interactive elements (buttons, selectors, form inputs) are placed outside the natural single-thumb zone.
2. Provide exact CSS/layout recommendations to implement a high-converting Sticky Bottom Action Bar.

### STEP 2: Visual Hierarchy & Cognitive Load Teardown
Audit the page against the 5-Second Test:
- Critique typography sizes, contrast ratios, and color distribution.
- Identify distracting visual bloat (e.g., auto-sliding carousels, intrusive popups) that should be eliminated immediately.
- Define the optimal 3-color palette rule: Base background, Neutral text, and the single high-contrast Accent CTA color.

### STEP 3: Cart Drawer / Lead Form Ergonomics
Provide a step-by-step wireframe design for:
- If D2C: The high-converting Slide-Out Cart Drawer (including free-shipping threshold tier, express checkout integration, and micro-upsells).
- If B2B: The frictionless 2-step Lead Capture Form (reducing required fields, integrating smart autofill, and framing the submit button).

### STEP 4: Executive UI/UX Action Checklist (Top 5 Priority Fixes)
Deliver an engineering-ready checklist of the 5 highest-ROI interface changes to implement this week, categorized by: Problem, Recommended Fix, and Expected Metric Impact.
```
