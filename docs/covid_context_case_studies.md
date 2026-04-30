# COVID Case Studies: Empirical Grounding for Fair Contextual Bandits

**Project:** Fair Contextual Bandits for Equitable Diagnostic Decision-Making Under Missing Context  
**Course:** DSCI 601 – Applied Data Science I (Spring 2026)  
**Author:** Piter Z. Garcia Bautista  
**Last updated:** 2026-04-30

---

## Purpose

This document anchors the two core claims of the DSCI601/602 research project in real, reputable
empirical evidence.  Both claims map directly onto the project's central research question:

> *When does informative context — and how it is modeled — materially reduce disparity and error in
> sequential decision-making under distribution shift?*

**Claim 1 — Inefficient routing due to missing / ignored context.**  
COVID-19 test resources were distributed without adequately incorporating risk context (who was most
vulnerable), resulting in a systematic mismatch between test access and community need that harmed
minority and high-SVI populations.

**Claim 2 — Unreliable diagnostics due to missing group context at evaluation time.**  
A key COVID-19 triage diagnostic (pulse oximetry) was calibrated and validated without sufficient
representation of darker-skinned patients, producing systematically biased readings and delayed or
denied care for Black, Hispanic, and Asian patients.

Both failures are instances of the same problem: *the decision system lacked or ignored informative
context about affected subgroups*, producing both performance harm and fairness harm.  A
contextual-bandit framework that explicitly models and constraints group-level disparities is a
principled solution for both.

---

## Case Study 1 – Inequitable COVID-19 Test Allocation

### 1.1 Background and Evidence

Early in the U.S. COVID-19 pandemic (March–May 2020), testing resources — sites, kits, and mobile
units — were severely constrained.  The key policy question was *where* to place them.  The
allocation that actually occurred failed to account for the most informative contextual signals:

| Contextual signal ignored | Source evidence |
|---|---|
| Hispanic communities had disproportionately high case and death burden | Bilal et al. (2021), *Social Science & Medicine* |
| Low-SVI and affluent ZIP codes received test sites at higher rates | Escobar et al. (2021), PMC |
| Black communities faced higher exposure risk and healthcare barriers | CDC MMWR 70(11), 2021 |
| Long-term care / Medicaid facilities had near-zero early test access | Landes et al. (2020), *Journal of Aging & Social Policy* |

**Key quantitative finding (Bilal et al. 2021):**  
On 7 May 2020, newly announced U.S. COVID-19 testing sites were placed in ZIP codes with a
*higher* White population share and *lower* Hispanic population share than would be expected under
a burden-proportional or random-within-county allocation.  For every 1 percentage-point increase in
the underrepresentation of Hispanic residents in testing-site ZIP codes, the Hispanic share of
COVID-19 deaths in subsequent weeks was approximately **1.04 percentage points higher** than
expected.

This is a direct, quantifiable link between missing context (risk-adjusted need by race/ethnicity)
at the allocation stage and downstream mortality disparities.

**Massachusetts multi-community study (Escobar et al. 2021):**  
Testing was characterized as *"inequitable and misaligned with community need"*, with more
accessible testing concentrated in affluent, predominantly White neighborhoods, despite higher
exposure, positivity, and social vulnerability in diverse, low-income areas.

### 1.2 Affected Groups

| Group | How they were harmed | Evidence |
|---|---|---|
| Hispanic communities | Underrepresented in ZIP codes with testing sites; higher subsequent mortality | Bilal et al. (2021) |
| Black communities | Higher exposure + barriers; delayed access during critical early weeks | CDC MMWR (2021); Escobar et al. (2021) |
| High-SVI / low-income communities | Fewer test sites, less mobile-unit coverage, even with higher positivity rates | Escobar et al. (2021) |
| Long-term care / elderly residents | Testing prioritized for hospitals and first responders; SNFs left behind | Landes et al. (2020) |

### 1.3 Bandit Framing (Graph 1 – Real-World Network; Graph 2 – Fair Routing)

#### Environment setup

Each **community node** (county or ZIP code) is associated with a context vector
\(\mathbf{x}_t \in \mathbb{R}^d\) built from publicly available data:

| Feature | Source |
|---|---|
| `cases_per_100k`, `deaths_per_100k` | CDC Health Disparities Dashboard |
| `positivity_rate` | HHS Community Profile (historical) |
| `percent_hispanic`, `percent_black`, `percent_white` | U.S. Census |
| `svi_score` (0–1 Social Vulnerability Index) | CDC SVI |
| `percent_over_65`, `poverty_rate`, `crowding_index` | ACS / Census |
| `essential_worker_share` | BLS / Census occupation proxies |

