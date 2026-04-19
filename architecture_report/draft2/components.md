# Draft 2 system components and interfaces

This note explains the component view for the draft2 architecture package. It
is written to match the repository as a **push-validated, CRISP-DM-aligned
review system** rather than as a small standalone ML demo.

## Architectural intent

The architecture has to satisfy two obligations at the same time:

- preserve the project's CRISP-DM logic,
- preserve the repository's review logic as work is pushed and checked.

That means the important components are not only modeling stages. They also
include repository triggers, configuration, orchestration, validation, artifact
publication, and merge evidence.

## Layered component model

### 1. Event layer
This layer determines when the architecture becomes active.

Representative inputs:
- repository pushes
- pull requests
- developer stage commands
- `run-all`
- `merge-check`

Why it matters:
- the repository is not just run manually once; it is meant to check work as it changes.

### 2. Review policy and configuration subsystem
Representative component:
- `PipelineConfig`

Role:
- loads the active JSON configuration,
- stores deterministic run settings,
- defines fairness thresholds, split policy, output paths, and other run controls.

Why it matters:
- this is the reproducibility contract for the whole review path.

### 3. Shared execution context
Representative components:
- `PipelineContext`
- `StageResult`

Role of `PipelineContext`:
- stores run metadata, artifact paths, and stage summaries,
- provides the shared state passed across the pipeline,
- avoids hard-coded coupling between stages.

Role of `StageResult`:
- standardizes what each stage returns,
- records artifact paths and concise summary metadata,
- makes stage contracts visible.

Why they matter:
- together they make provenance explicit rather than implicit.

### 4. Pipeline stage interface
Representative component:
- `PipelineStage`

Role:
- shared abstract base / interface for executable stages,
- defines the common execution contract used by the orchestrator.

Why it matters:
- it preserves narrow responsibilities and testable stage boundaries.

## CRISP-DM execution components

The repository realizes CRISP-DM through explicit review stages.

### 5. Business-understanding realization
This phase is represented operationally rather than as a separate numerical stage.

Repository realization:
- fairness objective
- acceptance criteria
- merge policy
- configuration values

Why it matters:
- it defines what counts as a successful run and what evidence is required.

### 6. Data-understanding realization
Representative stage components:
- `DataCollectionStage`
- `DataExplorationStage`

Role:
- generate or ingest the reviewer-safe dataset,
- expose what the dataset contains before downstream modeling,
- summarize group balance, completeness, and basic dataset structure.

Why it matters:
- reviewers can inspect both the incoming data and the exploratory evidence.

### 7. Data-preparation realization
Representative stage components:
- `DataCleaningStage`
- `DataPreparationStage`

Role:
- validate schema,
- remove intentionally invalid records,
- create deterministic train/test artifacts.

Why it matters:
- preprocessing stays visible instead of being hidden inside modeling code.

### 8. Modeling realization
Representative stage component:
- `DataMiningStage`

Role:
- run the lightweight modeling / prediction step,
- produce predictions as explicit artifacts.

Why it matters:
- modeling is reviewable without dominating the whole architecture.

### 9. Evaluation realization
Representative stage component:
- `EvaluationStage`

Role:
- compute utility-oriented and fairness-oriented metrics,
- produce the evidence needed for quality judgment.

Why it matters:
- evaluation is a first-class phase, not a footnote after modeling.

### 10. Deployment and review-delivery realization
Representative stage component:
- `ResultsPostprocessingStage`

Role:
- convert raw outputs into reviewer-facing tables and figures,
- publish final CSV / SVG outputs,
- support manifest-based reproducibility and review delivery.

Why it matters:
- in this assignment context, deployment means producing merge-ready evidence.

## Orchestration and validation components

### 11. `ReviewPipeline`
Role:
- builds the ordered execution plan,
- runs stages end-to-end or to a named stopping point,
- writes the final manifest after execution completes.

Why it matters:
- it connects methodology, execution order, and provenance.

### 12. CLI module
Role:
- exposes one runnable command per required stage,
- exposes orchestration commands such as `run-all` and `merge-check`,
- gives reviewers a stable control surface.

Why it matters:
- the architecture is reviewable as software rather than as one notebook.

### 13. Validation subsystem
Representative behaviors:
- unit tests
- smoke checks
- local `merge-check`
- CI mirror of the same validation path

Why it matters:
- this is the actual merge-readiness contract of the repository.

## Artifact and provenance components

Expected artifact classes:
- configuration snapshot
- raw records
- exploratory summaries
- clean records
- train/test artifacts
- predictions
- metrics
- final CSV tables
- SVG figures
- `pipeline_manifest.json`

Expected storage pattern:
- stable output root from config,
- numbered stage directories,
- final manifest tying the run together.

Why it matters:
- reviewers can follow the evidence chain from event to merge decision.

## Bottom-line architectural claim

The repository should be understood as a reviewer-safe system in which pushes or
review commands trigger a deterministic CRISP-DM-aligned workflow. The central
strength of the architecture is not algorithmic scale. It is the clear coupling
between methodology, stage execution, validation, artifact lineage, and merge
readiness.
