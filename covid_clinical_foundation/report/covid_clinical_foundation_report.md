# Comprehensive Clinical Foundation: COVID-19 Context-Aware Routing and Diagnostic Equity

## Purpose

This report completes the clinical foundation for the DSCI601 project. It turns the earlier COVID notes into a standalone research artifact that can support slides, papers, and future experiments. The goal is to validate the project claim that clinical and quantum-routing systems share a core decision problem: scarce resources are routed under uncertainty, and unequal context quality can turn that uncertainty into repeated group-level harm.

The existing project architecture already has the clinical pieces needed to test this claim. The DSCI601 workspace describes a clinical path that runs through `ClinicalExperimentEvaluator`, `ClinicalExperimentRunner`, `ClinicalEnvironment`, clinical allocation, clinical model objects, and the EQUITAS mediator. It also records model families such as `Oracle`, `ClinicalBaseline`, `FairAllocatorV1`, and `ClinicalBanditUCB`. This report maps the COVID evidence into that implemented evaluation surface.

We use two COVID-era clinical cases:

1. **COVID-19 testing access and routing**: testing capacity was often deployed without enough population vulnerability context, leaving high-risk communities under-served.
2. **Pulse oximetry bias during COVID care**: a widely used diagnostic device overestimated oxygen saturation more often for darker-skinned patients, delaying recognition of hypoxemia and treatment eligibility.

Together, these cases cover the two clinical failure modes we need: **inefficient routing** and **unreliable diagnostics**.

---

## Case 1: Inefficient COVID-19 test routing

### Clinical problem

Early in the pandemic, COVID-19 testing was scarce. The practical question was not only how many tests existed, but where they were placed and which communities could realistically access them. A fair and clinically efficient system should have used context such as case burden, positivity, Social Vulnerability Index (SVI), essential-worker exposure, housing crowding, age risk, comorbidity risk, and racial/ethnic disparities in hospitalization.

The literature shows that this did not consistently happen. Testing sites and testing access were often aligned with existing medical infrastructure and convenience rather than vulnerability. That matters because a high positivity rate is not just an epidemiological statistic; it is a routing signal. High positivity usually means testing capacity is too low relative to community disease burden, so many infections remain undetected.

### Evidence used

The report uses evidence from peer-reviewed and public-health sources including CDC racial/ethnic COVID risk documentation, studies of testing-site geography and mortality, studies of racialized exposure and outcomes, and the existing DSCI601 clinical evaluation notes. The previously committed clinical evaluation report already frames this case as a routing failure in which Hispanic, Black, and high-SVI communities received less testing access than their vulnerability justified.

For the project, the key empirical pattern is this:

- high-vulnerability communities had high COVID burden and high need;
- testing access was lower or delayed in those communities;
- lower-vulnerability, infrastructure-rich areas often had greater testing access;
- therefore, a context-blind allocation policy was clinically inefficient and unfair.

### Bandit formulation

Each community is modeled as a context vector:

```text
x_i,t = [SVI, case_rate, positivity, percent_Hispanic, percent_Black,
         essential_worker_share, age_risk, comorbidity_proxy]
```

The action is an allocation tier:

```text
a_i,t in {none, low, medium, high}
```

The reward should combine detected infections, reduced missed infections, and a fairness penalty:

```text
reward = detected_cases - missed_case_penalty - lambda * group_disparity
```

The EQUITAS-style fairness term compares burden-adjusted testing access across groups:

```text
disparity = max_g(tests_per_1000_g / burden_g)
          - min_g(tests_per_1000_g / burden_g)
```

A baseline policy uses weak context, such as population share or existing facility access. A fair CMAB policy uses vulnerability context and penalizes under-allocation to high-risk groups.

### Graph results

The package includes:

- `figures/fig1_testing_network.mmd`: a network graph showing testing resources connected to communities.
- `figures/fig2_routing_counterfactual.mmd`: a bar chart comparing actual/context-blind allocation to fair CMAB allocation.
- `data/routing_inputs.csv`: the transparent values used for the chart.

The routing input table shows the main result:

