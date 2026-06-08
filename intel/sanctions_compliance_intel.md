# Sanctions & Compliance Intel — Mining & Non-Ferrous Metals

**Author:** Anton Zaytsev
**Purpose:** Reference for DD on assets with Russia, CIS, or sanctions-adjacent exposure. This is Anton's structural moat — Western advisors avoid this terrain, Anton operates inside it but with full compliance discipline.
**Last calibration:** 2026. Sanctions landscape changes monthly — verify current state via primary sources before each engagement.
**Critical caveat:** This is **technical/operational intelligence** for use in DD scoping and risk assessment. It is **NOT legal advice**. Every engagement with sanctions exposure must have specialist sanctions counsel on the client side. Anton's role is to surface the technical reality (what metal is flowing where, who pays whom, what equipment is sourced from where) so legal counsel can render compliance opinion.

---

## 1. Why this file exists

Post-February 2022, the sanctions architecture for mining & metals is fragmented across multiple regimes:

- **OFAC (US Treasury)** — SDN list, sectoral sanctions, secondary sanctions threat
- **EU** — Council regulations, sectoral and entity-specific, with periodic packages (currently 14+ packages as of 2026)
- **UK (OFSI / HMT)** — Largely parallel to EU but separate consolidated list
- **Switzerland, Norway, Iceland, Liechtenstein** — Align with EU but separate listings
- **Canada (SEMA), Australia (DFAT), Japan (METI/MOF)** — Each with own list and rules
- **LME (London Metal Exchange)** — Not government but de facto regulator for Russian-origin metal listing/delivery
- **LBMA (London Bullion Market Association)** — Gold/silver/PGM responsible sourcing standard

For Western buyers, financiers, and advisors looking at any asset with Russian touch-points, the compliance question is multi-layered: not just "is this entity sanctioned" but "does any beneficial owner, key supplier, key customer, key financier, or key off-taker have sanctions exposure that propagates risk."

Anton operates in this environment legally because he is Russia-resident, and Russian compliance regime permits/requires what some Western regimes prohibit. The job is to provide clean technical analysis that Western legal counsel can use to render compliance opinion, **without** Anton himself making compliance representations.

---

## 2. The compliance framing Anton uses in DD reports

Standard wording in every DD report involving Russia/CIS exposure (see also `compliance_overlay.md` Block A):

> **Sanctions & Compliance Note.** This report provides technical due diligence on the operational, geological, metallurgical, and project-execution aspects of the Asset. It does **not** constitute legal advice on sanctions compliance, export controls, or jurisdiction-specific regulatory matters. The author is resident in the Russian Federation and operates under Russian regulatory framework. Findings related to ownership structures, counterparty relationships, and trade flows are reported as factually identified from public and disclosed sources. The Client is advised to obtain independent specialist sanctions counsel before any transaction decision. The author has not screened any party against any sanctions list and makes no representation regarding the sanctions status of any party referenced herein.

This positions Anton as a technical advisor whose work is **inputs to** legal compliance review, not a substitute for it. This is honest and protects everyone.

---

## 3. Russian mining & metals — entity-level sanctions snapshot

**Verify currency before every engagement.** This is a 2026 baseline — assume entities have moved between categories.

### 3.1 SDN-listed (US OFAC)

Generally the most restrictive — US persons cannot deal, secondary sanctions risk for non-US persons.

- Selected oligarch-owned holding companies and personal SDNs
- Some financial institutions (Sberbank, VTB, Gazprombank under various OFAC programs)
- Sectoral and SSI lists separately apply

**[VERIFY CURRENT]** Specific mining/metals entities on SDN list change quarterly. As of recent listings, check status of: USM Holdings entities, EuroChem, certain Polymetal-successor entities, Mechel, MMK, Severstal — these have moved in and out of various lists.

### 3.2 EU sanctions — sectoral & entity

- EU Council Regulation 833/2014 (as amended) — sectoral restrictions on Russian energy, finance, technology
- Specific bans on certain Russian metal products (varies by package)
- **Aluminium**: EU 14th package (June 2024) banned imports of Russian primary aluminium, unwrought and certain semi-finished. **Verify current status** as derogations may apply for specific contracts pre-dating package.
- **Copper**: imports of Russian copper to EU restricted under specific packages
- **Nickel**: as of 2026 baseline, refined Class 1 nickel from Russia has been subject to various restrictions; check current state
- **Iron, steel**: extensive product-by-product restrictions
- **Diamonds, gold**: bans with phase-in
- **PGMs (platinum, palladium)**: more complex — strategic importance to Western industry created exemptions; verify current state by HS code

