# JORC, NI 43-101, ГКЗ — Public Report Red Flags

**Author:** Anton Zaytsev
**Purpose:** Reference for reading public technical reports (JORC, NI 43-101, S-K 1300, PERC, ГКЗ) for what's NOT said. Public reports are constructed by Competent Persons / Qualified Persons under strict liability; they will not lie, but they can omit, qualify ambiguously, or use language that experienced readers parse differently from retail investors.
**Cross-reference:** Used in §3 (Geology) and §4 (Mining) of all sector DD skeletons.

---

## 1. The reporting code landscape

| Code | Jurisdiction | Authority | Equivalent |
|------|--------------|-----------|------------|
| JORC | Australia, ASX-listed | AusIMM, AIG | Industry-standard global reference |
| NI 43-101 | Canada (TSX, TSXV) | Canadian Securities Administrators | Equivalent disclosure |
| S-K 1300 | US (SEC reporters) | SEC | Aligned post-2021 |
| PERC | Pan-Europe | PERC | Equivalent |
| SAMREC | South Africa | SAIMM | Equivalent |
| KazRC | Kazakhstan | Kazakhstan Society for Geology and Mining | Aligned |
| CRIRSCO Template | Global umbrella | CRIRSCO | Source of all above |
| **ГКЗ / GKZ** | **Russia** | **Государственная комиссия по запасам** | **Different classification system, not directly equivalent** |
| **KZ NKZ** | **Kazakhstan (state)** | **National Commission on Reserves** | **State system parallel to KazRC** |

CRIRSCO codes (JORC, NI 43-101, etc.) classify by **geological confidence × economic viability**:
- Inferred → Indicated → Measured (resources, geological confidence increasing)
- Probable → Proven (reserves, after modifying factors applied)

ГКЗ classifies by **degree of exploration**:
- C2 (preliminary) → C1 (detailed) → B (developed) → A (operational)
- Plus categories for "балансовые" (in-balance) vs "забалансовые" (off-balance)

**Critical**: ГКЗ and CRIRSCO are NOT directly mappable. A common shorthand is:
- C2 ≈ Inferred (loose)
- C1 ≈ Indicated (loose)
- B/A ≈ Measured (loose)

But this is approximate at best. A proper translation requires re-estimation under CRIRSCO methodology by a Competent Person, often producing materially different tonnage and grade.

**[ANTON NOTE]** Russian state classification has historically been more permissive on tonnage (deeper extrapolation from limited drilling) and stricter on cut-off (state-set minimum grade for "in-balance"). The combination produces resources that look larger than CRIRSCO equivalent but with lower confidence and stricter economic basis. In DD, always require CRIRSCO re-classification before relying on Russian-classified resources for valuation.

---

## 2. The five categories of red flag

### 2.1 Language red flags — qualified statements

Competent Persons cannot lie, but they can write defensively. The following phrases warrant scrutiny:

| Phrase | Often means | What to check |
|--------|-------------|---------------|
| "In the opinion of the Competent Person" | They are saying something the data doesn't directly support | Pull the supporting data |
| "Subject to confirmation" | Confirmation not done | What's missing? |
| "Based on management representations" | Not independently verified | What was the source? |
| "Reasonable prospect of eventual economic extraction" | Standard JORC test — but how much modification needed? | Modifying factors detail |
| "The Competent Person was unable to verify" | Material fact unverified | What was it? |
| "Within industry-standard tolerances" | Doesn't say what the tolerances are | Compare to specific peer benchmark |
| "Comparable to similar deposits" | Comparison may not be apt | What deposits, what comparison? |
| "Pre-feasibility study level" | Not feasibility study — typically AACE Class 4 estimate | Don't treat numbers as Class 3 |
| "Conceptual" / "Order of magnitude" | AACE Class 5 / scoping — wide uncertainty | ±30–50% accuracy band |
| "Production target" | NOT a reserve — speculative | JORC reserves required if listed |
| "Exploration target" | NOT a resource — speculative | Disclosure required, often misread |

### 2.2 Methodology red flags

Things to look for in technical sections:

**Sampling and assay:**
- Drill spacing for resource classification — is it tighter than the standard for Indicated/Measured?
- Bulk density — measured (cores), assumed (literature), or what?
- QA/QC: are blanks, duplicates, standards (CRMs) shown? Failures explained?
- Lab accreditation — ISO/IEC 17025?
- Assay methodology appropriate for ore type (e.g. fire assay for Au, not just aqua regia)
- Top-cut / capping applied? Justified?

**Resource estimation:**
- Estimation method — ordinary kriging, inverse distance, polygonal? Appropriate for deposit type?
- Variogram model — short range vs deposit dimensions?
- Block size vs drill spacing — too small (over-confident) or too large (smoothed)?
- Cut-off grade — economic, marginal, geological? Realistic at current/forecast metal price?
- Mining recovery and dilution assumed — typical for method?
- Reconciliation with mined production (for operating mines) — within 5–10%?

**Modifying factors (reserves):**
- Metal price used — vs. spot, vs. forward, vs. consensus?
- OpEx assumptions — vendor quotes, benchmarks, asset-specific?
- Recoveries — testwork-based or assumed?
- Mining method appropriate?

