# DD Standard — Skeleton Template

**Package:** DD Standard ($22–30K, 80–120 hours, 4–6 weeks)
**Use case:** M&A bid prep, IC submission, pre-acquisition < $50M
**Output:** 15–20 page report, Markdown → docx

---

## How to use

1. Fill `_meta` block (asset, client, scope).
2. Run `scripts/build_dd.py` (Phase 2) — pulls Anton cases by tags, public-source research, CapEx benchmarks.
3. Auto-generated draft populates §1–§4 and §6 placeholders.
4. **Anton writes §5 (Risk Register interpretation), §7 (Recommendations), and final §8 (Executive Summary).** This is the 20–25 hours of irreplaceable judgment.
5. `pandoc` → docx via docx skill. Send.

---

## `_meta`

```yaml
asset_name: ""
asset_location: ""
asset_type: ""           # smelter | refinery | mine | hydromet | mixed
sector: ""               # aluminium | copper | nickel | gold | alumina | other
client: ""               # internal name; anonymize in report
client_industry: ""      # PE | corporate | family office | bank
deal_size_usd: 0
dd_package: "standard"   # lite | standard | deep
date_start: ""
date_due: ""
authors_credentials_from_kg: []   # auto-filled from anton_cases.json by tags
```

---

## 1. Executive Summary

*Anton writes last. 1 page max. Structure:*

- **Asset:** one sentence, type + location + scale.
- **Deal context:** what client is considering, deal size.
- **Top-line view:** Go / Caution / Walk away — one paragraph.
- **3 biggest risks:** bullets.
- **3 biggest upside drivers:** bullets.
- **What to ask in management session:** 3–5 killer questions.

---

## 2. Author Credentials

*Auto-filled from `anton_cases.json` by `tags` matching `sector` and `asset_type`.*

Default block (always included):

> Anton Zaytsev — 16 years in mining and non-ferrous metals across UC RUSAL, Norilsk Nickel, UMMC and ERG. Project Director on a $550M CapEx program (FEL 1–3) at UMMC. Co-author of 7 patents on aluminium alloys at RUSAL. Turnaround lead at Norilsk Nickel covering 305 staff with zero LTI through the campaign.

Then 2–3 sector-specific cases pulled by tag match.

**Compliance footer (mandatory):**

> This DD is built on public sources and Anton Zaytsev's expert interpretation. No confidential information from prior employers is used. Specific company names of prior advisory clients are anonymized.

---

## 3. Asset Overview

### 3.1 Asset identity
- Owner / operator (current)
- Asset commissioning year, last major CapEx
- Nameplate capacity vs actual utilization (last 3 years if public)
- Production split (products, grades)

### 3.2 Location and context
- Country, region, geopolitical context
- Regulatory regime (licensing, environmental, fiscal)
- Sanctions/compliance exposure
- Logistics: export routes, customer geography

### 3.3 Ownership history
- Past 10 years: M&A, restructuring, ownership changes
- Public disputes / litigation if any

*Auto-research populates §3.1–§3.3 from public sources (annual reports, regulator filings, news ≥ 24 months).*

---

## 4. Technology and Operations Assessment

### 4.1 Process flow and technology
- Process route (BOM → product)
- Vintage of core equipment
- Technology benchmark vs current global standard
- Key process bottlenecks (if visible from public ops data)

### 4.2 Energy and feedstock
- Energy source(s), tariff structure, contractual arrangements
- Feedstock supply: own / contracted / spot
- Self-sufficiency vs market exposure

### 4.3 Operational KPIs (public)
- Recovery / current efficiency / specific energy consumption — vs industry benchmark
- HSE record (LTI frequency, major incidents past 5 years)
- Maintenance regime (campaigns, turnaround frequency)

### 4.4 Workforce
- Headcount, productivity (t/man if available)
- Union exposure, labor cost structure
- Key technical leadership turnover

*This section is where Anton's RUSAL/Nornickel/UMMC operational benchmark intuition shows. Cite cases from KG.*

---

## 5. Risk Register

*Anton writes the interpretation. System pre-fills typical risks by sector.*

| ID | Category | Risk | Likelihood (1–5) | Impact (1–5) | Score | Mitigation visible | DD verdict |
|----|----------|------|------------------|---------------|-------|---------------------|------------|

**8 standard categories** (pre-populated by sector):
1. Geology / reserve confidence
2. Processing / metallurgical
3. Energy / utilities
4. Logistics / supply chain
5. Regulatory / permitting
6. Sanctions / compliance
7. ESG / community / closure
8. Technology / equipment obsolescence

Each category gets 2–4 standard risks pre-listed → Anton scores L×I and writes mitigation/verdict column.

---

## 6. CapEx and OpEx Benchmark

### 6.1 CapEx assessment
- Stated CapEx (if any future investment in asset)
- Benchmark from `benchmarks/non_ferrous_capex_ranges.json` (Phase 2)
- Variance analysis: where is asset above/below
- FEL maturity assessment (where in FEL 1–3 the published numbers actually are)

### 6.2 OpEx structure
- Cash cost (C1) decomposition if disclosed
- AISC vs sector cost curve position
- Sensitivity: energy, feedstock, FX, labor

### 6.3 Sustaining CapEx
- Implied annual sustaining vs benchmark
- Deferred CapEx red flags

---

## 7. Recommendations

*Anton writes. Structured as:*

### 7.1 Go / Caution / Walk away
One paragraph, blunt.

### 7.2 Deal-breakers
What would change the verdict to "walk away."

### 7.3 Renegotiation levers
What client should push for in price/structure based on DD findings.

### 7.4 Management session — killer questions
5–7 questions. Each tied to a specific DD finding.

### 7.5 Out-of-scope follow-ups
What's NOT in this DD but should be done before signing (site visit, specialist DDs, legal).

---

## 8. Appendices

### A. Sources consulted
*Auto-generated list from `dd-projects/{asset}/sources/`*

### B. CapEx benchmark methodology
Reference to `benchmarks/methodology.md`

### C. Risk scoring methodology
1–5 likelihood × 1–5 impact scale, with definitions.

### D. Author's prior cases referenced
Auto-pulled from KG by tag match.

### E. Glossary
Reference to `/mnt/project/glossary.md`

---

## Retainer Conversion Hook (do not delete)

*Last section, separate page. Auto-generated at end. Anton edits before sending.*

> **Beyond this DD**
>
> The DD above answers the questions in scope. Items that surfaced as "out-of-scope follow-ups" (§7.5) and ongoing market shifts in [sector] often warrant continued advisory presence post-close.
>
> If useful, two formats are available:
>
> - **Strategic retainer** — monthly 1h call + 8–10h ad-hoc + email access. $8–10K/mo. For PE / family office with CIS exposure.
> - **Embedded retainer** — weekly call + 20–25h delivery + monthly memo. $18–25K/mo. For active M&A or post-close 100-day integration.
>
> Happy to discuss after you've absorbed this DD.
