# DD — Aluminium Smelter (Primary)

**Package fit:** DD Standard ($22–30K, 80–120h) or DD Deep ($55–85K, 180–240h)
**Asset type:** primary aluminium smelter (Hall–Héroult process)
**Scope:** technical, operational, CapEx, market, ESG, sanctions/compliance overlay
**Author signature domain:** RUSAL 10y, 7 patents, $350M+ CapEx portfolio across aluminium value chain

---

## `_meta`

```yaml
asset_name: ""
operator: ""
ubo_chain: ""
location: ""                       # country / region / town
commissioning_year: 0
last_major_capex_year: 0
nameplate_capacity_ktpa: 0
actual_production_last_3y_ktpa: []
product_mix: []                    # billet | slab | sow | wire-rod | T-bar | alloy
cell_technology: ""                # prebake / Söderberg / specific generation (RA-300/400/550, AP-30/40/50/60, EGA DX/DX+, etc.)
current_density_A_per_cm2: 0
number_of_potlines: 0
pots_per_potline: 0
power_source: ""                   # hydro / coal / gas / nuclear / grid mix
power_contract_structure: ""       # PPA / regulated / merchant / wholesale
alumina_source: ""                 # captive / contracted / spot mix
anode_source: ""                   # captive / contracted
client: ""
deal_type: ""                      # M&A buy-side | M&A sell-side | financing | IPO advisory
dd_package: ""                     # standard | deep
date_start: ""
date_due: ""
```

---

## 1. Executive Summary

*Written last. 1–2 pages.*

- **Asset one-liner.** Type, location, capacity, technology generation.
- **Strategic context.** Why this asset is on the market / under review.
- **Top-line verdict.** Go / Caution / Walk away — paragraph form, not just label.
- **3 critical risks** (the ones that would change the verdict).
- **3 upside drivers** (the ones that could materially improve the case).
- **Killer questions for management session.** 5–7, each linked to a specific DD finding.
- **Out-of-scope items.** What this DD does not answer and should be done before signing.

---

## 2. Author Credentials and Compliance

### 2.1 Author background
*Auto-filled from KG `author_credentials` tag. Default core block + 2–3 sector-specific cases.*

### 2.2 Methodology and sources
- Public sources only (annual reports, regulator filings, sector journals, satellite imagery where applicable)
- No use of prior-employer confidential information
- Anonymisation of prior advisory clients

### 2.3 Compliance statement
*Pull from `compliance_overlay.md` per buyer jurisdiction.*

---

## 3. Asset Identity and Ownership

### 3.1 Legal identity
- Operating entity name and corporate structure
- Ultimate Beneficial Owner chain to natural persons
- Cross-shareholdings, golden shares, board appointment rights

### 3.2 Sanctions and compliance overlay
- OFAC SDN check on entity, UBO, named officers
- EU consolidated list check
- UK OFSI check
- Sectoral sanctions exposure (US 14024, EU Regulation 833/2014 metals provisions)
- Secondary sanctions exposure for non-Russian buyers

### 3.3 Asset history
- Commissioning year and technology generation
- Major modernisation events with dates and scope
- Ownership transitions (M&A, restructuring, bankruptcy, nationalisation)
- Significant litigation, regulatory action, public disputes
- Production history last 10 years (recovery from any disruptions)

### 3.4 Local context
- Town/region socio-economic dependence on asset
- Workforce as % of local population
- Tax revenue contribution to regional budget
- Political importance to federal/regional government

---

## 4. Process Technology Assessment

### 4.1 Cell technology generation
*Cell tech is the single most important technology variable. Drives current efficiency, energy intensity, environmental footprint, and brownfield modernisation economics.*

- Cell technology line (RA-300, RA-400, RA-550 for Russian; AP-30, AP-40, AP-50, AP-60 for Pechiney lineage; EGA DX, DX+ for EGA; Hall, Søderberg legacy for some Russian/Indian assets)
- Year of cell technology selection and any retrofits since
- Comparison to best-available-technology (BAT) for primary aluminium today
- Modernisation roadmap visible from public filings

### 4.2 Cell operating parameters
- **Current density** (A/cm²): historical and current. Higher = more aluminium per cell-day, more energy stress on cell components.
  - Legacy Söderberg: 0.6–0.8
  - Modern prebake: 0.85–1.0
  - High-amperage prebake (post-2010): 1.0–1.3
  - Frontier (EGA DX+, latest Chinese): 1.3+
