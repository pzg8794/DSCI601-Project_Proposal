# CRISP+ML Pipeline — Component Reference (draft1)

This file documents each software component in the pipeline and its role.

## Configuration Layer

| Component | File | Role |
|---|---|---|
| `PipelineConfig` | `src/dsci601_experiments/config.py` | Loads JSON config; exposes seed, split, bias, fairness threshold, output root |

## Data Model Layer

| Component | File | Role |
|---|---|---|
| `Record` | `src/dsci601_experiments/models.py` | Dataclass for synthetic observations; carries group membership and fairness-relevant fields |
| `PipelineContext` | `src/dsci601_experiments/models.py` | Shared state passed across stages; holds config, artifact paths, stage results |
| `StageResult` | `src/dsci601_experiments/models.py` | Per-stage output metadata: artifact paths and summary dict |

## Stage Layer

| # | Class | CRISP-DM Phase | Output artifact |
|---|---|---|---|
| 1 | `DataCollectionStage` | Data Understanding | `01_data_collection/raw_records.json` |
| 2 | `DataCleaningStage` | Data Understanding | `02_data_cleaning/clean_records.json` |
| 3 | `DataPreparationStage` | Data Preparation | `03_data_preparation/train_records.json`, `test_records.json` |
| 4 | `DataExplorationStage` | Data Understanding | `04_data_exploration/exploration_summary.csv`, `exploration_group_counts.svg` |
| 5 | `DataMiningStage` | Modeling | `05_data_mining/predictions.json`, `model_summary.json` |
| 6 | `EvaluationStage` | Evaluation | `06_evaluation/evaluation.json` |
| 7 | `ResultsPostprocessingStage` | Deployment | `07_results_postprocessing/final_results.csv`, `final_accuracy_chart.svg`, `final_report.md` |

## Orchestration Layer

| Component | File | Role |
|---|---|---|
| `ReviewPipeline` | `src/dsci601_experiments/pipeline.py` | Builds ordered stage list; runs end-to-end or to a named stage; writes `pipeline_manifest.json` |

## Interface Layer

| Command | What it does |
|---|---|
| `run-all` | Execute all 7 stages in sequence |
| `merge-check` | Run full pipeline + unit tests (local quality gate) |
| `collect` / `clean` / `prepare` / `explore` / `mine` / `evaluate` / `postprocess` | Run one stage individually |

## CI / Publish

| Workflow | File | Role |
|---|---|---|
| CI | `.github/workflows/ci.yml` | Runs `pytest -q` on every push/PR to main |
| Publish | `.github/workflows/publish.yml` | Builds sdist + wheel on tagged releases |