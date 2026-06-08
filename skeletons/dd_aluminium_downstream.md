# DD Skeleton — Aluminium Downstream Asset

**Применимость:** casthouse (DC casting, continuous casting), rolling mill (hot and cold), extrusion press, foil mill, recycling (secondary aluminium), alloy production. Standalone or integrated downstream of smelter.

**Anton signature domain:** RUSAL casthouse operations, 7 patents on aluminium alloys (composition, processing), 40 ktpa casting expansion (18% under benchmark capex). Deep knowledge of alloy chemistry, grain refining, melt treatment, casting defects, recycling integration.

**Авторские сильные стороны:**
- Aluminium alloy chemistry (1xxx, 3xxx, 5xxx, 6xxx, 7xxx series + casting alloys)
- DC casting process and defects (hot tearing, surface segregation, butt curl)
- Grain refiner and modifier selection (Ti-B, Sr, P)
- Melt cleanliness (degassing, filtration)
- Scrap integration (UBC, mixed scrap, swarf)
- Alloy patent IP defense

**Critical scope distinction:** this skeleton is downstream of smelter (or standalone billet/slab/extrusion). For smelter DD see `dd_aluminium_smelter.md`. For integrated complex DD use both.

---

## §0. Executive Summary

Структура:
1. Asset overview (location, capacity by product, customer base, integration with smelter or scrap-based)
2. Top 3 deal-defining findings
3. Recommendation
4. Conditional levers
5. Key management session findings

**Anchoring rule:** в первом абзаце — capacity by product line (ktpa billet/slab/sheet/extrusion) AND **conversion margin $/t** (revenue minus aluminium metal input cost). Without conversion margin, downstream value is invisible behind LME volatility.

---

## §1. Ownership, Sanctions, Counterparty Risk

### 1.1 UBO and sanctions
- Standard cascade — see `compliance_overlay.md`
- For Russian aluminium downstream: indirect Rusal exposure cascading through ownership
- Western buyer exposure: LME deliverable brand status, US Section 232 tariffs, EU CBAM exposure
- China imports: Section 301 considerations for US-bound product

### 1.2 Customer concentration
- Top 10 customers % revenue
- OEM qualification status (automotive, aerospace especially critical)
- Long-term contracts vs spot
- Pricing structure: LME + premium + conversion + alloy surcharge

### 1.3 Aluminium brand status
- LME deliverable brand (P1020, etc.)
- LBMA-equivalent? No, LME alone.
- Russian P1020 status: technically still LME deliverable but with discount post-2024 (US ban + LME warehouse stop on new Russian)
- For downstream products: brand of input metal matters for customer compliance

---

## §2. Resource Position (Metal Input)

### 2.1 Integrated source (if downstream of own smelter)
- Smelter capacity vs downstream demand
- Internal transfer pricing methodology
- Logistics cost (molten transfer is huge savings: $50-150/t vs solid + remelt)

### 2.2 External purchased metal
- Purchase contracts: term, volume, pricing formula
- Sources: domestic primary, imports, scrap
- Inventory levels (working capital)
- Hedging policy

### 2.3 Scrap inputs
- UBC (used beverage cans) supply chain
- Mixed scrap sources (industrial, automotive end-of-life)
- Swarf and machining returns
- Scrap pricing relationship to LME (typically 75-95% LME for clean grades)
- Quality variability

---

## §3. Casthouse Operations

### 3.1 Furnace technology

**Melting furnace types:**
- **Reverberatory (gas-fired):** most common for remelt. Capacity 30-100 t/heat typical.
- **Induction:** smaller, more flexible, no fuel.
- **Sidewell furnace:** for high scrap with shredded material.
- **Tilting rotary:** for dross processing or contaminated scrap.

**Holding furnaces (mixers):**
- Hold cleaned and alloyed metal at temperature for casting
- Capacity 20-80 t typical

### 3.2 Key casthouse KPIs

