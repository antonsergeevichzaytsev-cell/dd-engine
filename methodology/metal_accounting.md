# Metal Accounting — DD Methodology

**Author:** Anton Zaytsev
**Purpose:** Framework for assessing metal accounting integrity at concentrators, smelters, refineries. A weak metal accounting system masks losses, enables theft, and inflates reported recoveries. Strong system tightens economics by 1–3% — material on any large asset.
**Cross-reference:** Used in §10 of `dd_nickel_pgm.md`, §7 of `dd_gold_hydromet.md`, §8 of `dd_copper_concentrator.md`, §6 of `dd_alumina_refinery.md`, §6 of `dd_aluminium_smelter.md`.
**Standard:** AMIRA P754 Metal Accounting — Code of Practice and Guidelines (the global reference). Russian standards (ГОСТы on металлургический учёт) are compatible but less granular.

---

## 1. Why metal accounting matters in DD

A concentrator producing 100,000 t/y Cu in concentrate at 25% grade processes ~400,000 t of concentrate. If reported recovery is 88% and actual recovery is 86%, the gap is ~2,000 t/y Cu missing — at $9,500/t that is **$19 million/year unaccounted**. Over a 20-year mine life, $380 million NPV impact.

The DD question is not "what is the recovery?" but **"how do you know what the recovery is, and how tight is your error band?"**

Metal accounting integrity scales with metal value:
- Gold operation losing 0.1 g/t in tails is $X/year material — every operation tightens this
- Copper concentrator with 1% recovery uncertainty is $X million/year material
- PGM circuit with 5% accounting uncertainty on PGE distribution is potentially $10M+/year material
- Aluminium smelter with metallurgical-grade vs commercial-purity accounting confusion can hide alloy mis-pricing

---

## 2. Core principles of AMIRA P754

A metal accounting system must satisfy ten principles:

1. **Transparency** — every flow is documented, every adjustment is signed.
2. **Accuracy** — measurement uncertainty is quantified, not assumed.
3. **Reconciliation** — every account balances within stated tolerance.
4. **Defined responsibility** — every node has a single accountable person.
5. **Single source of truth** — one master accounting system, not parallel manual logs.
6. **Independence** — metal accounting reports outside operations (to CFO or General Director), not to plant manager.
7. **Auditability** — full audit trail, sample chain of custody.
8. **Document control** — procedures, versions, sign-off.
9. **Review** — periodic internal and external audit.
10. **Calibration** — instruments calibrated and certified.

If any one of these is missing, system is weak. In DD, score each principle 1–5 and report.

---

## 3. The four mass balance points

Every metal accounting system has four primary balance points. Weakness in any one undermines the whole:

### 3.1 Inputs (ore feed)

**Measurement points:**
- Mine truck weights (bucket scales, weighbridge)
- Stockpile reconciliation (survey, drone, vehicle counts)
- Plant feed conveyor weightometer (calibrated belt scale)
- Grade samples (continuous online vs. cross-belt cut samples)

**Common weakness:** Weightometer not calibrated regularly (monthly minimum). Cross-belt sampler not maintained. Grade samples taken too infrequently for the variability of the ore.

**DD test:**
- Show me the calibration certificates for the past 24 months
- Show me the sampler maintenance log
- Show me the variance between mine call factor (geology block model) and reconciled head grade — should be <±5% over 12-month rolling average

### 3.2 Process products

**Concentrate stream:**
- Belt scale on concentrate
- Concentrate moisture (regularly measured, not assumed)
- Concentrate assay (composite sample, multiple labs, umpire procedure)
- Stockpile reconciliation (survey)
- Shipment weights (rail/truck/ship) — must reconcile to plant outturn

**Tailings stream:**
- Tailings flow (magflow on slurry, calibrated)
- Tailings density
- Tailings assay (composite sample)
- Tailings reconciliation = (Feed − Concentrate) / Feed, by element

**Common weakness:** Tailings assays manipulated to "balance" the calc. Concentrate moisture assumed at fixed % vs measured. Shipment weights reconciled to seller's calc rather than independent surveyor.

**DD test:**
- Show me 24 months of tailings assays — is variability realistic or is data smoothed?
- Show me an independent surveyor's outturn report on a concentrate shipment vs. plant calculation
- Show me the moisture trend on concentrate — should track ore type and process conditions, not be flat

### 3.3 Metal in process (lock-up)

In a smelter or refinery, significant metal is held up in furnaces, ladles, slag pots, anode casting, electrolytic cells, refining circuits, dust circuits.

**Lock-up types:**
- Active inventory (metal currently in process, expected to come out within 30 days)
- Frozen inventory (metal in furnace bottoms, slag, dust — recoverable over years)
- Lost inventory (metal in disposed slag, baghouse rejects — written off)

**Common weakness:** Lock-up not measured at start and end of accounting period — losses hidden in "lock-up change". Frozen inventory grows year on year and is never reconciled. Slag inventory not assayed for tail.

