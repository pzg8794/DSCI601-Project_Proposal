# System components and interfaces

This document is the draft2 component note for the DSCI601 architecture package.
It is intentionally aligned with the current implementation repository rather
than with earlier bandit- or simulator-oriented planning documents.

## Design goals

- Reproducible: the same configuration and random seed should recreate the same outputs.
- Reviewable: each stage should be runnable, inspectable, and testable in isolation.
- Traceable: the writeup, the diagram, the implementation docs, and the code-review docs should describe the same system.
- Lightweight: reviewers should be able to install and run the workflow quickly on a normal CPU environment.

## Canonical architecture components

### 1. `PipelineConfig`
Role:
- loads the active JSON configuration,
- defines the parameters controlling the workflow,
- separates experiment settings from stage logic.

Expected fields include:
- random seed
- record count
- invalid record frequency
- missingness frequency
- bias level
- train/test split
- fairness threshold
- output directory

Why it matters:
- it provides the reproducibility contract for the whole run.

### 2. `PipelineContext`
Role:
- stores run metadata, artifact paths, and stage summaries,
- provides the shared state passed across the pipeline,
- prevents hard-coded file-path coupling between stages.

Why it matters:
- it keeps orchestration explicit and reviewable.

### 3. `StageResult`
Role:
- records what an individual stage produced,
- captures artifact paths and concise summary metadata,
- standardizes the outputs returned by each stage.

Why it matters:
- it gives every stage a visible output contract.

### 4. `PipelineStage`
Role:
- shared abstract base/interface for all executable stages,
- defines the common execution contract used by the orchestrator.

Why it matters:
- it is the mechanism that preserves narrow responsibilities and unit-test boundaries.

### 5. Seven concrete stage classes
The repository realizes the review workflow through seven explicit classes:

1. `DataCollectionStage`
   - generates the synthetic reviewer-safe dataset
   - writes raw records

2. `DataCleaningStage`
   - validates schema
   - removes intentionally invalid records
   - writes clean records

3. `DataPreparationStage`
   - creates deterministic train/test artifacts
   - prepares data for downstream modeling

4. `DataExplorationStage`
   - writes lightweight dataset summaries
   - reports group balance and completeness information

5. `DataMiningStage`
   - runs the lightweight modeling / prediction step
   - writes prediction artifacts

6. `EvaluationStage`
   - computes utility and fairness-oriented metrics
   - writes evaluation summaries

7. `ResultsPostprocessingStage`
   - converts outputs into reviewer-facing summary tables and figures
   - writes final CSV and SVG artifacts

Why they matter:
- together they operationalize a CRISP-DM-aligned workflow in a form that is directly reviewable.

## Orchestration layer

### 6. `ReviewPipeline`
Role:
- builds the ordered stage list,
- executes the stages end-to-end or to a named stopping point,
- writes the final manifest after execution completes.

Manifest responsibilities:
- store a copy of the active configuration,
- record stage outputs,
- preserve stage-level summary metadata.

Why it matters:
- it connects methodology, implementation order, and provenance.

## Interface layer

### 7. CLI module
Role:
- exposes one runnable command per required stage,
- exposes orchestration commands such as `run-all` and `merge-check`,
- makes the repository reviewable as software instead of as one notebook.

Why it matters:
- it is the reviewer-facing control surface.

## Artifact and storage contracts

Expected output pattern:
- a stable output root defined by config,
- numbered stage directories under the run output folder,
- final manifest written at the end of the run.

Representative artifacts:
- raw JSON
- clean JSON
- train/test JSON
- summary CSV
- predictions JSON
- metrics JSON
- final CSV
- SVG figure
- `pipeline_manifest.json`

Why it matters:
- reviewers can inspect intermediate and final outputs without guessing where anything was written.

## Validation layer

### 8. `merge-check` and CI validation
Role:
- run the fast reviewer configuration,
- confirm expected artifacts exist,
- execute the unit-test suite,
- mirror the same validation path locally and in GitHub Actions.

Why it matters:
- this is the merge-readiness contract for the repository.

## Bottom-line architectural claim

The repository should be understood as a CRISP-DM-aligned, reviewer-safe,
deterministic pipeline whose main strength is not algorithmic complexity but
clean stage boundaries, reproducible outputs, and merge-checkable validation.