- **Cell amperage** (kA): total cell current. Drives capacity per cell.
- **Anode–cathode distance (ACD)**: target 4.0–5.0 cm. Lower ACD = lower voltage drop = energy saving but instability risk.
- **Bath chemistry**: AlF₃ excess, cryolite ratio (NaF/AlF₃ molar). Drives bath temperature, alumina solubility, current efficiency.
- **Cell voltage**: typical 4.0–4.5 V per cell modern; 4.5–4.8 V legacy.

### 4.3 Key performance indicators
*The four numbers that define an aluminium smelter's competitive position.*

| KPI | Top-tier benchmark | Investigate below |
|-----|--------------------|-----------------|
| Current efficiency (%) | 94–96 | < 92 |
| Specific energy consumption (kWh/kg Al) | 13.0–13.5 | > 14.0 |
| Anode net carbon consumption (kg C/kg Al) | 0.40–0.42 | > 0.45 |
| Anode change cycle (days) | 24–30 | < 22 (driven by bath chemistry issues) |

**Trend matters more than absolute level.** Improving trend on a sub-benchmark asset = good operations team. Declining trend on benchmark asset = problem accumulating.

### 4.4 Anode supply and quality
- **Anode source.** Captive baked anode plant on-site (typical for major smelters) or external supply (small smelters and some Chinese).
- **Anode quality drivers.** Petroleum coke quality (S, V, Ni content), pitch binder grade, baking temperature profile.
- **Critical impurity thresholds.** Sulphur in anode → SO₂ in pot gas; Vanadium → reduces current efficiency; Sodium contamination → cell instability.
- **Anode plant CapEx exposure.** Anode butts handling, baking furnace refractories age, off-gas treatment compliance.
- **Petroleum coke supply.** Source diversity, contract structure, exposure to refining-margin cycles.

### 4.5 Alumina (Smelter-Grade Alumina, SGA) supply and quality
- **Source structure.** Captive refinery (e.g., RUSAL Achinsk, EGA Al Taweelah) vs contracted vs spot.
- **SGA specification.** Na₂O, SiO₂, Fe₂O₃, LOI tolerances. Off-spec alumina increases impurity flux through Hall–Héroult cell.
- **Granulometry.** Particle size distribution affects dust generation, dry scrubber efficiency, point-feeder behaviour.
- **Logistics dependence.** Distance from refinery, transport mode, exposure to weather/political disruption.

### 4.6 Power supply (the deal-defining variable)

*On a primary aluminium asset, power supply structure is the most important single factor. Anton's principle: read the power agreement before the metallurgy.*

#### 4.6.1 Power source
- Hydro (lowest cost, lowest carbon — Norwegian, Russian Siberian, Canadian, Brazilian)
- Coal (highest carbon, often lowest stated cost but CBAM-exposed — Indian, Chinese, Australian, Kazakh)
- Gas (mid-carbon, exposed to gas market cycles — Middle Eastern, some US)
- Nuclear (low-carbon, rigid baseload — French historical)
- Mixed grid (heterogeneous — Russian European, Turkish, Indonesian)

#### 4.6.2 Contractual structure
- Long-term PPA vs regulated tariff vs merchant exposure
- Take-or-pay obligations
- Tariff escalation mechanism (CPI-linked, fuel-linked, regulated reset, none)
- Force majeure terms
- Counterparty risk on PPA provider

#### 4.6.3 Sensitivity analysis
- $/MWh delta → $/t Al cost impact at asset specific energy consumption
- Position on global aluminium cash-cost curve at base case and stress cases
- Tariff stress that moves asset above/below break-even

#### 4.6.4 Power supply security
- Single-line dependency vs redundancy
- Backup generation capacity (typically only emergency, not full operation)
- Historical outage events and recovery time

### 4.7 Casthouse and product mix
*Cross-reference to `dd_aluminium_downstream.md` for casthouse-specific deep dives.*

- Casting technology (VDC slab, VDC billet, sow caster, wire rod line — Properzi/Southwire SCR)
- Product mix (commodity ingot vs value-added VAP: slab for rolling, billet for extrusion, wire rod, foundry alloy)
- VAP premium realisation and customer concentration
- Casthouse CapEx vintage and capacity vs upstream production

### 4.8 Bath and pot maintenance regime
- Anode change scheduling and crew structure
- Tap-out frequency and quantity
- Bath chemistry adjustment protocol
- Pot lining age distribution (the relining backlog driver)
- Critical spares (anode rods, cathode blocks, refractory) inventory