| Parameter | Industry range | Red flag |
|-----------|----------------|----------|
| Metal yield (cast / input) | 96-99% | <95%: dross losses or process issues |
| Dross generation | 1-4% | >5%: oxidation, poor charging practice |
| Melt energy consumption (gas) | 150-300 kWh/t (gas equivalent) | >350: poor refractory or burner |
| Reverberatory throughput | t/hour vs design | -10%+: bottleneck |
| Inclusion level (PoDFA, LiMCA) | <1 K/kg metal cleanliness | High: filter inadequate or upstream contamination |
| Hydrogen content | 0.10-0.20 ml/100g | >0.25: degassing inadequate |

### 3.3 Melt treatment

**Degassing:**
- SNIF (Spinning Nozzle Inert Flotation) — most common, chlorine-argon or just argon
- Rotary degasser (lance-mounted impeller)
- Performance: H₂ reduction 50-80%
- Cl₂ usage: environmental control, sometimes replaced with argon-only

**Filtration:**
- Ceramic foam filter (CFF) — standard
- Bed filter (rigid media) — for premium products (foil, can stock)
- Filter change frequency
- Bypass control

**Grain refining:**
- TiB₂ master alloy (3/1, 5/1 Ti:B) rod
- Addition rate kg/t metal
- Effectiveness measured by macroetch grain size or thermal analysis

**Modifier (for Al-Si casting alloys):**
- Sr (most common)
- Na (older)
- Sb (specific)

[Anton domain — patent landscape on grain refining and modifying. 7 patents relate to alloy composition and processing. Critical IP review for downstream DD where IP transfers.]

### 3.4 DC casting (Direct Chill)

**Process types:**
- **Vertical DC** — most common, slab and billet
- **Horizontal DC** — billet, some specialty
- **Hot-top casting** — premium quality
- **EMC (Electro-Magnetic Casting)** — billet, surface quality focus

**Key parameters:**
| Parameter | Description | Issues |
|-----------|-------------|--------|
| Casting speed | mm/min | Higher = more risk hot tearing |
| Cooling water rate | l/m·s | Affects shell, structure |
| Mould design | hot-top vs open-top vs Ag/Wagstaff | Surface quality, defect rate |
| Lubricant | oil/graphite/proprietary | Surface, butt curl |
| Pit size | length of slab/billet cast | Productivity, scrap rate |

**Casthouse defects (Anton expert domain):**
1. **Hot tearing (cracking)** — usually casting speed too high or alloy susceptibility (high Cu)
2. **Surface segregation (beta fir tree)** — composition gradient at surface
3. **Butt curl** — bottom of billet/slab deforms during start
4. **Inverse segregation** — solute concentration at surface (e.g., Cu, Mg)
5. **Cold cracks** — post-casting, residual stress
6. **Inclusions** — oxides, refractory, exogenous
7. **Porosity** — H₂, shrinkage

### 3.5 Continuous casting

**Twin-roll caster (TRC):**
- For foil stock, packaging sheet
- Capacity smaller than DC + hot mill
- Microstructure differs from DC (cell structure, surface)
- Hunter, Lauener, Fata Hunter, Pechiney-type equipment

**Belt caster (Hazelett):**
- For specific alloys
- Continuous strip

**Properzi:**
- Wire rod
- Continuous rod casting

### 3.6 Casting alloy specifics (foundry alloys)

If asset produces secondary aluminium casting alloys (e.g., A356, ADC12, AlSi9Cu3):
- Furnace mix (primary + scrap)
- Refining and degassing
- Pig casting or ingot casting
- Chemistry control (especially Fe, Cu, Zn for tightly-specified alloys)
- Trace element control (V, Cr for high-end automotive)

