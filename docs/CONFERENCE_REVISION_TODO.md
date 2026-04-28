# Conference Revision TODO

Purpose: track the work needed to turn the current rough draft into a conference-style manuscript. The main paper should read as a submission, not as a project diary, repository guide, or implementation handoff.

## Claim boundary

- [ ] Decide and state the current scientific claim boundary.
  - Current evidence supports a fairness-mediated cross-domain evaluation methodology.
  - Do not claim a fully active fairness-adjusted quantum learning rule until the quantum policy update or penalty is implemented and evaluated.
  - Clinical results can be described as embedded-method validation unless broader clinical experiments are run.

## Task 1: Rewrite the introduction for conference tone

- [ ] Remove unnecessary intro paragraph 3.
- [ ] Remove intro paragraph 4 if it refers to the paper, draft, or document structure.
- [ ] Move research-question material currently in Section 3C into the end of the introduction.
- [ ] End the introduction with explicit research questions and current findings/claim boundaries.
- [ ] Remove all manuscript meta-commentary, including phrases like "this paper will," "this section," "the project currently," or reviewer-facing language.

## Task 2: Replace implementation-heavy Sections 3 and 4 with formal methodology

- [ ] Replace long architecture/process prose with a unified sequential-decision formulation.
- [ ] Define context, partial/missing context, group/site/flow labels, action, reward, feedback, and fairness state.
- [ ] Add UCB, LinUCB/contextual bandit, and optional neural/contextual score equations only where they are relevant to the experiments.
- [ ] Add a fairness-mediated or fairness-penalized objective that matches what is actually implemented.
- [ ] Add one central pseudocode algorithm for cross-domain fairness-aware routing.
- [ ] Add short instantiations for quantum routing and clinical routing.

## Task 3: Remove low-level repository/run details from the main body

- [ ] Remove individual filenames, local commands, path names, and CI execution details from the main conference-paper sections.
- [ ] Keep only high-level architecture/implementation details needed to understand the method.
- [ ] Move reproducibility mechanics to appendix, supplement, README, or repository docs.

## Task 4: Rebuild experimental setup and results around research questions

- [ ] Make each result subsection answer one research question.
- [ ] Separate mature quantum efficiency results from smoke-scale clinical/fairness validation.
- [ ] Report what is actually validated: utility/efficiency, missing-context behavior, fairness summaries, model-stratified results, and artifact lineage.
- [ ] Avoid overstating clinical or quantum fairness mediation beyond existing evidence.

## Task 5: State novelty clearly

- [ ] Do not present UCB, contextual bandits, Thompson sampling, or NeuralUCB as new.
- [ ] Frame novelty as the shared missing-context routing formulation, cross-domain mapping, canonical fairness state/reporting layer, EQUITAS mediation seam, and reproducible model-stratified fairness validation workflow.
- [ ] Explain the improvement over older methodologies: non-contextual bandits ignore covariates, contextual methods use them, fairness-aware methods constrain disparity, and this work connects those pieces across quantum and clinical routing under missing context.

## Task 6: Clean structure and tone across the manuscript

- [ ] Target structure: Introduction, Related Work, Methodology, Experimental Setup, Results, Discussion/Limitations, Conclusion.
- [ ] Ensure the main body contains the science: problem, equations, algorithm, setup, results, and limitations.
- [ ] Keep repository, notebook, and validation workflow details outside the main narrative unless they directly support reproducibility claims.

## Status log

- 2026-04-28: TODO created from advisor feedback and deep-research revision plan.
