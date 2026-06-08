# CBAM & Carbon Intel — Mining & Non-Ferrous Metals

**Author:** Anton Zaytsev
**Purpose:** Reference for DD on assets exposed to EU Carbon Border Adjustment Mechanism (CBAM) or analogous regimes (UK, Australia, Canada, others). Direct material impact on asset economics for any commodity sold into EU/UK markets.
**Last calibration:** 2026. Verify current rates, scope, methodology via EU Commission and DG TAXUD before each engagement.

---

## 1. CBAM in 30 seconds

The **Carbon Border Adjustment Mechanism** prices the embedded carbon of imports into the EU at the same level as EU ETS (Emissions Trading System). Importers must surrender CBAM certificates equal to the embedded emissions of covered products, paying the prevailing EU ETS price minus any carbon price paid in country of origin.

**Coverage (2026 baseline — verify scope expansion):**
- **Cement** — clinker, cement
- **Iron & steel** — pig iron, crude steel, certain downstream products
- **Aluminium** — unwrought, certain semi-finished products
- **Fertilisers** — ammonia, urea, nitrates
- **Electricity** — imports
- **Hydrogen** — added under scope expansion
- **Future:** Scope expansion under discussion to **chemicals (downstream)**, **polymers**, **non-ferrous metals beyond aluminium** (copper, nickel), and downstream products with embedded CBAM commodities

**Timeline:**
- **Oct 2023 – Dec 2025:** Transitional period — reporting only, no financial obligation
- **Jan 2026:** Definitive period — financial obligation begins, importers must purchase and surrender CBAM certificates
- **2026–2034:** Phased reduction of free EU ETS allowances for EU producers, with corresponding phase-in of full CBAM obligation. By 2034, 100% CBAM applies, 0% free allocation for affected EU sectors

**DD relevance:** Every asset selling covered product into EU has a quantifiable CBAM cash exposure. This must be modelled, not ignored.

---

## 2. CBAM cash exposure calculation

### 2.1 The formula

```
CBAM cost per tonne product = 
  (Embedded emissions t CO₂e/t product) 
× (EU ETS price €/t CO₂ − Origin country carbon price €/t CO₂) 
× (Phase-in factor — 0% in 2025, ramping to 100% by 2034)
```

### 2.2 Inputs

**Embedded emissions:**
- Direct (Scope 1) — process emissions, on-site fuel combustion
- Indirect (Scope 2) — purchased electricity, heat
- Scope 3 not included in definitive CBAM (precursor materials separately handled via "embedded emissions of precursors")

Must use **EU CBAM methodology** for measurement and verification — not corporate sustainability reporting standards. The default values are punitive, so actual measured & verified emissions are economically essential.

**EU ETS price:**
- 2026 baseline: ~€80–100/t CO₂ (high volatility — has ranged €60–€110 in recent years)
- Forward curve typically trades €5–10/t above spot for 2027–2030 vintages
- Long-term forecasts ~€100–150/t by 2030 in most scenarios

**Origin country carbon price:**
- Russia: no enforced carbon price (some discussion of domestic scheme; verify)
- Kazakhstan: domestic ETS pilot — limited applicability for CBAM offset
- China: national ETS exists but verification for CBAM offset is contentious
- UAE: no carbon price
- Türkiye: emissions reporting system but no carbon price for offset
- Most CIS / Middle East / India: no offset available
- South Africa: carbon tax exists, may be partially creditable

**Phase-in factor (free allowance phase-out):**

| Year | EU free allocation reduction | CBAM obligation |
|------|------------------------------|-----------------|
| 2026 | 2.5% | 2.5% |
| 2027 | 5% | 5% |
| 2028 | 10% | 10% |
| 2029 | 22.5% | 22.5% |
| 2030 | 48.5% | 48.5% |
| 2031 | 61% | 61% |
| 2032 | 73.5% | 73.5% |
| 2033 | 86% | 86% |
| 2034 | 100% | 100% |

So in 2026, CBAM cost = full formula × 2.5%. By 2030 = × 48.5%. By 2034 = × 100%.

---

## 3. Indicative CBAM cash exposure by commodity

