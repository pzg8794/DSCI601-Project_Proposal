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
| Approach / Methodology | 1--2 pages | `Approach and Methodology` | Explains the shared missing-context routing model, reuses the approach write-up's four-phase domain/pipeline diagram, and justifies the main design decisions. | Complete |
| Implementation | 1--3 pages | `Implementation and Reproducibility` | Describes the quantum workflow, notebook/local/GCP paths, state/data-lake layer, evaluator/runner/visualizer architecture, CRISP+ML review package, and reuses the architecture report's system diagram. | Complete |
| Data Sets | 0.5--1 page | `Data Sets and Experimental Inputs` | Now documents the inherited GA quantum corpora in detail: master dataset row counts, column counts, testbed/topology coverage, allocator/scenario/model dimensions, shared Drive data-lake state folders, plus planned clinical simulation data. | Complete |
| Ethics / Fairness | Integrated requirement | `Ethics, Fairness, Privacy, and Security` | Expands fairness from a metric into an ethical design requirement covering clinical harm, service equity, privacy, security, reproducibility, and accountability. | Complete |
| Results | 1--3 pages, bonus if present | `Results and Current Validation Evidence` | Uses real preliminary GA quantum results and validated master datasets as bonus-worthy preliminary evidence, and now frames them explicitly as a context spectrum from no context to context to predictive context using a dedicated table and graph. | Included as preliminary/bonus |
| Future Work | 0.5 pages | `Future Work` | Lists concrete next-semester tasks: quantum fairness adapter, clinical simulator, mitigation mechanism, transfer analysis, final experiments, and limitations discussion. | Complete |
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
- **Draft response:** Figure 1 is adapted from the approach write-up and gives both the four-phase shared domain model and the operational allocator/config/evaluator/runner/model/visualizer expansion; the text explains environment, context observation, routing decision, evaluation/mitigation, and why MAB/CMAB/iCMAB policies are appropriate.

### Implementation (20%)

- **Rubric target:** enough detail to recreate software/results; include architecture diagrams and describe entities/layers.
- **Draft response:** includes notebook/local/GCP execution paths, CRISP+ML stage table, software entities such as configuration, pipeline stage objects, evaluator/runner/visualizer, artifacts, tests, and merge checks, plus the architecture report's CRISP-DM review/replication diagram.

### Future Work (15%)

- **Rubric target:** clear plan for following semester and incomplete work.
- **Draft response:** future work is explicit and staged around quantum adapter, clinical simulator, fairness mitigation, cross-domain transfer, final experiments, and final paper/demo.

### Conclusions (15%)

- **Rubric target:** describe and summarize work completed this semester.
- **Draft response:** conclusion summarizes proposal/survey/approach/architecture/code-review progress and frames the remaining work as results-generation and integration.

### Preliminary Results (Bonus 10%)

- **Rubric target:** charts/plots/visualizations or preliminary results with discussion.
- **Draft response:** now includes GA-derived preliminary-results tables plus a publication-style multi-panel context-spectrum figure that mirrors the stronger visual style used in the quantum manuscript, together with discussion of what those results already show and what the fairness layer will add.

### Ethics and Fairness Integration

- **Project target:** fairness is central to the project and should not appear only as a post-hoc metric.
- **Draft response:** adds a dedicated ethics/fairness section describing clinical harm, quantum service equity, privacy/security considerations, reproducibility/accountability, and how these concerns alter implementation.

## What Was Done to Meet the Requirements

1. Created a standalone rough-draft report directory so the Overleaf/paper repo has a clean deliverable package.
2. Reused IEEE-style formatting from existing survey and architecture reports for consistency.
3. Condensed the full related-work survey into a shorter final-paper section.
4. Integrated the approach report's missing-context routing argument and reused its stronger domain/pipeline diagram in the methodology section.
5. Integrated the architecture report, reused its CRISP-DM review/replication diagram, and incorporated the code README into an implementation/reproducibility section.
6. Added a dataset section covering current quantum/synthetic assets and planned clinical simulation inputs.
7. Added cautious preliminary validation evidence without overstating unfinished experimental results.
8. Added future-work and conclusion sections tied directly to remaining project milestones.

## Diagram Integration Update

- Replaced the initial simplified rough-draft-only domain figure with the stronger two-panel diagram from the approach report: shared domain model plus modular evaluation framework.
- Added the architecture report's CRISP-DM review and replication pipeline diagram as a full-width architecture figure.
- Copied `architecture_diagram.tex` into the rough-draft report directory so the rough draft compiles as a standalone Overleaf/report package.
- Updated the report text and checklist so the rough draft clearly reflects the already completed approach and architecture write-ups.

## Comprehensive Expansion Update

- Expanded the introduction to clarify that the rough draft consolidates proposal, survey, approach, architecture, ethics, and code-review work into a preliminary final-paper structure.
- Expanded related work with offline policy evaluation, estimator/fairness concerns, and a literature-role table.
- Expanded methodology with a planned mitigation strategy covering fairness-regularized updates, missingness-aware context augmentation, and calibration/thresholding.
- Expanded implementation with a reviewer recreation path and clearer notebook/local/GCP/Drive execution explanation.
- Added a full ethics/fairness/privacy/security section because ethics is a major paper component, not a side note.
- Expanded preliminary validation evidence and future work so the rough draft reads closer to a mostly complete final-paper draft.
- Added detailed quantum dataset coverage from `GA-Work/Validated_Logs`, including row/column counts and external testbed slices.
- Upgraded the results section from generic validation language to real preliminary GA results so the report can legitimately target the preliminary-results bonus.
- Reframed the preliminary results around the paper's core context thesis: no-context, context, and predictive-context model families are now compared directly in a dedicated context-spectrum table and figure.
- Replaced the rough-draft-only bar chart with a stronger GA-style multi-panel figure and added a cross-testbed uplift table so the preliminary-results section better matches the quality of the underlying quantum paper.