### 3.3 UK sanctions

Generally parallel to EU on metals but separate enforcement. UK OFSI publishes Russia sanctions guidance.

### 3.4 Self-sanctioning by Western buyers

Even where formal sanctions don't apply, many Western buyers, banks, and insurers refuse to deal with Russian-origin metal due to reputational and operational risk. This **self-sanctioning** is often more restrictive than formal sanctions and changes the commercial reality.

**DD implication:** Even if a metal product is formally exportable to EU/US, the question is "who would actually buy it, at what discount." Russian-origin Cu/Ni/Al has often traded at discount to LME (5–25% depending on product and counterparty profile) regardless of formal sanctions status.

---

## 4. LME and LBMA — non-governmental gatekeepers

### 4.1 LME

- LME suspended new Russian-origin metal (Al, Cu, Ni, Pb, Zn) from listing as good delivery from **13 April 2024** for metal produced on or after that date.
- Russian metal produced before April 2024 remains good delivery (legacy stock).
- Metal that cannot be delivered to LME warrants effectively loses LME pricing — sold bilaterally at discount.

**DD implication:** For any Russian smelter/refinery producing post-April 2024 metal, the **pricing model collapses**. Cannot price at LME flat. Must model at LME minus discount, with discount uncertain and time-varying.

### 4.2 LBMA

- LBMA suspended Russian gold refiners (March 2022) and Russian PGM refiners.
- Specific delistings: see LBMA Good Delivery List for current state.
- Russian gold doré and bullion cannot be sold through LBMA good-delivery chain.
- Alternative refining routes — UAE, Türkiye, China, India — exist but at higher cost and lower price realisation.

**DD implication:** For Russian gold or PGM asset, the offtake structure determines half of the economics. "Sells to Russian Central Bank at LBMA London PM fix" — no longer real. Real offtake = parallel refining channels at discount.

---

## 5. Beneficial ownership analysis

This is the most common gap in DD scoping. The asset may appear unsanctioned but the beneficial owner chain may include sanctioned individuals.

**DD approach:**

1. **Pull full UBO chain to natural persons.** Russian assets often have 5–8 intermediate vehicles (LLCs in Russia, Cyprus, BVI, Hong Kong, UAE) before reaching natural persons.
2. **Screen each layer** against OFAC, EU, UK consolidated lists (legal counsel job, but Anton can flag candidates).
3. **Time-of-acquisition test** — does any UBO have sanctions history pre-2022? If they were sanctioned and "sold" the asset in 2022–2023, was it a real divestment or paper transfer to family/proxy?
4. **Control test** — does any sanctioned person retain influence even without formal ownership (board seat, voting rights, key-management influence)?

**Red flags:**
- UBO chain "ends" at a Russian individual without OFAC/EU/UK match — but no independent verification
- 2022–2023 ownership reshuffle from sanctioned individual to spouse/sibling/employee
- Bearer shares in any intermediate vehicle
- Russian Federal Service / FSB-linked individuals in management even without ownership
- Cyprus or BVI vehicles with nominee directors

---

## 6. Supply chain and counterparty exposure

The asset itself may not be sanctioned. The counterparties may be. Key DD checks:

### 6.1 Equipment & technology suppliers
- Major OEMs (Siemens, ABB, Andritz, Outotec/Metso, FLSmidth, Hitachi, Komatsu, Caterpillar) — many have withdrawn from Russia formally. Continuing supply often through parallel imports / replacement OEMs (Chinese substitutes).
- Replacement Chinese suppliers: SUY Machinery, NHI, Citic Heavy Industries, Sinosteel — quality variable, support model different.
- DD test: pull equipment list, identify suppliers, check withdrawal status. Spare parts continuity is a real risk.