**DD test:**
- Show me the metal in process inventory record by node
- Show me change in inventory year-on-year — if it grows ≥5% per year without explanation, it is masking losses
- Show me the assay protocol for slag and dust — frequency, lab, audit trail
- For non-ferrous (Ni, PGM, Cu): show me the historical "campaign reconciliation" when furnace was rebuilt and inventory was actually weighed

### 3.4 Final products

**Refined metal:**
- LME-grade, LBMA-grade, or specified-grade assays
- Cathode/ingot/anode weight
- Shipment manifests
- Customer outturn assays

**Common weakness:** Customer outturn deductions absorbed silently — variance between plant ship-out weight/assay and customer accept weight/assay should be tracked monthly. Persistent debit balance with customers indicates measurement bias.

**DD test:**
- Show me the customer outturn variance log for the past 24 months — by customer, by metal
- Show me how disputes are resolved (umpire assay, third-party reweigh)
- For precious metals: show me the refiner reconciliation (gold/silver in vs. doré in vs. refined out)

---

## 4. The reconciliation hierarchy

Five levels of reconciliation, each tighter than the last:

| Level | Description | Tolerance (typical) | Frequency |
|-------|-------------|---------------------|-----------|
| Level 1 — Block model | Geology grade × tonnes vs mine production | ±10–15% | Annual |
| Level 2 — Mine to mill | Mine production reconciled to plant feed | ±5% | Monthly |
| Level 3 — Plant input/output | Feed = Concentrate + Tailings, by element | ±2% | Monthly |
| Level 4 — Smelter/refinery | Concentrate in = Metal out + Slag + Dust + In-process change | ±0.5–1% | Monthly, with campaign rebuilds annual |
| Level 5 — Metal accounting | Final refined metal balance, fully auditable | ±0.1–0.3% (Au, PGM); ±0.3–0.5% (Cu, Ni); ±0.5–1% (Al) | Monthly |

If any level fails to balance, all subsequent levels are corrupted. DD must check each level.

**Anton's signature insight (Norilsk Nickel turnaround context):** The biggest hidden losses in a vertically integrated complex are at the **transition points** — mine to mill, mill to smelter, smelter to refinery. Each business unit has incentive to over-report what it ships out and under-report what it receives. The corporate reconciliation must be done at corporate level, with single source of truth, signed by both sender and receiver, with umpire procedure for disputes.

**[TODO_ANTON]** Specific Norilsk case where transition-point losses were identified and tightened.

---

## 5. Sampling — the unseen weak link

90% of metal accounting failures are sampling failures, not assay failures. The lab can be perfect; if the sample is biased, the answer is biased.

### 5.1 Theory of Sampling (Pierre Gy)

Every sampling operation has seven error types:
1. Fundamental sampling error (FSE) — minimum unavoidable error based on particle size, grade, mass
2. Grouping and segregation error
3. Long-range periodic error (drift, seasonality)
4. Short-range periodic error (process cycling)
5. Increment delimitation error (cutter not correctly designed)
6. Increment extraction error (cutter not correctly executing)
7. Preparation error (sample contamination, segregation in subsampling)

In DD, check that target has done a Theory of Sampling audit at least once on each sampling station. If they haven't heard of TOS, they don't know their sampling error.

### 5.2 Practical sampling DD tests

- Cross-belt cutter dimensions vs. P754 minima (cutter opening ≥ 3× max particle size, cutter speed ≤ 0.6 m/s)
- Number of increments per shift / per shipment (more = lower error)
- Sample mass per increment vs. theoretical minimum
- Sample reduction protocol (riffling, rotary divider — NOT cone-and-quartering for production samples)
- Reference sample retention — composite samples retained for 6+ months for umpire
- Lab accreditation (ISO/IEC 17025) and proficiency testing (round robins)

---

## 6. Lab integrity

**DD tests:**

- Accreditation scope — is the specific method (e.g. fire assay for Au, multi-element ICP for base metals) within scope?
- Round-robin participation — last 12 months, with check sample performance
- Repeat assay program — fraction of samples re-assayed, variance trend
- Umpire procedure — when production sample disputes occur, what is the third lab and protocol?
- Standards (CRMs) — are certified reference materials run in every batch?
- Blanks — for low-grade or trace analyses, are blanks run to detect contamination?

**Red flag patterns:**
- All standards run "within tolerance" with suspiciously low variance (data fabrication)
- Sudden change in assay variance after lab manager change (procedure change)
- Internal lab without external check (no round-robin, no umpire)
- For Au: fire assay vs. cyanidation discrepancy not investigated

---

## 7. Metal accounting governance

The single most important governance question: **Does the metal accountant report to operations, or to finance?**

| Reporting line | Risk |
|----------------|------|
| Plant manager | Operations has incentive to under-report losses to protect KPIs. High risk of optimization of reported recovery vs. actual. |
| Operations director | Same issue at higher level |
| **CFO / Finance director** | **Correct.** Metal accountant independent of operations performance. |
| General director / CEO | Acceptable for small operations |
| External auditor with full access | Best practice for high-value (Au, PGM) operations |

