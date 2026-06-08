# DD Production Line — Phase 1b

**Status:** principal-grade infrastructure in place. Ready for live-fire pilot on next DD engagement. To be refined in practice.

**Owner:** Anton Zaytsev — Independent Technical Advisor, Mining & Non-Ferrous Metals
**Audience:** Anton (operating engine) + future subcontracted specialists if scaled
**Vintage:** June 2026 baseline; sanctions/CBAM/market data needs re-verification each engagement

---

## What this is

A complete operational engine for delivering **principal-grade technical due diligence** on mining and non-ferrous metals assets, calibrated to Anton's competitive positioning under Strategy v3:

- Russia-resident + CIS-deep + Western-compliance-clean
- Solo practice with subcontracted specialists, not a firm
- Pricing: Standard DD $22–30K / 35–45h, Deep DD $55–85K / 80–120h
- Selectivity: non-ferrous + CIS focus; honest scope limits stated explicitly

The infrastructure converts Anton's 16 years of operating experience (UC RUSAL, Norilsk Nickel, UMMC, ERG/McKinsey) into a reusable, auditable, compounding asset base.

---

## Directory structure

```
dd-engine/
├── README.md                          # This file
├── compliance_overlay.md              # Universal author statement + per-jurisdiction blocks
├── knowledge/
│   └── anton_cases.json               # v2.0 — 13 cases with layered citation policy
├── skeletons/                         # Sector-specific DD report skeletons
│   ├── dd_standard.md                 # Generic skeleton (legacy, low priority)
│   ├── dd_aluminium_smelter.md        # Hall-Héroult — Anton signature
│   ├── dd_aluminium_downstream.md     # Casthouse + rolling + extrusion — RUSAL signature + 7 patents
│   ├── dd_nickel_pgm.md               # Cu-Ni sulphide + PGM — Norilsk signature
│   ├── dd_gold_hydromet.md            # Gold + tailings reprocessing — UMMC signature
│   ├── dd_copper_concentrator.md      # Porphyry Cu — honest scope statement
│   ├── dd_alumina_refinery.md         # Bayer process — ERG/RUSAL context
│   └── killer_questions.json          # Sector × dimension question library
├── methodology/                       # Cross-cutting analytical frameworks
│   ├── fel_methodology.md             # Anton's FEL framework — UMMC + RUSAL + ERG signature
│   ├── owner_team_engineering.md      # CapEx defense — RUSAL casthouse 18%-under-benchmark case
│   ├── dd_workflow.md                 # Phase 0–8 execution playbook
│   └── metal_accounting.md            # AMIRA P754 — mass balance, sampling, governance
├── intel/                             # Domain intelligence files
│   ├── sanctions_compliance_intel.md  # CIS/Russia structural moat — OFAC/EU/UK/LME/LBMA
│   ├── cbam_carbon_intel.md           # EU CBAM 2026 obligation — per-commodity exposure
│   ├── tailings_intel.md              # GISTM, construction methods, failure modes, Russian context
│   └── jorc_ni43101_red_flags.md      # Reading public technical reports for what's NOT said
├── risk/                              # Risk register infrastructure
│   ├── risk_register_prefill.json     # 8 categories × ~30 typical risks
│   ├── red_flags_decision_trees.json  # 40+ red-flag patterns per sector
│   └── mitigation_playbook.json       # Risk → mitigation library
├── benchmarks/                        # Quantitative reference data
│   └── capex_benchmark_database.json  # Per-tonne capacity costs by sector
├── templates/                         # Client-facing deliverable templates
│   ├── ic_memo_template.md            # IC submission, 6–10 pages target
│   ├── management_session_protocol.md # Killer questions session playbook
│   └── red_flag_alert_template.md     # Mid-DD escalation to client
└── scripts/                           # [PHASE 2] Auto-assembly scripts
```

---

## What Phase 1b adds beyond Phase 1

Phase 1 (May 2026) shipped 5 baseline files. Phase 1b (June 2026) raised these to principal-grade and added 11 new files:

**Phase 1 (baseline — kept):**
- `anton_cases.json` v2.0 — 13 cases with layered citation
- `dd_aluminium_smelter.md` — 40+ section skeleton
- `dd_standard.md` — generic skeleton
- `killer_questions.json` — ~50 sector × dimension questions
- `risk_register_prefill.json`, `red_flags_decision_trees.json`, `mitigation_playbook.json`
- `capex_benchmark_database.json`
- `compliance_overlay.md` — full author statement + per-jurisdiction blocks