These are **rough orders of magnitude** for DD scoping. Always model with asset-specific data.

### 3.1 Primary aluminium (smelter)

| Production route | Direct CO₂ (t/t Al) | Indirect CO₂ from power (t/t Al) | Total Scope 1+2 (t CO₂e/t Al) | CBAM at 2034 / €100 ETS |
|------------------|---------------------|----------------------------------|--------------------------------|-------------------------|
| Hydropower-based (e.g. RUSAL Krasnoyarsk, Hydro Sunndal) | ~1.5–2.0 | ~0.5–1.0 | ~2.0–3.0 | ~€200–300/t Al |
| Coal-power-based (typical Chinese) | ~1.5–2.0 | ~12–15 | ~14–17 | ~€1,400–1,700/t Al |
| Mixed grid (typical Indian, Middle East gas) | ~1.5–2.0 | ~7–11 | ~9–13 | ~€900–1,300/t Al |

**Critical insight:** CBAM creates a structural price advantage for low-carbon aluminium (hydro, nuclear, renewable). Russian hydro-based primary Al has lowest carbon intensity globally. **But this advantage is neutralised if sanctions block EU sales** — see `sanctions_compliance_intel.md`.

LME pricing is starting to differentiate "low-carbon" aluminium (LME launched a separate low-carbon contract — verify current liquidity and premium). Combined with CBAM, this creates 2-tier market.

### 3.2 Alumina (refinery)

