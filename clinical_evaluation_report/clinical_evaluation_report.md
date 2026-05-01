# Clinical Evaluation Report: Context-Aware Routing and Diagnostic Bias in COVID-19

*DSCI 601 – Foundations of Data Science*  
*Author: Piter Garcia*  
*Repos: `DSCI601-workspace`, `DSCI601-Project_Proposal`*

---

## 1. Motivation and Scope

This report establishes the **clinical evaluation foundation** for our broader DSCI 601 project on context-aware, fair routing of scarce resources across both classical and quantum settings.[cite:130][cite:133] We focus on the healthcare side, where the "routed" resources are tests, diagnostic attention, and treatment decisions under uncertainty. Our core claim is that:

> **When contextual information about risk and vulnerability is missing, mis-specified, or unequally reliable across groups, sequential allocation mechanisms (including bandits) systematically reinforce inequities instead of reducing them.**[cite:133]

We validate this claim using two concrete COVID-19 case studies drawn from reputable epidemiologic and clinical literature:

1. **Inequitable COVID-19 test allocation** (routing failure): test sites and capacity were placed in ways that ignored known vulnerability context, particularly for Hispanic, Black, and high–social-vulnerability communities.
2. **Racial bias in pulse oximetry** (diagnostic failure): a widely used COVID triage device systematically overestimated oxygen saturation in darker-skinned patients due to underrepresentation in calibration, leading to delayed treatment and worse outcomes.

For each case, we:

- Summarize the **empirical evidence** from peer-reviewed sources.
- Map the problem into our **Clinical Bandit Environment** and **EQUITAS-mediated fair allocation** framework implemented under `Evaluation_Framework/` in `DSCI601-workspace`.[cite:133]
- Define the **confusion matrices and metrics** that our evaluation pipeline should log (per group and per policy) to reproduce and extend these analyses.

This document is intended to be a **standalone, clinical-side root** of the project: methodologically complete, clearly cited, and ready to be connected to the quantum-routing half of the work.

---

## 2. Background: Clinical Environment, Bandits, and EQUITAS

### 2.1 Clinical Bandit Environment in DSCI601-workspace

Our `Evaluation_Framework` submodule defines a generic **experiment runner** that reads configuration files, instantiates environments and policies, and logs structured results for comparison and fairness auditing.[cite:133][cite:134] In the clinical setting, we interpret this as:

- **Environment** `E`: generates context vectors \(x_t\) representing patients or communities, underlying (latent) risk \(y_t\), and ground-truth outcomes when available.
- **Policy** \(\pi_\theta\): a contextual bandit or constrained bandit that selects an action \(a_t\) given context and historical feedback.
- **Reward** \(r_t\): a scalar function of outcomes (e.g., infections detected, hypoxemia avoided, deaths averted) and possibly fairness penalties.
- **Logging and evaluation**: for each time step and group, we track decisions, outcomes, and fairness metrics.

In `Evaluation_Framework/experiments/src`, the modules `pipeline.py` and `stages.py` orchestrate this experimental flow: loading configs, running multiple policies over the same environment, and producing standardized outputs (CSV logs, metric summaries). Our clinical report is designed to slot directly into this framework by specifying *what* to log and *how* to interpret it for the two COVID case studies.[cite:135]

### 2.2 EQUITAS Mediation and Fairness Constraints

Our fairness approach follows the spirit of the EQUITAS framework: instead of treating fairness as an afterthought, we model it as a **mediation layer** that constrains or re-weights bandit policies to keep group-level disparities within specified budgets.

In abstract form, let groups \(g \in G\) (e.g., racial/ethnic groups, SVI strata), and let \(M_g(t)\) be some group-level metric at time \(t\) (e.g., tests per 1,000 people, missed hypoxemia probability). EQUITAS enforces:

\[
\bigl| M_g(t) - M_{g'}(t) \bigr| \leq \delta, \quad \forall g, g' \in G,\; \forall t,\tag{1}
\]

for some fairness budget \(\delta\). In our implementation, this appears as:

- **Penalty terms** in the reward used by the bandit (soft constraints).
- **Hard constraints** in allowable actions or in post-hoc re-weighting of logged decisions.

The evaluation goal is to show that **fairness-aware policies** can substantially reduce clinically relevant disparities with acceptable (and often small) utility cost, relative to baseline policies that ignore group-dependent context.

---

## 3. Case Study 1 – Inequitable COVID-19 Test Allocation

### 3.1 Epidemiologic and Policy Context

In early 2020, the United States ramped up PCR testing capacity under extreme resource scarcity. Public health agencies knew, by April 2020, that **Hispanic/Latino and Black/African American communities were at far higher risk** of infection, hospitalization, and death, driven by structural factors such as essential-worker roles, crowded housing, and reduced access to remote work and healthcare.[cite:23]

Despite this, several analyses have shown that **test site placement and test access were misaligned with this vulnerability context**:

- A national analysis of 7,392 COVID-19 testing sites (50 states, early May 2020) found that **ZIP codes with test sites had higher median income and a larger share of White, non-Hispanic residents** than ZIP codes without sites, even within the same counties.[cite:17]
- In that dataset, ZIP codes hosting test sites had, on average, **a smaller proportion of Hispanic residents than ZIP codes without test sites**, indicating underrepresentation of Hispanic communities in the testing network.[cite:17]
- The same work showed that a 1-percentage-point increase in underrepresentation of Hispanic residents in testing ZIP codes was associated with approximately **1.04 percentage points higher Hispanic share of COVID-19 deaths** later on, suggesting a link between routing inequity and mortality.[cite:17]
- A Massachusetts multi-community assessment reported that in cities such as Chelsea (majority Hispanic, low income), **test positivity rates reached over 40%**, yet tests per capita remained lower than in nearby wealthier, predominantly White communities with much lower positivity.[cite:18]
- CDC summary data from mid-2020 documented that **age-adjusted hospitalization rates** for COVID-19 were ~4.6× higher for Hispanic/Latino persons and ~4.7× higher for Black persons than for White, non-Hispanic persons — precisely the groups that received fewer test sites and lower per-capita testing in early rollouts.[cite:29]

These findings collectively support the claim that **test site routing ignored critical population context** (race/ethnicity, SVI, occupation) and instead followed convenience and existing infrastructure. Our bandit-based framework offers a principled way to demonstrate how this misalignment appears structurally and how a context-aware policy could have performed better.

### 3.2 Network Graph of the Deployed Test Network

Empirically, test sites form a **bipartite network** between testing facilities and communities. Even without PHI, this structure can be inferred from published site lists (addresses), census data, and county-level case/death counts.[cite:17][cite:18]

We define:

- **Facility nodes** \(S_j\): hospitals, drive-through test sites, community clinics, and mobile units. Each has an estimated daily capacity \(C_j\).
- **Community nodes** \(C_i\): ZIP codes or counties. Each has attributes:
  - Demographics: \(\%\text{Hispanic}_i, \%\text{Black}_i, \%\text{White}_i\).
  - Vulnerability: CDC Social Vulnerability Index (SVI), poverty rate, crowding, essential worker share.
  - COVID burden: case rate and death rate per 100,000 over a defined window.
- **Edges** \(S_j \to C_i\): represent the capacity share of facility \(j\) effectively accessible to community \(i\). Edge weights can be approximated using distance/travel time and service areas.

A **network visualization** based on representative metro areas (e.g., NYC boroughs, Cook County IL, Los Angeles County) reveals the following pattern:[cite:17][cite:18]

- Large hospital hubs (high \(C_j\)) have **thick edges to low-SVI, majority-White communities** with lower case and death rates.
- High-SVI, majority-Hispanic or majority-Black communities with very high burden (e.g., >2,500 cases per 100k) often connect via **thin edges**, frequently from small clinics or mobile units with much lower \(C_j\).
- Some high-burden communities have **no edge** to a facility within a reasonable travel radius (testing deserts).

Although exact numeric edge weights require geospatial computation, the published reports are sufficient to support a qualitative picture: the **capacity-weighted degree of the network is skewed toward communities that were already better off**.[cite:17][cite:18]

### 3.3 Bandit Formulation and Fair Routing Counterfactual

We model test allocation as a **contextual bandit problem** at the community level.

#### 3.3.1 Context Vector and Arms

For each community \(C_i\) at decision round \(t\), we define a context vector:

\[
x_{i,t} = [\text{SVI}_i,\ \text{case\_rate}_{i,t},\ \text{positivity}_{i,t},\ \%\text{Hispanic}_i,\ \%\text{Black}_i,\ \%\text{essential\_worker}_i].\tag{2}
\]

Actions (arms) represent **allocation tiers** of testing capacity to each community per planning period (e.g., day or week):

\[
A = \{\text{none},\ \text{low},\ \text{medium},\ \text{high}\}.\tag{3}
\]

A baseline policy \(\pi_0\) might be non-contextual (e.g., proportional to population size only) or might use only a subset of context (e.g., case rate, but not SVI or race). A fairness-aware policy \(\pi_F\) uses the full \(x_{i,t}\) and a fairness-aware objective.

#### 3.3.2 Reward and Fairness Term

The reward for community \(i\) at time \(t\) under allocation \(a_{i,t}\) can be defined as:

\[
r_{i,t} = \alpha \cdot \text{detected\_infections}_{i,t} - \beta \cdot \text{missed\_infections}_{i,t},\tag{4}
\]

where missed infections are estimated from positivity rate and an assumed underlying infection rate. The fairness-aware policy extends this to include a penalty on group-level allocation disparities:

\[
R_t = \sum_i r_{i,t} - \lambda \cdot \text{GroupDisparity}_t,\tag{5}
\]

with

\[
\text{GroupDisparity}_t = \max_g \left(\frac{\text{tests\_per\_1000}_{g,t}}{\text{burden\_index}_{g,t}}\right) - \min_g \left(\frac{\text{tests\_per\_1000}_{g,t}}{\text{burden\_index}_{g,t}}\right),\tag{6}
\]

where \(g\) indexes racial/ethnic or SVI-based groups.[cite:17][cite:18]

Under this objective, **Hispanic and Black communities with high burden and high SVI become high-reward targets for allocation**, and the fairness term prevents the policy from starving them relative to low-SVI, lower-burden communities.

#### 3.3.3 Confusion Matrices for Allocation Decisions

To evaluate policies, we define a per-group **allocation confusion matrix** that treats the decision "did this high-risk community receive adequate testing?" as a binary classification problem.

For each group \(g\) and each time window, we label communities as:

- **Positive**: high burden & high vulnerability (e.g., top quantile of \(\text{burden\_index}_{g}\)).
- **Negative**: lower burden or lower vulnerability.

We then define, for policy \(\pi\):

- **True Positive (TP\_g)**: high-risk community in group \(g\) that receives **high or medium** testing allocation.
- **False Negative (FN\_g)**: high-risk community in group \(g\) that receives **low or no** testing allocation.
- **False Positive (FP\_g)**: low-risk community in group \(g\) that receives high/medium allocation.
- **True Negative (TN\_g)**: low-risk community in group \(g\) that receives low/no allocation.

The confusion matrix for group \(g\) is then:

|               | Predicted Adequate (High/Med) | Predicted Inadequate (Low/None) |
|---------------|--------------------------------|----------------------------------|
| **Actual High-Risk**   | TP\_g                        | FN\_g                           |
| **Actual Low-Risk**    | FP\_g                        | TN\_g                           |

Key derived metrics:

- **Sensitivity (recall) for high-risk communities**: \(\text{TPR}_g = \frac{\text{TP\_g}}{\text{TP\_g} + \text{FN\_g}}\).
- **Specificity**: \(\text{TNR}_g = \frac{\text{TN\_g}}{\text{TN\_g} + \text{FP\_g}}\).
- **High-risk false negative rate** (most clinically important): \(\text{FNR}_g = 1 - \text{TPR}_g\).

Our expectation, based on Rodriguez et al. and related studies, is that **baseline policies have much higher \(\text{FNR}_g\) for Hispanic and Black communities than for White communities**, whereas fairness-aware bandit policies can reduce these gaps significantly.[cite:17][cite:18][cite:29]

By logging counts \(\text{TP\_g}, \text{FP\_g}, \text{FN\_g}, \text{TN\_g}\) in the evaluation pipeline, we can compute these metrics and quantify improvements from fair routing.

---

## 4. Case Study 2 – Racial Bias in Pulse Oximetry and COVID-19 Treatment

### 4.1 Device Bias and Under-Representation in Calibration

Pulse oximeters measure peripheral oxygen saturation (SpO₂) by passing red and infrared light through tissue and computing absorption ratios. Melanin absorbs light in both wavelength bands, which can systematically bias readings in darker skin tones. Multiple studies have demonstrated that pulse oximeters **overestimate true arterial oxygen saturation (SaO₂)** more often in Black, Asian, and Hispanic patients than in White patients, especially in the clinically critical range.[cite:38][cite:49]

Key empirical findings during the COVID-19 era:

- **Sjoding et al., NEJM 2020** analyzed 10,789 patients with paired SpO₂ and SaO₂ measurements at the University of Michigan. They found that **occult hypoxemia** (SaO₂ < 88% despite SpO₂ ≥ 92%) occurred in **~11.7% of Black patients vs. ~3.6% of White patients**.[cite:35]
- **Fawzy et al., JAMA Internal Medicine 2022** evaluated 3,069 hospitalized COVID-19 patients across multiple hospitals. Occult hypoxemia occurred in **29.0% of Black patients vs. 16.7% of White patients**, and Black patients with occult hypoxemia were less likely to receive supplemental oxygen within 4 hours.[cite:50]
- **Fawzy et al., JAMA Network Open 2023** expanded this to 24,504 patients at four health systems. Overestimation of oxygen saturation was more frequent in Black, Asian, and Hispanic patients, and was associated with delayed COVID-specific therapy and a **higher risk of hospital readmission (OR ~1.31 for those with undetected hypoxemia)**.[cite:33]
- A **VA Evidence Synthesis Program meta-analysis** pooled 21 studies and found that, on average, SpO₂ overestimated SaO₂ by about **+1.7 percentage points in Black patients vs. +0.5 percentage points in White patients**, with Asian and Hispanic patients in between.[cite:52]

These biases are not random; they are the consequence of **device calibration studies that enrolled predominantly White subjects** and regulatory standards that historically did not require stratified performance data by race or skin tone.[cite:38][cite:49] In our framework, this is a textbook example of **missing or mis-modeled context**: the function linking the measurement (SpO₂) to the latent state (true oxygenation) depends on skin tone, but the model was built as if it did not.

### 4.2 Clinical Consequences for COVID-19

During the COVID-19 pandemic, pulse oximetry became central to triage and treatment decisions:

- Home monitoring programs and telehealth visits used **SpO₂ thresholds** (often 92% or 94%) to decide whether patients required hospital evaluation.
- Hospital protocols used SpO₂ values to determine eligibility for **supplemental oxygen, dexamethasone, remdesivir, and other therapies**.

Given the evidence above, this created a systematic disparity:

- A Black or Hispanic COVID-19 patient with true SaO₂ < 88% was **more likely to have SpO₂ ≥ 92%** than a White patient in the same physiological state, causing them to be classified as "stable" rather than hypoxemic.[cite:35][cite:50][cite:52]
- Studies from integrated health systems (e.g., Sutter Health) estimate that device bias led to **delays of ~4.5 hours in supplemental oxygen** and **~37 minutes in dexamethasone initiation** for Black patients compared to counterfactual race-neutral measurements, with downstream increases in admission and readmission risk.[cite:47][cite:53]

This is a form of **group-dependent measurement error**: the observed feature (SpO₂) is a biased proxy for the latent state (oxygenation), with bias \(b_g\) depending on group \(g\). Standard threshold policies that ignore \(b_g\) produce **higher missed-hypoxemia rates** for some groups than others — a diagnostic failure that our evaluation framework can quantify and that fairness-aware policies can mitigate.

### 4.3 Confusion Matrices for Hypoxemia Detection

We treat hypoxemia detection as a **binary classification** task driven by SpO₂-based decision rules.

For each group \(g\), we define:

- **Actual Positive**: true hypoxemia, SaO₂ < 88%.
- **Actual Negative**: SaO₂ ≥ 88%.
- **Predicted Positive**: decision to treat as hypoxemic (e.g., escalate care, start oxygen) based on SpO₂ and other features.
- **Predicted Negative**: decision not to treat as hypoxemic.

Under a baseline single-threshold policy (e.g., escalate if SpO₂ < 92%):

- **True Positive (TP\_g)**: hypoxemic patient in group \(g\) with SpO₂ below threshold who receives escalation.
- **False Negative (FN\_g)**: hypoxemic patient in group \(g\) whose SpO₂ is at or above the threshold and who is not escalated.
- **False Positive (FP\_g)**: non-hypoxemic patient escalated based on low SpO₂.
- **True Negative (TN\_g)**: non-hypoxemic patient correctly not escalated.

The confusion matrix for group \(g\) is:

|               | Predicted Hypoxemic (Escalate) | Predicted Non-Hypoxemic (No Escalation) |
|---------------|---------------------------------|------------------------------------------|
| **Actual Hypoxemic**   | TP\_g                           | FN\_g                                     |
| **Actual Non-Hypoxemic** | FP\_g                           | TN\_g                                     |

Key metrics (to be logged per-group in the evaluation framework):

- **Missed hypoxemia rate (FNR)**: \(\text{FNR}_g = \frac{\text{FN\_g}}{\text{TP\_g} + \text{FN\_g}}\) — central fairness concern.
- **Sensitivity (recall)**: \(\text{TPR}_g = 1 - \text{FNR}_g\).
- **Positive predictive value (PPV)**: \(\text{PPV}_g = \frac{\text{TP\_g}}{\text{TP\_g} + \text{FP\_g}}\).

Empirically, Sjoding et al. and Fawzy et al. show that **\(\text{FNR}_g\) is 2–3× higher in Black patients than in White patients under baseline policies**, which matches the elevated occult hypoxemia rates in their cohorts.[cite:35][cite:50][cite:33][cite:52]

### 4.4 Bandit/EQUITAS Corrections: Contextual Policies for Hypoxemia

We now reframe hypoxemia detection as a **contextual decision problem**:

- **Context** \(x_p\) for patient \(p\):

  \[
  x_p = [\text{SpO}_{2,p},\ \text{resp\_rate}_p,\ \text{work\_of\_breathing}_p,\ g_p,\ \text{skin\_tone\_proxy}_p,\ \text{comorbidity\_index}_p].\tag{7}
  \]

- **Actions**: \(a \in \{\text{observe only},\ \text{order ABG},\ \text{escalate care}\}\).
- **Reward**: balances early detection of hypoxemia (benefit) vs. unnecessary interventions and ABG draws (cost).

A fairness-aware bandit policy \(\pi_F\) explicitly models **group-dependent SpO₂ bias** (e.g., via calibration functions or group-specific thresholds) and incorporates an EQUITAS-style constraint on missed-hypoxemia disparities:

\[
\left| P_\pi(\text{missed hypoxemia} \mid g = g_1) - P_\pi(\text{missed hypoxemia} \mid g = g_2) \right| \leq \epsilon,\tag{8}
\]

for all pairs \(g_1, g_2\). In practice, this means:

- Lowering effective SpO₂ thresholds for groups with higher overestimation bias (e.g., treating Black patients with SpO₂ 93–94% as higher risk than White patients at the same SpO₂).[cite:52]
- Allocating more ABG confirmations in the ambiguous SpO₂ range for groups with known bias.

In the evaluation pipeline, we can compare:

- **Baseline policy**: single threshold, group-agnostic.
- **Fair contextual policy**: group-aware thresholds or calibrated posterior risk estimates.

By logging confusion matrices and derived metrics for each policy and group, we can quantify how much **\(\text{FNR}_g\) gap closes** under fairness-aware policies and what cost, if any, appears in \(\text{FP\_g}\) or resource use (ABGs ordered).

---

## 5. Integrated Evaluation Design and Confusion Matrices

### 5.1 Logging Schema in Evaluation_Framework

To make the above analyses executable within `Evaluation_Framework`, we recommend extending the experimental logging schema with the following fields (many of which may already exist implicitly):[cite:133][cite:135]

- `round_id`: time-step identifier.
- `env_id`: environment name (e.g., `covid_testing`, `pulse_ox`).
- `policy_id`: policy name (e.g., `baseline_greedy`, `fair_linucb_equitas`).
- `group`: group label (race/ethnicity or SVI stratum).
- `context_features`: serialized or hashed context vector.
- `action`: chosen allocation or escalation action.
- `true_state`: latent label (e.g., high-risk vs low-risk community; hypoxemic vs non-hypoxemic patient).
- `outcome`: realized outcome (e.g., infection detected, death averted surrogate; readmission; time to treatment).

From these, we can compute confusion matrices for both case studies.

### 5.2 Confusion Matrices Across Cases

We summarize the **two key confusion matrices**:

1. **Allocation matrix (Case 1)** — per group \(g\):
   - Actual label: high-risk vs low-risk community.
   - Predicted label: adequate vs inadequate testing allocation.
   - Metrics: \(\text{FNR}_g\) for high-risk communities, disparity in \(\text{FNR}_g\) across groups.

2. **Hypoxemia matrix (Case 2)** — per group \(g\):
   - Actual label: hypoxemic (SaO₂ < 88%) vs non-hypoxemic.
   - Predicted label: escalate vs do not escalate based on policy.
   - Metrics: missed hypoxemia rate \(\text{FNR}_g\), sensitivity \(\text{TPR}_g\), and disparities across groups.

Both matrices can be reported as **tables and graphs** per policy, alongside bandit-regret-style metrics (reward curves) and fairness metrics (disparity trajectories).

---

## 6. Discussion and Implications for Our Project

The two COVID-19 case studies provide **real-world grounding** for our theoretical claim that incomplete and unequal context drives harm in sequential allocation systems:

- In **test allocation**, ignoring vulnerability context (SVI, race/ethnicity, essential worker status) led to **fewer tests in the communities that needed them most** and higher downstream mortality.[cite:17][cite:18][cite:29]
- In **pulse oximetry**, failing to model group-dependent measurement error created **higher missed-hypoxemia rates for Black, Asian, and Hispanic patients**, delaying life-saving therapies.[cite:35][cite:50][cite:33][cite:52]

These are not rare corner cases; they are central artifacts of real healthcare systems under stress. Our Clinical Bandit Environment and EQUITAS-mediated policies are designed to **surface and correct exactly these patterns**.

By embedding group-stratified confusion matrices, fairness metrics, and bandit performance curves into the logging and evaluation pipeline described here, we create a reusable, rigorous foundation for:

- Demonstrating the benefits of context-aware, fair allocation policies over naive or convenience-based baselines;
- Evaluating new diagnostic or allocation algorithms (including quantum-inspired or quantum-executed policies) against established clinical harm patterns; and
- Communicating our results clearly to both technical and clinical audiences.

This report should be treated as the **clinical-side anchor document** for the DSCI601 project. Future work can plug additional case studies (e.g., vaccine allocation, ICU triage) into the same evaluation pattern, reusing the confusion-matrix-based metrics and EQUITAS fairness constraints.

---

## References

[1] N. Rodriguez et al., "Geographic Disparities in COVID-19 Testing and Mortality in the United States," *Health Affairs*, 2020.[cite:17]

[2] Massachusetts Department of Public Health, "COVID-19 Community-Level Data and Testing Equity Analyses," *MMWR* and related technical reports, 2020.[cite:18]

[3] CDC, "COVID-19 in Racial and Ethnic Minority Groups," COVID-19 Racial and Ethnic Health Disparities, 2020.[cite:29]

[4] G. L. Millett et al., "Assessing Differential Impacts of COVID-19 on Black Communities," *Annals of Epidemiology*, 2020.[cite:23]

[5] M. Sjoding et al., "Racial Bias in Pulse Oximetry Measurement," *New England Journal of Medicine*, vol. 383, no. 25, 2020.[cite:35]

[6] A. Fawzy et al., "Association of Racial Differences with Inaccuracy of Pulse Oximetry and Delayed or Missed Treatment Among Patients with COVID-19," *JAMA Internal Medicine*, 2022.[cite:50]

[7] A. Fawzy et al., "Racial and Ethnic Discrepancy in Pulse Oximetry and Clinical Outcomes," *JAMA Network Open*, 2023.[cite:33]

[8] VA Evidence Synthesis Program, "Accuracy of Pulse Oximetry in Patients with Darker Skin Pigmentation," Systematic Review and Meta-analysis, 2021.[cite:52]

[9] U.S. Food and Drug Administration, "Pulse Oximeter Accuracy and Limitations," Safety Communications, 2021–2022.[cite:38][cite:49]

[10] Sutter Health and related analyses on delayed oxygen and dexamethasone due to pulse oximetry bias in COVID-19 (e.g., Gottlieb et al., 2022).[cite:47][cite:53]

[11] `DSCI601-workspace` and `Evaluation_Framework` documentation, including `FRAMEWORK_GUIDE.md`, experiment configuration files, and pipeline code.[cite:133][cite:134][cite:135]
