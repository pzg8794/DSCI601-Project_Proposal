
# DSCI601 architecture/report rewrite package

This package contains:
1. a diagnosis of the current problems
2. paste-ready replacement LaTeX for the most important write-up sections
3. a replacement `architecture_diagram.tex`
4. a repo cleanup checklist

---

## 1) What is wrong right now

### Core problems
- The current report still presents the repository as a **"Hybrid CRISP+ML"** pipeline instead of a **CRISP-DM-aligned** implementation.
- The current narrative lists seven review stages, but it does **not explain how those seven executable stages map onto CRISP-DM**.
- The current diagram is not only visually weak; it is **structurally misleading**:
  - the flow from exploration to mining is not connected,
  - the configuration / CLI / validation layer is described in the caption but not actually connected in the figure,
  - the figure therefore does not fully represent the system it claims to represent.
- `components.md` appears stale and conceptually mismatched with the current repo. It talks about YAML configs, environments, policies, and baseline bandit runners rather than the current synthetic, reviewer-safe code-review pipeline.

### What the write-up should prove instead
Your architecture artifact should prove four things:

1. **Methodological legitimacy**  
   The implementation is CRISP-DM-aligned, not a random script chain.

2. **Reviewability**  
   Every stage is independently runnable, testable, and inspectable.

3. **Reproducibility**  
   The same config and seed recreate the same artifacts.

4. **Traceability**  
   The architecture report, diagram, implementation docs, and code-review docs say the same thing.

---

## 2) Paste-ready replacement text for `architecture_report.tex`

### Replace the title with this

```latex
\title{{\LARGE\textbf{Architecture of a Reproducible CRISP-DM-Aligned Review Pipeline}}\\
{\Large\textit{Fairness-Aware Data Science Code Review Infrastructure}}\\
{\large\texttt{(Architecture Writeup)}}}
```

---

### Replace the full `Architecture Overview` section with this

```latex
%% ─────────────────────────────────────────────────────────────
\section{Architecture Overview}
%% ─────────────────────────────────────────────────────────────

This architecture writeup documents the implementation repository prepared for
the DSCI 601 code review assignment. The repository is intentionally designed as
a small, deterministic, reviewer-safe system whose stages can be executed
independently, inspected locally, and validated through the same merge-check
path used in continuous integration. The design goal is therefore not raw model
complexity. It is reproducible evidence that the repository satisfies the
assignment's expectations for separable execution, visible intermediate
artifacts, and test-backed reviewability.

Methodologically, the repository should be described as a
\textit{CRISP-DM-aligned} implementation rather than as a generic
``CRISP+ML'' pipeline. CRISP-DM provides the conceptual lifecycle, while the
repository decomposes that lifecycle into seven executable review stages that
match the code review deliverable. In that mapping, business understanding is
represented by the configuration, fairness objective, and reviewer-facing merge
criteria; data understanding is operationalized through data collection and data
exploration; data preparation is deliberately split into cleaning and
preparation so those responsibilities remain reviewable; modeling is represented
by the data-mining stage; evaluation remains explicit; and deployment is
represented by results postprocessing, artifact publication, and manifest-based
reproducibility.

The architecture therefore has two simultaneous logics. At the conceptual
level, it follows the CRISP-DM lifecycle. At the implementation level, it
exposes seven narrow stage boundaries so a reviewer can run, test, and inspect
each step independently. This dual framing is the central architectural claim of
the repository: it is not a loose collection of scripts, but a reproducible
pipeline whose methodological phases, software interfaces, and output artifacts
are intentionally aligned.
```

---

### Insert this immediately after the overview section for a higher-standard mapping

```latex
\begin{table}[t]
\centering
\caption{Mapping from CRISP-DM phases to executable review stages in the repository.}
\label{tab:crispdm_mapping}
\begin{tabular}{p{3.0cm} p{4.5cm}}
\toprule
\textbf{CRISP-DM phase} & \textbf{Repository realization} \\
\midrule
Business Understanding & configuration, fairness threshold, reviewer merge criteria \\
Data Understanding & data collection, data exploration / visualization \\
Data Preparation & data cleaning, data preparation \\
Modeling & data mining \\
Evaluation & evaluation \\
Deployment & results postprocessing, final artifacts, manifest, merge-check path \\
\bottomrule
\end{tabular}
\end{table}
```

