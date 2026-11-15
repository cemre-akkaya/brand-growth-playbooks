# Protocol 00: The Universal Tiered Data Connector & Intake Protocol
**Version:** 1.0 (2026 Production Standard)  
**Objective:** Guarantee that every playbook executes on verified, high-quality data without forcing expensive third-party tools (like Apify). Provides a 4-tier fallback hierarchy (Free Native ➔ Free Official API ➔ Manual Drop ➔ Paid Cloud).

---

## 1. The Core Philosophy: "No Hallucinations, Minimum Cost"

An elite AI agent must **never guess or invent data** when doing competitive analysis, CRO audits, or positioning. However, it must also **never force expensive cloud scrapers** when free, native, or manual options exist.

Before running any analysis, the agent executes **Step 0: The Data Connector Check**, auditing available inputs and offering the user the most cost-effective path.

---

## 2. The 4-Tier Data Hierarchy for Every Task

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       THE 4-TIER DATA INTAKE MATRIX                         │
├─────────────────┬───────────────────────────────────────────────────────────┤
│ TIER 1: FREE    │ • Direct Python scrapers (Shopify /products.json, sitemaps)│
│ NATIVE (Cost: $0│ • Public Reddit .json feeds & RSS endpoints               │
│                 │ • Meta Ad Library direct search URL extraction            │
├─────────────────┼───────────────────────────────────────────────────────────┤
│ TIER 2: FREE    │ • Google Search Console & GA4 Service Account credentials │
│ DIRECT API ($0) │ • Reddit PRAW API (Free 100 queries/min developer tier)   │
│                 │ • Meta Graph API / Free Developer Token                   │
├─────────────────┼───────────────────────────────────────────────────────────┤
│ TIER 3: MANUAL  │ • Drag-and-drop CSV export from GA4, Shopify, or Klaviyo  │
│ 10-SEC DROP ($0)│ • Paste 5-10 raw review snippets or competitor URLs       │
│                 │ • Upload a screenshot of the mobile landing page          │
├─────────────────┼───────────────────────────────────────────────────────────┤
│ TIER 4: CLOUD   │ • Apify / Bright Data actors (Only when explicitly        │
│ AUTOMATED ($$)  │   authorized by the user for massive bulk scale)         │
└─────────────────┴───────────────────────────────────────────────────────────┘
```

---

## 3. Task-by-Task Connector Menu

| Task / Playbook | Tier 1: Free Native Method ($0) | Tier 2: Free Official API ($0) | Tier 3: 10-Sec Manual Drop ($0) | Tier 4: Paid Cloud ($$) |
| :--- | :--- | :--- | :--- | :--- |
| **01. Market & Competitors** | Direct web scraping of competitor homepages, sitemaps, and public Meta Ad Library links. | Free Meta Ad Library Graph API token. | Paste competitor URLs and 3 longest-running ad copy angles. | Apify Meta Ad Library Scraper actor. |
| **04. CRO & Funnel Audit** | Free PageSpeed Insights API + Python mobile viewport screenshot / HTML audit. | Google Search Console & GA4 read-only service account. | Export 30-day GA4 Landing Pages report as CSV and drop in chat. | Full Hotjar / FullStory recording sync. |
| **05. Lifecycle / Klaviyo** | Public newsletter signup test to capture welcome sequence. | Klaviyo Read-Only Private API Key (`pk_...`). | Export Flow performance metrics table as CSV. | Third-party retention intelligence tool. |
| **09. Voice of Customer (VoC)**| Free Reddit public JSON endpoints + Amazon public review DOM scraping. | Reddit Developer API (PRAW with free client ID). | Copy-paste 10 recent customer support tickets or 3-star reviews. | Apify Trustpilot / Amazon Scraper. |
| **10. GEO / AI Search** | Python query to Google AI Overviews & Perplexity free search. | Free Bing Web Search / Google Custom Search API. | Paste 5 queries you typed into ChatGPT and what came up. | Enterprise Semrush / BrightEdge API. |
| **11. E-Commerce PDP** | Free scraping of Shopify `/products.json` & theme source code. | Shopify Admin Read-Only Custom App Token. | Paste product URL + screenshot of the mobile PDP above-the-fold. | Headless e-commerce crawler. |

---

## 4. The Universal "Step 0" Agent Check Protocol

Every playbook system prompt must begin with this mandatory execution block:

```markdown
### STEP 0: Data Verification & Connector Audit (MANDATORY BEFORE PROCEEDING)

Before generating any strategic or tactical output, audit the data provided by the user:

1. **Check for Ground-Truth Data:** Do you have verified real-world data (actual ad copies, real customer reviews, verified funnel metrics, or live URL contents)?
2. **If Data is Missing or Generic:** DO NOT guess or hallucinate. Stop and present the user with the **Tiered Data Ingestion Menu**:

   > "To ensure this playbook is 100% grounded in your actual business reality, please choose how you'd like to provide the input data:
   > 
   > 🟢 **Option A (Free Native Scrape - Recommended):** Give me the public URLs (Website, Competitors, Reddit keywords), and I will use our free internal Python scripts to pull the live pages, catalog, and public data for $0.
   > 
   > 🟡 **Option B (10-Second Manual Drop):** Drop a quick CSV export or paste 5-10 raw bullet points (e.g., your top 5 customer complaints, your GA4 funnel drop-off numbers, or your competitor's ad copy).
   > 
   > 🔵 **Option C (Direct Free API Key):** If you have a free Google Cloud Service Account, Reddit API, or Klaviyo read-only key, let me know and I will pull the data directly.
   > 
   > 🟣 **Option D (Apify Cloud Scraper):** If you prefer full automation at scale and have Apify compute credits, provide authorization and I will run the cloud actor.
   > 
   > Which option would you like to use?"

3. **Once the user selects an option or provides data:** Proceed immediately to Step 1.
```
