# Final Presentation Draft 2

This is the final presentation package for the DSCI601 project. It replaces the earlier proposal-presentation naming.

Main file:

- `final_presentation_draft2.tex`

The deck is written to use the artifacts you added under:

- `presentation/analysis_artifacts/`

The GitHub connector available in this session could not list that directory because its search index was still showing an older commit, but the LaTeX source references the directory directly and tries multiple likely artifact filenames before falling back to built-in TikZ/PGFPlots slides. This keeps the deck compile-safe in Overleaf while still allowing your pushed graphs to appear automatically when their filenames match one of the expected names.

## Compile

From this directory in Overleaf:

```bash
pdflatex final_presentation_draft2.tex
pdflatex final_presentation_draft2.tex
```

## Files

```text
presentation/final_presentation_draft2/
  README.md
  final_presentation_draft2.tex
  artifact_selection_notes.md
```

## Expected analysis artifact names

The `.tex` checks common names such as:

- `../analysis_artifacts/fig1_testing_network.pdf` or `.png`
- `../analysis_artifacts/fig2_routing_counterfactual.pdf` or `.png`
- `../analysis_artifacts/fig3_pulseox_bias.pdf` or `.png`
- `../analysis_artifacts/fig4_confusion_matrices.pdf` or `.png`
- `../analysis_artifacts/fig5_utility_fairness_frontier.pdf` or `.png`

It also checks several alternate descriptive names for each figure. If a specific image is missing, the slide still compiles with a built-in fallback chart.
