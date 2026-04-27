# Rough Draft Architecture Update

This note records the exact manuscript-body updates that belong in `rough_draft_report/rough_draft_report.tex` so the rough draft reflects the architecture report updates directly.

## Abstract replacement

Replace the sentence block beginning with:

> The work develops a reusable evaluation framework for non-contextual bandits...

with:

> The work develops a reusable evaluation framework for non-contextual bandits, contextual bandits, and informative contextual bandits across two executable environment families. The quantum path reuses the legacy quantum-routing evaluation stack and saved-state paths from the quantum-routing evaluation paper, while the clinical path now runs through an embedded synthetic clinical environment with clinical models, resource allocation, EQUITAS mediation, and governed fairness artifacts. Work completed so far includes the related-work synthesis, domain model, architecture specification, embedded clinical evaluator path, legacy quantum fairness sidecar, default and fairness reporting datasets, validation-hub artifacts, and CI-protected smoke gates.

## Introduction replacement

Replace the paragraph beginning with:

> The project uses two complementary testbeds.

with:

> The project uses two complementary environment families. The first is an existing quantum-routing evaluation stack based on hybrid contextual bandits for entanglement routing and qubit allocation. That stack already exposes uncertainty, adversarial or non-stationary conditions, legacy testbed conventions, and stateful evaluator artifacts. The second is an embedded clinical simulation motivated by equitable bioinformatics and fairness auditing work. The clinical environment models the routing of scarce tests, retesting capacity, escalation decisions, diagnostic attention, and model-assisted triage across sites and cohorts. Under volatile conditions such as a pandemic, threat, demand, evidence quality, and resource availability can change rapidly; this makes the clinical routing setting structurally comparable to quantum routing under noisy links, uncertain entanglement generation, and non-stationary service conditions. The two-domain design tests whether fairness mechanisms and policy-update strategies transfer across fundamentally different applications with the same partial-feedback allocation structure.

## Methodology replacement

Replace the opening paragraph of `Shared Missing-Context Routing Model` with:

> The methodology treats both domains as routing under missing context. Business Understanding identifies the shared harm mechanism: clinical and quantum systems route scarce resources under uncertainty, and unequal context quality can produce repeated allocation harm. Data Understanding identifies the measurable patterns that make that harm testable, including group, site, cohort, service line, test distribution, escalation action, latency, reward, success, scenario, allocator, route choice, and evaluator-state fields.
>
> In the clinical domain, the routed resource is diagnostic attention: scarce tests, retests, triage escalation, model-assisted prioritization, or model/pipeline selection. In the quantum domain, the routed resource is entanglement-generation effort, qubit allocation, or path capacity. In both domains, the policy observes partial context, chooses an action, receives partial feedback, and updates. The key experimental variable is the richness and reliability of context available to the policy.

## Execution-path replacement

Replace the opening paragraph of `Execution Paths` with:

> The implementation is designed around reproducibility. The quantum side uses three execution paths inherited from the upstream quantum project: notebooks for fast interactive replication, a local environment for development and testing, and GCP/batch scripts for longer runs. The notebook and local paths support the legacy quantum testbeds and saved-state conventions documented in the quantum-routing evaluation paper. The clinical side now runs through an embedded evaluator path consisting of `ClinicalExperimentEvaluator`, `ClinicalExperimentRunner`, `ClinicalEnvironment`, clinical resource allocation, clinical model objects, and EQUITAS mediation. The local path uses a virtual environment, dependencies from `requirements.txt`, and validation scripts. The GCP path uses startup and dynamic-runner scripts for larger allocator and time-scale experiments.

## Architecture-caption replacement

Replace the architecture figure caption with:

> Architecture diagram adapted from the architecture report. The workflow is an evidence-flow view rather than a full implementation graph. It connects problem formulation and data/context understanding to repository/user entry paths, control and validation layers, executable data-processing stages, the fairness--performance synthesis layer, and final replication artifacts. In application terms, each environment supplies a saved-state or simulator source, a runner/model/allocator decision path, and evaluator-facing outcomes. The framework converts those outcomes into canonical states, default and fairness reporting datasets, visualizer outputs, report manifests, and validation-hub evidence.