### 4.9 Process control and digitalisation
- Pot control system generation (EPCM, Alcoa, Aluterv, Rio CTI, ABB, EGA, Russian custom)
- Sensors per cell (voltage, resistance, alumina feed rate, bath temperature, anode position)
- Data infrastructure (historian, MES integration with casthouse and anode plant)
- Predictive analytics maturity (AI-assisted anode change scheduling, anomaly detection)
- Cybersecurity exposure (segmentation between IT and OT)

---

## 5. Operational Performance

### 5.1 Production history
- Last 5 years actual production vs nameplate
- Reasons for utilisation gaps (turnarounds, market, power, labour)
- Production stability indicators (monthly variance, recovery from disruptions)

### 5.2 Pot life and relining backlog
- **Pot life distribution.** Healthy distribution is roughly uniform across 0–2500 days; concentrated old population = imminent CapEx wave.
- **Relining capacity.** In-house cathode lining capacity vs annual relining need.
- **Relining CapEx exposure.** $200,000–$600,000 per pot depending on size/technology. A 300-pot line with average pot age 1800/2500 = $30–90M CapEx need within 5 years.
- **Historical pot life trend.** Improving = good cell ops; declining = bath chemistry or current density issue.

### 5.3 Turnaround and shutdown history
- Planned turnaround frequency and duration (norm: 22–30 days per potline)
- Unplanned shutdown events with cause and recovery time (norm-breaking: anything > 60 days)
- Restart from cold metal — has it been done at this asset, with what outcome
- Restart from frozen metal — exceptional event, multi-month recovery if happens

### 5.4 HSE record
- Lost-Time Injury frequency rate (LTIFR) last 5 years vs sector benchmark (sector top tier < 0.5 per 200,000 hours; concerning > 2.0)
- Total Recordable Injury Frequency Rate (TRIFR)
- Fatalities last 10 years — even one is a deep-dive trigger
- Process safety incidents (molten metal, gas, electrical)
- Tap-out incidents, anode effects, cell explosions
- Occupational health: fluoride exposure, noise, heat stress, dust

### 5.5 Workforce
- Headcount by function (potroom, casthouse, anode plant, maintenance, services)
- Productivity (t Al per employee per year) vs sector benchmark
- Union exposure and collective agreement structure
- Key technical leadership stability (years in role for plant manager, potroom manager, casthouse manager, technology manager)
- Skills pipeline (apprenticeships, technical schools, retention)

### 5.6 Maintenance
- Maintenance philosophy (preventive vs predictive vs reactive)
- Critical equipment age (rectifiers, cranes, anode stub setters, alumina handling)
- Maintenance spend as % of revenue (sector typical 3–6%; sustained < 3% = deferred maintenance risk)
- OEM support for vintage equipment (Pechiney, Reynolds, Soviet-era Russian)

---

## 6. Environmental, Social, Governance

### 6.1 Carbon footprint
- **Scope 1** (direct: anode CO₂, pot gases): typical 1.5–2.0 t CO₂eq / t Al
- **Scope 2** (electricity): the swing variable, 0–18 t CO₂eq / t Al depending on power source
- **PFC emissions** (CF₄, C₂F₆): GWP × 7400 and × 12200 respectively. Anode effect frequency drives PFC.
- **Total carbon intensity** vs sector segments:
  - Hydro-powered: 2–5 t CO₂eq / t Al
  - Gas: 8–12
  - Modern coal with capture: 10–14
  - Indian/Chinese coal: 14–20+

### 6.2 CBAM exposure (EU customers)
- Carbon Border Adjustment Mechanism phased in 2026–2034
- Embedded emissions definition under CBAM
- Likely tariff impact on $/t for asset's specific intensity
- Mitigation: low-carbon power contracting, anode technology (inert anodes still pre-commercial)

### 6.3 Local air emissions
- Dry scrubber efficiency for fluoride capture (sector standard > 99%, modern > 99.5%)
- HF, total fluoride, dust emission limits and compliance margin
- SO₂ emissions (driven by anode S content and capture)
- Stack monitoring continuity

### 6.4 Water
- Once-through cooling vs closed-circuit
- Wastewater volume and quality
- Discharge permit conditions
- Stormwater management (potroom basement, anode plant)

