# Owner Team Engineering — Methodology

**Author:** Anton Zaytsev
**Purpose:** Framework for owner-side technical leadership on large CapEx in mining/non-ferrous metallurgy. The discipline that separates an asset that gets built within ±15% of sanctioned budget from one that overruns 40–80%.
**Use case in DD:** Section §13 of standard DD skeleton ("Project execution capability"). When client asks "can this team actually build it?" — this file is the answer framework.

---

## 1. What "Owner Team Engineering" actually means

Most CapEx failures are not engineering failures. They are **owner-side governance failures** that allow engineering, procurement, or construction to drift unchecked. The owner team's job is not to do the work — it is to ensure the work is done right by EPC/EPCM/vendors, on cost, on schedule, to specification.

Three core functions:

1. **Define and protect scope** — what is being built, what is NOT being built, who pays when scope changes.
2. **Independent verification** — every number from EPC/vendor is checked by the owner against parallel estimate, benchmark, or first-principles calculation.
3. **Decision authority and discipline** — clear gates, clear delegation, no scope/cost decisions made in operational meetings.

If any of these three fails, project will overrun. Empirically, ≥60% of mining/metallurgy CapEx overruns trace to owner team failure, not EPC failure. EPC behaves as the owner permits.

---

## 2. Owner team structure — minimum viable

For a >$200M project FEL 2 onward, owner team should have these distinct roles. Combining roles is allowed only if the person has bandwidth and prior experience in both:

| Role | Minimum FTE | Responsibility | Common failure mode |
|------|-------------|----------------|---------------------|
| Project Director | 1.0 FTE, dedicated | Final accountability. Reports to Steerco/IC. | Part-time PD = no PD. |
| Project Controls Lead | 1.0 FTE | Cost, schedule, change control, contingency drawdown. | Reports to PD only, not to CFO/Finance — captured. |
| Lead Process Engineer (Owner) | 1.0 FTE | Owns the flowsheet. Reviews FEED. Approves vendor selection on critical equipment. | Hired late (FEL 3) — flowsheet already locked by EPC. |
| Lead Mechanical/Civil/E&I (Owner) | 0.5–1.0 each | Discipline review of EPC deliverables. | All reviews delegated to EPC — no independent check. |
| Construction Manager (Owner) | 0.5 FEL → 1.0 EPC stage | Constructability review FEL. Site interface during execution. | Brought in at construction start — no FEL input. |
| Procurement Lead (Owner) | 1.0 FTE | Long-lead equipment, contract structure, vendor selection. | Procurement done by EPC under cost-plus contract — no owner visibility. |
| Cost Estimator (Owner, independent) | 0.5–1.0 FTE | Parallel estimate to FEED. Benchmark database. Class 3 → Class 2 sanity check. | Does NOT exist in 70%+ of Russian/CIS projects — EPC estimate accepted at face value. **This is the #1 gap.** |
| Risk Manager | 0.3–0.5 FTE | Risk register, quantitative analysis, contingency model. | Outsourced to EPC — risks of EPC underreported. |
| Permitting/HSE/Stakeholder Lead | 1.0 FTE | All non-technical fatal flaws sit here. | Underrated, understaffed. Sole permitting failure can kill a $500M project. |
| Commissioning Manager | 0.0 FEL 1 → 1.0 FEL 3 | Commissioning plan, operability review, ramp-up plan. | Brought in at mechanical completion — no FEED input. |

**Anton's rule of thumb:** Total owner team headcount should be **5–10% of EPC engineering headcount** for non-greenfield, **10–15% for greenfield in unfamiliar geography**. If owner team is 1–2% of EPC team, project is exposed. If owner team is >20%, owner is duplicating EPC and wasting money.

**[TODO_ANTON]** UMMC ~$550M project — own team final composition, what worked, what was understaffed.

---

## 3. The four owner-team failure patterns Anton sees most often in DD

### 3.1 The "thin owner" pattern