Each **arm** \(a \in \{0, 1, 2, 3\}\) represents a discrete level of testing resource allocation
(e.g., 0 = no mobile unit, 1 = minimal, 2 = moderate, 3 = prioritized deployment).  Total budget
is constrained across communities per round.

**Reward:** reduction in undetected infections or deaths-averted proxy, combining:
- `tests_allocated × risk_index_t` (proportional to SVI and burden),
- minus a penalty for undetected infections in high-burden communities.

**Fairness metrics:**
- Tests per 1,000 residents, disaggregated by majority race/ethnicity group and SVI quartile.
- Positivity-adjusted access: tests per detected case, by group.
- Disparity ratio: ratio of tests-per-capita in highest-SVI quartile vs lowest-SVI quartile.

#### Policies to compare

| Policy | Description |
|---|---|
| Non-contextual baseline (ε-greedy / UCB) | Allocates to historically "easy" or already-monitored areas; reproduces real-world inequity |
| Contextual utility-only (LinUCB) | Uses context to maximize detected infections but ignores group fairness; can still under-serve noisy or under-measured groups |
| Fairness-aware iCMAB | LinUCB + penalty/constraint term that bounds group disparity in tests-per-capita or tests-per-case |

#### Graph specifications

**Graph 1 – Real-world inequitable network:**
- Nodes: communities (colored by majority race/ethnicity or SVI quartile; sized by COVID burden),
  and test site nodes (sized by capacity).
- Edges: weighted by testing capacity accessible per community under the *observed* early-pandemic
  allocation.
- Annotation: highlight which communities are underserved relative to their burden (edge color =
  under/over-served vs burden-proportional baseline).
- Data: derived from Bilal et al. (2021) tables + CDC health disparities aggregate data for 3–5
  representative states.

**Graph 2 – Bandit fair-routing counterfactual:**
- Side-by-side network: actual allocation vs iCMAB fair-routing output.
- Summary bar chart: tests per 1,000 people by race/ethnicity group under baseline vs fair policy,
  with disparity gap annotations.
- Time-series line chart: group-wise disparity metric over bandit rounds for all three policies.

### 1.4 Data Sources

| Dataset | URL / Reference | Notes |
|---|---|---|
| Bilal et al. (2021) racial/ethnic inequities in early test distribution | https://pmc.ncbi.nlm.nih.gov/articles/PMC8420583/ | Aggregate tables; manually extract per-state data |
| Escobar et al. (2021) testing inequities in underserved communities | https://pmc.ncbi.nlm.nih.gov/articles/PMC8987278/ | MA-focused; qualitative + some quantitative |
| CDC COVID-19 Health Disparities Dashboard | https://www.cdc.gov/nchs/nvss/vsrr/covid19/health_disparities.htm | Death counts by race/ethnicity |
| CDC MMWR 70(11) – racial/ethnic disparities by age and sex | https://www.cdc.gov/mmwr/volumes/70/wr/mm7011e1.htm | Incidence rates by group |
| CDC Social Vulnerability Index (SVI) | https://www.atsdr.cdc.gov/placeandhealth/svi/ | County/tract level SVI scores |

---

## Case Study 2 – Biased COVID-19 Diagnostics: Pulse Oximetry

### 2.1 Why Pulse Oximetry

While PCR and antigen tests drove case identification, **pulse oximeters** were the primary
*triage and monitoring* diagnostic used at home and in hospitals for COVID-19 patients throughout
2020–2022.  Oxygen saturation (SpO₂) thresholds directly determined:
- Whether a patient qualified for supplemental oxygen,
- Whether they were eligible for dexamethasone, remdesivir, or other COVID-19–specific therapies,
- Whether they were admitted or sent home.

Pulse oximeters were calibrated and evaluated without adequate representation of darker-skinned
individuals and without explicitly modelling the confounding effect of melanin on near-infrared
light absorption.  The result is a well-documented pattern of **systematic overestimation of oxygen
saturation** in Black, Hispanic, and some Asian patients — an artefact of missing group context
at the device design and regulatory evaluation stage.

This maps directly onto the DSCI601 project framing: the "diagnostic test" was built and deployed
without informative context about a key covariate (skin pigmentation / race), producing higher
false-negative rates (missed hypoxemia) and inequitable downstream care for minority groups.

