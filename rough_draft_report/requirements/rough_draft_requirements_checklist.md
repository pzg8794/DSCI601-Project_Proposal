# Rough Draft Report Requirements Checklist

## Source

- Assignment: `Report Rough Draft - DSCI.601.01 - Applied Data Science I.pdf`
- Due artifact: mostly finished preliminary final-paper draft, excluding full results and conclusion if not final.
- Format: IEEE LaTeX conference template.
- Length target: at most 10 pages, excluding references.

## Assignment Requirements

| Requirement | Target Length | Rough Draft Section | How This Draft Meets It | Status |
|---|---:|---|---|---|
| Abstract | 0.25--0.5 pages | `Abstract` | States the project domain, goals, two-testbed design, completed work so far, and expected impact. | Complete |
| Introduction | 1--1.5 pages | `Introduction` | Expands the abstract with motivation, scientific importance, project overview, current status, and section roadmap. | Complete |
| Related Work | 0.75--1.5 pages | `Related Work` | Condenses the related-work survey into grouped categories: bandits, fairness, missing context/non-stationarity, clinical fairness, and quantum routing. | Complete |
| Approach / Methodology | 1--2 pages | `Approach and Methodology` | Explains the shared missing-context routing model, includes a domain-model figure, and justifies the main design decisions. | Complete |
| Implementation | 1--3 pages | `Implementation and Reproducibility` | Describes the quantum workflow, notebook/local/GCP paths, state/data-lake layer, evaluator/runner/visualizer architecture, and CRISP+ML review package. | Complete |
| Data Sets | 0.5--1 page | `Data Sets and Experimental Inputs` | Describes the quantum routing testbed outputs, reviewer-safe synthetic CRISP+ML dataset, and planned clinical diagnostic simulation. | Complete |
| Results | 1--3 pages, bonus if present | `Preliminary Results and Current Validation Evidence` | Includes cautious preliminary validation evidence: reproducible package execution and current quantum-routing grounding, without overstating unfinished scientific results. | Included as preliminary/bonus |
| Future Work | 0.5 pages | `Future Work` | Lists concrete next-semester tasks: quantum fairness adapter, clinical simulator, mitigation mechanism, transfer analysis, and final experiments. | Complete |
| Conclusion | 0.5--1 page | `Conclusion` | Summarizes current semester accomplishments and expected impact. | Complete |
| References | No page limit | `References` | Uses the survey bibliography and cites representative state-of-the-art work. | Complete |

## Rubric Alignment

### Abstract (15%)

- **Rubric target:** clearly and concisely describe domain, goals, and what has been accomplished so far.
- **Draft response:** the abstract identifies fairness-aware contextual bandits under missing context, the clinical and quantum-routing domains, current implementation/documentation progress, and expected contributions.

### Related Work (15%)

- **Rubric target:** connect to state of the art, compare project to existing work, categorize related work, cite well.
- **Draft response:** related work is organized by technical role instead of source-by-source summary and explicitly states gaps: fairness work is often static/offline, bandit work is utility-centered, and quantum routing work usually lacks service-equity monitoring.

### Approach / Methodology (15%)

- **Rubric target:** include domain diagram, describe components and interactions, justify algorithms/design decisions.
- **Draft response:** Figure 1 gives a four-phase shared domain model; the text explains environment, context observation, routing decision, evaluation/mitigation, and why MAB/CMAB/iCMAB policies are appropriate.

### Implementation (20%)

- **Rubric target:** enough detail to recreate software/results; include architecture diagrams and describe entities/layers.
- **Draft response:** includes notebook/local/GCP execution paths, CRISP+ML stage table, and software entities such as configuration, pipeline stage objects, evaluator/runner/visualizer, artifacts, tests, and merge checks.

### Future Work (15%)

- **Rubric target:** clear plan for following semester and incomplete work.
- **Draft response:** future work is explicit and staged around quantum adapter, clinical simulator, fairness mitigation, cross-domain transfer, final experiments, and final paper/demo.

### Conclusions (15%)

- **Rubric target:** describe and summarize work completed this semester.
- **Draft response:** conclusion summarizes proposal/survey/approach/architecture/code-review progress and frames the remaining work as results-generation and integration.

### Preliminary Results (Bonus 10%)

- **Rubric target:** charts/plots/visualizations or preliminary results with discussion.
- **Draft response:** includes validation evidence and a compact table rather than claiming final results. This is appropriate because final scientific results are still incomplete.

## What Was Done to Meet the Requirements

1. Created a standalone rough-draft report directory so the Overleaf/paper repo has a clean deliverable package.
2. Reused IEEE-style formatting from existing survey and architecture reports for consistency.
3. Condensed the full related-work survey into a shorter final-paper section.
4. Integrated the approach report's missing-context routing argument into the methodology section.
5. Integrated the architecture report and code README into an implementation/reproducibility section.
6. Added a dataset section covering current quantum/synthetic assets and planned clinical simulation inputs.
7. Added cautious preliminary validation evidence without overstating unfinished experimental results.
8. Added future-work and conclusion sections tied directly to remaining project milestones.