**Signal:** Owner team <2% of EPC team. PD is also CEO or COO with day job. No independent cost estimator. Project Controls reports to PD only.

**Consequence:** EPC scope creep absorbed silently. Change orders approved at site without IC visibility. Contingency drawdown invisible until 80%+ exhausted. Schedule slip reported only when it becomes unrecoverable.

**DD question:** "Show me the org chart of the owner project team, with names, FTE allocation, and reporting lines. Show me the last 3 change orders, who approved, and what was the cost impact."

**Red flag:** Org chart shows roles but not names. "We are hiring" = role is empty today.

### 3.2 The "EPC captured owner" pattern

**Signal:** Owner team is composed of secondees from the same EPC firm doing FEED or execution. PD was hired from the EPC firm 6 months before contract award.

**Consequence:** Owner team cannot challenge EPC. Reviews are rubber-stamps. Cost estimates accepted as-is. Independent verification does not happen.

**DD question:** "Where was each member of the owner project team employed in the 24 months before joining this project?" Map the network.

**Red flag:** ≥40% of owner team came from EPC firm now executing. Especially if PD, Project Controls Lead, or Lead Process Engineer.

### 3.3 The "no parallel cost estimate" pattern

**Signal:** FEED contractor produces the AACE Class 3 estimate. Owner team accepts it (sometimes after "review"). No owner-side independent estimator. No benchmark database.

**Consequence:** Estimate is biased toward sanction (FEED contractor wants project to proceed so it gets execution scope). Optimism baked in. Overrun ~25–40% by mechanical completion is normal.

**DD question:** "Who produced the AACE Class 3 estimate? Did the owner produce an independent parallel estimate? What was the variance between owner estimate and FEED estimate? How were variances reconciled?"

**Red flag:** Variance was reconciled by "agreeing on FEED number." Owner number quietly disappeared.

**[TODO_ANTON]** Personal case where parallel estimate flagged $X gap and forced rebaseline. RUSAL or UMMC example.

### 3.4 The "operations not engaged" pattern

**Signal:** Future operating personnel (plant manager, maintenance manager, metallurgy manager) are not part of project reviews FEL 1–2. They are presented with a finished design at commissioning.

**Consequence:** Operability and maintainability gaps. Spares list incomplete. Operator-unfriendly layout. Ramp-up takes 18–24 months instead of 6–9 months. NPV destroyed in years 1–3.

**DD question:** "Who from the future operating team signed off the FEL 2 deliverables? Show me the operability and maintainability review reports."

**Red flag:** Operations team did not exist at FEL 2 — to be hired during construction. Or operations team existed but had no formal review role.

---

## 4. IC defense framework — what owner team owes the Investment Committee

When owner team takes a sanction request to IC at FEL 3 → execution gate, they must defend on **four axes simultaneously**. Failure on any one = no sanction.

### Axis 1: Scope is locked and complete

- WBS to Level 3 or 4
- Battery limits document signed by all interface owners
- Scope deviation log from FEL 2 → FEL 3 with cost impact each
- Confirmation that no major scope additions are pending

**IC challenge question:** "What scope item is NOT in this estimate that we will discover at FEL 3 → execution gate?" If answer is "nothing", you are about to overrun.

### Axis 2: Cost estimate is defensible

