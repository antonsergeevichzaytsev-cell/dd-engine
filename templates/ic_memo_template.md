# IC Memo Template — Investment Committee Submission

**Author:** Anton Zaytsev
**Purpose:** Standardised format for delivering DD findings to client's Investment Committee. Used as standalone deliverable or as appendix to full DD report.
**Length:** Target 6–10 pages. IC memos longer than 10 pages don't get read; shorter than 4 pages signal insufficient work.
**Audience:** IC members are typically senior PE/family office/corporate strategy people. They are NOT mining experts. Write accordingly.

---

## INSTRUCTIONS FOR USE

1. Replace all `[BRACKETS]` with engagement-specific content
2. Delete sections marked `[OPTIONAL]` if not applicable
3. Keep section headings — IC members navigate by them
4. Maintain BLUF (Bottom Line Up Front) discipline — recommendation on page 1
5. Quantify everything quantifiable; range estimates rather than false precision
6. Cite sources internally with footnotes — full sourcing in main DD report
7. Final version goes through `humanize` and `scrub` skills before delivery

---

# INVESTMENT COMMITTEE MEMORANDUM

**To:** [Client Investment Committee]
**From:** Anton Zaytsev, Independent Technical Advisor
**Date:** [Date]
**Subject:** Technical Due Diligence — [Asset Name]
**Transaction:** [Acquisition / Investment / Financing / JV — value $XXX M]
**DD Scope:** [Standard / Deep / Topic-specific]
**Status:** Final / Draft for Discussion

---

## 1. RECOMMENDATION

[One sentence. One of three options:]

> **PROCEED** — [Specific deal structure or price recommended]

> **PROCEED WITH CONDITIONS** — [Conditional on specific actions listed in §6]

> **DO NOT PROCEED** — [At any price / At terms proposed / Without resolution of fatal flaw in §X]

### Headline rationale (3–5 bullets, no more)

- [Key finding 1 — quantified]
- [Key finding 2 — quantified]
- [Key finding 3 — quantified]
- [Top 1 risk — with magnitude]
- [Top 1 opportunity not in base case — with magnitude]

---

## 2. ASSET SUMMARY

**Asset:** [Name]
**Location:** [Country, region, specific district]
**Type:** [Operating mine / Greenfield project / Brownfield expansion / Integrated complex]
**Commodity:** [Primary + by-products]
**Capacity:** [Annual production at steady state]
**Life of Mine / Project Life:** [Years at sanctioned plan]
**Stage:** [Producing / Construction / FEL 3 / FEL 2 / FEL 1 / Exploration]

**Ownership:**
- [Entity name] — [%] — [Jurisdiction]
- [Entity name] — [%] — [Jurisdiction]
- Ultimate beneficial owners: [Names if disclosable / Reference to UBO chain analysis in §X of main report]

**Counterparty:** [Vendor name in this transaction]
**Transaction structure:** [Asset purchase / Share purchase / Merger / Investment / Project finance]
**Indicative value:** [$XXX M, with multiple of EBITDA or per-tonne-capacity benchmark]

---

## 3. ECONOMIC SNAPSHOT

| Metric | Vendor base case | DD-adjusted view | Variance |
|--------|------------------|-------------------|----------|
| NPV (post-tax, 8% real) | $XXX M | $YYY M | -ZZ% |
| IRR | XX% | YY% | -ZZ pp |
| Payback | X yrs | Y yrs | +Z yrs |
| Capex (remaining to spend) | $XXX M | $YYY M | +Z% |
| Steady-state OpEx (C1) | $X/lb / $/oz / $/t | $Y/lb / $/oz / $/t | +Z% |
| LOM | X yrs | Y yrs | -Z yrs |

**Key DD adjustments to vendor base case:**

1. **CapEx adjustment** [+$XX M] — [Specific reason: independent estimate variance / contingency adequacy / scope gap]
2. **OpEx adjustment** [+$XX/unit] — [Reason]
3. **Recovery adjustment** [-X%] — [Reason]
4. **Schedule adjustment** [+X months] — [Reason]
5. **Risk allowance** [-$XX M from NPV] — [Reason]

**Sensitivity highlights:**
- At metal price -20% from base: NPV becomes $XXX M [or negative]
- At CapEx +20% from DD case: NPV becomes $XXX M
- At schedule +12 months: NPV becomes $XXX M
- **Break-even price for DD-adjusted case:** $X/unit