---

### Replace the intro paragraph in `System Architecture` with this

```latex
%% ─────────────────────────────────────────────────────────────
\section{System Architecture}
%% ─────────────────────────────────────────────────────────────

Figure~\ref{fig:architecture} presents the system as three coupled views. The
top layer contains the cross-cutting control mechanisms: configuration,
command-line orchestration, and validation. The middle layer contains the seven
executable repository stages that implement the review workflow. The bottom
layer contains the artifact and provenance model through which each stage writes
inspectable outputs and the pipeline records the final manifest. This framing is
important because the architecture is being evaluated not only as software
structure, but as a reviewer-facing reproducibility contract.
```

---

### Replace the figure caption with this

```latex
\caption{CRISP-DM-aligned architecture of the reviewer-safe pipeline. The figure
distinguishes cross-cutting control mechanisms from the seven executable review
stages and the shared artifact/provenance layer. Together these elements make
the workflow deterministic, stage-testable, and merge-checkable.}
```

---

### Replace the first paragraph of `Stage Layer` with this

```latex
Each lifecycle step is implemented as its own concrete class under a shared
\texttt{PipelineStage} interface. This is not merely an object-oriented style
choice. It is the mechanism that preserves review boundaries. Each stage owns a
narrow responsibility, a concrete input contract, a concrete output contract,
and a corresponding testing surface. The architecture therefore maps methodology
to software in a form that another party can validate both stage-by-stage and
end-to-end.
```

---

### Replace the opening paragraph of `Conclusion` with this

```latex
The architecture emphasizes methodological clarity, determinism, and
inspectability. Its main contribution is not algorithmic novelty, but the clean
translation of a CRISP-DM-aligned workflow into a reviewable software artifact
with explicit stage boundaries, reproducible outputs, and a merge-validation
path. That is the level at which the repository should be judged, and it is the
level at which this architecture writeup should present it.
```

---

## 3) Replacement `architecture_diagram.tex`

Use this as a full replacement for the current TikZ file.