### 3.7 Alloy series produced
- **1xxx (pure):** food, electrical
- **2xxx (Al-Cu):** aerospace, premium aerospace customers
- **3xxx (Al-Mn):** can body, container
- **4xxx (Al-Si):** welding wire, brazing
- **5xxx (Al-Mg):** automotive body sheet, marine, structural
- **6xxx (Al-Mg-Si):** extrusion (commodity to high-end), automotive body sheet
- **7xxx (Al-Zn-Mg(-Cu)):** aerospace, defense (controlled exports)

**Aerospace customer qualification — high barrier:**
- Boeing, Airbus, Embraer approved supplier
- Nadcap accreditation for processing
- AMS specifications
- Lot acceptance test discipline

---

## §4. Rolling Mill

### 4.1 Hot rolling

**Configuration:**
- Reversing hot mill (most common for ingot start)
- Tandem hot mill (continuous, higher capacity)
- Throughput: 100k - 1M+ tpa
- Slab thickness: 400-600mm typical
- Exit gauge: 3-6mm hot band

**KPIs:**
- Mill yield (% input to hot band)
- Throughput vs design
- Rolling speed
- Reduction per pass
- Slab heating efficiency (kWh/t)

### 4.2 Cold rolling

**Configuration:**
- Single-stand vs tandem
- Foil mill vs sheet mill
- Reversing or unidirectional
- Maximum width and minimum gauge

**KPIs:**
- Mill yield
- Pass schedule efficiency
- Surface quality (Ra, defects)
- Profile and flatness control (AGC, hydraulic crowning)

### 4.3 Finishing operations

- **Annealing:** batch or continuous, atmosphere control
- **Tension levelling, stretching:** flatness
- **Slitting:** to customer width
- **Cut-to-length:** sheet customers
- **Coating:** pre-paint, anodise prep, lacquer
- **Cladding:** rare, e.g., brazing sheet

### 4.4 Product mix

**Common product lines:**
- Can stock (body, lid, tab) — high volume, specific 3xxx/5xxx
- Automotive body sheet (ABS) — 5xxx and 6xxx, growing
- Heat exchanger fin stock — 1xxx/3xxx/4xxx
- Building & construction — various
- Foil — 1xxx/8xxx
- Plate — aerospace, defense

### 4.5 Quality systems
- ISO 9001
- IATF 16949 (automotive)
- AS9100 (aerospace)
- Lot acceptance test discipline
- Statistical process control

---

## §5. Extrusion

### 5.1 Press technology

**Press types:**
- **Direct extrusion:** standard, billet pushed through die
- **Indirect extrusion:** die moves into billet
- **Hydrostatic:** rare
- **Forging-extrusion hybrid:** specialty

**Press tonnage range:**
- 1,800-25,000 ton common
- Larger for big sections (7,000+ ton needed for large auto profiles)

**Key equipment:**
- Billet heater (gas-fired oven or induction)
- Press
- Quench (water, fan, mist)
- Stretcher (correction)
- Saw
- Age oven
- Surface finishing line (anodise, paint, etc.)

### 5.2 Extrusion KPIs

| Parameter | Industry range | Red flag |
|-----------|----------------|----------|
| Recovery (output / billet weight) | 85-95% | <85%: high scrap, dies issues |
| Press productivity | t/hour vs design | -15%: bottleneck |
| Die life | extrusions/die | Falling: die material or process issue |
| Surface quality reject % | 2-8% | >10%: cosmetic or die issue |
| Mechanical property compliance | >98% | <95%: aging or alloy issue |

### 5.3 Alloy split typical

- 6063 (architectural, building) — commodity
- 6061, 6082 (structural) — semi-commodity
- 6005, 6005A (transport) — specialty
- 6463, 6863 (anodise quality) — specialty
- 7xxx (high-end aerospace, defense) — very specialty
- 2xxx (aerospace) — rare in extrusion

### 5.4 Surface finishing

**Anodising:**
- Architectural anodise (Class I 25 μm, Class II 18 μm)
- Hard anodise
- Color (dye, electrolytic color, integral color)

**Painting:**
- Powder coat
- Liquid paint
- Qualified to AAMA standards (architecture)

