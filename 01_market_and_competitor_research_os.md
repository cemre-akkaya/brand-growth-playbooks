# Playbook 1: Market & Competitor Intelligence OS
**Version:** 1.0 (2026 Production Standard)  
**Objective:** Deconstruct any market, identify unserved customer demand, expose competitor vulnerabilities, and extract profitable creative/product hooks.

---

## 1. The Expert Mindset: What Amateurs Do vs. What Pros Do

| Amateur Approach | Veteran Intelligence Operator Approach |
| :--- | :--- |
| Browses competitor homepages and lists features in a spreadsheet. | Mines competitors' longest-running paid ads (longevity = profitability) to uncover their validated cash-cow messaging. |
| Reads 5-star reviews to see what people like. | Scrapes 2-star and 3-star reviews to find the "Flaw Mine"—systemic operational failures competitors cannot fix without rebuilding their core business. |
| Assumes the biggest competitor is invincible. | Identifies what the market leader is forced to ignore because of their legacy pricing or enterprise contract model. |
| Focuses on surface UI/UX design. | Maps the competitor's unit economics, pricing psychology, onboarding friction, and post-purchase churn triggers. |

---

## 2. Intake Architecture: What Data to Demand Before Starting

Before running this playbook for any brand, collect or extract these 5 inputs:
1. **Target Brand & Product URL:** Core offer, pricing, current positioning.
2. **Top 3–5 Direct & Indirect Competitors:** URLs, primary product names.
3. **Competitor Ad Library Links:** Direct links to their Meta Ad Library and Google Ads Transparency pages.
4. **Unfiltered Review Datasets:** Amazon reviews, Trustpilot, G2/Capterra, or Reddit community threads where users discuss the category.
5. **Customer Support / Sales Objections:** Top 10 reasons prospects say "no" or cancel.

---

## 3. The 5-Phase Execution Framework

### Phase 0: The Unit Economics & Financial Guardrails Baseline (Common Thread Collective Standard)
Top operators **never touch ad spend, copy, or funnels before auditing unit economics**. If unit economics are broken, scaling spend only accelerates cash exhaustion:
1. **Marketing Efficiency Ratio (MER):**
   $$\text{MER} = \frac{\text{Total Top-Line Revenue}}{\text{Total Paid Ad Spend}}$$
   - *Target:* **$3.0\times – 4.5\times+$** for healthy scaling. In-platform platform ROAS (Meta/Google Ads Manager) is often inaccurate post-iOS 14.5; MER measures true business-level leverage.
2. **Break-Even ROAS (The Floor):**
   $$\text{Break-Even ROAS} = \frac{1}{\text{Gross Margin \%}}$$
   - *Example:* If gross margin after COGS is 65% ($0.65$), Break-Even ROAS is $1 / 0.65 = 1.54$. Any ad campaign operating below $1.54$ is destroying cash on Day 1.
3. **Contribution Margin 1 & 2 (CM1 & CM2):**
   - $\text{CM1} = \text{Revenue} - \text{COGS} - \text{Shipping/Pick-Pack-Fulfill}$. (Measures product delivery efficiency).
   - $\text{CM2} = \text{CM1} - \text{Paid Ad Spend}$. (Measures true variable operational profit before fixed overhead). Top 1% operators manage paid media to maximize total CM2 dollar volume, not vanity platform ROAS.
4. **Post-Purchase Attribution Survey (Zero-Party Truth):**
   - Install a 1-question post-purchase survey on the order confirmation screen (Fairing / Kno Commerce): *"How did you first hear about us?"*
   - Cross-reference self-reported customer attribution against platform pixel reports to discover dark-social, podcast, creator, and word-of-mouth lift.

### Phase 1: The "Flaw Mine" Extraction (2-Star & 3-Star Audit)
* Do not look at 1-star reviews (mostly shipping delays or angry rants) or 5-star reviews (often incentivized or generic).
* Focus strictly on **2-star and 3-star reviews**. These come from thoughtful customers who wanted the product to work but hit a structural failure.
* Cluster complaints into 3 buckets:
  1. *Product Performance Gaps:* What did the product promise that it failed to deliver?
  2. *Hidden Operational Costs:* Surprise fees, forced subscriptions, terrible customer support, difficult cancellation.
  3. *Onboarding / Usability Friction:* Where did the user feel stupid, overwhelmed, or confused?

