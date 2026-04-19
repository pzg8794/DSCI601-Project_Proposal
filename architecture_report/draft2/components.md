# Draft 2 system components, stage ownership, and replication interfaces

This note now matches the strengthened `draft2` architecture report and figure.
It describes the repository as a **reproducible CRISP-DM review and replication
pipeline** built on inherited `quantum_project` components.

## Architectural intent

The architecture must satisfy four obligations at once:

- preserve the CRISP-DM logic of the project,
- preserve the code-review and validation workflow for the repository,
- preserve the ability for another party to recreate the system and replicate
  the presented results,
- add a repository-side layer that measures **fairness against performance**
  rather than treating fairness as detached commentary.

That means the important components are not only stage classes. They also
include shared-drive storage access, notebooks, local and GCP entry paths,
orchestration, validation, provenance, and the new fairness--performance
synthesis layer.

## Layered component model

### 1. High-level context layer
Representative responsibilities:
- business understanding,
- data understanding,
- fairness criteria,
- acceptance rules,
- replication target.

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

### 3. Execution layer
Representative responsibilities:
- collection,
- cleaning,
- preparation and exploration,
- modeling / mining,
- evaluation.

Why it matters:
- this is where inherited quantum components produce the results that later get
  reviewed and compared.

### 4. Fairness--performance synthesis layer
Representative responsibilities:
- combine allocator context,
- consume runner outputs,
- consume evaluator summaries,
- compare fairness criteria against inherited performance metrics,
- generate tradeoff tables and figures.

Why it matters:
- this is the new layer missing from the earlier draft.

### 5. Artifacts and replication outputs layer
Representative responsibilities:
- save figures,
- save tables,
- save manifest/provenance outputs,
- keep notebooks and shared-drive outputs reproducible and shareable.

Why it matters:
- this layer is what another party actually reruns and inspects.

## Stage-to-object master mapping

| Stage | Component / quantum object | Description (what it does) | Usage (how it is used) |
|---|---|---|---|
| Data Collection | `LocalBackupManager`, `GoogleDriveBackupManager`, registry / latest-state lookup | resolves shared-drive paths and retrieves matching framework/model state | notebooks, local scripts, and GCP runs begin by scanning `quantum_data_lake/` and loading compatible saved state |
| Data Cleaning | `MultiRunEvaluator`, `_infer_models_from_state()`, `__eq__()`, `ensure_summary_contract()` | validates state compatibility, normalizes scenario storage, and repairs summary payloads when needed | collection outputs are filtered into evaluator-valid state before downstream analysis or plotting |
| Data Preparation / Exploration | `state_analysis.py`, evaluator `scenarios_stats`, evaluator `scenarios_results` | consumes evaluator summaries and restructures them into flattened, scenario-oriented analysis tables | notebooks and local scripts use these outputs for scenario summaries, master datasets, and replication-ready tables |
| Modeling / Mining | `AllocatorRunner`, `QuantumExperimentRunner`, allocator objects | executes runs, assigns route qubit allocations, and produces model-level outputs and traces | local, notebook, and GCP paths all use the runner chain to generate comparable outputs across scenarios |
| Evaluation | `MultiRunEvaluator.calculate_scenario_winner()`, `calculate_scenario_performance()`, `calculate_scenarios_performance()` | computes winner counts, average gap, average efficiency, oracle reward, and scenario-level summaries | used to turn raw runner outputs into reviewer-visible performance evidence |
| Fairness--Performance Synthesis | new repository-side fairness component, evaluator metrics, allocator context, runner outputs, `QuantumEvaluatorVisualizer`, robustness plotting path | compares fairness criteria against inherited performance metrics and creates tradeoff views | used after evaluation to produce fairness-versus-performance tables, plots, and reviewer-facing comparisons |
| Review Delivery / Replication Outputs | notebooks, `visualizer.py`, shared-drive exports, `pipeline_manifest.json` | publishes figures, tables, notebooks, and provenance artifacts | collaborators rerun notebooks and inspect shared-drive artifacts to reproduce, interpret, and share results |

## Inherited storage and execution components

### 6. Shared-drive quantum data lake
Representative responsibility:
- shared upstream source for framework state, model state, visualizations, and
  day-partitioned outputs.

Representative path pattern:
- `quantum_data_lake/{component}/day_YYYYMMDD/`

Why it matters:
- this is the authoritative source and destination for replication artifacts.

### 7. Backup-manager / registry path
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

### 8. `AllocatorRunner`
Role:
- initialize allocator objects,
- propagate testbed and physics configuration,
- execute full runs through the evaluator,
- invoke robustness plotting,
- verify that evaluator summaries were persisted correctly.

Why it matters:
- this object sits between configuration and full experiment execution.

### 9. `QuantumExperimentRunner`
Role:
- execute per-experiment runs,
- generate model-specific results and traces,
- store experiment-level outputs consumed by the evaluator.

Why it matters:
- this object is where mining and experiment execution become concrete.

### 10. `MultiRunEvaluator`
Role:
- validate and clean state,
- own evaluation summaries,
- compute scenario-level winners and metrics,
- normalize scenario storage,
- preserve the evaluation contract consumed by analysis.

Why it matters:
- cleaning and evaluation are intentionally concentrated here.

### 11. `state_analysis`
Role:
- consume evaluator summaries,
- restructure scenario outputs,
- support preparation, exploration, flattened analysis, and replication-ready
  summary tables.

Why it matters:
- this is the bridge between saved evaluator state and human-readable analysis.

### 12. `QuantumEvaluatorVisualizer` and plotting path
Role:
- load saved results,
- generate comparison plots,
- expose robustness and scenario summaries visually.

Why it matters:
- this is one of the main consumers of the fairness--performance layer.

## User workflow components

### 13. Setup path
Representative steps:
- clone repo and install requirements locally,
- or open shared notebook and mount Drive,
- or provision GCP VM and run startup script.

### 14. Run path
Representative actions:
- run notebook cells,
- run local smoke/validation scripts,
- run GCP batch scripts,
- run `merge-check` for repository validation.

### 15. Interpretation path
Representative components:
- visualizer,
- notebook plots,
- evaluator summaries,
- saved day directories in the data lake.

### 16. Sharing path
Representative behavior:
- save outputs back into the shared-drive data lake so collaborators can inspect,
  compare, and rerun them.

## Bottom-line architectural claim

`draft2` should be understood as a reviewer-safe and replication-safe system in
which users may enter through notebooks, local installation, or GCP execution;
collection begins from the shared-drive quantum data lake; allocator, runner,
evaluator, and state-analysis logic structure the core pipeline; and a new
fairness--performance synthesis layer compares fairness criteria against the
performance metrics already produced by the inherited quantum workflow.