In Russian/CIS practice, metal accounting is often under "Главный технолог" (chief technologist) reporting to General Director — which is acceptable if there is genuine independence from the production manager. But in many cases the technologist is dependent on production for resources and protection, so independence is weak.

**DD test:** Map the org chart. Where does metal accountant sit? Has anyone in this role been removed/replaced in the past 24 months — and why?

---

## 8. Specific commodity considerations

### 8.1 Gold (cross-ref `dd_gold_hydromet.md`)

- Bullion / doré accounting: vault inventory, weighed in independent presence
- Refiner outturn vs. plant calculation — typically refiner is umpire
- Lock-up in CIL/CIP tanks: significant gold in solution and on carbon — measured at year-end
- Tails assay: Au reports to tails as fine free gold (1–3% of feed) and as locked-in-sulphide (refractory) — must be distinguished

### 8.2 Copper (cross-ref `dd_copper_concentrator.md`)

- Concentrate moisture: easily 8–12% — every percentage point is direct revenue
- By-product credits: Au, Ag, Mo accounting often weaker than Cu — by-product revenue is "free money" mentally and gets less scrutiny
- Penalty elements: As, Bi, Sb, F — assays must be accurate, penalty deductions reconciled to smelter

### 8.3 Nickel-PGM (cross-ref `dd_nickel_pgm.md`)

- PGM distribution through smelter dust, slag, refinery anodes — most complex of all base metal circuits
- Lock-up can be 6–18 months between concentrate and refined PGM
- Campaign reconciliation when furnace is rebuilt — actual hold-up vs. calculated
- "PGM" includes 6 elements (Pt, Pd, Rh, Ru, Ir, Os) — each must be tracked individually, not as "PGE"

### 8.4 Aluminium (cross-ref `dd_aluminium_smelter.md`, `dd_aluminium_downstream.md`)

- Hot metal vs. cold metal accounting (smelter → casthouse)
- Alloy composition: alloying additions tracked by mass and assay
- Recycle integration: scrap-in mass and grade, dilution
- Customer-grade reconciliation: 99.7% standard vs. higher-purity premium product

### 8.5 Alumina (cross-ref `dd_alumina_refinery.md`)

- Bauxite quality (Al₂O₃ content, A/S modulus) at receipt vs. nominated
- Liquor productivity and inventory
- Red mud: volume and Al content (lost Al revenue, plus future liability)
- Hydrate vs. calcined product accounting

---

## 9. DD scoring framework

Score the metal accounting system on each of 8 dimensions, 1–5 scale:

| Dimension | 1 (Weak) | 3 (Adequate) | 5 (Best practice) |
|-----------|----------|--------------|-------------------|
| Sampling per TOS | No audit, manual cone-and-quarter | One-time audit done | Annual TOS audit, all stations meet P754 |
| Lab quality | Internal only, no round-robin | ISO 17025, occasional umpire | Full QA/QC, monthly round-robin, blind duplicates |
| Reconciliation tolerance | >5% on Level 3 monthly | 2–5% on Level 3 monthly | <2% on Level 3 monthly |
| Lock-up management | Not measured | Measured annually | Measured monthly, campaign rebuilds |
| Governance | Reports to plant manager | Reports to operations director | Reports to CFO with audit committee oversight |
| Calibration | Annual or less | Quarterly | Monthly with documented certificates |
| Audit | None | Internal annual | External annual + internal continuous |
| Documentation | Paper, fragmented | Spreadsheet system | Integrated software (e.g. Met Manager, Mass Bal, Pi-AF, custom) |

**Total score:**
- 32–40 → Best practice, low DD risk
- 24–31 → Adequate, normal DD risk, room for improvement
- 16–23 → Weak, material DD risk, hidden losses likely 1–3% of revenue
- <16 → Critical weakness, recommend full external audit pre-close

---

## 10. Quick DD checklist (1-hour review during management session)

- [ ] Who is the metal accountant? Reports to whom?
- [ ] When was the last AMIRA P754 audit (or equivalent)? Show me the report.
- [ ] What is the Level 3 monthly reconciliation tolerance, and how often is it breached?
- [ ] Show me last 24 months of mine call factor variance (Level 1).
- [ ] Show me last 24 months of customer outturn variance.
- [ ] Show me the calibration log for the main belt weightometer.
- [ ] Are sampling stations TOS-audited?
- [ ] What round-robin program does the lab participate in?
- [ ] What is the year-on-year change in metal in process inventory?
- [ ] Who signs off the monthly metal balance?

---

## TODO_ANTON consolidated

1. Norilsk Nickel turnaround — specific metal accounting tightening case (transition points, lock-up reconciliation)
2. RUSAL casthouse — alloy composition accounting and customer-grade discipline
3. UMMC gold-from-tailings — sampling pattern for variable secondary tailings
4. Personal cases where weak metal accounting masked losses — anonymised
5. Specific software systems used at Russian/CIS assets — what works, what doesn't