---

## §6. Secondary Aluminium (Recycling)

### 6.1 Scrap supply chain
- UBC (used beverage cans) — most clean
- Old scrap (end-of-life consumer goods, automotive, demolition)
- New scrap (industrial process scrap)
- Twitch (shredded mixed metal)
- Mill returns (own swarf, runaround)

### 6.2 Pre-processing
- Shredding
- Sorting (magnetic, eddy current, sensor-based — LIBS, XRF, color)
- De-coating (paint/lacquer removal — pyrolysis or chemical)
- Sizing for furnace

### 6.3 Melting technologies for scrap
- Reverberatory (most common)
- Sidewell furnace
- Tilting rotary (for low-grade, dross processing)
- Salt furnace (rotary salt) — for dross, drosses

### 6.4 Salt cake processing
- Hazardous waste (NaCl, KCl, oxides, residual Al)
- Some operations recycle salt — capital intensive
- Disposal regulation increasing stringent (EU, US)

### 6.5 Recycling KPIs

| Parameter | Industry range | Red flag |
|-----------|----------------|----------|
| Metal recovery from scrap | 80-95% | <80%: oxidation, salt loss |
| Scrap mix flexibility | High = competitive | Single-source: vulnerability |
| Carbon intensity | <0.5 tCO₂/t vs 12-16 for primary | Major selling point post-CBAM |
| Energy intensity | 5-8% of primary | Major competitive advantage |

### 6.6 Carbon credit potential
- Verified scope 1/2/3 reduction vs primary
- Tradeable carbon credits (varies by jurisdiction)
- Customer demand for low-carbon aluminium (EVs especially)

---

## §7. ESG / HSE

### 7.1 Air emissions
- VOC from coatings
- NOx, SOx from furnaces
- HF from electrolytic processing (if integrated with smelter)
- Particulates

### 7.2 Water
- Coolant water (slabs, billets DC casting)
- Process water (anodising, painting)
- Heavy metals discharge (Pb, Cu, Zn from coatings)

### 7.3 Waste
- Salt cake (recycling — hazardous)
- Dross (recyclable typically)
- Filter media spent
- Anodising sludge (Al hydroxide)
- Spent rolling oils

### 7.4 Worker safety
- Molten metal exposure (most critical risk)
- LME standard 1.5-3.5 LTIFR for downstream operations
- Fatalities patterns (explosions due to water contact with molten, dross fires, equipment crush)
- Critical control management for molten metal handling

### 7.5 Carbon footprint
- Scope 1: gas combustion in furnaces, coating ovens
- Scope 2: electricity (rolling mills high-load)
- Scope 3: primary aluminium input (dominant for non-recycling operations — 80%+ of footprint)
- CBAM exposure for EU customers — primary intensity matters

---

## §8. Power, Water, Infrastructure

### 8.1 Power
- Downstream less power-intensive than smelter
- Major loads: rolling mill drives, induction heating, motors
- Typical 100-500 kWh/t product depending on process

### 8.2 Water
- Cooling water (closed loop typically)
- Process water (anodising, painting, scrubbing)

### 8.3 Logistics
- Inbound: aluminium ingots/slabs/billets (heavy)
- Outbound: finished products (often value-dense, sensitive to handling)
- Container shipping for export

---

## §9. Operating Costs

### 9.1 Conversion margin economics

**Critical metric for downstream:** revenue minus aluminium metal cost = **conversion margin** $/t.

Conversion margin = sale price - LME - regional premium - alloy surcharge

For different products:
- Commodity extrusion: $400-700/t conversion margin
- Specialty extrusion: $800-1,500/t
- Can body stock: $600-900/t
- Automotive body sheet: $1,200-2,200/t
- Foil: $800-1,400/t
- Aerospace plate: $2,500-5,000/t

### 9.2 Cost structure (conversion costs)