### 6.2 Off-takers
- Metal sales contracts: who buys, where do they pay (which jurisdiction's bank), which currency?
- Many post-2022 contracts use Chinese, Indian, Turkish, UAE counterparties with non-USD settlement.
- DD test: pull off-take agreements (or summaries if NDA-protected). Identify chain to ultimate buyer. Pricing benchmark used.

### 6.3 Finance & insurance
- Project finance lenders — any Western bank? Likely no. ECA backing? Likely no.
- Replacement structures: Chinese banks (CDB, ICBC, EXIM China), Russian banks (Sber, VTB, Gazprombank — themselves SDN/sanctioned), Eurasian Development Bank.
- Insurance: Western P&C and marine insurance largely withdrawn from Russian risk. Replacement: Russian state-backed insurers, Chinese insurers, captive insurance.

### 6.4 Logistics
- Western shipping companies (Maersk, MSC, CMA-CGM) largely withdrawn. Russian and Chinese carriers replacing.
- Western ports: discharge of Russian-origin cargo restricted or refused. Alternative routes via Türkiye, UAE, India.

---

## 7. Russia-specific operational realities

### 7.1 Currency

- Ruble is non-convertible internationally for most counterparties
- USD payments via Russian banks heavily restricted
- Replacement: CNY, INR, AED, TRY corridors
- Currency exposure on CapEx (often Euro/USD denominated equipment) vs. ruble revenue (domestic sales) or yuan/rupee revenue (export) — material risk
- DD impact: financial model must stress-test under multi-currency scenarios

### 7.2 Banking

- Russian access to SWIFT restricted for major banks (selectively)
- Replacement: SPFS (Russian SWIFT alternative), CIPS (Chinese), bilateral correspondent arrangements
- For Western counterparty, payment routing to Russia is operationally painful even when legally permitted
- DD impact: any contract requiring Western-bank settlement is at risk

### 7.3 Parallel imports

- Russian government legalised "parallel imports" of certain Western goods (no need for trademark holder consent)
- For mining equipment, spares, this allows continuing supply via Türkiye, UAE, Kazakhstan, China
- Cost is 30–50% higher than direct supply (intermediaries, longer logistics)
- Quality and warranty risk
- DD impact: spare parts and replacement equipment OpEx materially higher than pre-2022 baseline

### 7.4 Talent

- Some Western-trained engineers and managers left Russia 2022–2024
- Russian engineering schools producing well — Moscow Institute of Steel and Alloys, Ural Federal University, Tomsk Polytechnic — but some loss of international experience
- DD impact: project execution capability on complex Western-technology projects may be reduced

---

## 8. Specific commodity-jurisdiction matrix

| Commodity | EU import status (2026 baseline — verify) | US import status (verify) | LME / LBMA | Self-sanctioning |
|-----------|------------------------------------|----------------------|------------|------------------|
| Primary aluminium (unwrought) | EU ban under 14th package (verify) | Tariffs and restrictions | LME post-April 2024 not good delivery | High |
| Aluminium semis (sheet, foil, extrusion) | Restrictions by HS code | Varies | n/a | Medium-high |
| Copper cathode | Restricted, varies by package | Restricted | LME post-April 2024 not good delivery | High |
| Refined nickel (Class 1) | Restricted | Restricted | LME post-April 2024 not good delivery | High |
| Nickel matte / intermediates | Less restricted historically | Verify | n/a | Medium |
| Palladium | Strategic exemption tendencies | Tariff varies | LBMA refiners delisted | Medium |
| Platinum | Strategic exemption tendencies | Tariff varies | LBMA refiners delisted | Medium |
| Gold doré / bullion | Banned | Banned | LBMA refiners delisted | Very high |
| Iron / steel | Extensive HS-code restrictions | Tariff | n/a | Very high |
| Coking coal | Restrictions | Restrictions | n/a | High |
| Uranium | EU and US restrictions evolving | Restrictions in process | n/a | High |
| Diamonds | EU/G7 ban with origin tracking | G7 ban | n/a | Very high |

**Critical:** Always verify current status via primary sources before scoping DD:
- OFAC: https://ofac.treasury.gov
- EU: https://www.sanctionsmap.eu and Official Journal
- UK OFSI: gov.uk consolidated list
- LME notices
- LBMA Good Delivery list

---

## 9. CIS-specific notes

### 9.1 Kazakhstan

- Generally not sanctioned. Strategic partner of both Russia and West.
- Has become significant transit and processing jurisdiction (parallel imports, gold refining, metals trading)
- Major mining: KAZ Minerals (Cu), Kazakhmys (Cu), KazZinc (Zn-Pb-Au-Ag), ENRC successors (Cr, Al, Cu), Kazakhmys Smelting
- Compliance question: extent to which Kazakh-origin metals contain or commingle Russian-origin metals (sanction circumvention risk)
- Western banks have increased scrutiny on Kazakh metal trade — DD should expect this

### 9.2 Uzbekistan

- Generally not sanctioned. Major Au, Cu, U producer (Almalyk, Navoi)
- Increasing Western engagement post-Karimov era
- Lower sanctions complexity than Russia

### 9.3 Mongolia

- Not sanctioned. Oyu Tolgoi (Rio Tinto), Erdenet (joint with Russia)
- Erdenet specifically: Russian state ownership — potential exposure

### 9.4 Belarus

- Sanctioned in parallel with Russia under several Western regimes
- Belaruskali (potash), but mining/metals exposure limited
- Treat similarly to Russia in DD

### 9.5 Tajikistan, Kyrgyzstan, Turkmenistan

- Generally not sanctioned but compliance complexity from Chinese, Russian, Iranian linkages
- Specific assets: Talco (Tajikistan aluminium), Kumtor (Kyrgyzstan gold), various Au/Cu projects

---

## 10. Practical DD workflow with sanctions exposure

### 10.1 Pre-engagement
- Identify all jurisdiction touch-points (asset location, UBO, customers, suppliers, banks, advisors)
- Flag to client: "This engagement has sanctions complexity. Confirm specialist counsel is engaged."
- Confirm Anton's role boundary in writing: technical DD, not compliance advice

### 10.2 During DD
- Map ownership, supply chain, off-take chain — surface facts, do not screen
- Use public sanctions databases for awareness, not for screening (screening is legal counsel job)
- Flag any pattern suggesting sanctions evasion (recent shell company in chain, payment routing through unusual jurisdictions, equipment supply from sanctions-listed entity)

### 10.3 In DD report
- Use standard compliance note (§2 above)
- State factual ownership, counterparty, equipment, off-take chains as identified
- Flag risks as "potential sanctions exposure to be confirmed by counsel" — never make compliance statement

### 10.4 Post-DD
- Be willing to walk away from any engagement where compliance counsel finds material exposure
- Document the walk-away — protects Anton's record

---

## 11. DD red flags specifically related to sanctions

- Sudden ownership restructuring in 2022–2023 without economic logic (paper transfer)
- Off-take contracts with new (post-2022) counterparties in UAE, Türkiye, Hong Kong, with no track record
- Banking through small obscure banks (not majors) — sanctions evasion routing
- Payment in cryptocurrency or non-conventional instruments
- Documentation gaps in shipping (BL marked "various ports" without specific consignee)
- Equipment suppliers replaced 2022–2023 without quality validation
- "Customer of last resort" pricing (deep discount to spot — distress signal or evasion routing)
- Refusal to disclose end-customer identity

---

## 12. Quick reference — primary sources

- **OFAC SDN search**: https://sanctionssearch.ofac.treas.gov
- **EU sanctions map**: https://www.sanctionsmap.eu
- **EU consolidated list**: https://www.consilium.europa.eu/en/policies/sanctions/
- **UK OFSI**: https://www.gov.uk/government/organisations/office-of-financial-sanctions-implementation
- **Canada SEMA**: https://www.international.gc.ca
- **Australia DFAT**: https://www.dfat.gov.au
- **LME notices**: https://www.lme.com/en/News
- **LBMA Good Delivery**: https://www.lbma.org.uk/good-delivery
- **OpenCorporates** (UBO research): https://opencorporates.com
- **OCCRP Aleph** (investigative data): https://aleph.occrp.org

---

## TODO_ANTON consolidated

1. Specific recent transactions Anton has heard of where sanctions structuring was the deal driver — anonymized
2. List of Russian/CIS assets currently being marketed to Western buyers in 2026 — landscape view
3. Specific Chinese equipment suppliers known to substitute Western OEMs in CIS mining (with quality observations)
4. Payment routing structures Anton has observed for Russian metal sales to non-Western buyers
5. Specific jurisdictions/banks Anton sees being used for CIS metal trade settlement
