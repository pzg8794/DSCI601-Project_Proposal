# CRISP+ML Pipeline — Component Reference (draft1)

Each component is listed with its CRISP-DM role and the quantum-project object it inherits from or mirrors directly.

## Quantum Data Lake

Stage 1 fetches real experiment artifacts from the Google Shared Drive folder:
`12mZyGQHD__G54g2yCYIyWfXydhO3DxIt`

## Stage Layer — CRISP-DM → Stage → Quantum Object

| # | Stage class | CRISP-DM phase | Quantum object | Output artifact |
|---|---|---|---|---|
| 1 | `DataCollectionStage` | Data Understanding | `GoogleDriveBackupManager` → `build_registry()` + `get_latest_state()` | `01_data_collection/raw_records.json` |
| 2 | `DataCleaningStage` | Data Understanding | `MultiRunEvaluator` → `_infer_models_from_state()` + `__eq__` validation contract | `02_data_cleaning/clean_records.json` |
| 3 | `DataPreparationStage` | Data Preparation | `state_analysis` → `scenarios_stats` decomposition → seeded train/test split | `03_data_preparation/train_records.json`, `test_records.json` |
| 4 | `DataExplorationStage` | Data Understanding | `state_analysis` → `display_experiment_conditions()`, `print_summary()` | `04_data_exploration/exploration_summary.csv`, `exploration_group_counts.svg` |
| 5 | `DataMiningStage` | Modeling | `QuantumExperimentRunner` → `run_experiment()` | `05_data_mining/predictions.json`, `model_summary.json` |
| 6 | `EvaluationStage` | Evaluation | `MultiRunEvaluator` → `calculate_scenario_winner()` | `06_evaluation/evaluation.json` |
| 7 | `ResultsPostprocessingStage` | Deployment | `visualizer.py` | `07_results_postprocessing/final_results.csv`, `final_accuracy_chart.svg`, `final_report.md` |