Less direct CBAM exposure currently — alumina is sometimes treated as precursor material to aluminium (so its embedded emissions count toward aluminium's CBAM), sometimes separately listed. Verify current scope.

Typical alumina CO₂e intensity: 0.7–1.5 t CO₂e/t alumina, depending on:
- Bayer process temperature (low-T gibbsite vs high-T diaspore — diaspore higher)
- Heat source (coal, gas, oil)
- Calciner technology

### 3.3 Iron & steel

| Route | t CO₂e/t crude steel | CBAM at 2034 / €100 ETS |
|-------|----------------------|-------------------------|
| EAF with scrap (e.g. modern EU recycler) | ~0.5–0.8 | ~€50–80/t steel |
| Blast furnace / BOF (integrated) | ~1.8–2.3 | ~€180–230/t steel |
| Coal-DRI (e.g. some Indian) | ~1.5–2.0 | ~€150–200/t steel |
| Gas-DRI/EAF (e.g. some Middle East) | ~1.0–1.3 | ~€100–130/t steel |
| H2-DRI/EAF (future) | ~0.3–0.5 | ~€30–50/t steel |

### 3.4 Copper, Nickel, Zinc, Lead — not in current scope but under consideration

Watch this space. Scope expansion to base metals expected in coming review cycles.

If included, indicative carbon intensities:
- Copper cathode (mine-to-metal): 4–8 t CO₂e/t Cu typical, can be 10+ for coal-power smelters
- Refined nickel Class 1: highly variable, 8–60 t CO₂e/t Ni depending on ore type (sulphide vs laterite) and processing route
- Zinc: 1.5–3.5 t CO₂e/t Zn

---

## 4. Sources of embedded emissions data — what DD must verify

Asset will report emissions. DD must check:

### 4.1 Methodology
- Is asset using **EU CBAM methodology** (Implementing Regulation (EU) 2023/1773) or **corporate ESG methodology** (GHG Protocol)? They are different.
- Boundary correct? CBAM defines specific system boundaries per commodity.
- Allocation of emissions to co-products correct? Disputes here can swing numbers materially.

### 4.2 Data quality
- Direct measurement vs. emission factors vs. defaults
- Use of default values for unverified inputs = highest CBAM cost
- Continuous emissions monitoring (CEMS) for SO₂, NOx, CO₂ — best evidence
- Fuel quantities and quality — invoices, mass balance
- Electricity sourcing — separate factor by source (e.g. specific PPA vs. grid average)

### 4.3 Verification
- CBAM requires verification by EU-accredited verifier
- Verifier list at https://ec.europa.eu/clima/eu-action/european-green-deal/cbam_en
- Non-EU verifiers: limited availability, must be EU-accredited
- For Russian assets: very limited verifier availability — operational risk

### 4.4 Precursor materials
- Embedded emissions of intermediate inputs (e.g. alumina input to aluminium) carried through
- Each precursor must have its own CBAM-compliant emission data
- Supply chain weakness: if alumina supplier can't provide compliant data, downstream aluminium product must use defaults (punitive)

---

## 5. Strategic carbon intelligence per major Russian asset

**[VERIFY CURRENT BEFORE USE]** Strategic positioning of major Russian metals players on carbon:

- **RUSAL** — Operates the largest hydro-powered aluminium fleet globally (~90% of primary capacity on hydro). Lowest verifiable carbon intensity globally. **But EU market access constrained by sanctions** (see `sanctions_compliance_intel.md`). Carbon advantage flowing through to non-EU markets (China, Türkiye, India) at varying realisations.
- **Norilsk Nickel** — Nickel and PGM production carbon profile complex. Sulphide ore route is structurally lower carbon than laterite (HPAL or pyrometallurgical) but is highly intensive in sulphur capture energy. Серная программа 2.0 has reduced SO₂ emissions dramatically but at energy cost.
- **EuroChem, PhosAgro** — Fertiliser producers; CBAM exposure direct. Russian gas advantage in cost partly offset by carbon cost.
- **Severstal, MMK, NLMK, Mechel** — Integrated steel producers; high CBAM exposure on EU-bound product. Most have lost or restricted EU access; pivoted to other markets.
- **UMMC, KAZ Minerals, Kazakhmys** — Cu producers; not currently in CBAM scope but exposed to scope expansion.

---

## 6. CBAM cost modelling — DD-level approach

### 6.1 Quick-and-dirty (for screening)
- Identify product, jurisdiction of sale, current and projected carbon intensity
- Apply formula from §2 with simple assumptions
- Range estimate by 2030, 2034

### 6.2 Asset-specific (for transaction DD)
- Pull actual emissions data (Scope 1, Scope 2 with sourcing detail)
- Identify precursors and their emission data
- Build CBAM cost time series 2026–2034
- Sensitivity: ETS price (60/80/100/120/150 €/t), grid decarbonisation pathway, precursor data availability
- Compare to peer assets (LME registered, Western-jurisdiction producers)
- Determine: does CBAM cost erode margin to negative under reasonable scenario?

### 6.3 Modelling discipline
- Don't double-count: CBAM cost is paid by **importer**, not producer directly. But economically it flows through pricing. Whether producer or buyer absorbs depends on market structure (price-taker producer absorbs more, price-maker producer can pass through).
- For Russian/CIS assets sold into EU: assume seller absorbs majority of CBAM cost via price discount (markets work, buyers will not pay premium for high-carbon product when alternative exists).
- For low-carbon producers: assume neutral or positive impact — premium for low-carbon may emerge.

---

## 7. Decarbonisation lever — DD assessment

Asset's CO₂ reduction roadmap is now part of DD. Evaluate:

### 7.1 Power sourcing
- Existing PPA or self-generation profile
- Available local low-carbon power (hydro, nuclear, wind, solar, geothermal)
- Tariff implications of switching
- Grid carbon intensity trajectory

### 7.2 Process technology
- For aluminium: inert anode technology (in pilot at Elysis, RUSAL) eliminates direct CO₂ from anode oxidation. 10+ years to commercial deployment. Game-changing if commercial.
- For steel: H2-DRI route — depends on H2 cost and availability
- For copper, nickel: bioleaching as alternative to roast/smelt (limited applicability)
- For alumina: alternative refining processes under pilot (verify current TRL)

### 7.3 Carbon capture / offsets
- CCUS at concentrated CO₂ point sources — alumina calciner, cement plant
- Nature-based offsets: limited recognition by CBAM (currently NOT offsetable)
- DAC + storage: not currently economic for industrial CO₂ price

### 7.4 Product mix shift
- Increasing share of recycled metal (scrap-based) reduces embedded emissions
- For aluminium downstream: 100% scrap-based product has ~5% of primary CO₂ intensity
- Strategic: even primary producers should integrate downstream scrap-based capacity

---

## 8. Beyond CBAM — other carbon regimes to track

### 8.1 UK CBAM
- Announced for 2027 introduction, scope similar to EU
- Verify current status

### 8.2 US — IRA tax credits and CO₂ tariffs
- Inflation Reduction Act tax credits for low-carbon production (Section 45X, 45Y, 45Q)
- Proposed Foreign Pollution Fee Act (status varies — verify)
- Section 232 tariffs may incorporate carbon dimension

### 8.3 Australia
- Safeguard Mechanism: domestic ETS for large emitters, expanding
- CBAM-equivalent discussed; status to verify

### 8.4 Canada
- Federal carbon price ~CAD 80/t in 2026, rising
- Some provincial schemes
- CBAM-equivalent under consultation

### 8.5 Voluntary markets (LME, LBMA, ICSG)
- LME low-carbon aluminium contract
- LBMA responsible sourcing guidance
- ICSG (copper) considering CO₂ disclosure framework
- These move faster than government policy and create commercial differentiation

---

## 9. DD checklist — carbon

### 9.1 Quick screen (1 hour)
- [ ] Product covered by CBAM today? (Y/N, refer §1)
- [ ] EU market share of output? (% of revenue)
- [ ] Production route — power source, fuel, technology
- [ ] Rough carbon intensity estimate (use defaults if no asset data)
- [ ] Rough CBAM cost at 2030 and 2034 (range)

### 9.2 Detailed assessment (8–16 hours)
- [ ] CBAM-compliant emissions data exists? Verified?
- [ ] Verifier identified and engaged?
- [ ] Precursor materials data chain complete?
- [ ] Internal carbon accounting system (boundary, methodology)
- [ ] Decarbonisation roadmap exists? Funded? Realistic technology?
- [ ] Power supply transition plan if relevant
- [ ] CapEx and OpEx of decarbonisation
- [ ] Sensitivity analysis at multiple ETS prices and timing scenarios

### 9.3 Killer questions for management

- "What is your verified Scope 1 and Scope 2 carbon intensity per tonne of CBAM-covered product, using CBAM methodology, for the most recent 12 months?"
- "Who is your CBAM verifier? When was their last on-site verification?"
- "What is your modelled CBAM cost in 2030 under EU ETS at €100/t? What is your sensitivity to ETS at €150/t?"
- "What is your decarbonisation pathway and what does it cost? How does it compare to peer benchmarks?"
- "For your major precursor inputs, do you have CBAM-compliant emissions data from suppliers, and is it verified?"

---

## 10. Red flags

- Asset claims "low carbon" without verified data
- Emissions data based on industry averages rather than measurement
- No CBAM verifier identified despite 2026 obligation start
- Decarbonisation plan is roadmap-only with no CapEx allocation
- Carbon intensity worse than peer benchmarks with no acknowledgement
- Strategy assumes CBAM will be delayed or weakened (political risk hedge)
- Free-allocation forecast embedded in financial model post-2027 (will be wrong)

---

## 11. Primary sources

- **EU CBAM regulation**: Regulation (EU) 2023/956
- **Implementing regulation**: Regulation (EU) 2023/1773
- **DG TAXUD CBAM portal**: https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en
- **CBAM transitional registry**: cbam.ec.europa.eu
- **EU ETS price data**: https://ember-climate.org/data/data-tools/carbon-price-viewer/
- **EU verifier list**: search "CBAM accredited verifier"
- **ICAP (carbon market tracker)**: https://icapcarbonaction.com
- **CDP industry reports**: https://www.cdp.net (corporate emissions disclosure)

---

## TODO_ANTON consolidated

1. Specific RUSAL Scope 1+2 numbers per smelter (Krasnoyarsk, Bratsk, Sayanogorsk) — layered citation
2. Inert anode technology status — RUSAL and Elysis updates
3. Nornickel Серная программа 2.0 carbon-vs-SO₂ tradeoff specifics
4. Any actual CBAM verifier engagement experience Anton has seen in CIS assets
5. Pricing observations on low-carbon vs high-carbon aluminium since LME contract launch
