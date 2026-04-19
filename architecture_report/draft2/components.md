# Draft 2 system components and interfaces

This note explains the component view for the draft2 architecture package. It
is now aligned with the actual inherited design you described: quantum shared-
drive storage for collection, `evaluator` for cleaning and evaluation, and
`state_analysis` for preparation, exploration, and mining.

## Architectural intent

The architecture has to satisfy two obligations at the same time:

- preserve the project's CRISP-DM logic,
- preserve the repository's review logic as work is pushed and checked.

That means the important components are not only modeling stages. They also
include repository triggers, inherited storage access, orchestration,
validation, artifact publication, and merge evidence.

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
Representative responsibility:
- run settings and merge policy

Role:
- loads the active configuration,
- stores deterministic run settings,
- defines fairness thresholds, output paths, and review controls.

Why it matters:
- this is the reproducibility contract for the whole review path.

### 3. Quantum storage access path
Representative responsibility:
- inherited collection logic from the quantum project

Role:
- connects the repository to the shared-drive quantum data storage,
- treats that storage as the upstream data source,
- replaces the earlier placeholder notion of local synthetic collection.

Why it matters:
- the architecture is an integration architecture, not just a toy local pipeline.

## Core analysis objects

### 4. `evaluator`
Role:
- performs data cleaning,
- applies validity logic,
- computes evaluation summaries,
- serves as the quality-judgment object.

Why it matters:
- cleaning and evaluation are intentionally concentrated in one object that already owns quality logic.

### 5. `state_analysis`
Role:
- supports data exploration,
- performs data preparation,
- carries data-mining / state-level analytical logic.

Why it matters:
- this object sits across multiple CRISP-DM phases, which is exactly why the architecture should mention it explicitly.

### 6. Shared execution context / artifact contracts
Representative responsibilities:
- store run metadata,
- track artifact paths,
- standardize what each review phase produces.

Why they matter:
- they keep provenance explicit instead of burying it inside object internals.

## CRISP-DM execution responsibilities

### 7. Business-understanding realization
Repository realization:
- fairness objective
- acceptance criteria
- merge policy
- configuration values

Why it matters:
- it defines what counts as a successful run and what evidence is required.

### 8. Data-understanding realization
Repository realization:
- collection from shared-drive quantum storage
- exploratory work through `state_analysis`

Why it matters:
- reviewers can inspect both the upstream source and the exploratory interpretation of that source.

### 9. Data-preparation realization
Repository realization:
- cleaning through `evaluator`
- preparation through `state_analysis`

Why it matters:
- preprocessing stays visible and responsibility is assigned clearly.

### 10. Modeling realization
Repository realization:
- mining / analytical transformation through `state_analysis`

Why it matters:
- the architecture should show where actual mining responsibility lives.

### 11. Evaluation realization
Repository realization:
- metric computation and fairness checks through `evaluator`

Why it matters:
- evaluation is a first-class responsibility and should not be buried inside mining.

### 12. Deployment and review-delivery realization
Repository realization:
- postprocessing,
- figure/table generation,
- manifest writing,
- merge-ready reviewer outputs.

Why it matters:
- in this assignment context, deployment means publishing evidence for review.

## Orchestration and validation components

### 13. Review pipeline / CLI path
Role:
- builds the execution order,
- exposes `run-all` and `merge-check`,
- routes events into a reproducible validation path.

Why it matters:
- the architecture is reviewable as software rather than as one notebook.

### 14. Validation subsystem
Representative behaviors:
- unit tests
- smoke checks
- local `merge-check`
- CI mirror of the same validation path

Why it matters:
- this is the merge-readiness contract of the repository.

## Artifact and provenance components

Expected artifact classes:
- configuration snapshot
- shared-drive source references
- cleaned states
- prepared analysis inputs
- mined outputs / predictions
- evaluation summaries
- final tables and figures
- `pipeline_manifest.json`

Expected storage pattern:
- stable output root from config,
- reviewer-visible artifacts,
- final manifest tying the run together.

Why it matters:
- reviewers can follow the evidence chain from upstream source to merge decision.

## Bottom-line architectural claim

The repository should be understood as a reviewer-safe system in which pushes or
review commands trigger a deterministic CRISP-DM-aligned workflow built on top
of inherited quantum-project tooling. The central strength of the architecture
is the clear coupling between methodology, shared-drive collection,
`evaluator`, `state_analysis`, validation, artifact lineage, and merge
readiness.