### Phase 2: Creative & Messaging Intelligence (Meta Ad Library Longevity Audit)
* Open the competitor’s Meta Ad Library.
* Filter for ads running **more than 60–90 days**. Any ad running for 3+ months is demonstrably profitable; if it weren't making money, they would have turned it off.
* Deconstruct their top 3 evergreen ads:
  - **The Hook:** What visual pattern interrupt or statement stops the scroll in the first 2 seconds?
  - **The Angle:** Is it Fear/Anxiety, Desired Identity, Convenience/Time, or Scientific Proof?
  - **The Format:** Founder-to-camera, 3D render, UGC split-screen, comparison chart, or press quote?
  - **The Call-to-Action & Destination:** Does the ad link to the homepage, a collection page, or a dedicated presell advertorial listicle?

### Phase 3: The Blue Ocean Value Curve Analysis
Plot your target brand against competitors across 6 competitive vectors on a scale of 1 to 5:
1. *Price / Capital Outlay*
2. *Time-to-Value (Speed)*
3. *Simplicity / Ease of Use*
4. *Customization / Modularity*
5. *High-Touch Human Support*
6. *Category Focus (Generalist vs. Niche Specialist)*

> **Strategic Law:** Never try to beat a market leader at their own high scores. If they score 5/5 on Scale and Brand Awareness, win by scoring 5/5 on Niche Focus and Onboarding Simplicity.

### Phase 4: Competitive Battlecard Formulation
Synthesize findings into a 1-page executive battlecard per major competitor:
* *Their Core Value Proposition:* (What they tell the market).
* *Their Real Vulnerability:* (What their customers complain about in secret).
* *The Wedge:* (How to position against them in one sentence without sounding petty).

---

## 4. The Drop-in Agent Prompt (Copy & Paste)

```markdown
You are a Principal Market Intelligence Analyst and Product Strategist with 15+ years of experience deconstructing competitive landscapes for high-growth challenger brands and private equity rollups.

I want you to conduct a comprehensive, zero-fluff competitive and market teardown for:
- Brand Name: {{BRAND_NAME}}
- Website / Offer: {{BRAND_URL}}
- Competitors to Analyze: {{COMPETITOR_NAMES_OR_URLS}}
- Target ICP (Ideal Customer Profile): {{TARGET_ICP}}

Follow this exact 4-step execution framework. Do not output generic advice or marketing platitudes. Ground every finding in specific, actionable operational observations.

### STEP 1: The "Flaw Mine" & Negative Review Audit
Analyze customer sentiment across competitors (simulating Trustpilot, Reddit, Amazon, G2).
1. Identify the top 3 recurring operational flaws or broken promises competitors are guilty of.
2. For each flaw, identify WHY the competitor cannot easily fix it (legacy code, business model conflict, cost).
3. Translate each flaw into an immediate opportunity wedge for {{BRAND_NAME}}.

### STEP 2: Competitor Creative & Messaging Deconstruction
Examine the messaging and positioning used by these competitors:
1. What are their primary selling angles (e.g., Fear, Status, Speed, Cost, Clinical Efficacy)?
2. What are the specific hooks and claims they lean on most heavily?
3. What gaps or underserved desires are they completely ignoring in their ad messaging?

### STEP 3: The Strategic Value Curve Matrix
Construct a markdown comparison table scoring {{BRAND_NAME}} and each competitor (1–5) across:
- Price & Total Cost of Ownership
- Speed to Value
- Onboarding Simplicity
- Feature Depth
- Trust & Human Support
- Niche Specialization
Provide a 2-sentence tactical summary of where {{BRAND_NAME}} should intentionally compete and where it should refuse to compete.

### STEP 4: Executive Competitive Battlecards
Deliver a sharp, 1-page battlecard for the top 2 competitors:
- Competitor Overview & Stated Promise
- Their Real Vulnerability (The Achilles' Heel)
- The Exact 1-Sentence "Us vs. Them" Wedge to train sales reps, ads, or landing pages on.
```