[INSERT SENSITIVITY TABLE]

---

## 4. KEY FINDINGS

### 4.1 Resources & Reserves

**What we found:** [Plain-language summary of resource confidence, reserve quality, drill data integrity]

**Material observations:**
- [Resource classification compliant / partially compliant / non-compliant with claimed standard]
- [Drill spacing adequate / marginal / inadequate for category]
- [QA/QC robust / partial / weak]
- [Year-on-year resource changes driven by drilling / re-classification / both]
- [LOM plan based on Reserves / Resources / mix — material implication if Resources]

**Implication for transaction:** [Specific impact on valuation, deal structure, or conditions]

[Cross-reference: Section X of main DD report, with intel from `intel/jorc_ni43101_red_flags.md`]

### 4.2 Operations & Process

**What we found:** [Plain-language on operational health, technology fit, process recoveries, throughput vs design]

**Material observations:**
- [Recovery vs design — gap, root cause]
- [Throughput vs design — gap, root cause]
- [Reagent / energy consumption vs benchmark]
- [Equipment condition and maintenance backlog]
- [Process technology vintage and fit-for-purpose]

**Implication for transaction:** [Specific impact]

### 4.3 Capital Project (if applicable — greenfield, expansion, modernisation)

**What we found:** [Plain-language on CapEx confidence, FEL maturity, execution readiness]

**Material observations:**
- [FEL stage achieved vs. claimed]
- [Independent cost estimate variance to FEED]
- [Contingency methodology — risk-based or %]
- [Schedule confidence — critical path, float, dependencies]
- [Owner team capability — adequacy for project size and complexity]
- [Permits status — secured / pending / at risk]
- [Off-take secured / draft / not started]

**Implication for transaction:** [Specific impact]

[Cross-reference: `methodology/fel_methodology.md`, `methodology/owner_team_engineering.md`]

### 4.4 ESG, Tailings, HSE

**What we found:** [Plain-language on tailings, environment, community, safety]

**Material observations:**
- [TSF construction method, consequence classification, GISTM compliance]
- [ITRB constituted? Last meeting?]
- [Closure liability quantified? Funded?]
- [HSE record — LTIFR trend, fatalities last 5 years]
- [Community / Indigenous status — agreements, disputes]
- [Carbon footprint and CBAM exposure if applicable]

**Implication for transaction:** [Specific impact — escrow, R&W, post-close action]

[Cross-reference: `intel/tailings_intel.md`, `intel/cbam_carbon_intel.md`]

### 4.5 Markets, Off-take, Commercial

**What we found:** [Plain-language on customer base, pricing structure, hedging, sanctions exposure]

**Material observations:**
- [Off-take contracts: signed / draft / not started]
- [Customer concentration]
- [Pricing structure vs benchmark]
- [Sanctions exposure on counterparty side]
- [LME / LBMA marketability for refined products]

**Implication for transaction:** [Specific impact]

### 4.6 Governance, Sanctions, Counterparty [CRITICAL FOR CIS/RUSSIA ASSETS]

**What we found:** [Plain-language on UBO chain integrity, sanctions exposure, regulatory status]

**Material observations:**
- [UBO chain verified to natural persons / partial / black box]
- [Sanctions screening at each layer — flagged risks for legal counsel]
- [Recent ownership changes 2022–present — paper or substantive]
- [Equipment / banking / off-take supply chain sanctions exposure]
- [Currency, payment routing complexity]

**Implication for transaction:** [Specific impact — sanctions counsel must opine]

**IMPORTANT:** This memo does not constitute sanctions advice. Specific compliance opinion required from legal counsel before any deal action. See `intel/sanctions_compliance_intel.md` for context.

---

## 5. RISK REGISTER — TOP 10

| # | Risk | Likelihood | Impact ($M or qual.) | Owner post-close | Mitigation |
|---|------|------------|----------------------|------------------|------------|
| 1 | [Specific risk] | H/M/L | $X / Qual | [Function] | [Specific mitigation] |
| 2 | [Specific risk] | H/M/L | $X / Qual | [Function] | [Specific mitigation] |
| 3 | [Specific risk] | H/M/L | $X / Qual | [Function] | [Specific mitigation] |
| 4 | [Specific risk] | H/M/L | $X / Qual | [Function] | [Specific mitigation] |
| 5 | [Specific risk] | H/M/L | $X / Qual | [Function] | [Specific mitigation] |
| 6 | [Specific risk] | H/M/L | $X / Qual | [Function] | [Specific mitigation] |
| 7 | [Specific risk] | H/M/L | $X / Qual | [Function] | [Specific mitigation] |
| 8 | [Specific risk] | H/M/L | $X / Qual | [Function] | [Specific mitigation] |
| 9 | [Specific risk] | H/M/L | $X / Qual | [Function] | [Specific mitigation] |
| 10 | [Specific risk] | H/M/L | $X / Qual | [Function] | [Specific mitigation] |

