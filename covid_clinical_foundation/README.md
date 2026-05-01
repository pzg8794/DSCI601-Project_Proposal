# COVID Clinical Foundation

Standalone clinical evidence package for the DSCI601 project.

This directory contains a comprehensive report, data tables, figure code, and renderable Mermaid chart files for two COVID-era case studies:

1. inequitable COVID-19 testing access and context-aware routing;
2. pulse oximetry bias and context-aware diagnostic decision support.

## Contents

```text
covid_clinical_foundation/
  README.md
  data/
    README.md
    routing_inputs.csv
    pulseox_inputs.csv
    confusion_matrix_examples.csv
  figures/
    fig1_testing_network.mmd
    fig2_routing_counterfactual.mmd
    fig3_pulseox_bias.mmd
    fig5_utility_fairness_frontier.mmd
  report/
    covid_clinical_foundation_report.md
    references.md
  scripts/
    generate_figures.py
```

Start with `report/covid_clinical_foundation_report.md`. The Mermaid files in `figures/` render in GitHub-compatible Markdown tools and can be copied into slide tooling. The CSV files preserve the chart inputs and confusion-matrix values.
