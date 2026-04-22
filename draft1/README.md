# draft1

This directory contains a substantive rough-draft revision package for the DSCI601 project report.

## What changed

The original draft had a strong idea but it blurred three different things:

1. inherited preliminary quantum-routing evidence,
2. the reviewer-safe reproducibility scaffold, and
3. the planned clinical diagnostic simulator.

This revision package separates those layers clearly. The goal is to make the report more defensible, less vague, and closer to PhD-level standards for scope control, evidence discipline, and reproducibility.

## Package contents

- `report/revised_report.tex`  
  Revised IEEE-style report with sharper framing, clearer limitations, cleaner claims, and new scope/evidence positioning.

- `tables/evidence_status.csv`  
  Completed vs. partial vs. planned components.

- `tables/claim_audit.csv`  
  Claims that should be kept, softened, or removed.

- `tables/experiment_matrix.csv`  
  Cross-domain comparison schema for methods, rewards, fairness metrics, and current evidence status.

- `figures/project_scope.mmd`  
  Scope-and-evidence diagram source showing what is completed now and what belongs to the next phase.

- `appendix/reproducibility_checklist.md`  
  Paper-facing reproducibility checklist.

- `appendix/README_experiments.md`  
  Reviewer-oriented notes for rerunning the lightweight path and the quantum path.

## Editorial stance used in this revision

The revised report does **not** present the project as a completed dual-domain fairness study. It presents it as:

- a reproducible framework for fairness-aware contextual bandits under missing context,
- supported by inherited preliminary quantum-routing evidence, and
- extended next by a simulation-first clinical diagnostic testbed.

That is the strongest accurate version of the story based on the current repositories.

## Immediate next step

Use `report/revised_report.tex` as the new working paper in `draft1/`, then pull over any validated figures or tables from the older draft only when their provenance is explicit.
