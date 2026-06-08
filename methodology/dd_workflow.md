# DD Workflow — Execution Methodology

**Author:** Anton Zaytsev
**Purpose:** Operational playbook for executing a paid DD engagement end-to-end. Translates strategic positioning ("principal-grade DD") into specific hours, deliverables, and decision points.
**Pricing context:** Standard DD $22–30K / target 35–45 hours. Deep DD $55–85K / target 80–120 hours.
**Use case:** Each engagement starts here. Phase-by-phase, what gets done, when, by whom (Anton + subcontracted specialists if needed).

---

## 1. Engagement phases — at a glance

| Phase | Standard DD hours | Deep DD hours | Output |
|-------|-------------------|---------------|--------|
| 0. Scoping & contract | 2–3 | 3–5 | SoW, NDA, MSA signed |
| 1. Document review | 8–12 | 20–30 | Issues log, KQ list, data room map |
| 2. Public research | 3–5 | 8–12 | Public-domain intel pack |
| 3. Management session | 4–6 (1–2 sessions) | 10–15 (3–4 sessions) | Session notes, gap closures |
| 4. Site visit (if scoped) | 8–12 | 16–24 | Site report, photos, interviews |
| 5. Specialist input (if scoped) | 0–5 (coordination) | 5–15 (coord) | Subcontracted reports |
| 6. Synthesis & risk register | 6–10 | 15–25 | Risk register, red flag log |
| 7. IC memo / report draft | 6–10 | 15–25 | Draft DD report |
| 8. Client review cycle | 2–3 | 5–8 | Final report |
| **Total** | **39–61** (target 35–45) | **97–159** (target 80–120) | |

The "target" hours assume Anton's pre-built infrastructure (skeletons, benchmark database, red flag trees, killer questions library) is leveraged. Without infrastructure, hours are 1.5–2x.

---

## 2. Phase 0 — Scoping & contract (before clock starts)

**Trigger:** Inbound lead via platform / referral / direct outreach. Lead has been qualified (BANT) — budget exists, decision authority confirmed, real need, timing realistic.

**Activities:**

1. **30-min scoping call** with client decision-maker. Questions:
   - What is the asset? Stage? Size? Geography?
   - What decision is the DD informing — bid/no-bid, valuation refinement, financing, partnership?
   - What is the client's existing knowledge — what have they already done?
   - Who else is in the DD process (other advisors, banks, lawyers)?
   - What is the timeline? Hard deadline?
   - What is access — full data room, partial, public sources only? Management access? Site access?
   - What language for deliverables — Russian, English, both?

2. **Internal go/no-go decision** (Anton, ≤24 hours):
   - Do I have the sector expertise? If partial — what gaps need subcontracted specialist?
   - Are there sanctions/compliance issues that make this non-viable? See `compliance_overlay.md`.
   - Is the timeline realistic vs my current load and the proposed scope?
   - Is the pricing in line with Standard ($22–30K) or Deep ($55–85K)? Will this be a discounted rate or full?
   - Is there a retainer conversion path post-DD?

3. **SoW + commercial proposal** — sent within 48 hours of scoping call. Must include:
   - Asset & scope description
   - Specific deliverables (DD report sections, risk register, IC memo support)
   - Out-of-scope items (explicit)
   - Hours budget and fee
   - Timeline with milestones
   - Subcontracted specialists if any (named or to-be-named)
   - Compliance disclosures (Russia residency, regulated-info handling — see `compliance_overlay.md` Block A)
   - Payment terms — 30% upfront for new clients, NET-30 after delivery for established
   - Independence and limitation of liability statements

4. **Contract execution** — MSA + NDA + SoW. Russia residency requires careful structuring of payment route and currency. For Western clients, often invoiced via Kazakhstan/UAE counterparty if Anton has set this up; otherwise direct USD invoicing where permitted.