| Group | Actual tests per 1,000/week | Fair CMAB tests per 1,000/week | Burden cases per 100k |
|---|---:|---:|---:|
| High-SVI Hispanic | 2.1 | 8.4 | 3100 |
| High-SVI Black | 2.7 | 7.9 | 2410 |
| High-SVI Mixed | 3.1 | 6.8 | 2290 |
| Low-SVI White | 8.9 | 4.2 | 720 |
| Low-SVI Mixed | 7.4 | 3.8 | 890 |

The strongest finding is the inversion: under context-blind routing, the lowest-burden groups receive the most testing access. Under fair CMAB routing, the allocation moves toward the communities with the highest burden and vulnerability.

### Confusion-matrix interpretation

For routing, the confusion matrix treats a community as the unit of decision:

- Actual positive: high-risk/high-burden community.
- Actual negative: lower-risk/lower-burden community.
- Predicted positive: received adequate testing allocation.
- Predicted negative: received inadequate testing allocation.

The committed `data/confusion_matrix_examples.csv` provides scenario matrices. For high-SVI Hispanic communities, the baseline matrix has 79 false negatives per 150 community-window units, while the fair CMAB matrix reduces that to 24. For high-SVI Black communities, false negatives fall from 72 to 28. These are illustrative evaluation matrices, not raw historical patient counts. Their purpose is to define exactly how the clinical evaluator should report routing harm: a false negative is a high-risk community that the policy failed to serve adequately.

---

## Case 2: Unreliable diagnostics from missing calibration context

### Why pulse oximetry is the better diagnostic case

The original question asked whether COVID tests themselves were less reliable for minority groups because validation trials lacked enough representation. Direct public aggregate evidence for PCR or antigen-test false-positive disparity by race is limited and not strong enough to carry the claim responsibly. The stronger COVID-relevant diagnostic case is pulse oximetry.

Pulse oximeters were central to COVID triage, home monitoring, oxygen escalation, dexamethasone eligibility, remdesivir eligibility, and hospital admission decisions. The device estimates oxygen saturation using light absorption. Skin pigmentation affects that optical measurement pathway, but historical calibration did not adequately model performance across skin tone. The result was group-dependent measurement error.

### Evidence used

The key evidence base includes:

- Sjoding et al., NEJM 2020: occult hypoxemia was much more frequent among Black patients than White patients when pulse oximetry appeared reassuring.
- Fawzy et al., JAMA Internal Medicine 2022: among COVID patients, pulse-ox overestimation delayed recognition of treatment eligibility and was worse across minority groups.
- Fawzy et al., JAMA Network Open 2023: larger multi-system analysis linking overestimation to delayed therapy and worse care pathways.
- FDA safety communications: pulse oximeter accuracy can be affected by skin pigmentation and other factors.

This is exactly the second failure mode the project needs: the diagnostic signal is not equally reliable across groups because critical context was missing from calibration and decision thresholds.

### Diagnostic decision formulation

Each patient is modeled as a context vector:

```text
x_p = [SpO2, respiratory_rate, work_of_breathing,
       comorbidity_index, group, skin_tone_proxy]
```

The action set is:

```text
a_p in {observe, order_confirmatory_ABG, escalate_treatment}
```

The baseline policy uses a single SpO2 threshold for everyone. The fair contextual policy either adjusts thresholds or orders confirmatory arterial blood gas testing in the ambiguous zone where pulse-ox bias is most likely to change the decision.

The EQUITAS-style constraint is:

```text
abs(P(missed_hypoxemia | group = g1) - P(missed_hypoxemia | group = g2)) <= epsilon
```

### Graph results

The package includes:

- `figures/fig3_pulseox_bias.mmd`: occult hypoxemia rates by group.
- `figures/fig5_utility_fairness_frontier.mmd`: a utility/fairness frontier showing how remaining disparity shrinks as context and EQUITAS mediation are added.
- `data/pulseox_inputs.csv`: the transparent values used for the diagnostic bias chart.

The Fawzy COVID cohort values in the input table are:

| Group | Occult hypoxemia rate (%) | SpO2 overestimation vs reference |
|---|---:|---:|
| White | 17.2 | 0.0 pp |
| Asian | 30.2 | 1.7 pp |
| Black | 28.5 | 1.2 pp |
| Hispanic | 29.8 | 1.1 pp |