### 2.3 Geometry / geology red flags

- Deposit geometry from limited drilling — extrapolated grade laterally or vertically
- Structural complexity not captured (faults, dykes, alteration)
- Oxide / sulphide transition zone — different metallurgy, different recovery
- Grade-tonnage curve flat or stepwise — suggests artificial cut-offs or smoothing
- High-grade core surrounded by low-grade halo — risk of over-mining high-grade in early years (cherry-picking)
- Underground operations with significant ore left in pillars / sill pillars at high grade — recoverable?
- Resource increase year-on-year without commensurate drilling — re-classification only, not new discovery

### 2.4 Economic red flags

- Cut-off grade well below industry benchmark at similar metal price
- LOM (Life of Mine) plan based on resources, not reserves
- NPV calculated at metal price above consensus forecast
- High-grade Year 1–3 followed by lower-grade later — classic cherry-pick to support early NPV
- OpEx not benchmarked to peer assets
- Sustaining capex understated
- Closure cost included as "future" but not NPV-discounted to current
- Working capital not modelled
- Inflation treatment inconsistent (constant-dollar OpEx with current-dollar metal price = double-count error)

### 2.5 Process / metallurgy red flags

- Recovery based on bench-scale testwork only — no locked-cycle, no pilot
- Recovery range cited — apply the low end in DD model
- Metallurgical "complications" mentioned briefly — investigate (refractory, deleterious elements, variability)
- Throughput at design assumed achievable from day 1 — ramp-up curve needed
- Reagent consumption based on testwork without contingency
- Smelter penalty elements not addressed (As, Sb, Bi, F, Hg, Pb)
- Concentrate grade and quality vs. saleability — buyer specifications

---

## 3. Competent Person / Qualified Person — who is signing?

The CP/QP is personally liable for the report. Look at them carefully.

### 3.1 CP/QP red flags
- Same CP/QP signs for multiple unrelated projects across many years — bandwidth issue
- CP/QP has limited site time (1 day, 2 days) for a complex asset
- CP/QP is in-house at the company, not independent
- For NI 43-101, QP must be independent for technical reports filed with SEDAR — verify
- For JORC, CP must be MAusIMM/AIG/similar — verify membership status
- CP/QP has previously signed reports later revised materially down — track record

### 3.2 Site visit
- CP/QP must have done site visit for current report — recency matters
- Site visit duration and scope disclosed?
- What did CP/QP physically inspect (drill core? mine workings? plant?)

### 3.3 Sample of past reports
- Pull the CP/QP's signed reports from past 3–5 years
- Track record of revisions, asset failures, delistings
- This is a 30-min Google search and often very revealing

---

## 4. Specific sector tells

### 4.1 Gold

- Top-cut on grade — typical for vein-style; uniform deposits less needed
- Geometric anisotropy — high-grade shoots; estimation must capture
- Reconciliation with production: bulk sampling, trial mining? Or just block model trust?
- Bullion vs. doré reporting — recovery includes refining stage or not?

### 4.2 Copper

- Cu equivalent grade (CuEq) — formula must be disclosed. By-product credits (Au, Mo, Ag) at what price? At what recovery? CuEq can hide marginal economics.
- Acid soluble Cu vs. total Cu — for porphyries, acid soluble portion can be SXEW vs. flotation
- Pyrite presence — implications for flotation, acid generation

### 4.3 Nickel

- Sulphide vs. laterite — completely different DD universe
- For laterite: Ni grade, Co credit, scandium credit, processing route (HPAL, ferronickel, NPI)
- NiEq grade — formula essential
- Pentlandite vs. pyrrhotite Ni — recovery differential

### 4.4 PGMs

- 6E vs. 4E reporting (6E includes all 6 PGE, 4E typically Pt+Pd+Rh+Au) — make sure consistent
- Prill split (% Pt, Pd, Rh, etc.) — recovery and value implications
- Reef geometry — Merensky, UG2, Platreef (Bushveld); Norilsk disseminated/massive

### 4.5 Iron ore

- Fe% vs. recoverable Fe% (after beneficiation losses)
- DSO (direct ship ore) vs. beneficiable
- Phosphorus, alumina, silica — penalty elements
- Crystalline form — hematite/magnetite/goethite

### 4.6 Bauxite / alumina

- Reactive silica vs. total silica — Bayer plant economics
- A/S modulus — alumina/silica ratio
- Type — gibbsite, boehmite, diaspore — process temperature

### 4.7 Aluminium primary (smelter side, less geology)

- Power cost (¢/kWh) — single largest variable
- Power source carbon intensity (for CBAM)
- Anode quality and cost
- Pot technology (Söderberg, point-feed prebake, point-feed prebake high-amperage)
- Current efficiency (~92–95% best practice for modern PFPB)

### 4.8 Lithium, REE — outside Anton's core but tells:

- Lithium: hard rock vs. brine; lithium carbonate equivalent (LCE); processing route
- REE: light vs heavy REE split (HREE is the value driver); separation technology