## Local application command

Because the TeX file is large and remote file reads are truncated by the connector, apply this update locally in the canonical paper checkout and then commit the resulting TeX diff:

```bash
cd /Users/pitergarcia/DataScience/Semester5/DSCI601/implementation/paper
python - <<'PY'
from pathlib import Path
p = Path('rough_draft_report/rough_draft_report.tex')
s = p.read_text(encoding='utf-8')

replacements = [
    (
        '''The work develops a reusable\nevaluation framework for non-contextual bandits, contextual bandits, and\ninformative contextual bandits across two testbeds: a quantum-routing\nenvironment grounded in prior hybrid-bandit experiments and a planned\nsimulation-first diagnostic workflow. Work completed so far includes the\nrelated-work synthesis, domain model, architecture specification, quantum-first\nexecution plan, and a reproducible CRISP+ML code-review package with unit\ntests and merge validation.''',
        '''The work develops a reusable\nevaluation framework for non-contextual bandits, contextual bandits, and\ninformative contextual bandits across two executable environment families. The\nquantum path reuses the legacy quantum-routing evaluation stack and saved-state\npaths from the quantum-routing evaluation paper, while the clinical path now\nruns through an embedded synthetic clinical environment with clinical models,\nresource allocation, EQUITAS mediation, and governed fairness artifacts. Work\ncompleted so far includes the related-work synthesis, domain model,\narchitecture specification, embedded clinical evaluator path, legacy quantum\nfairness sidecar, default and fairness reporting datasets, validation-hub\nartifacts, and CI-protected smoke gates.'''
    ),
    (
        '''The project uses two complementary testbeds. The first is an existing\nquantum-routing evaluation stack based on hybrid contextual bandits for\nentanglement routing and qubit allocation~\\cite{garcia2026threat_aware_quantum_routing}.\nThat testbed already exposes uncertainty, adversarial or non-stationary\nconditions, and stateful evaluator artifacts. The second is a planned\ndiagnostic-like simulation motivated by equitable bioinformatics and fairness\nauditing work~\\cite{garcia2025equitable_bioinformatics}. The diagnostic\nsimulation will model test selection, retesting, and escalation under\ncontrollable missingness, measurement noise, and group-dependent context\nquality. The two-domain design tests whether fairness mechanisms and\npolicy-update strategies transfer across fundamentally different applications.''',
        '''The project uses two complementary environment families. The first is an\nexisting quantum-routing evaluation stack based on hybrid contextual bandits\nfor entanglement routing and qubit allocation~\\cite{garcia2026threat_aware_quantum_routing}.\nThat stack already exposes uncertainty, adversarial or non-stationary\nconditions, legacy testbed conventions, and stateful evaluator artifacts. The\nsecond is an embedded clinical simulation motivated by equitable bioinformatics\nand fairness auditing work~\\cite{garcia2025equitable_bioinformatics}. The\nclinical environment models the routing of scarce tests, retesting capacity,\nescalation decisions, diagnostic attention, and model-assisted triage across\nsites and cohorts. Under volatile conditions such as a pandemic, threat,\ndemand, evidence quality, and resource availability can change rapidly; this\nmakes the clinical routing setting structurally comparable to quantum routing\nunder noisy links, uncertain entanglement generation, and non-stationary\nservice conditions. The two-domain design tests whether fairness mechanisms\nand policy-update strategies transfer across fundamentally different\napplications with the same partial-feedback allocation structure.'''
    ),
    (
        '''\\subsection{Shared Missing-Context Routing Model}\nThe methodology treats both domains as routing under missing context. In the\nclinical domain, the routed resource is diagnostic attention: tests, retests,\ntriage escalation, or model/pipeline selection. In the quantum domain, the\nrouted resource is entanglement-generation effort or path capacity. In both\ndomains, the policy observes partial context, chooses an action, receives\npartial feedback, and updates. The key experimental variable is the richness\nand reliability of context available to the policy.''',
        '''\\subsection{Shared Missing-Context Routing Model}\nThe methodology treats both domains as routing under missing context. Business\nUnderstanding identifies the shared harm mechanism: clinical and quantum\nsystems route scarce resources under uncertainty, and unequal context quality\ncan produce repeated allocation harm. Data Understanding identifies the\nmeasurable patterns that make that harm testable, including group, site,\ncohort, service line, test distribution, escalation action, latency, reward,\nsuccess, scenario, allocator, route choice, and evaluator-state fields.\n\nIn the clinical domain, the routed resource is diagnostic attention: scarce\ntests, retests, triage escalation, model-assisted prioritization, or\nmodel/pipeline selection. In the quantum domain, the routed resource is\nentanglement-generation effort, qubit allocation, or path capacity. In both\ndomains, the policy observes partial context, chooses an action, receives\npartial feedback, and updates. The key experimental variable is the richness\nand reliability of context available to the policy.'''
    ),
    (
        '''\\subsection{Execution Paths}\nThe implementation is designed around reproducibility. The quantum side uses\nthree execution paths inherited from the upstream quantum project: notebooks\nfor fast interactive replication, a local environment for development and\ntesting, and GCP/batch scripts for longer runs. The notebook path supports\nPaper2, Paper7, Paper8, and Paper12-style testbed configurations. The local\npath uses a virtual environment, dependencies from \\texttt{requirements.txt},\nand validation scripts. The GCP path uses startup and dynamic-runner scripts\nfor larger allocator and time-scale experiments.''',
        '''\\subsection{Execution Paths}\nThe implementation is designed around reproducibility. The quantum side uses\nthree execution paths inherited from the upstream quantum project: notebooks\nfor fast interactive replication, a local environment for development and\ntesting, and GCP/batch scripts for longer runs. The notebook and local paths\nsupport the legacy quantum testbeds and saved-state conventions documented in\nthe quantum-routing evaluation paper~\\cite{garcia2026threat_aware_quantum_routing}.\nThe clinical side now runs through an embedded evaluator path consisting of\n\\texttt{ClinicalExperimentEvaluator}, \\texttt{ClinicalExperimentRunner},\n\\texttt{ClinicalEnvironment}, clinical resource allocation, clinical model\nobjects, and EQUITAS mediation. The local path uses a virtual environment,\ndependencies from \\texttt{requirements.txt}, and validation scripts. The GCP\npath uses startup and dynamic-runner scripts for larger allocator and\ntime-scale experiments.'''
    ),
    (
        '''\\caption{Architecture diagram adapted from the architecture report. The\nworkflow connects high-level CRISP-DM context, repository/user entry paths,\ncontrol and validation layers, executable data-processing stages, the\nfairness--performance synthesis layer, and final replication artifacts. This\ndiagram clarifies how notebook, local, and cloud execution paths all produce\nauditable evidence for review and final analysis.}''',
        '''\\caption{Architecture diagram adapted from the architecture report. The\nworkflow is an evidence-flow view rather than a full implementation graph. It\nconnects problem formulation and data/context understanding to repository/user\nentry paths, control and validation layers, executable data-processing stages,\nthe fairness--performance synthesis layer, and final replication artifacts. In\napplication terms, each environment supplies a saved-state or simulator source,\na runner/model/allocator decision path, and evaluator-facing outcomes. The\nframework converts those outcomes into canonical states, default and fairness\nreporting datasets, visualizer outputs, report manifests, and validation-hub\nevidence.}'''
    ),
]

for old, new in replacements:
    if old not in s:
        raise SystemExit('Missing expected block; rough draft has drifted. First missing block starts: ' + old[:120])
    s = s.replace(old, new, 1)

p.write_text(s, encoding='utf-8')
PY

grep -n "two executable environment families\|embedded clinical simulation\|Business Understanding identifies\|legacy quantum testbeds and saved-state conventions\|evidence-flow view" rough_draft_report/rough_draft_report.tex
```