```latex
% Revised architecture diagram for the DSCI601 architecture report.
% This version fixes the broken stage flow, makes the cross-cutting layers
% explicit, and frames the repository as a CRISP-DM-aligned review pipeline.

\begin{tikzpicture}[
  font=\sffamily,
  >=Latex,
  support/.style={
    rectangle,
    draw=black,
    rounded corners,
    minimum height=0.95cm,
    text width=3.2cm,
    align=center,
    fill=gray!10,
    line width=0.45pt
  },
  stage/.style={
    rectangle,
    draw=black,
    rounded corners,
    minimum height=1.2cm,
    text width=2.25cm,
    align=center,
    line width=0.45pt
  },
  store/.style={
    rectangle,
    draw=black,
    rounded corners,
    minimum height=1.0cm,
    text width=12.8cm,
    align=center,
    fill=gray!8,
    line width=0.45pt
  },
  framebox/.style={
    rectangle,
    draw=black!45,
    rounded corners,
    inner sep=8pt,
    line width=0.4pt
  },
  arrow/.style={->, line width=0.75pt},
  dashedarrow/.style={->, dashed, line width=0.6pt},
  note/.style={font=\scriptsize, align=center}
]

% ─────────────────────────────────────────────────────────────
% Support / control layer
% ─────────────────────────────────────────────────────────────
\node[support, fill=phase1blue!12] (config) at (2.7, 2.2)
  {\textbf{Configuration}\\seed, split, missingness,\\fairness threshold};

\node[support, fill=phase2green!12] (cli) at (8.1, 2.2)
  {\textbf{CLI Interface}\\stage commands,\\\texttt{run-all}, \texttt{merge-check}};

\node[support, fill=phase4purple!12] (tests) at (13.5, 2.2)
  {\textbf{Validation Layer}\\unit tests, smoke run,\\CI merge gate};

% ─────────────────────────────────────────────────────────────
% Executable stage layer
% ─────────────────────────────────────────────────────────────
\node[stage, fill=phase1blue!16] (collect) at (0.0, 0)
  {\textbf{1. Data}\\\textbf{Collection}\\\scriptsize raw JSON};

\node[stage, fill=phase1blue!16] (clean) at (2.7, 0)
  {\textbf{2. Data}\\\textbf{Cleaning}\\\scriptsize clean JSON};

\node[stage, fill=phase2green!16] (prepare) at (5.4, 0)
  {\textbf{3. Data}\\\textbf{Preparation}\\\scriptsize train/test JSON};

\node[stage, fill=phase2green!16] (explore) at (8.1, 0)
  {\textbf{4. Exploration}\\\textbf{/ Visualization}\\\scriptsize summaries};

\node[stage, fill=phase3orange!16] (mine) at (10.8, 0)
  {\textbf{5. Data}\\\textbf{Mining}\\\scriptsize predictions};

\node[stage, fill=phase3orange!16] (evaluate) at (13.5, 0)
  {\textbf{6. Evaluation}\\\scriptsize utility + fairness\\\scriptsize metrics};

\node[stage, fill=phase4purple!16] (post) at (16.2, 0)
  {\textbf{7. Results}\\\textbf{Postprocessing}\\\scriptsize CSV + SVG};

% Stage flow
\draw[arrow] (collect) -- (clean);
\draw[arrow] (clean) -- (prepare);
\draw[arrow] (prepare) -- (explore);
\draw[arrow] (explore) -- (mine);
\draw[arrow] (mine) -- (evaluate);
\draw[arrow] (evaluate) -- (post);

% Framing box for executable pipeline
\node[framebox, fit=(collect)(post), label={[font=\small]above:Executable review pipeline (CRISP-DM-aligned)}] (pipelineframe) {};

% Cross-cutting control arrows
\draw[dashedarrow] (config.south) -- (pipelineframe.north west);
\draw[dashedarrow] (cli.south) -- (pipelineframe.north);
\draw[dashedarrow] (tests.south) -- (pipelineframe.north east);

% ─────────────────────────────────────────────────────────────
% Artifact / provenance layer
% ─────────────────────────────────────────────────────────────
\node[store] (storage) at (8.1, -2.2)
  {\textbf{Artifact and provenance layer}\\
   numbered stage outputs under \texttt{results/fast\_review/} \quad + \quad
   \texttt{pipeline\_manifest.json} recording configuration, stage outputs, and summaries};

\draw[dashedarrow] (pipelineframe.south) -- (storage.north);

% Mapping note
\node[note] at (8.1, -3.55)
  {\textbf{CRISP-DM mapping:} business understanding = configuration + fairness goals;
   data understanding = collection + exploration;
   data preparation = cleaning + preparation;
   modeling = mining;
   evaluation = evaluation;
   deployment = postprocessing + manifest + merge validation.};

\end{tikzpicture}
```

---

## 4) One more fix you should not skip

### `components.md` needs to be rewritten or removed from the submission path
Right now it appears to describe a different system:
- YAML configs
- environment / simulator APIs
- policy APIs
- baseline runner scripts
- bandit-oriented output files

That creates a credibility problem because your canonical architecture folder says
`components.md` supports the write-up. If a reviewer opens it and finds a
different architecture, it weakens the whole package.

### Safer replacement direction
Rewrite `components.md` to match the current repo and keep it short:

- `PipelineConfig`
- `PipelineContext`
- `StageResult`
- `PipelineStage`
- seven concrete stage classes
- `ReviewPipeline`
- CLI commands
- artifact directories
- manifest / provenance record
- merge-check / CI validation

---

## 5) Final repo cleanup checklist

- [ ] Rename the framing from `CRISP+ML` to `CRISP-DM-aligned`
- [ ] Add an explicit CRISP-DM mapping table
- [ ] Replace the diagram with a flow that is actually connected
- [ ] Make the support layer visibly connected to the executable pipeline
- [ ] Keep the write-up centered on reproducibility, testability, and reviewability
- [ ] Rewrite or retire stale `components.md`
- [ ] Keep wording aligned with the survey/proposal vocabulary
- [ ] Avoid vague claims like “recognized methodology”; name CRISP-DM directly