**Red flags in scoping that should kill the engagement:**
- Client refuses to disclose what the DD will be used for
- Client wants Anton to "validate" a pre-decided outcome (sanction the deal, justify the price)
- Hard sanctions exposure (asset is OFAC SDN, client wants help structuring around US sanctions)
- Timeline incompatible with reasonable scope ("we need this in 5 days, it's a $500M asset")
- Client refuses to engage on independence or expects Anton to act as the seller's expert

---

## 3. Phase 1 — Document review

**Trigger:** Data room access granted.

**Activities:**

### 3.1 Data room map (first 2 hours)

Build an inventory of what is provided:

| Category | Provided | Quality | Gap |
|----------|----------|---------|-----|
| Geology & resources | JORC report 2023 ✓ | Class 2 indicated | No drill spacing map |
| Mining plan | LOM 2024 ✓ | Block model present | No cut-off grade sensitivity |
| Process | PFD ✓, P&ID ✗ | Limited | P&ID critical for process risk |
| CapEx estimate | AACE Class 4 ✓ | FEL 2 stage | No independent verification |
| OpEx model | ✓ | Industry-standard | Unit rates aged |
| Permits | Mining licence ✓ | EIA pending | EIA not in data room |
| Sanctions/compliance | ✗ | — | Major gap |
| Financials | Audit 2023, 2024 ✓ | KPMG | OK |
| Contracts | Off-take draft ✓ | Indicative | Not signed |
| ESG | Phase 1 ESIA ✓ | IFC PS3 partial | Tailings stability missing |

**Output:** Data room map document. This is the foundation of the issues log.

### 3.2 Issues log (first 4–6 hours)

For each document, record:
- Document name, date, author
- Key facts extracted
- Inconsistencies found (vs other documents or known benchmarks)
- Questions for management
- Red flags

Use a structured spreadsheet — not narrative notes. Issues log becomes the master tracking document for the engagement.

### 3.3 First-pass red flag scan (parallel)

Use `risk/red_flags_decision_trees.json` to scan for sector-specific red flags. Flag immediately to client if any "deal-killer" red flag found in week 1 — don't sit on it.

Examples of deal-killer red flags warranting immediate client alert (use `templates/red_flag_alert_template.md`):
- Sanctions exposure not disclosed
- Tailings facility with documented stability concerns and no remediation
- Resource estimate non-compliant with claimed standard (JORC/NI 43-101)
- Major permit denied or revoked, not disclosed
- Litigation that could result in licence revocation

### 3.4 Killer questions list (last 2 hours of Phase 1)

From the issues log, distill 20–30 killer questions for the management session. Group by:
- Resources/reserves (5–8 questions)
- Mining/process (5–8 questions)
- CapEx/OpEx (5–8 questions)
- Permits/HSE/social licence (3–5 questions)
- Commercial/markets (3–5 questions)
- Execution capability (3–5 questions)

Use `skeletons/killer_questions.json` for sector-specific question library.

**Standard DD:** keep to 15–20 KQs to fit single management session.
**Deep DD:** 30+ KQs across 3–4 sessions.

---

## 4. Phase 2 — Public research

**Trigger:** Document review well underway (Phase 1 day 3+).

**Activities:**

1. **Sanctions screening** — OFAC SDN, EU consolidated list, UK HMT, Canada, Australia, Switzerland, Japan. Check entity, beneficial owners, key counterparties (off-takers, EPC). See `intel/sanctions_compliance_intel.md`.

2. **Regulatory & permits** — local mining licence registry (Russia: Rosnedra; Kazakhstan: NCREK; etc.), environmental permit databases, court cases.

3. **Industry benchmarks** — pull from `benchmarks/capex_benchmark_database.json` and update with most recent comparable transactions. For Cu, check published TC/RC. For Au, check published AISC. For Al, check published cash cost curves.

4. **News & litigation** — Bloomberg, Reuters, S&P Capital IQ if available, local press, court databases.

5. **JORC/NI 43-101 / Russian ГКЗ filings** — public filings of comparable assets in same district/sector.

6. **Carbon/CBAM** — if EU exposure, check `intel/cbam_carbon_intel.md`. Assess product CO₂e/t against benchmark, CBAM cash exposure.