The Sjoding signal is also included for the White/Black paired-measure comparison:

| Group | Occult hypoxemia rate (%) |
|---|---:|
| White | 3.6 |
| Black | 11.7 |

The result is clear: the same clinical threshold does not produce the same diagnostic reliability across groups.

### Confusion-matrix interpretation

For pulse oximetry, the confusion matrix treats hypoxemia detection as the decision:

- Actual positive: true hypoxemia by arterial oxygen saturation.
- Actual negative: no true hypoxemia.
- Predicted positive: escalate care or confirm with ABG.
- Predicted negative: do not escalate.

The committed example matrices show the project metric directly. Under the baseline single-threshold policy, the White matrix has 17 false negatives per 200 patients and the Black matrix has 29. Under an EQUITAS-calibrated threshold or targeted confirmation policy, the Black false negatives fall to 6 while the White reference matrix remains stable. That is the clinical point: fairness does not require blindly over-testing everyone; it requires using context where the diagnostic signal is known to be less reliable.

---

## Cross-case synthesis

| Dimension | Testing allocation | Pulse oximetry diagnosis |
|---|---|---|
| Failure type | scarce resource routing | diagnostic measurement reliability |
| Missing context | SVI, burden, race/ethnicity, exposure risk | skin pigmentation, group-dependent measurement error |
| Most affected groups | Hispanic, Black, high-SVI communities | Black, Asian, Hispanic patients |
| Baseline failure | high-risk communities get too few tests | a fixed threshold misses true hypoxemia |
| CMAB/EQUITAS fix | route tests by vulnerability and burden | adjust threshold or confirm diagnosis where uncertainty is group-dependent |
| Evaluation artifact | allocation confusion matrix by group | diagnostic confusion matrix by group |

The two cases validate the same research claim from different directions. In Case 1, missing context causes the wrong communities to receive scarce testing capacity. In Case 2, missing context causes the same diagnostic number to mean different things for different patients. In both cases, the model that ignores context appears simple and neutral, but its errors are not distributed neutrally.

## Why this supports the DSCI601 clinical framework

The DSCI601 fairness framework is already designed around this evidence chain. The workspace status notes describe governed clinical evaluation, model-stratified fairness summaries, clinical model families, EQUITAS mediation, fairness sidecar artifacts, and reporting manifests. The architecture report similarly defines clinical routing as an environment-runner-model-allocator-evaluator process that feeds shared fairness outputs. This package gives that framework a real clinical evidence base.

The clinical foundation should now be used as follows:

1. Use the case studies to motivate the clinical side of the project.
2. Use the CSV files as first-pass aggregate inputs for figures and presentations.
3. Use the confusion-matrix definitions as evaluation metrics for future ClinicalEnvironment runs.
4. Use the fair-routing and fair-diagnostic policy sketches to justify FairAllocatorV1, ClinicalBanditUCB, and EQUITAS mediation.
5. Keep the limitation explicit: these are aggregate, literature-grounded analyses and counterfactual evaluation scenarios, not patient-level causal estimates.

## Limitations

This package intentionally avoids unsupported claims. It does not claim access to patient-level data, and it does not claim that PCR or antigen tests had race-specific false-positive rates unless such evidence is directly available. For the diagnostic-bias case, pulse oximetry is used because it is the stronger, COVID-relevant, well-documented diagnostic example.

The routing values are structured as a transparent scenario built from the pattern reported in the literature: high-burden, high-SVI communities had lower access, while lower-burden communities often had greater access. The fair CMAB values are counterfactual allocation targets used to demonstrate how the DSCI601 evaluator should compare policies.

## Bottom line

The clinical side of the research is now grounded in two defensible COVID-era examples. Testing access shows why context-aware allocation matters. Pulse oximetry shows why context-aware diagnostics matter. The combined lesson is the core of the project: fair sequential decision-making is not achieved by pretending context does not exist; it is achieved by measuring context, auditing disparities, and routing scarce resources toward the places where the cost of being wrong is highest.
