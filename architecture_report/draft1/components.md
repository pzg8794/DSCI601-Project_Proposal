# Draft 1 system components and replication interfaces

This note now matches the strengthened `draft1` architecture report and figure.
It describes the repository as a **reproducible CRISP-DM review and replication
pipeline** that inherits its main storage, evaluator, notebook, and analysis
workflow from `quantum_project`.

## Architectural intent

The architecture must satisfy three obligations at once:

- preserve the CRISP-DM logic of the project,
- preserve the code-review and validation workflow for the repository,
- preserve the ability for another party to recreate the system and replicate
  the presented results.

That means the important components are not only stage classes. They also
include shared-drive storage access, notebooks, local and GCP entry paths,
orchestration, validation, provenance, and result-sharing behavior.

## Layered component model

### 1. High-level context layer
Representative responsibilities:
- business understanding,
- data understanding,
- fairness and acceptance criteria,
- knowledge of shared-drive storage and notebook expectations.

Why it matters:
- this layer determines what counts as a valid run and what another party is
  expected to be able to reproduce.

### 2. Control and review layer
Representative responsibilities:
- configuration loading,
- command routing,
- run ordering,
- merge policy,
- local validation and CI mirroring.

Representative interfaces:
- `run-all`
- `merge-check`
- local scripts
- notebook entry cells
- GCP batch scripts

Why it matters:
- this is the executable control surface of the architecture.

### 3. Replication entry paths
Supported user entry paths:
- shared notebooks / Colab,
- local clone + virtual environment,
- GCP VM + startup and batch scripts.

Why they matter:
- the architecture must explain how another party actually recreates the system
  and reruns the workflow.

## Inherited storage and execution components

### 4. Shared-drive quantum data lake
Representative responsibility:
- shared upstream source for framework state, model state, visualizations, and
  day-partitioned outputs.

Representative path pattern:
- `quantum_data_lake/{component}/day_YYYYMMDD/`

Why it matters:
- this is the authoritative source and destination for replication artifacts.

### 5. Backup-manager / registry path
Representative components:
- `LocalBackupManager`
- `GoogleDriveBackupManager`
- registry / latest-state resolution methods

Role:
- resolve shared-drive storage,
- discover available saved state,
- retrieve the latest or matching experiment artifacts.

Why it matters:
- this is the real implementation of the collection stage.

### 6. `MultiRunEvaluator`
Role:
- validate and clean state,
- own evaluation summaries,
- compute scenario-level winners and metrics,
- serve as the core quality-judgment object.

Why it matters:
- cleaning and evaluation are intentionally concentrated here.

### 7. `state_analysis`
Role:
- consume evaluator summaries,
- restructure scenario outputs,
- support preparation, exploration, flattened analysis, and replication-ready
  summaries.

Why it matters:
- this is the bridge between saved evaluator state and human-readable analysis.

### 8. Notebook and visualization path
Representative components:
- shared Colab notebooks,
- `QuantumEvaluatorVisualizer`,
- notebook cells that mount Drive, install dependencies, load results, and plot
  comparisons.

Why it matters:
- notebooks are part of the replication architecture, not just optional demos.

## Stage responsibilities

### 9. Data Collection stage
Repository realization:
- retrieve saved experiment or evaluator state from the shared-drive quantum
  data lake through inherited backup-manager / registry logic.

Typical outputs:
- source references,
- retrieved state files,
- raw experiment inputs.

### 10. Data Cleaning stage
Repository realization:
- evaluator-owned validation and compatibility checks,
- removal or rejection of invalid state.

Typical outputs:
- cleaned or validated state,
- contract-consistent records.

### 11. Data Preparation and Exploration stage
Repository realization:
- `state_analysis` transformation,
- scenario summaries,
- preparation of analysis-ready tables or train/test-style structures.

Typical outputs:
- scenario summaries,
- prepared tables,
- exploratory artifacts.

### 12. Modeling / Mining stage
Repository realization:
- inherited experiment-running or analysis logic,
- notebook or scripted mining that produces substantive outputs from prepared
  state.

Typical outputs:
- mined outputs,
- traces,
- predictions,
- derived analysis artifacts.

### 13. Evaluation stage
Repository realization:
- evaluator metrics,
- scenario winner logic,
- fairness and utility summaries.

Typical outputs:
- comparison metrics,
- winner summaries,
- reviewer-visible evaluation evidence.

### 14. Review Delivery / Replication Outputs stage
Repository realization:
- figures,
- tables,
- notebook-visible outputs,
- manifest writing,
- shared result exports.

Typical outputs:
- charts,
- CSV summaries,
- notebook artifacts,
- `pipeline_manifest.json` or equivalent provenance record.

Why it matters:
- this stage is where replication becomes visible and shareable.

## User workflow components

### 15. Setup path
Representative steps:
- clone repo and install requirements locally,
- or open shared notebook and mount Drive,
- or provision GCP VM and run startup script.

### 16. Run path
Representative actions:
- run notebook cells,
- run local smoke/validation scripts,
- run GCP batch scripts,
- run `merge-check` for repository validation.

### 17. Interpretation path
Representative components:
- visualizer,
- notebook plots,
- evaluator summaries,
- saved day directories in the data lake.

### 18. Sharing path
Representative behavior:
- save outputs back into the shared-drive data lake so collaborators can inspect,
  compare, and rerun them.

## Bottom-line architectural claim

`draft1` should be understood as a reviewer-safe and replication-safe system in
which users may enter through notebooks, local installation, or GCP execution;
collection begins from the shared-drive quantum data lake; evaluator and
state-analysis logic structure the core pipeline; and artifacts are written in a
way that allows another party to recreate the software, rerun the workflow, and
replicate the presented results.