7. **Patent & technology** — for non-standard technology, check patent status, licensing structure, alternative providers.

**Output:** Public research pack — 5–10 page memo summarising findings. Used as input to issues log and management session.

---

## 5. Phase 3 — Management session

**Trigger:** Document review and public research substantially complete.

**Format:** 90–120 minute virtual session (or in-person if site visit combined). Use `templates/management_session_protocol.md` for structured execution.

**Attendees (target side):**
- CEO or COO
- CFO
- Technical Director / VP Operations
- Project Director (if relevant CapEx project)
- Geology Manager (if greenfield/early stage)
- HSE Manager (if HSE concerns flagged)

**Attendees (client side):**
- Anton (lead)
- Client decision-maker or DD coordinator (observer, not advocate)
- Subcontracted specialist if relevant area is covered

**Structure:**
1. Opening 5 min — agenda, confirm recording (with consent), confirm confidentiality
2. Strategy/context 15 min — let target speak. Listen for inconsistencies vs documents.
3. Targeted KQs 60–90 min — go through pre-prepared list. Push back where answers are vague or contradict documents.
4. Open-ended close 10 min — "What should we be asking that we haven't?"
5. Documents request — list of additional documents to provide post-session
6. Next-step confirmation 5 min — site visit logistics, follow-up sessions

**Anton's interview discipline:**
- Never accept "trust me" — ask for the document, model, or data backing the claim
- Never let a contradictory statement pass — flag it gently in session, follow up in writing
- Probe for what is NOT being said — what topic does management steer away from?
- Note tonality, hesitation, deflection — qualitative signal goes in session notes
- End with documented agreements on follow-up items

**Post-session, within 24 hours:**
1. Session notes — structured by KQ, capturing answer quality (Strong / Partial / Weak / Evasive)
2. New issues raised → added to issues log
3. Follow-up documents requested → tracked
4. Updates to red flag log

---

## 6. Phase 4 — Site visit (if scoped)

**Standard DD:** Usually not in scope (additional ~$8–12K if added).
**Deep DD:** Often required for execution capability assessment, HSE, tailings.

**Preparation (pre-site, 4–6 hours):**
1. Site visit plan — sites to visit, areas to inspect, interviews to conduct
2. Inspection checklist by area (use `met-accounting.md`, `tailings_intel.md`, and sector skeletons as input)
3. Logistics — visa (Russia residency may complicate Western jurisdictions), transport, PPE requirements
4. Pre-brief with client on what to look for

**On-site (2–4 days):**
1. Opening meeting with site management
2. Plant walk-through with operations
3. Targeted area inspections (concentrator, smelter, tailings, refinery — sector-specific)
4. Operator and supervisor interviews (separately from management — different perspective)
5. Lab visit if metal accounting in scope
6. Document inspection on-site (some documents only available on-site)
7. Closing meeting with site management to clarify findings

**Post-site (4–6 hours):**
1. Site report — structured by area
2. Photo log (anonymised if needed for compliance)
3. Interview transcripts/notes
4. New issues to add to issues log

---

## 7. Phase 5 — Specialist input (if scoped)

Anton's strength is mining + non-ferrous metallurgy + CapEx project management. For depth in adjacent areas, subcontract:

| Area | Anton's coverage | When to subcontract |
|------|------------------|---------------------|
| Resource estimation / QP | Read JORC/NI 43-101, flag red flags | Detailed block model audit, signed QP statement |
| Geotech/pit slope | Identify red flags | Quantitative slope stability analysis |
| Hydrogeology/pit dewatering | Identify red flags | Detailed water balance, dewatering design audit |
| Tailings stability | Identify red flags, principles | Detailed dam safety review, GISTM compliance |
| Metallurgical testwork | Strong (Cu/Ni/Au/Al) | When asset has unusual ore (e.g. refractory complex) |
| Environmental/social impact | Identify red flags | Full ESIA review under IFC PS or Equator Principles |
| Legal/permitting | Identify red flags | Full legal opinion on licence chain, contractual structures |
| Financial/tax | Read financial statements, flag issues | Full financial DD (Big 4 or boutique) |