### 2.2 Background and Evidence

| Study | Population | Key finding |
|---|---|---|
| Fawzy et al. (2022), *JAMA Internal Medicine* | COVID-19 inpatients, US academic centres | Pulse oximetry overestimated SaO₂ more in Black, Hispanic, and Asian patients; higher rates of occult hypoxemia; delayed recognition of therapy eligibility |
| Fawzy et al. (2023), *JAMA Network Open* | 24,504 patients with paired SpO₂ and SaO₂ | Overestimation in minority groups associated with delayed COVID therapies and increased readmission risk |
| Sjoding et al. (2020), *NEJM* | US ICU patients | Black patients ~3× more likely than White patients to have occult hypoxemia (SaO₂ < 88% while SpO₂ ≥ 92%) |
| Sutter Health / Gottlieb et al. (2022) | COVID inpatients | Bias could delay oxygen by ~4.5 hours and dexamethasone by ~37 min for Black patients |
| BMJ / VA general-care cohort (Valbuena et al. 2022) | VA inpatients 2013–2019 | Black patients: ~19–20% occult hypoxemia rate vs ~15–16% for White patients; mean SpO₂ overestimation ~1.7–1.8 pp higher in Black patients |
| VA Evidence Synthesis (2022) | Meta-analysis | Average overestimation ~1.5 pp higher in Black patients vs White patients across studies |

The root cause is consistently identified as: calibration populations were predominantly
light-skinned, and regulatory standards (ISO 80601-2-61) did not mandate adequate dark-skin
representation until after these devices were already ubiquitous.

### 2.3 Affected Groups

| Group | Primary harm | Mechanism |
|---|---|---|
| Black patients | Highest rates of occult hypoxemia; longest treatment delays | Melanin most strongly attenuates NIR signal; least represented in calibration |
| Hispanic patients | Elevated occult hypoxemia; delayed care | Intermediate melanin levels; also underrepresented in calibration studies |
| Asian patients | Elevated bias in some sub-groups and COVID cohorts | Heterogeneous; some sub-groups also underrepresented |
| White patients | Reference group; least biased SpO₂ readings | Predominantly represented in calibration |

The critical point for the DSCI601 narrative: **the context that was missing was race / skin
pigmentation at the device design stage**, and the result was differential false-negative rates
across groups — exactly the "subgroup error spike" that the fair contextual bandit framework is
designed to detect and mitigate.

### 2.4 Bandit Framing (Graph 3 – Bias Visualization; Graph 4 – Fair Decision Policy)

#### Environment setup

Each **patient encounter** is one round.  The agent must decide on a clinical action given an
observed context vector:

| Feature | Notes |
|---|---|
| `spo2_measured` | Pulse oximeter reading (potentially biased by race) |
| `respiratory_rate` | Direct severity indicator |
| `heart_rate`, `work_of_breathing` | Clinical severity markers |
| `race_ethnicity` | The "missing context" in the baseline device/policy |
| `comorbidities` (obesity, diabetes, COPD) | Modifies risk profile |

**Arms:**
- `treat_now` — initiate oxygen therapy / COVID-specific treatment,
- `watch_and_wait` — monitor with repeat SpO₂,
- `order_abg` — order confirmatory arterial blood gas (resource cost).

**Reward:**
Composite utility penalizing:
- occult hypoxemia events (SaO₂ < 88% while agent chose `watch_and_wait`),
- unnecessary ABGs (resource waste),
- delayed treatment beyond clinically appropriate window.

**Fairness metric:**  
Group-wise occult hypoxemia rate (GWOHR): for each race/ethnicity group \(g\),
\[
\text{GWOHR}_g = P(\text{occult hypoxemia not caught} \mid \text{group} = g)
\]
Fairness constraint: \(\max_g \text{GWOHR}_g - \min_g \text{GWOHR}_g \leq \epsilon\).

#### Policies to compare

| Policy | Description |
|---|---|
| Baseline (single SpO₂ threshold) | Act if SpO₂ < 92%; does not use race context; reproduces device-calibration bias in decisions |
| Calibrated group thresholds | Lower threshold for groups with documented overestimation (e.g., treat Black patients at SpO₂ < 94%); simple fairness fix |
| Contextual bandit (LinUCB) | Uses all context including race; maximizes utility; no explicit fairness constraint |
| Fair iCMAB | LinUCB + penalty on group-wise GWOHR disparity; maps directly to DSCI601 CMAB/iCMAB stack |

#### Graph specifications