- AACE Class 3 minimum, preferably Class 2 for high-confidence projects
- Independent owner estimate within ±10% of FEED estimate (if larger, reconcile transparently, don't paper over)
- Benchmark comparison to 3–5 analogous projects (per-tonne capacity cost, per-kt or per-Moz)
- Contingency is **bottom-up risk-based**, NOT percentage. Document each risk → contingency dollar with probability and severity.

**IC challenge question:** "If you remove the contingency, what is the P50 cost? What is the P90 cost? What is the gap?" If they can't answer, contingency is theatre.

**Anton's signature:** ≥80% of Russian/CIS projects sanctioned with **percentage contingency** (10%, 15%, "we always use 12%"). This is not contingency — it is a placeholder. Real contingency = sum of (risk probability × risk cost impact) across the risk register, with explicit overhead for unknown unknowns calibrated to project class and geography.

### Axis 3: Schedule is defensible

- Level 3 schedule, resource-loaded
- Critical path identified, with float on non-critical activities
- Long-lead equipment list with order dates, delivery dates, fabrication shop confirmed
- Permits status with all "in-progress" permits showing realistic close dates
- Ramp-up curve based on benchmarked startup of comparable assets, not optimistic vendor curves

**IC challenge question:** "What activity is on the critical path? What is the float? What event would push first-metal date by 6 months?" If "nothing critical, lots of float", the schedule is fiction.

### Axis 4: Risks are identified and mitigated

- Quantitative risk register, top 20–30 risks with owners
- Top 5 risks have explicit mitigation plans with cost and schedule impact
- Fatal-flaw risks (permits not obtainable, social licence collapse, technology not proven at scale) explicitly addressed
- Sensitivity analysis: NPV/IRR vs metal price (-20%/-10%/base/+10%/+20%), vs CapEx (+10%/+20%/+30%), vs schedule (+6 mo / +12 mo)

**IC challenge question:** "At what metal price does this project NPV = 0? At what CapEx overrun does NPV = 0? At what schedule slip?" If breakeven scenarios are not far from base case, project is not robust — it requires everything to go right.

---

## 5. The "Anton parallel estimate" methodology

This is a specific deliverable the owner cost estimator produces, independent of FEED. Used in IC defense and continuously through execution.

**Inputs:**

1. FEED deliverables (PFD, P&ID, equipment list, civil/structural quantities, E&I quantities)
2. Benchmark database (per-tonne capacity, per-discipline allocation, by geography)
3. Vendor budget quotes (independent of FEED — owner re-quotes critical packages)
4. Productivity factors for local labour, transport multipliers, currency exposure

**Method:**

1. **Quantity takeoff** — owner does parallel takeoff from PFD/P&ID, not from FEED takeoff. Variance >5% on critical disciplines = investigate.
2. **Unit rates** — owner applies own unit rates (from benchmark + recent project actuals). Compares to FEED unit rates.
3. **Equipment costing** — owner sends RFQs to 2–3 vendors per critical package. Compares to FEED's vendor pricing.
4. **Indirect costs and overhead** — owner builds independent EPCM, owner's costs, insurance, freight. FEED tends to under-allocate.
5. **Contingency** — built bottom-up from risk register. Compared to FEED contingency (almost always lower than FEED's percentage allowance).

**Output:** Two columns side by side — FEED estimate and owner estimate, with variance and reconciliation per line. Variance >10% on any major line item is escalated to PD and IC.

**Typical findings on a poorly-prepared FEED:**
- Equipment 10–15% under (vendor quotes too low or scope creep ignored)
- Indirect costs 20–30% under (EPCM, owner's costs, insurance, contingency on owner's costs)
- Schedule risk not priced (escalation, productivity loss)
- Currency exposure not stressed (especially for non-USD components)

**[TODO_ANTON]** Specific case: parallel estimate found $X gap → was rebaselined → final outcome.

---

## 6. The "RUSAL casthouse" public-layer case

**Use as illustration of owner team engineering done right, no figures disclosed beyond what is in CV.**

Project: greenfield casthouse expansion, RUSAL alumina-aluminium complex.
Anton's role: Head of Technology / project owner-side technical lead.
Outcome (public layer): commissioned ~18% under industry CapEx benchmark for comparable capacity.

What was done differently:

1. **Owner-side metallurgical and process expertise was strong before FEED started** — flowsheet was specified, not delegated. FEED contractor optimised within the owner's flowsheet, not invented it.
2. **Equipment specifications were owner-driven** — DC casting line, holding furnaces, in-line metal treatment. Owner team had operated similar equipment elsewhere and knew exactly what was a must-have vs nice-to-have. Cut ~15% scope that FEED would have included as "good practice".
3. **Vendor selection was owner-led** — 3-vendor RFQ on every critical package, with technical bid tabulation done by owner's process engineers, not FEED's procurement.
4. **Parallel cost estimate** at every gate — FEED Class 3 was checked against owner's bottom-up estimate. Variances reconciled before IC.
5. **Operations engaged from FEL 1** — future plant manager was on the project team. Layout, maintainability, spares list all reviewed.
6. **No EPCM** — direct multi-contract execution under owner's project team. Higher owner team cost, much lower contract margin paid to EPCM, faster decision cycles.

**What this proves in DD context:** Strong owner team can sanction at 80–85% of "industry benchmark" cost. Weak owner team will sanction at 100% benchmark and execute at 120–140% benchmark. The owner team is the single largest CapEx lever.

**[TODO_ANTON]** Refine specific layered numbers, dates, equipment vendors at layered citation level. Public layer above is safe.

---

## 7. Application in DD — how to use this file

### When reviewing target company's CapEx pipeline

1. Pull org chart of project teams. Map roles vs §2 minimum-viable list. Gaps = risk.
2. Identify project director's bandwidth (full-time? Other roles?).
3. Check independence of project controls and cost estimator from EPC.
4. Review most recent IC submissions — were they defended on all four axes (§4)?
5. Pull change order history — change order frequency >2/month on a project in execution = no scope discipline.
6. Look at contingency drawdown profile — if drawdown is faster than physical progress, project is overrunning silently.

### Killer questions for management session

- "Who owns scope discipline on this project? What was the last scope item rejected and why?"
- "Show me your parallel cost estimate vs FEED. Where are the variances and how were they resolved?"
- "Of your last three CapEx projects >$100M, what was the final cost vs sanction? What did the owner team learn?"
- "If I doubled the scope tomorrow, who has authority to approve and at what threshold does it escalate to IC?"
- "Walk me through your bottom-up contingency model. What are the top five risks and what dollar amounts do they carry?"

### Red flags in management responses

- "We trust our EPC, they have done this before" — no challenge culture.
- "Our contingency is industry-standard at 12%" — no risk-based model.
- "The project director handles change orders" — no governance.
- "We will hire the construction manager when construction starts" — no constructability input at FEL.
- "Operations will be involved during commissioning" — operability gaps locked in.

### IC memo language

If owner team is strong:
> "Owner project organisation is well-established with [X] dedicated FTEs at FEL [N]. Project controls, independent cost estimation, and scope governance are in place and demonstrably independent from EPC/FEED contractor. Historical project delivery on the past three [size] projects shows [X]% average cost variance vs sanction. Cost estimate is defensible."

If owner team is weak:
> "Owner project organisation is under-resourced for a project of this size. Specifically, no independent owner-side cost estimator was identified; project controls reports to PD without independent reporting line to Finance/CFO; no parallel cost estimate was produced to challenge the FEED estimate. We assess base-case cost overrun probability at [X]% with expected magnitude [Y]%, materially above sanctioned contingency. Recommend [conditions for sanction / no-sanction]."

---

## 8. Cross-reference

- `methodology/fel_methodology.md` — gate criteria each owner team must defend
- `skeletons/dd_standard.md` §13 — where this is used in DD writeup
- `knowledge/anton_cases.json` — UMMC, RUSAL cases referenced here
- `risk/red_flags_decision_trees.json` — execution risk red flags

---

## TODO_ANTON consolidated

1. UMMC ~$550M project owner team final composition (§2, §6 cross-ref)
2. Personal case: parallel estimate flagged $X gap and forced rebaseline (§3.3, §5)
3. RUSAL casthouse layered numbers, dates, equipment vendors (§6)
4. Specific lessons on Project Controls capture by EPC — 1–2 stories
5. Any case where strong owner team rescued a project mid-execution