**Coordination model:**
- Anton stays as principal contact and integrator
- Specialist reports as appendix to main DD report, integrated into risk register
- Specialist fees passed through with 0–15% coordination margin (transparency to client)

---

## 8. Phase 6 — Synthesis & risk register

**Trigger:** All inputs received — documents, public, management, site, specialists.

**Activities:**

### 8.1 Master risk register

Build risk register using `risk/risk_register_prefill.json` as starting point. For each risk:

| Field | Content |
|-------|---------|
| Risk ID | R-001, R-002, etc. |
| Category | Geological, Mining, Process, CapEx, OpEx, Market, Permits, HSE, Sanctions, etc. |
| Description | Specific to this asset |
| Likelihood | H/M/L or 1–5 scale |
| Impact | $ million or qualitative |
| Risk score | L × I |
| Mitigation in place | What target is already doing |
| Mitigation gap | What is not being done |
| Action for deal | Price adjustment, condition precedent, post-close action |
| Owner | Who would own this risk post-close |

Top 20 risks → executive summary. Top 5 risks → IC memo headline.

### 8.2 Red flag consolidation

From red flag log, categorize:
- **Deal-killer** — should not proceed at any price (e.g. sanctions exposure that can't be resolved, fatal-flaw permit issue)
- **Re-price** — proceed only with material price adjustment (e.g. CapEx overrun risk, resource downgrade)
- **Condition precedent** — proceed only with specific actions before close (e.g. signed off-take, completed permit)
- **Post-close action** — proceed, but address within first 6–12 months (e.g. management strengthening, governance changes)

### 8.3 Valuation impact (light touch — Anton not a valuer)

Anton is not a corporate finance / valuation professional, but DD findings have valuation implications. State them qualitatively or in ranges, not point estimates:

- CapEx +15–25% over sanction → NPV impact of $X–Y million at base price deck
- Schedule slip 6–12 months → NPV impact of $X–Y million
- Resource downgrade from Indicated to Inferred on Y% → reserve depletion risk, mine life impact

**Caveat clearly:** "Valuation impact is indicative based on stated assumptions. Independent valuation by corporate finance specialist is recommended."

---

## 9. Phase 7 — IC memo / DD report draft

**Output structure:**

### Section 1: Executive summary (2–3 pages)
- Asset overview
- DD scope and limitations
- Headline recommendation (proceed / proceed with conditions / do not proceed)
- Top 5 risks with quantified impact
- Top 3 actions required pre-close
- Key gaps in DD (what we couldn't verify and why)

### Section 2: Main DD report (40–80 pages standard / 100–200 pages deep)
- Follow sector skeleton (`skeletons/dd_aluminium_smelter.md`, `dd_nickel_pgm.md`, `dd_gold_hydromet.md`, etc.)
- Each section: facts → analysis → red flags → mitigation → DD opinion

### Section 3: Risk register (5–15 pages or separate workbook)
- All identified risks
- Top 20 in main report, full list as appendix

### Section 4: Killer questions outstanding (1–2 pages)
- Questions that could not be answered satisfactorily in DD
- Recommended follow-up

### Section 5: Appendices
- Site visit report
- Specialist reports
- Document list reviewed
- Public sources referenced
- Compliance disclosures (see `compliance_overlay.md`)

**Writing discipline:**
- Conclusions before evidence in each section (BLUF — bottom line up front)
- Quantify where possible, qualify uncertainty when not
- No promotional language ("excellent", "world-class", "tier 1") unless explicitly justified with peer benchmark
- No hedging language without substance ("may be at risk", "could potentially") — state the risk with calibration: "P50 CapEx overrun is estimated at 15–20%"
- No copying from data room documents — paraphrase, attribute, cite

---

## 10. Phase 8 — Client review cycle

**Trigger:** Draft delivered.

**Typical client feedback:**
- Specific factual corrections — accept, correct
- Tone softening on findings — push back. DD opinions are independent.
- "Can you remove this section?" — push back. If finding is real, it stays.
- Additional questions arising from draft — answer if in scope, flag as scope expansion if not

**Final delivery:**
- Final report in PDF (locked) + Word (for client annotation)
- Risk register in Excel
- Executive summary as standalone deck if requested (add-on, ~$3–5K)

**Post-delivery:**
- 30-min walk-through call
- Q&A support for 2 weeks (included)
- Q&A support beyond 2 weeks billed at hourly rate

---

## 11. Retainer conversion — building the post-DD path

Every DD is an opportunity for retainer conversion. Build the path during execution:

### During Phase 0 (scoping)
- Ask "What happens after the deal closes?" Identify the operational role the client will need filled.

### During Phase 6 (synthesis)
- Identify 3–5 post-close actions where client will need ongoing technical support
- These become the natural retainer scope

### During Phase 8 (delivery)
- In the executive summary, list "Post-close priority actions" — these are the seed of the retainer scope
- In the walk-through call, propose retainer structure if natural:
  - "I see these 5 priority post-close actions. I can support these on a [Strategic $8–10K/mo / Embedded $18–25K/mo] basis for the first [3/6/12] months, then we can reassess."

### Post-delivery follow-up
- 30 days after delivery: check in. "How is post-close going? Where are the gaps?"
- 60 days: more specific. "On action 3 (CapEx defense), how is the parallel estimate going?"
- 90 days: propose retainer if gap is real

**See:** `dynamic-pricing` skill for fee structuring, `referral-program` skill for converting DD client to repeat referrer.

---

## 12. Quality control — Anton's own DD audit checklist

Before final delivery, run this self-audit:

- [ ] Have I stated my limitations clearly (compliance overlay)?
- [ ] Have I checked every claim that could affect the recommendation against at least 2 sources?
- [ ] Have I cited public sources for any externally-derived data?
- [ ] Have I paraphrased rather than copied from data room documents?
- [ ] Is every "red flag" I've raised supported by evidence in the report?
- [ ] Have I given management a fair chance to respond to each red flag (covered in management session or follow-up)?
- [ ] Have I quantified uncertainty (ranges, P50/P90) rather than point estimates where appropriate?
- [ ] Have I been clear about what I can verify vs. what I have to take on management representation?
- [ ] Have I avoided promotional language that overstates the asset?
- [ ] Have I avoided understating in a way that exposes me to disagreement later?
- [ ] Have I separated my DD opinion from valuation opinion (which I do not give)?
- [ ] Have I read the executive summary as a standalone document — does it convey the right decision?
- [ ] Have I checked I am not exposing myself or the client to sanctions risk through the engagement structure?

---

## 13. Lessons learned — post-engagement

After every DD, within 1 week of final delivery, capture:

1. **What worked** — methodology elements that delivered well
2. **What didn't** — friction, time overruns, quality issues
3. **What was new** — sector knowledge, regulatory development, technical learning
4. **What to add to infrastructure** — new red flags, killer questions, benchmark data points, intel

Update relevant files:
- `knowledge/anton_cases.json` — add case (anonymized if needed)
- `risk/red_flags_decision_trees.json` — add new red flags discovered
- `skeletons/killer_questions.json` — add new questions
- `benchmarks/capex_benchmark_database.json` — add new data points
- `intel/*.md` — update jurisdiction or topic-specific intel

This is the compounding mechanism. Each DD makes the infrastructure better, which makes each subsequent DD faster and higher-quality.

---

## TODO_ANTON consolidated

1. Personal experience on optimal Phase 1 → Phase 3 sequence (parallel vs serial)
2. Specific Russian/CIS payment routing structures for Western clients (Kazakhstan, UAE, direct)
3. Subcontractor specialist contacts — to be built into `partner-dd` skill
4. Past DD time-actual log — to calibrate hours estimates above
