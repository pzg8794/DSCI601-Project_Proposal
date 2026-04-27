# Rough Draft Report Addendum: Fairness Framework Implementation Update

**Purpose:** Update the rough draft package with the latest implementation status and clarify the research-methodology framing behind the architecture.

---

## Why This Methodology Matters

The methodology section should make the early research-design phases explicit. In this project, **Business Understanding** and **Data Understanding** are not generic project-management labels. They are research-design steps that connect the motivating harm mechanism, the observable data, the experimental interventions, and the evidence artifacts used for reporting.

### Business Understanding means harm/problem formulation

For this project, Business Understanding means identifying the shared harm mechanism across the target applications:

> clinical diagnostic systems and quantum-network routing systems both allocate scarce resources under uncertainty, and both can repeatedly harm the groups or flows whose context is least reliable.

That is the reason the two domains belong together. The shared problem is not simply "two domains use bandits." The shared problem is that both domains make sequential routing decisions from partial feedback, and unequal context quality can convert measurement or service uncertainty into repeated allocation harm.

In clinical settings, routing includes the distribution of scarce tests, retesting capacity, escalation decisions, diagnostic attention, and model-assisted triage across sites and cohorts. During volatile conditions such as a pandemic, threat, demand, evidence quality, and resource availability can shift rapidly, making the clinical environment chaotic in a way that is structurally similar to quantum routing under noisy links, uncertain entanglement generation, and non-stationary service conditions. In quantum routing, the harm appears as degraded service quality: lower success probability, longer latency, or less reliable access for some flow classes. These harms differ ethically, but the decision structure is the same.

### Data Understanding means evidence mechanism identification

Data Understanding means identifying which recorded patterns make the shared harm mechanism measurable.

In the clinical setting, those patterns include:

- site
- cohort
- service line
- group
- test distribution and retesting capacity
- escalation or diagnostic-routing action
- allocation label
- latency
- reward
- success
- EQUITAS audit/mitigation fields

In the quantum setting, those patterns include:

- testbed/source environment
- scenario
- allocator
- route or model choice
- success
- latency
- reward
- oracle gap or efficiency
- evaluator state

The point is not merely to inspect data. The point is to identify which data fields explain the commonality between domains and which fields expose the paths that harm or mediate outcomes most strongly.

### Stronger paper wording

Use wording like this in the architecture and rough draft:

> Business Understanding identifies the shared harm mechanism: both clinical and quantum systems route scarce resources under uncertainty, and unequal context quality can produce repeated allocation harm. Data Understanding identifies the measurable patterns that make that harm testable: group, site, cohort, service line, test distribution, escalation action, latency, reward, success, scenario, allocator, route choice, and evaluator-state fields. These phases justify the cross-domain architecture because they connect the ethical problem, the observed data, the experimental interventions, and the reporting artifacts.

---

## How the Architecture Interacts With Target Applications

The architecture should be described as an application-facing contract, not as a disconnected pipeline diagram.

Each target application supplies:

1. an environment or saved state source,
2. a model or policy family,
3. an allocator/action mechanism,
4. an evaluator-facing outcome record.

The framework then normalizes those outputs into shared fairness/reporting artifacts.

```text
application environment or saved state
  -> runner / model / allocator decision path
  -> evaluator or adapter normalization
  -> canonical outcome and fairness state
  -> default and fairness reporting datasets
  -> visualizer outputs, report manifests, and validation hubs
```

### Quantum interaction

Legacy quantum experiments keep their original runner/evaluator/allocator path. The fairness layer attaches as a sidecar and extracts fairness-compatible states without rewriting the old experiment code. This is why the framework can test the Chaudhary, Liu, Clayton, and other archived legacy quantum testbed paths while preserving old behavior.

### Clinical interaction

Clinical experiments run through the embedded clinical path:

```text
ClinicalExperimentEvaluator
  -> ClinicalExperimentRunner
  -> ClinicalEnvironment
  -> clinical allocator
  -> clinical model object
  -> EQUITAS mediator
  -> fairness states
```

The clinical path proves that a non-quantum environment can be plugged into the same architecture while producing comparable fairness/reporting artifacts.

---

## Architecture Figure Treatment

The architecture figure should be presented as an evidence-flow view rather than as a full implementation graph.

