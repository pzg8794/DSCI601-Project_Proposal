# Proposal Presentation Draft 2

This directory contains the final-presentation draft for the DSCI601 project.

Main file:

- `proposal_presentation_draft2.tex`

The LaTeX source is Overleaf-safe: it uses `\IfFileExists` to load external figure files when present and falls back to TikZ/PGFPlots/table versions if the image files are missing. This means the `.tex` can compile even before binary figures are uploaded to Overleaf.

Expected optional figure assets:

- `figures/fig1_testing_network.pdf`
- `figures/fig2_routing_counterfactual.pdf`
- `figures/fig3_pulseox_bias.pdf`
- `figures/fig4_confusion_matrices.pdf`
- `figures/fig5_utility_fairness_frontier.pdf`

Compile from this directory with:

```bash
pdflatex proposal_presentation_draft2.tex
pdflatex proposal_presentation_draft2.tex
```

The deck integrates the new COVID clinical foundation analysis:

1. COVID testing access and fair CMAB routing.
2. Pulse oximetry bias as the stronger diagnostic-bias case.
3. Confusion-matrix findings for routing false negatives and diagnostic missed hypoxemia.
4. Architecture, code-review targets, demo plan, results, limitations, and next-semester plan.