| Cost component | % conversion cost | Notes |
|----------------|---------------------|-------|
| Labor | 25-40% | Highly skilled for premium products |
| Energy (gas+power) | 15-25% | Higher for rolling mill |
| Consumables (rolling oil, dies, refractory) | 5-15% | |
| Maintenance | 10-15% | |
| Conversion overheads | 10-15% | |
| Logistics out | 3-8% | |

### 9.3 Yield and scrap economics

**Yield is critical:**
- Each 1% yield loss = ~$30-80/t metal value lost (recovered as scrap at discount)
- Process yield benchmarks vary by product complexity

**Internal scrap recycling:**
- Runaround (own scrap to own remelt) — essentially "free" if integrated
- Closed-loop scrap value: 95-100% of LME

---

## §10. CapEx, FEL, Sustaining

### 10.1 CapEx benchmarks ($/t annual capacity)

**Casthouse (DC casting):**
- Greenfield casthouse with full melt treatment: $1,200-2,500/t capacity (slab/billet)
- Casthouse expansion (brownfield): $800-1,800/t [Anton's RUSAL 40 ktpa expansion at 18% under benchmark — strong reference]

**Rolling mill:**
- Greenfield hot+cold rolling: $5,000-12,000/t capacity (depending on product mix)
- Foil mill: $8,000-15,000/t
- Auto body sheet line: $12,000-25,000/t (CALP — continuous annealing pre-treatment line)

**Extrusion:**
- Greenfield extrusion plant (medium press, mid-spec): $2,500-5,000/t
- Specialty/aerospace: $5,000-10,000/t

**Recycling:**
- Tilting rotary furnace operation: $400-900/t recycled capacity
- Full UBC recycling line: $1,500-3,000/t

### 10.2 FEL stage gating

Same methodology as smelter and gold (see `methodology/fel_methodology.md`).

### 10.3 Owner team engineering — Anton's RUSAL signature

[Anton signature methodology — full detail in `methodology/owner_team_engineering.md`]

**RUSAL 40 ktpa casthouse expansion case [public layer]:**
- Initial EPC bid 22% above FEL 2 estimate
- Owner team analyzed bid line-by-line
- Decided to break EPC into 6 separate packages, manage integration in-house
- Final capex 18% below industry benchmark — defended at IC

**Key lessons applicable to ANY aluminium downstream DD:**
1. EPC monopoly pricing for specialty equipment (cast tables, holding furnaces) — break it
2. Integration engineering is the value lever, not equipment specs
3. Owner team needs deep tech to negotiate; outsourced FEED + EPC = vendor capture
4. Contingency methodology defended on risk register, not %

---

## §11. Commercial / Marketing

### 11.1 Customer relationships and qualification

**Critical for downstream value:**
- OEM approval pathway typically 2-5 years (especially automotive, aerospace)
- Specifications by customer (proprietary, supplier list managed)
- Long-term contracts (1-5 years) typical for major OEMs

### 11.2 Pricing structure

**Standard:**
- Aluminium price (LME 3-month or settlement)
- + Regional premium (Midwest, Rotterdam Duty Paid, Shanghai, Japan CIF)
- + Conversion charge
- + Alloy surcharge (composition-based)
- + Coating surcharge (if applicable)
- + Logistics

### 11.3 Hedging
- Customers often want fixed metal price
- Producer hedges on LME to lock conversion margin
- Hedging policy and exposure

### 11.4 LME premium dynamics
- Midwest premium history
- Rotterdam DP premium history
- Russian metal: post-2024 LME ban on new Russian, but old stocks deliverable; significant disruption to premium structures

---

## §12. Intellectual Property

### 12.1 Alloy IP

[Critical for Anton-domain DD — 7 patents on aluminium alloys give specific expertise]

**For any aluminium downstream asset, IP includes:**
- Alloy composition patents (composition + processing combinations)
- Process patents (casting parameters, heat treatment cycles)
- Surface treatment patents
- Trade secrets (alloy "fine-tuning" by customer)

**DD review:**
- Patent portfolio: granted, pending, expired
- Patent prosecution status in target markets
- Freedom-to-operate analysis vs major patents (Alcan/RTA, Alcoa, Norsk Hydro, Constellium, Kaiser, Aleris)
- License agreements in/out
- Patent litigation history

### 12.2 Customer-specific developments
- Joint development agreements
- Customer IP ownership clauses
- "Frozen" alloys (composition locked for specific customer)

---

## §13. Workforce

- Skilled trades (millwrights, mechanics, electricians)
- Operators (casters, rollers, extruders) — high skill, long training
- Quality lab (chemistry, mechanical testing)
- Sales/technical sales (customer interface)
- Engineering (process, R&D)

**Anton-domain specific:**
- Russian downstream typically large workforce (legacy), Western typically lean
- Knowledge depth on senior operators irreplaceable
- Succession risk

---

## §14. IT / OT / Automation

- DCS for casthouse and finishing
- AGC (Automatic Gauge Control) for rolling
- Profile and flatness control systems (Honeywell, Stressometer, etc.)
- MES integration for product tracking
- Lab automation (XRF, OES for chemistry)
- Customer EDI/portal integration

---

## §15. Anton-Specific Insights

### 15.1 RUSAL 40 ktpa casthouse expansion case [Signature]

[See §10.3 above and `knowledge/anton_cases.json`]

### 15.2 7 patents on aluminium alloys

[TODO_ANTON: structure under layered citation policy:]
- Patent numbers and titles (public — once verified)
- Co-inventors (public)
- Scope of innovation: composition / processing / surface (high-level public)
- Internal context of how IP supports downstream business (Russian-IP context, possibly internal)

[Public statement template:]
«The author co-authored 7 patents on aluminium alloy composition and processing during work at UC RUSAL. These cover [general areas: e.g., grain refinement, melt treatment, surface treatment for specific alloy systems]. Specific patent details available on request under appropriate framing.»

### 15.3 Casthouse defect troubleshooting framework
[Anton expert knowledge — apply during DD interpretation]

When DD reveals quality issues (high reject rates, customer claims):
1. Surface defects → check melt cleanliness (filter, degasser), mould lubrication, cooling water
2. Internal defects → check melt treatment (degas, grain refine), composition control
3. Mechanical property failures → check homogenization, aging cycle, composition
4. Customer-reported issues → may be application-specific (forming, welding, painting)

[TODO_ANTON: refine framework with specific case examples appropriate for sharing]

### 15.4 Grain refining and modifier selection methodology
[Anton patent area]

Framework:
- Alloy system → standard refiner/modifier
- Casting type → adjusted addition rate
- Product end-use → fine-tuned chemistry
[TODO_ANTON: develop into structured methodology]

### 15.5 Scrap integration into primary-quality production
[Anton domain — bridge between primary aluminium and downstream]

Key considerations:
- Trace element accumulation (Fe, V, Cr, Ti, Mn from scrap)
- Hydrogen and inclusion control with scrap
- Sort and segregation discipline
- Customer acceptance of secondary content
[TODO_ANTON: structure for DD application]

---

## §16. Killer Questions

1. Conversion margin trend by product line last 3 years?
2. OEM qualification status — top 5 customers, audit status?
3. Customer concentration top-5 % revenue?
4. Yield by product line — actual vs design?
5. Hot tearing / surface defect reject rate last 12 months?
6. Melt cleanliness (PoDFA, LiMCA) — actual vs target?
7. Energy intensity (gas + power) per tonne — trend vs benchmark?
8. Patent portfolio — granted, pending, expired in last 5 years?
9. R&D spend % revenue — trend?
10. Sustaining capex vs depreciation — last 5 years?
11. Major maintenance backlog (rolls, dies, refractory, motors)?
12. Major incidents (molten metal, dross fire, equipment) last 5 years?
13. Customer claims and warranty costs trend?
14. Aluminium input contract structure (smelter integration or purchased)?
15. CBAM exposure quantified for EU customers?
16. Russian/sanctioned content question for non-CIS buyers?
17. Aerospace/defense exports — controlled, ITAR/EAR exposure?
18. Recycling content — current % and trajectory?
19. Workforce age distribution and succession plan?
20. Anodising / coating effluent compliance — variance, trend?

---

## §17. Red Flags Checklist

- [ ] Conversion margin declining 3+ consecutive quarters
- [ ] OEM qualification at risk (audit findings, lost approval)
- [ ] Customer concentration top-3 >60%
- [ ] Yield falling without identified cause
- [ ] Reject rate trending up
- [ ] Sustaining capex <60% of depreciation
- [ ] Patent portfolio expiring without renewal pipeline
- [ ] R&D spend declining
- [ ] No FEED accuracy validation on growth projects
- [ ] Aluminium input source single-point dependency
- [ ] Russian content >25% in product for EU/US customers (sanctions risk)
- [ ] Anodising/coating effluent exceedances
- [ ] Energy intensity worsening (efficiency degrading)
- [ ] Major customer contract expiring in <12 months without renewal pipeline
- [ ] Workforce average age >55 without succession plan
- [ ] Dross/salt cake disposal unresolved
- [ ] Molten metal incident pattern (LTIFR, near-miss)
- [ ] Hedging program incomplete (commodity exposure)

---

## §18. Recommendation Logic

### PROCEED:
- Conversion margin stable or growing
- OEM qualification stable, audit clean
- Customer diversification OK
- Yield stable or improving
- Sustaining capex aligned with depreciation
- Strong patent position

### PROCEED WITH CONDITIONS:
- Price adjustment for [conversion margin trend, customer risk]
- Escrow for [OEM re-qualification, environmental compliance, IP defense]
- R&W on [customer contracts, IP ownership, environmental]
- Post-close 100-day [yield improvement, customer diversification, IP review]

### DO NOT PROCEED:
- SDN ownership
- Loss of all major OEM qualifications
- Patent litigation existential threat
- Environmental order with no path to compliance
- Aluminium supply lost without replacement
- LME deliverability lost (Russian context post-2024)

---

## §19. Appendix — Document Request List

**Operations:**
- Last 3 years monthly production by product
- Yield by product line
- Reject rate by product line and customer
- Maintenance records

**Commercial:**
- Customer contracts (top 10, redacted as needed)
- Sales by product, customer, region
- Conversion margin analysis
- Hedging policy and exposure

**Quality:**
- OEM audit reports (last 3 years)
- Customer complaint/claim log
- Quality lab certification (ISO 17025?)
- Lot acceptance test discipline

**IP:**
- Patent portfolio with status
- License agreements (in and out)
- Patent prosecution costs
- Litigation history

**HSE:**
- LTIFR/incidents
- Molten metal incident detail
- Environmental compliance reports
- Anodising/coating discharge

**Capex:**
- Last 5 years capex actuals vs budget
- Sustaining capex plan
- Growth project FEED documents

**Financial:**
- Last 3 years management accounts
- Conversion cost build-up
- Working capital analysis

---

## §20. Author Statement

[Standard block per `compliance_overlay.md`. Specific to aluminium downstream:]

«The author has direct operational experience in aluminium downstream operations including casthouse, rolling, and extrusion at UC RUSAL during 10+ years in technology leadership roles. The author co-authored 7 patents on aluminium alloys during this period. Any references in this DD to UC RUSAL or to specific patent contents are confined to publicly available information and the author's general industry knowledge. No internal UC RUSAL data is disclosed.»

---

## Status

- **Skeleton version:** 1.0 (Phase 1b)
- **Anton review priority on:** §15 (patents, casthouse expertise depth), §10.3 (RUSAL signature case)
- **Live-fire pilot:** TBD