Full risk register (typically 30–60 risks) in main DD report appendix.

---

## 6. CONDITIONS FOR PROCEED (if recommendation is "Proceed with Conditions")

### 6.1 Pre-close conditions (must be satisfied before signing / close)

1. **[Condition]** — [Owner: client legal / vendor / both]. [Evidence required.] [Deadline.]
2. **[Condition]** — [Owner.] [Evidence required.] [Deadline.]
3. **[Condition]** — [Owner.] [Evidence required.] [Deadline.]

### 6.2 Deal structure recommendations

- **Price adjustment:** [-$XX M from indicative, OR negotiate against specific finding]
- **Earnout / contingent consideration:** [Specific milestone-tied payment for X period]
- **Escrow:** [$XX M for X months against specific liability — tailings, closure, environmental]
- **Reps & warranties:** [Specific reps required — resource accuracy, off-take status, permits, HSE compliance, sanctions]
- **Indemnification:** [Specific carve-outs and caps]

### 6.3 Post-close 100-day plan

[Specific actions for first 100 days post-close. Typically 5–10 items.]

1. **[Action]** — [Function/owner]. [Resource needed.] [Deadline within 100 days.]
2. **[Action]** — [Owner.] [Resource.] [Deadline.]
3. **[Action]** — [Owner.] [Resource.] [Deadline.]

### 6.4 Post-close 12-month critical actions

[Higher-effort items requiring 6–12 months. Typically 3–5.]

1. **[Action]** — [Owner. Cost. Timeline.]
2. **[Action]** — [Owner. Cost. Timeline.]
3. **[Action]** — [Owner. Cost. Timeline.]

---

## 7. WHAT WE COULD NOT VERIFY

[Explicit list of things DD scope did not allow us to verify, with implication]

- **[Item]** — Not in scope / Not accessible / Time-constrained. Implication: [What this means for confidence in finding.]
- **[Item]** — [Reason and implication]
- **[Item]** — [Reason and implication]

**Recommendation on these gaps:** [Additional DD scope? Acceptance of risk? Conditional precedent?]

---

## 8. DD METHODOLOGY & SCOPE SUMMARY

**Engagement:** [Dates of work, hours engaged, in-scope deliverables]
**Documents reviewed:** [Number, summary categories]
**Management interviews:** [Number, key personnel]
**Site visit:** [Yes / No, duration, scope]
**Specialist input subcontracted:** [Disciplines, named or not]
**Limitations:** [Specific limitations of DD process]

**Author independence:** Anton Zaytsev has no current or prior relationship with [Target / Vendor] beyond [specific declaration]. The author has not received any compensation other than from [Client] for this engagement. The author has not relied on non-public information from prior employment.

[Cross-reference: `compliance_overlay.md` Block A for full author statement.]

---

## 9. SOURCES — KEY PUBLIC REFERENCES

[List 5–10 key public sources used. Full citations in main DD report.]

- [Source 1 — Annual report, technical report, regulatory filing]
- [Source 2]
- [Source 3]
- [Industry benchmark database: source, date]
- [Sector-specific reference]

---

## APPENDICES (separate documents)

- A — Full DD Report ([XXX] pages)
- B — Risk Register (Excel, [XX] line items)
- C — Site Visit Report (if applicable)
- D — Specialist Sub-Reports (if applicable)
- E — Issues Log (Excel)
- F — Document Inventory

---

## SIGN-OFF

**Prepared by:**
Anton Zaytsev
Independent Technical Advisor — Mining & Non-Ferrous Metals
[Date]

[Signature block]

---

## TODO_ANTON consolidated

1. Real case studies of past IC memos — language, length, what worked / what was challenged
2. Specific IC styles by client type (PE, family office, corporate strategy, lender) — adjust template by audience
3. Client-side IC member feedback Anton has received — content/format suggestions