**Graph 3a – Occult hypoxemia rates by race (bar chart):**
- X-axis: race/ethnicity (White, Black, Hispanic, Asian).
- Y-axis: occult hypoxemia rate (%) under each policy.
- Error bars from meta-analysis / multi-study ranges.
- Data sources: BMJ/VA cohort (Valbuena 2022), VA ESP meta-analysis, Fawzy JAMA cohorts.

**Graph 3b – Mean SpO₂ overestimation by race (bar chart with CI):**
- X-axis: race/ethnicity.
- Y-axis: mean bias = SpO₂ − SaO₂ (percentage points).
- Data: VA ESP pooled estimates + individual cohort values.
- Clearly annotate the "calibration gap": the difference between groups is the direct result of
  under-representation in calibration.

**Graph 4 – Fairness–utility trade-off curve:**
- X-axis: overall utility (correct / timely treatment decisions per 100 patients).
- Y-axis: group disparity in GWOHR (max − min across groups).
- Pareto frontier: baseline policy in upper-left (high disparity), fair iCMAB in lower-right
  (lower disparity, modest utility cost), utility-only LinUCB somewhere in between.

### 2.5 Data Sources

| Dataset | URL / Reference | Notes |
|---|---|---|
| Fawzy et al. (2022) — COVID inpatient cohort | https://pubmed.ncbi.nlm.nih.gov/35639368/ | Occult hypoxemia and therapy-delay data by race |
| Fawzy et al. (2023) — JAMA Network Open | https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2808735 | 24,504-patient paired SpO₂/SaO₂; outcomes by race |
| Valbuena et al. (2022) — BMJ / VA | https://www.bmj.com/lookup/doi/10.1136/bmj-2021-069775 | Occult hypoxemia rates by race in general inpatient care |
| VA ESP Report (2022) — meta-analysis | https://www.hsrd.research.va.gov/publications/esp/pulse-oximetry.pdf | Pooled bias estimates by race |
| Gottlieb et al. / Sutter Health (2022) | https://vitals.sutterhealth.org/study-uncovers-how-medical-device-bias-could-lead-to-5-hour-delays-in-covid-19-treatment-for-black-patients/ | Treatment delay quantification for Black COVID patients |
| Sjoding et al. (2020) — NEJM | https://www.nejm.org/doi/10.1056/NEJMc2029240 | Original occult hypoxemia racial disparity in ICU |
| Annals ATS review (2022) | https://academic.oup.com/annalsats/article/19/12/1951/8417773 | Evidence and implications of racial disparity in SpO₂ accuracy |

---

## Mapping Case Studies to the DSCI601 Framework

| Dimension | Case Study 1 (Test Allocation) | Case Study 2 (Diagnostic Bias) |
|---|---|---|
| **Core failure** | Routing ignored risk context (SVI, race, burden) | Device calibration ignored skin-tone context |
| **Groups most harmed** | Hispanic, Black, high-SVI communities | Black, Hispanic, some Asian patients |
| **"Missing context" type** | Epidemiological and demographic context missing from allocation policy | Biological / phenotypic context missing from device design + validation |
| **Bandit arm** | Allocation level of test resources to a community | Clinical action: treat, wait, or confirm via ABG |
| **Context vector \(\mathbf{x}\)** | Cases, SVI, race/ethnicity, poverty, crowding | SpO₂, severity, race/ethnicity, comorbidities |
| **Reward** | Infections detected / deaths averted | Correct, timely clinical decisions |
| **Fairness metric** | Tests per 1,000 by group; disparity ratio | Group-wise occult hypoxemia rate (GWOHR) |
| **Baseline policy** | Non-contextual or convenience-based allocation | Single SpO₂ threshold ignoring race bias |
| **Fair iCMAB policy** | Burden + vulnerability-weighted allocation with group constraints | Context-aware decision rule with GWOHR disparity penalty |
| **Key graph** | Network: communities ↔ test sites (real vs fair) | Bar: occult hypoxemia by race; trade-off curve |

---

## File and Code Scaffold (for DSCI601-workspace)

The following layout in `DSCI601-workspace` is recommended to match this documentation:

```
experiments/
  covid_test_allocation/
    env_test_allocation.py        # CovidTestAllocationEnv class
    run_bandits.py                # Runs baseline + fair policies, logs group metrics
    01_network_graph.ipynb        # Produces Graphs 1 and 2
  diagnostic_bias_pulseox/
    env_pulseox_decision.py       # Patient encounter simulator (group-specific bias params)
    run_bandits.py                # Runs baseline + fair policies, logs GWOHR
    01_bias_and_fairness_figures.ipynb  # Produces Graphs 3 and 4

data_sources/
  covid_context/
    test_allocation_context.csv   # Community context: SVI, race/eth, burden, baseline access
    pulseox_bias_summary.csv      # Group-wise mean bias and occult hypoxemia rates (from papers)

figures/
  covid_case_studies/
    test_allocation_network_real.png
    test_allocation_network_fair.png
    test_allocation_bars_by_group.png
    pulseox_occult_hypoxemia_by_race.png
    pulseox_mean_bias_by_race.png
    pulseox_fairness_utility_tradeoff.png
```

### `test_allocation_context.csv` — column schema

```
region_id, state, county_fips, population,
cases_per_100k, deaths_per_100k, positivity_rate,
percent_white, percent_black, percent_hispanic, percent_asian,
svi_score, percent_over_65, poverty_rate, crowding_index,
essential_worker_share,
baseline_tests_per_1000, baseline_test_sites
```

### `pulseox_bias_summary.csv` — column schema

```
study_id, race_ethnicity,
mean_bias_spo2_minus_sao2, bias_ci_lower, bias_ci_upper,
occult_hypoxemia_rate, ohx_ci_lower, ohx_ci_upper,
n_patients, population, source_doi
```

---

## References

1. Bilal, U. et al. (2021). Racial and ethnic inequities in the early distribution of U.S. COVID-19
   testing sites. *Social Science & Medicine*.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC8420583/

2. Escobar, G.J. et al. (2022). Addressing COVID-19 Testing Inequities Among Underserved
   Communities. *JAMA Network Open* / PMC.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC8987278/

3. CDC MMWR 70(11) (2021). Racial and Ethnic Disparities in COVID-19 Incidence by Age, Sex, and
   Period of Community Transmission. https://www.cdc.gov/mmwr/volumes/70/wr/mm7011e1.htm

4. CDC COVID-19 Provisional Counts — Health Disparities.
   https://www.cdc.gov/nchs/nvss/vsrr/covid19/health_disparities.htm

5. Landes, S.D. et al. (2020). Who Are the Most At-Risk Older Adults in the COVID-19 Era?
   *Journal of Aging & Social Policy*. https://doi.org/10.1080/08959420.2020.1764310

6. Sjoding, M.W. et al. (2020). Racial Bias in Pulse Oximetry Measurement. *NEJM*.
   https://www.nejm.org/doi/10.1056/NEJMc2029240

7. Fawzy, A. et al. (2022). Racial and Ethnic Discrepancy in Pulse Oximetry and Delayed
   Identification of Treatment Eligibility Among Patients with COVID-19. *JAMA Internal Medicine*.
   https://pubmed.ncbi.nlm.nih.gov/35639368/

8. Fawzy, A. et al. (2023). Clinical Outcomes Associated With Overestimation of Oxygen Saturation
   by Pulse Oximetry. *JAMA Network Open*.
   https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2808735

9. Valbuena, V.S.M. et al. (2022). Racial Bias and Reproducibility in Pulse Oximetry Among Medical
   and Surgical Inpatients in General Care in the VA, 2013–2019. *BMJ*.
   https://www.bmj.com/lookup/doi/10.1136/bmj-2021-069775

10. VA ESP (2022). Differential Pulse Oximeter Accuracy, Occult Hypoxemia Prevalence, and Clinical
    Outcomes by Race/Ethnicity. VA Evidence Synthesis Program.
    https://www.hsrd.research.va.gov/publications/esp/pulse-oximetry.pdf

11. Gottlieb, E.R. et al. (2022). Assessment of Racial and Ethnic Differences in Oxygen
    Supplementation Among Patients in the ICU. *Annals of Internal Medicine*.
    https://vitals.sutterhealth.org/study-uncovers-how-medical-device-bias-could-lead-to-5-hour-delays-in-covid-19-treatment-for-black-patients/

12. Lutchmansingh, D.D. et al. (2022). Racial Disparity in Oxygen Saturation Measurements by Pulse
    Oximetry: Evidence and Implications. *Annals of ATS*.
    https://academic.oup.com/annalsats/article/19/12/1951/8417773

13. García Bautista, P.Z. (2026). Fair Contextual Bandits for Equitable Diagnostic Decision-Making
    Under Missing Context. DSCI601 Project Proposal, RIT.