**Phase 1b additions (sector skeletons, ~25K chars each, principal-grade):**
- `dd_nickel_pgm.md` — Norilsk signature, Cu-Ni sulphide → smelter → PGM refining, Vanyukov vs flash, Талнах ore body, Серная программа 2.0, autoclave/carbonyl refining
- `dd_gold_hydromet.md` — UMMC signature, gold-from-tailings methodology, refractory flowsheet selection (POX/BIOX/Albion/roast), cyanide management, ICMC compliance, Russian gold sector post-2022
- `dd_aluminium_downstream.md` — RUSAL signature + 7 patents, casthouse defects framework, DC casting, alloy series 1xxx-7xxx, OEM qualification (Boeing, Airbus, automotive), conversion margin economics
- `dd_copper_concentrator.md` — honest scope statement (not Anton's signature), CapEx defense angle, Cu-Mo separation, by-product credits, TC/RC dynamics
- `dd_alumina_refinery.md` — Bayer process (low-T gibbsite vs high-T diaspore), red mud disposal, ERG/RUSAL upstream context

**Methodology files (Anton signature frameworks):**
- `methodology/fel_methodology.md` — FEL stage gating, AACE class mapping, IC defense framework, owner team engineering during FEL, failure pattern library (7 patterns), quality assessment scoring
- `methodology/owner_team_engineering.md` — RUSAL casthouse 18%-under-benchmark case (public layer), parallel cost estimate methodology, four failure patterns, IC memo language templates
- `methodology/dd_workflow.md` — full Phase 0–8 execution with hours budget for Standard and Deep DD, retainer conversion path embedded
- `methodology/metal_accounting.md` — AMIRA P754, four mass balance points, sampling Theory of Sampling (Gy), lab integrity, governance, 8-dimension scoring framework

**Intel files (Anton's structural moat):**
- `intel/sanctions_compliance_intel.md` — OFAC/EU/UK/Canada/Australia/Japan landscape, LME post-April-2024 Russian metal status, LBMA Russian refiner suspensions, beneficial ownership analysis, CIS-specific operational realities, commodity × jurisdiction matrix
- `intel/cbam_carbon_intel.md` — EU CBAM 2026 obligation, formula, phase-in to 2034, per-commodity exposure (Al, alumina, steel, fertiliser, copper/nickel future scope), decarbonisation levers, Russian metals strategic positioning
- `intel/tailings_intel.md` — GISTM principles and consequence classification, construction methods (upstream/downstream/centerline/dry-stack), failure modes, ARD/cyanide/As/Hg by commodity, Russian regulatory framework, killer questions
- `intel/jorc_ni43101_red_flags.md` — language tells, methodology red flags, geometry/economic/metallurgy red flags, CP/QP red flags, ГКЗ → CRIRSCO translation discipline, 90-minute triage protocol

**Templates (client deliverables):**
- `templates/ic_memo_template.md` — IC submission format with BLUF discipline, 6–10 page target, sensitivity table, top-10 risk register, conditions for proceed
- `templates/management_session_protocol.md` — pre-session prep, opening discipline, question types, follow-up technique, reading the room, session formats (Standard/Deep/site-combined)
- `templates/red_flag_alert_template.md` — mid-DD escalation format, when to use, client response patterns, professional independence preservation

---

## How to use — engagement workflow

**For every new DD engagement:**

1. **Phase 0 — Scoping** (before clock starts)
   - Read `methodology/dd_workflow.md` §2
   - Apply `compliance_overlay.md` for engagement-specific compliance framing
   - Sign SoW with appropriate disclosures

2. **Phase 1 — Document review** (Standard: 8–12h / Deep: 20–30h)
   - Open relevant sector skeleton: `skeletons/dd_[sector].md`
   - Build data room map and issues log
   - Scan against `risk/red_flags_decision_trees.json`
   - If deal-killer found: trigger `templates/red_flag_alert_template.md`

3. **Phase 2 — Public research** (Standard: 3–5h / Deep: 8–12h)
   - Sanctions screening: `intel/sanctions_compliance_intel.md`
   - Carbon exposure: `intel/cbam_carbon_intel.md`
   - Resource credibility: `intel/jorc_ni43101_red_flags.md`
   - Benchmarks: `benchmarks/capex_benchmark_database.json`

4. **Phase 3 — Management session** (Standard: 4–6h / Deep: 10–15h)
   - Run per `templates/management_session_protocol.md`
   - Killer questions from `skeletons/killer_questions.json` + sector skeleton §15
   - For tailings deep-dive: `intel/tailings_intel.md` §9

5. **Phase 4 — Site visit** (if scoped — Standard: usually out / Deep: 16–24h)
   - Apply sector-specific checklists from skeleton
   - Use `methodology/metal_accounting.md` §5 if metal accounting in scope

6. **Phase 5 — Specialist input** (if scoped)
   - Coordinate per `methodology/dd_workflow.md` §7

7. **Phase 6 — Synthesis & risk register** (Standard: 6–10h / Deep: 15–25h)
   - Build risk register from `risk/risk_register_prefill.json`
   - Apply mitigations from `risk/mitigation_playbook.json`

8. **Phase 7 — Report & IC memo** (Standard: 6–10h / Deep: 15–25h)
   - Main report follows sector skeleton structure
   - IC memo per `templates/ic_memo_template.md`
   - Author statement per `compliance_overlay.md` Block A

9. **Phase 8 — Client review & delivery** (Standard: 2–3h / Deep: 5–8h)
   - Retainer conversion seeded per `methodology/dd_workflow.md` §11

10. **Post-engagement (within 1 week of delivery):**
    - Update `knowledge/anton_cases.json` with case (anonymized as needed)
    - Add new red flags to `risk/red_flags_decision_trees.json`
    - Add new questions to `skeletons/killer_questions.json`
    - Update relevant intel files
    - Capture lessons in `lessons_learned.md` (project Штаб)

This is the compounding mechanism. Each DD makes the engine better.

---

## What's still needed — TODO_ANTON consolidation

All Phase 1b files contain `[TODO_ANTON]` tags marking specific facts requiring Anton's verification or layered-citation framing. Highest priority:

### Anton's signature cases — refinement required

1. **UMMC ~$550M / ~50 bn RUB gold-from-tailings project (FEL 1-3 director)**
   - `dd_gold_hydromet.md` §14
   - `methodology/fel_methodology.md` §10
   - `methodology/owner_team_engineering.md` §5–§6
   - `knowledge/anton_cases.json`

2. **RUSAL casthouse 40 ktpa expansion (18% under benchmark)**
   - `dd_aluminium_downstream.md` §15 + §10.3
   - `methodology/owner_team_engineering.md` §6 (public-layer case included)
   - `knowledge/anton_cases.json`

3. **Norilsk Nickel 305-staff / 0-LTI turnaround**
   - `dd_nickel_pgm.md` §15
   - `knowledge/anton_cases.json`
   - Likely also relevant to `methodology/metal_accounting.md` §4

4. **7 patents on aluminium alloys**
   - `dd_aluminium_downstream.md` §12 + §15
   - `knowledge/anton_cases.json`
   - Numbers, titles, scope description under layered citation

5. **ERG / McKinsey CapEx transformation engagements**
   - `methodology/fel_methodology.md` §10
   - `methodology/owner_team_engineering.md`
   - `dd_alumina_refinery.md` §14

### Phase 2 build items (auto-assembly)

- `scripts/build_dd.py` — given `--asset --sector --client`, assembles draft skeleton from sector template + KG cases + risk register prefill
- DeepSeek auto-research module (already running in `metals-news-bot` digest infrastructure) — extend to per-engagement source pull
- Report assembler md → docx with corporate styling
- Lessons-learned auto-update from each DD post-mortem

### Infrastructure questions

- **Repo location decision pending** — subfolder in `metals-news-bot` vs separate `dd-engine` repo
- **Secrets / API key sharing** with metals-news-bot if subfolder approach

---

## Strategic context — why this matters

Per Strategy v3 (`Strategy_v3_Solo_Anton_Zaytsev.md`):

**Year 1 success metric is NOT revenue. It is one signed retainer by month 12.**

The DD Production Line is the engine that drives that retainer:

- Strong DD work → satisfied client → conversation about post-close priority actions → retainer offer naturally embedded
- Each DD is also a content asset — paraphrased case studies for `linkedinpro` skill, framework articles, conference talks
- Each DD compounds infrastructure — better skeletons, more killer questions, sharper red flag patterns
- Each DD calibrates pricing — by month 6, Anton should know whether $400/h is right floor for direct engagements

Without this engine, every DD starts from scratch. With this engine, the 5th DD takes 60% of the time of the 1st DD while producing higher-quality output.

---

## Calibration & maintenance

**Quarterly:**
- Re-verify sanctions intelligence (`intel/sanctions_compliance_intel.md`) — landscape changes monthly
- Re-verify CBAM rates and scope (`intel/cbam_carbon_intel.md`)
- Update benchmark database with most recent comparable transactions

**Per-engagement:**
- Run TODO_ANTON checklist for any files actively referenced
- Update lessons learned

**Annually:**
- Full review of skeleton structure — is anything missing? Anything redundant?
- Industry standards review — GISTM updates, JORC/NI 43-101 amendments, AACE changes
- Pricing recalibration per Strategy v3 §4.1 trajectory

---

## What's deliberately NOT in this engine

- **Financial / valuation modelling** — Anton is not a corporate finance specialist. DD reports state qualitative valuation implications and refer to client's own analysts or external valuers for point estimates.
- **Legal / sanctions opinion** — Anton flags compliance facts and risks; legal counsel opines.
- **Geological QP signing** — Anton does not sign as QP under NI 43-101 or CP under JORC. For QP-signed work, subcontract.
- **Commodity price forecasting** — Anton uses consensus / published forecasts; does not produce own forecast.
- **Pure financial DD** — Big 4 / financial DD specialists own this. Anton coordinates if integrated DD.

This selectivity is the discipline. Per Strategy v3: "Не комментирую то, в чём не разбираюсь — отказ + рекомендация коллеги."

---

## Version

- **Phase 1**: May 2026 — baseline files
- **Phase 1b**: June 2026 — principal-grade skeletons + methodology + intel + templates
- **Phase 2** (planned): July–August 2026 — auto-assembly, auto-research, repo decision
- **Phase 3** (planned): September–October 2026 — retainer conversion engine, lessons learned automation

---

## Quick links

- Strategy context: `/mnt/project/Strategy_v3_Solo_Anton_Zaytsev.md`
- Business profile: `/mnt/project/business_profile.md`
- Decisions log: `/mnt/project/decisions_log.md` (Штаб)
- Communication program (running parallel): `/mnt/project/communication_program.md`