Recommended treatment in the next figure revision:

- make the main figure an evidence-flow view, not a full component graph;
- reduce the scale conservatively, around `0.90\linewidth` in landscape mode;
- move low-level object names into a table instead of cramming them into the figure;
- explicitly state in the caption that detailed implementation mappings are provided in the stage-to-component table;
- emphasize the application contract:
  `environment -> runner/model/allocator -> evaluator/adapter -> canonical states -> reporting/validation`.

The architecture report has already been updated in this direction by resizing the figure and clarifying that the figure is a high-level evidence-flow diagram, while the detailed implementation mapping belongs in the table.

---

## Summary of Implementation Progress

Since the rough draft text was written, the project moved from planned clinical/fairness integration to an implemented and CI-protected multi-environment fairness framework.

The current implementation now supports:

- legacy quantum old-pipeline fairness extraction as an additive sidecar
- default/no-testbed quantum smoke coverage
- Chaudhary, Liu, Clayton, and other archived legacy quantum fairness smokes
- embedded clinical experiment execution through a clinical evaluator, runner, environment, allocator, model registry, and EQUITAS mediation seam
- governed fairness artifacts under `datalake/fairness/...`
- default and fairness reporting profiles
- model-stratified fairness summaries
- visualizer artifacts and visualization manifests
- report manifests for validation notebooks
- fairness validation hub notebook support
- path-scoped GitHub Actions gates for quantum and clinical/reporting surfaces

---

## Updated Architecture Claim

The rough draft should no longer describe the clinical side as only planned. The clinical path is now implemented as an embedded experiment path.

Updated description:

> The framework now supports two executable environment families. Legacy quantum experiments continue to run through the old quantum evaluator and runner path, with fairness extraction attached as a governed sidecar. Clinical experiments run through an embedded clinical path consisting of `ClinicalExperimentEvaluator`, `ClinicalExperimentRunner`, `ClinicalEnvironment`, clinical resource allocation, clinical model objects, and EQUITAS mediation. Both families emit canonical fairness states that feed the same governed fairness workflow, reporting layer, and validation manifests.

---

## Updated Reproducibility Claim

The rough draft currently emphasizes notebooks, local execution, GCP execution, and CRISP+ML review artifacts. The reproducibility story now includes CI smoke gates and report manifests.

Updated description:

> Reproducibility is enforced through three layers: executable notebooks/shared runners, local test commands, and path-scoped CI workflows. The Drive fairness smoke validates old quantum/default and source-backed legacy quantum smokes with credentials. The clinical fairness smoke validates the embedded clinical evaluator, fairness artifacts, model-stratified summaries, visualizer outputs, reporting manifests, and validation hub contracts. Reporting artifacts are tied together through `report_manifest.json`, allowing validation notebooks to trace paper-facing claims back to generated datasets, figures, and source fairness artifacts.

---

## Updated Reporting Layer

The reporting layer now formalizes the earlier `state_analysis.py` idea into a shared OOP interface while preserving the old reporting methodology.

Current reporting structure:

```text
StateAnalysis
  -> QuantumStateAnalysis
  -> ClinicalStateAnalysis

StateReporting
  -> build_default_master_dataset(...)
  -> build_fairness_master_dataset(...)
```

The two reporting profiles are:

- **default reporting**: legacy/performance-style columns such as model, scenario, reward, success, latency, oracle efficiency, oracle gap, and winner
- **fairness reporting**: default fields plus fairness/EQUITAS fields such as group, site, cohort, service line, action, allocation label, EQUITAS mediator, EQUITAS mode, and EQUITAS mitigation

This keeps legacy analysis stable while adding the fields required for fairness findings.

---

## Updated Validation and Notebook Interfaces

The framework now distinguishes reporting production from validation notebooks.

Current notebook-facing surfaces:

- `Evaluation_Framework/notebooks/Clinical/Clinical_Fairness_Testbed.ipynb`
- `Evaluation_Framework/notebooks/Clinical/_shared/run_clinical_fairness_pipeline.py`
- `Evaluation_Framework/notebooks/Reporting/Fairness_Validation_Hub.ipynb`
- `Evaluation_Framework/notebooks/Reporting/_shared/run_fairness_validation_hub.py`
- `Evaluation_Framework/notebooks/Reporting/README.md`