---

## 5. Russian / ГКЗ-specific red flags

When DD'ing a Russian asset whose only public technical disclosure is ГКЗ-style:

### 5.1 Categories
- A, B, C1 ≈ "developed" reserves with some confidence
- C2 = preliminary, often based on relatively sparse drilling
- P1, P2, P3 = prognostic resources (very speculative)

### 5.2 Common pitfalls
- "Запасы" (reserves) in Russian state sense ≠ JORC reserves — different economic test
- "Балансовые" (in-balance) means meets the state cut-off, NOT necessarily economic at current prices
- Russian reserves are reported in cumulative ore tonnage and average grade, often without grade-tonnage curve detail
- Drilling that supports a category may be done over decades with different methods — quality variable
- Russian deposits often classified higher (e.g. C1) on the basis of underground sampling rather than diamond drilling — equivalent CRIRSCO classification likely Inferred or low Indicated

### 5.3 Translation discipline
- For DD purposes: **require CRIRSCO-compliant statement** for any Russian asset where Western capital is in play
- Allow 2–4 weeks and $30–80K typically for re-classification by a Western CP
- Discount ГКЗ reserves by 20–40% as starting assumption if CRIRSCO not done — peer benchmarking on Russian assets that have been done both ways

### 5.4 Specific anomalies in Russian disclosure
- Drill spacing accepted by ГКЗ at category C1 would often be Inferred in JORC
- Cut-off grade set by state, not by economic optimisation — can be too low (over-tonnage) or too high (under-tonnage)
- Tailings re-treatment opportunities often hidden in "забалансовые" or "потери" (losses) categories — economically interesting if accessible

---

## 6. NI 43-101 specifically — Canadian disclosure tells

- Form 43-101F1 has specific section structure — non-compliance is rare but signals weakness
- QP must visit and sign per item
- "Recent and meaningful" exploration / development data required
- Annual reserve updates expected for material producers
- Material changes must trigger updated report — gap >24 months on operating mine = stale

---

## 7. Quick triage protocol — reading a 200-page technical report in 90 minutes

1. **5 min — Front matter:** Date, CP/QP, effective date of resources, company name, asset name
2. **10 min — Executive summary:** Key numbers, recommendations, material assumptions
3. **5 min — CP/QP statement:** Independence, qualifications, site visit detail
4. **10 min — Resource and reserve statement table:** Tonnage, grade, contained metal, by category, with prior comparisons
5. **15 min — Drill spacing and QA/QC sections:** Methodology, integrity
6. **10 min — Estimation methodology:** Kriging, IDW, polygonal; block size; capping
7. **5 min — Modifying factors / reserves derivation:** Pit shell or stope optimisation, cut-off, mining factors
8. **10 min — Process and metallurgy:** Testwork basis, recoveries, throughput, reagents
9. **10 min — CapEx and OpEx:** AACE class, breakdown, sustaining capex, contingency
10. **5 min — Financial analysis:** NPV, IRR, payback, metal price assumptions
11. **5 min — Risk and sensitivity:** What is acknowledged, what isn't

After 90 minutes, you should have a 2-page issues list and 10–15 killer questions.

---

## 8. Five "tells" Anton checks first in any public technical report

1. **Effective date of resource statement vs. report publication date** — gap >6 months means resource is stale
2. **CP/QP track record on three previous projects** — Google search
3. **Year-on-year resource change** — is increase from drilling or just re-classification?
4. **Grade-tonnage curve at next-lower cut-off** — does the deposit "stand up" if metal price drops 20%?
5. **CapEx contingency stated as % vs risk-based** — % means it's not really contingency

---

## 9. Killer questions for management (post-report-read)

- "Show me the underlying drillhole assay database — can I see the QA/QC dashboard?"
- "What is the year-on-year reconciliation of mined tonnes and grade vs. block model for the past 24 months?"
- "If metal price drops 20% from your base case, what is the resource at marginal cut-off, and how does this impact the LOM plan?"
- "How was the discount rate set, and what is the rationale for the country risk premium?"
- "Has the resource model been peer-reviewed externally? Show me the reviewer's letter."
- "For your reserve modifying factors, which factors are most sensitive? At what value of each does the project go from positive to negative NPV?"
- "If I commissioned a second independent CP to re-estimate, what's the probability they'd come within ±5% of your numbers?"

---

## 10. Cross-reference

- `intel/sanctions_compliance_intel.md` — Western capital implications of asset disclosure quality
- `methodology/fel_methodology.md` — AACE class vs. report stage
- `risk/red_flags_decision_trees.json` — automated screening
- `skeletons/dd_*.md` — sector-specific application

---

## TODO_ANTON consolidated

1. Specific Russian → JORC re-classification cases Anton has been involved in — outcomes
2. CP/QP firms Anton knows well in CIS / Russia, with quality observations
3. Specific patterns where ГКЗ B/A classified deposits came out at JORC Inferred — anonymised cases
4. UMMC gold-from-tailings: how was the resource classified, what re-classification was required?
5. Personal "tells" beyond the list above — pattern recognition from 16 years
