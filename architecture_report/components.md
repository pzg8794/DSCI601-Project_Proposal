# System components and interfaces

Overview
--------
This document enumerates the canonical system components, their responsibilities,
and the minimal interfaces (APIs / file contracts) required for reproducible
experiments and reviewer sanity checks.

File layout (canonical)
- `architecture/architecture_diagram.tex` — canonical TikZ diagram.
- `architecture/components.md` — this file (component responsibilities + interfaces).
- `architecture/requirements.md` — functional and non-functional requirements.
- `architecture/configs/` — small, fast example configs for reviewers (YAML).

Design goals (recap)
- Reproducible: configuration-driven experiments, fixed seeds, concise run artifacts.
- Reviewable: small, fast sample configs that run in minutes on CPU (no GPUs required).
- Traceable: logs and stats saved in structured JSON with run metadata and code version.
- Safe: use synthetic or small public subsets for reviewer runs; do not expose sensitive data.

Component descriptions
----------------------

Data Sources
- Role: provide input records (clinical-like records, synthetic traces, or quantum routing traces).
- Interface: dataset manifest (JSON/YAML) describing file paths, schema and access instructions.
- Output: files or streams containing rows with required fields (e.g., `group`, `features`, `label`, `sample_quality`).

Configs
- Role: single-source-of-truth for experiments. All runtime parameters are read from a YAML config.
- Example keys: `experiment_name`, `domain`, `n_steps`, `seed`, `policy.name`, `policy.params`, `env.params`, `output_dir`, `log_level`.
- Location: `architecture/configs/` for review configs; production configs live under `implementation/configs/`.

Environment / Simulator (Env)
- Role: model the testbed dynamics and sampling of contexts / observations.
- Minimal API (Python):

  class Env:
      def __init__(self, config: dict, seed: int | None = None):
          ...
      def sample_context(self) -> Any:
          """Return the next context or group id."""
      def pull(self, action: int, context: Any) -> float:
          """Apply action, return scalar reward (0/1 or real reward)."""
      def reset(self) -> None:
          """Reset RNG/state for reproducible runs."""

- Requirements: deterministic given the same `seed` and `config`.

Runner / Orchestrator
- Role: read config, initialize RNGs, run batched scenarios under fixed seeds, collect per-step logs and aggregated stats.
- CLI contract: `python run_baseline.py --config path/to/config.yaml` (or equivalent script). The runner must write results to `output_dir`.
- Output files (per run):
  - `baseline_logs.json` — array of per-step records: {t, seed, group/context, action, reward, extra}
  - `baseline_stats.json` — aggregated metrics (see Evaluator below)
  - `run_metadata.json` — config, code commit SHA, timestamps

Model / Policy (Policy)
- Role: implement action selection and online updates.
- Minimal API:
  - `select_action(context: Any) -> int`
  - `update(action: int, reward: float, context: Any | None = None) -> None`
- Examples: epsilon-greedy (non-contextual MAB), LinUCB (contextual baseline), iCMAB (informed contextual policy).

Evaluator
- Role: compute per-step and aggregated metrics for both utility and fairness.
- Required metrics (minimum):
  - utility: cumulative reward, average reward
  - per-group success rate: success_rate_g = sum(rewards_g)/count_g
  - fairness gaps: success_rate_gap = success_rate_0 - success_rate_1
  - clinical metrics: FNR_g, FPR_g (definitions in `requirements.md`)
  - routing metrics: path success rate, average latency
- Output: `baseline_stats.json` must include per-group metrics and `fairness_gap_*` keys.

Visualizer / Notebooks
- Role: generate reviewer-friendly figures and an executable notebook that reproduces the main plots.
- Typical figures: disparity-over-time, per-group selection rates, cumulative reward, calibration curves.
- Place notebooks in `implementation/code/notebooks/` and exported figures under `results/<run>/figures/`.

Results storage & provenance
- Layout: `results/<run_id>/` with `logs.json`, `stats.json`, `figures/`, and `run_metadata.json`.
- `run_metadata.json` must include: `config` (copy), `seed`, `start_time`, `end_time`, `git_commit_sha`, `python_version`.

Interfaces and contracts (summary)
- Runner must accept config YAML and write JSON artifacts.
- Env must implement deterministic `sample_context` and `pull` APIs.
- Policy must implement `select_action` and `update` and expose parameters for recording in `run_metadata`.

Quick CLI example (expected)

```bash
python implementation/code/run_baseline.py --config architecture/configs/fast_review.yaml
```

Configuration schema (minimal)

```yaml
experiment_name: fast_review_baseline
domain: synthetic
n_steps: 200
seed: 42
n_arms: 2
policy:
  name: epsilon_greedy
  params:
    epsilon: 0.05
env:
  group_prob: 0.7
  p_group0: [0.8, 0.2]
  p_group1: [0.2, 0.8]
output_dir: implementation/code/results/fast_review
```

Testing & CI
- Include unit tests for the Env and Policy interfaces (`implementation/code/tests/`).
- Provide a smoke-test GitHub Actions workflow that runs a fast config and verifies that `baseline_stats.json` exists.

Security & privacy
- Do not include protected health information in the canonical repo. When using real clinical datasets, provide a small synthetic sample and a `DATA_README.md` describing access steps.