### 6.5 Solid waste
- **Spent Potlining (SPL).** Hazardous waste (cyanide, fluoride). Storage volumes accumulated, treatment route. Major closure cost driver.
- **Carbon dust.** Anode handling, baking furnace.
- **Filter dust.** From dry scrubber, recycled to alumina.
- **Refractory waste.** From cell relining.

### 6.6 Social licence
- Community grievance history (air quality complaints, health concerns)
- Indigenous land rights (relevant for certain Russian/Canadian assets)
- Local NGO presence
- Media coverage tone

### 6.7 Closure liability
- Disclosed closure provisioning vs estimated true cost
- Closure plan filed with regulator
- Reclamation obligations (especially captive refinery / mine if vertically integrated)
- Long-tail SPL liability

---

## 7. CapEx Assessment

### 7.1 Stated CapEx programme
- Disclosed near-term CapEx (sustaining + growth)
- 5-year CapEx outlook from filings or guidance
- Allocation by segment (potroom, anode plant, casthouse, environmental, IT/OT)

### 7.2 FEL maturity of disclosed CapEx
- For each disclosed major item: where is it on the FEL 1–3 scale?
- **Red flag:** stated CapEx for FEL 2-stage scope at FEL 3 accuracy claim. Common in management presentations.
- Estimate accuracy: ±50% (FEL 1), ±25–30% (FEL 2), ±10–15% (FEL 3)

### 7.3 Benchmark vs sector
- $/t for greenfield primary: $4,500–6,500/t annual capacity (power-dependent)
- $/t for brownfield expansion: $2,500–4,000/t
- $/pot for relining: $200,000–600,000
- $/MW for power infrastructure on captive: $1.5–2.5M/MW for hydro greenfield, less for grid connection
- Anode plant: $1,500–2,500/t green anode annual capacity

### 7.4 Hidden CapEx
*This is where principal-grade DD differentiates from junior work. Stated CapEx is the surface; hidden CapEx is the deal-shaping number.*

- **Relining backlog** (see §5.2)
- **Spent potlining treatment infrastructure** (legacy SPL accumulated → mandatory treatment regulation closing the loophole)
- **Environmental compliance gap** (current vs tightening limits, especially fluoride and PFC)
- **Power infrastructure** (transformer age, busbar architecture refresh)
- **Casthouse capacity mismatch** (upstream nameplate vs downstream throughput)
- **Anode plant capacity vs potline expansion** (the common bottleneck)
- **Rectifier transformer refresh** ($10–25M per potline)
- **Critical spares strategic stock** (anode rods, cathode blocks if no captive supply)
- **OT cybersecurity** (segmented network, SCADA hardening)

### 7.5 Sustaining CapEx norm
- Sector typical $80–150/t annual production for sustaining
- Implied annual sustaining from filings vs benchmark
- Multi-year deferral indicators

---

## 8. OpEx and Cash Cost Position

### 8.1 Cash cost decomposition (C1)
*Aluminium smelter C1 typical structure:*

| Component | % of C1 | Sensitivity |
|-----------|---------|-----|
| Power | 30–50% | Highest. Each 10% power tariff move ≈ 5% C1 move |
| Alumina | 25–35% | LME alumina-linked typically; spot exposure asset-specific |
| Anode (carbon) | 8–12% | Pet coke market cycles |
| Labour | 8–15% | Geography-driven |
| Other materials and services | 5–10% | Inflation pass-through varies |
| Maintenance | 3–6% | Deferred-maintenance flag |

### 8.2 Cost-curve position
- C1 cost-curve position last 3 years (quartile)
- Curve movement trend
- Sensitivity to LME alumina, LME aluminium, power tariff, FX
- AISC (all-in sustaining cost) including sustaining CapEx

### 8.3 Working capital
- Inventory days (alumina, anodes, ingot)
- Receivables and payables structure
- Working capital sensitivity to LME swings

---

## 9. Commercial and Market Position

### 9.1 Product mix and premium realisation
- Commodity ingot share vs VAP (value-added products)
- VAP premium realisation $/t over LME by product
- VAP customer concentration
- Long-term contracts vs spot mix

### 9.2 Customer geography
- Domestic vs export split
- Export route dependence (relevant for Russian and Iranian assets)
- Customer credit quality concentration
- Customers exposed to CBAM (which would demand carbon disclosure)

