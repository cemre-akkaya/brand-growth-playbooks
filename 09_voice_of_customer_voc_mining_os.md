# Playbook 9: Voice of Customer (VoC) Mining & Review Scraping OS
**Version:** 1.0 (2026 Production Standard)  
**Objective:** Systematically scrape, extract, and categorize the raw, unfiltered language, emotional pain points, and vocabulary used by actual buyers to fuel high-converting ad copy, landing pages, and email messaging.

---

## 1. The Expert Mindset: What Amateurs Do vs. What Pros Do

| Amateur Approach | Master Direct-Response Copywriter Approach |
| :--- | :--- |
| Sits in front of a blank screen trying to brainstorm "clever" copy. | Never invents copy from scratch; **steals the exact words** customers use when venting in private. |
| Uses corporate industry jargon ("optimized synergy", "enterprise-grade"). | Uses the raw emotional slang and visceral metaphors customers use in Reddit threads and reviews. |
| Guesses what customers care about. | Mines 500+ customer reviews to identify the exact 3 phrases that appear in 80% of purchase decisions. |
| Writes copy to impress other marketers. | Writes copy that makes the prospect think: *"How does this person know exactly what I was thinking this morning?"* |

---

## 2. Intake Architecture: Where to Mine Customer Language

1. **Reddit Communities:** Search subreddits where your target ICP hangs out. Search for terms like: `"frustrated with"`, `"hate when"`, `"does anyone know how to"`, `"alternative to"`, `"waste of money"`.
2. **Amazon 2-Star & 3-Star Reviews:** Look at the top 3 best-selling category books or physical products.
3. **Trustpilot / G2 Negative Reviews:** Look at competitors' negative reviews to extract the emotional language of broken customer expectations.
4. **Internal Support / Sales Call Transcripts:** Gong / Chorus call transcripts or Zendesk/Gorgias tickets.

---

## 3. The 4-Bucket VoC Categorization Framework

When analyzing raw customer transcripts, sort quotes into 4 distinct operational buckets:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       THE 4-BUCKET VoC CODEBOOK                             │
├──────────────────────────────┬──────────────────────────────────────────────┤
│ Bucket 1: The Pain & Slang   │ • Visceral descriptions of the status quo    │
│ (Fuels Ad Hooks & Headlines) │ • Exact metaphors and emotional venting      │
│                              │ • e.g. "I felt like I was throwing money     │
│                              │   into a black hole every month."            │
├──────────────────────────────┼──────────────────────────────────────────────┤
│ Bucket 2: The Hesitations    │ • Why they almost didn't buy                 │
│ (Fuels FAQs & Guarantees)    │ • Pre-purchase skepticism and doubts         │
│                              │ • e.g. "I thought this was just another      │
│                              │   overhyped TikTok gimmick."                 │
├──────────────────────────────┼──────────────────────────────────────────────┤
│ Bucket 3: The "Aha!" Moment  │ • The exact moment the product delivered ROI │
│ (Fuels Us vs. Them Copy)     │ • The feeling of relief and vindication      │
│                              │ • e.g. "Within 10 minutes, our entire team   │
│                              │   finally knew what was shipping."           │
├──────────────────────────────┼──────────────────────────────────────────────┤
│ Bucket 4: The Unmet Desires  │ • What competitors failed to provide         │
│ (Fuels New Product Features) │ • e.g. "I just wanted a simple export button │
│                              │   without paying for the enterprise tier."   │
└──────────────────────────────┴──────────────────────────────────────────────┘
```

---

## 4. The Drop-in Agent Prompt (Copy & Paste)

```markdown
You are a Principal Voice of Customer (VoC) Intelligence Researcher and Lead Copywriting Strategist trained in the methodologies of Eugene Schwartz, Joanna Wiebe, and David Ogilvy.

I want you to conduct an in-depth Voice of Customer (VoC) Mining & Copy Extraction for:
- Brand / Category: {{BRAND_OR_CATEGORY}}
- Target ICP: {{TARGET_ICP}}
- Primary Competitors to Mine: {{COMPETITOR_NAMES}}
- Raw Customer Review / Reddit Snippets: {{RAW_TEXT_OR_DATA_INPUTS}}

Execute this research following this 4-step framework:

### STEP 1: The 4-Bucket VoC Codebook Extraction
Analyze the customer feedback and categorize the findings into:
1. **Bucket 1 (The Pain Metaphors):** Extract 5 verbatim or emotionally authentic quotes describing the daily frustration with the current state.
2. **Bucket 2 (The Hidden Hesitations):** Extract 3 specific anxieties that cause prospects to pause before purchasing.
3. **Bucket 3 (The "Aha!" Relief):** Extract 3 phrases capturing the emotional breakthrough of solving the problem.
4. **Bucket 4 (The Unmet Category Desires):** What is the one thing customers are begging for that existing solutions refuse to build?

### STEP 2: The High-Converting Headline Swipe File (10 Headlines)
Using the exact words and phrases mined in Step 1, write 10 high-converting landing page headlines:
- 3 Problem/Agitation Headlines.
- 3 Desired Transformation Headlines.
- 2 "Us vs. Them" Contrarian Headlines.
- 2 Direct Customer Quote Headlines.

### STEP 3: The Objection-Crushing FAQ Blueprint
Identify the top 3 objections discovered in Bucket 2. For each, write an authoritative, empathetic response that completely neutralizes the fear without being defensive.

### STEP 4: Ad Hook Translation
Translate the top 3 pain metaphors from Bucket 1 into 3 scroll-stopping 3-second visual and audio ad hooks for paid social.
```