The fairness validation hub currently validates preliminary fairness evidence rather than final scientific claims. It checks that generated report manifests provide evidence for:

- governed fairness artifact generation
- fairness-profile master dataset availability
- model-stratified fairness summaries
- EQUITAS audit/mitigation fields
- artifact lineage from datasets and figures back to source artifacts

The existing quantum-paper validation hub should remain focused on efficiency/performance findings. Fairness validation is intentionally separated into its own notebook surface.

---

## Updated Experimental Status

The rough draft should continue to avoid overstating final scientific results. The correct wording is:

> The implementation now validates the framework's ability to generate fairness artifacts from legacy quantum smokes and an embedded clinical fixture. These are smoke and reproducibility validations, not exhaustive full-scale experiments across all models, allocators, scenarios, and frame counts.

Specific validated paths:

- old quantum default/no-testbed smoke
- source-backed legacy quantum smokes, including Chaudhary, Liu, and Clayton testbed paths where source mappings are verified
- embedded clinical smoke with `Oracle`, `ClinicalBaseline`, `FairAllocatorV1`, and `ClinicalBanditUCB`
- clinical report package with default/fairness master datasets, visualizer figures, visualization manifest, and `report_manifest.json`

---

## Suggested Rough Draft Edits

The next full LaTeX revision should update these places:

1. **Abstract**
   - Replace "planned simulation-first diagnostic workflow" with "embedded simulation-first clinical experiment path."
   - Mention governed fairness/reporting artifacts and validation manifests.

2. **Introduction**
   - Clarify that the clinical setting is now implemented as a synthetic, non-PHI clinical fixture path.
   - Add the stronger harm-mechanism framing for Business Understanding and Data Understanding.
   - Tie clinical routing explicitly to test distribution, retesting capacity, escalation, diagnostic attention, and pandemic-like non-stationarity.
   - Keep final-results caveat.

3. **Approach and Methodology**
   - Add the application contract:
     `environment -> runner/model/allocator -> evaluator/adapter -> canonical states -> reporting/validation`.
   - Add the clinical execution chain:
     `ClinicalExperimentEvaluator -> ClinicalExperimentRunner -> ClinicalEnvironment -> allocator -> EQUITAS -> states`.
   - Clarify that quantum remains legacy-compatible and sidecar-based.

4. **Implementation and Reproducibility**
   - Add CI smoke gates.
   - Add report manifests.
   - Add default/fairness reporting profiles.
   - Add validation hubs.
   - Replace visible PaperX labels with source/author-based testbed labels wherever the source mapping is known.

5. **Preliminary Validation Evidence**
   - Report current validation as smoke/reproducibility evidence:
     old quantum testbed smokes, clinical 16-state smoke, reporting artifacts, and validation hub checks.
   - Do not present smoke results as final scientific conclusions.

6. **Future Work**
   - Add quantum/default report-manifest bridge.
   - Add broader full-scale fairness experiments.
   - Add portal/website as future interface over the manifest/reporting layer.

---

## Useful Implementation References

Workspace repo paths:

- `docs/guides/FAIRNESS_FRAMEWORK_STATUS.md`
- `docs/guides/FAIRNESS_LAYER_TODO.md`
- `docs/guides/REPORTING_INTERFACE_ROADMAP.md`
- `Evaluation_Framework/daqr/evaluation/clinical_experiment.py`
- `Evaluation_Framework/daqr/evaluation/clinical_models.py`
- `Evaluation_Framework/daqr/evaluation/equitas_mediator.py`
- `Evaluation_Framework/daqr/evaluation/state_reporting.py`
- `Evaluation_Framework/daqr/evaluation/reporting_manifest.py`
- `Evaluation_Framework/notebooks/Clinical/Clinical_Fairness_Testbed.ipynb`
- `Evaluation_Framework/notebooks/Reporting/Fairness_Validation_Hub.ipynb`

---

## Recommended Wording for the Rough Draft

Use this sentence to avoid overstating results:

> The current implementation demonstrates reproducible fairness artifact generation and validation over smoke-scale quantum and clinical runs. The system is ready for broader experimental evaluation, but the smoke gates should be interpreted as compatibility and reproducibility evidence rather than exhaustive scientific validation.