### 9.3 Sanctions and trade restrictions
- Direct sanctions on producer (e.g., RUSAL 2018 OFAC, later lifted)
- Sectoral metals sanctions (US ban on Russian aluminium, UK/EU LME restrictions)
- Trade case exposure (anti-dumping, countervailing duties in EU/US/India/Brazil)
- Diversion route viability (re-routing through third countries — UAE, Turkey)

### 9.4 Logistics
- Primary export modes (rail-to-port, river, road)
- Port concentration and alternatives
- Logistics cost as % of delivered price by route
- Insurance availability for cargo (sanctioned-asset constraint)

---

## 10. Risk Register

*Use `risk_register_prefill.json` filtered for `aluminium_smelter`. Anton scores L×I and writes verdict column.*

Aluminium-specific risk additions beyond generic prefill:

| ID | Risk | Trigger |
|----|------|---------|
| AS1 | Anode quality drift driving current efficiency loss | Anode S, V, dust content variability |
| AS2 | Potline age concentration creating CapEx wave | Pot age distribution skewed > 1800d |
| AS3 | Power contract expiry within DD horizon | Contract end date, renewal terms |
| AS4 | CBAM exposure for EU exporters | Carbon intensity > 8 t/t Al for EU export book |
| AS5 | SPL legacy liability crystallising | Regulator tightening, accumulated stockpile |
| AS6 | PFC emissions disclosure pressure | Aluminium Stewardship Initiative, customer audits |
| AS7 | Anode butt processing capacity bottleneck | Throughput vs butt generation balance |
| AS8 | Sanctions on logistics insurance | Western P&I clubs exposure |

---

## 11. Recommendations

### 11.1 Go / Caution / Walk-away verdict
*Blunt paragraph, not just a label.*

### 11.2 Deal-breakers
What single findings would force walk-away.

### 11.3 Renegotiation levers
Per finding, what client should push for in price/structure.

### 11.4 Killer questions for management session
5–7 questions. Each anchored to a specific DD finding. Format: "Given [DD finding], please explain [specific number / decision / mitigation]."

Sector-specific killer-question library available in `killer_questions.json`. Default selection for primary smelter:

1. **Power contract:** "Walk us through the tariff escalation mechanism in the current PPA and the renewal terms or merchant exposure post-expiry."
2. **Relining backlog:** "What is the pot age distribution by potline, and what is the relining CapEx provisioned for the next 5 years vs the maintenance budget?"
3. **CBAM:** "What is the asset's Scope 1+2 carbon intensity per tonne, and what is the EU export book share?"
4. **SPL:** "How much accumulated spent potlining is stockpiled, and what is the planned treatment route and CapEx?"
5. **Anode supply:** "Petroleum coke source diversity and S/V/Ni specification compliance margin over the last 24 months?"
6. **HSE:** "Process safety incident history last 5 years with root-cause categorisation?"
7. **VAP customer concentration:** "Top 3 VAP customer share of casthouse premium revenue and contract structure?"

### 11.5 Out-of-scope follow-ups
- Site visit (highly recommended for any DD Deep): pot age verification, casthouse equipment condition, anode plant walkthrough, SPL stockpile measurement.
- Specialist DDs to commission: legal (PPA review), environmental (compliance gap analysis), labour (collective agreement and pension liability).
- Modelling: cost-curve sensitivity model, FX/LME/power tariff scenarios.

---

## 12. Appendices

- **A. Sources consulted** — auto-generated from research folder
- **B. CapEx benchmark methodology** — reference to `benchmarks/aluminium_smelter_capex.json`
- **C. Risk scoring methodology** — L×I 1–5 scale with definitions
- **D. Author's prior cases** — auto-pulled from KG by tag match
- **E. Glossary** — reference to `/mnt/project/glossary.md`
- **F. Compliance disclaimer** — pulled from `compliance_overlay.md` per jurisdiction

---

## Retainer Conversion Hook

*Last page. Auto-generated. Anton edits before sending.*

> **Beyond this DD**
>
> Items surfaced as out-of-scope follow-ups (§11.5), plus ongoing shifts in the aluminium market (CBAM phasing, sanctions evolution, anode market dynamics) often warrant continued advisory presence post-close.
>
> Two formats are available:
>
> - **Strategic retainer** — monthly 1h call + 8–10h ad-hoc + email/Signal access. $8–10K/mo. PE or family office with CIS aluminium exposure.
> - **Embedded retainer** — weekly call + 20–25h delivery + monthly written memo. $18–25K/mo. Active M&A or post-close 100-day integration.
>
> Happy to discuss after you have absorbed this DD.
