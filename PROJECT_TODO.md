# DSCI601 — Project To‑Do Tracker

Tracking fields:
- **Ask**: what the meeting requested
- **Meaning**: why it matters / what “done” looks like
- **Suggested work**: concrete edits/experiments to perform
- **Status**: `todo` | `in_progress` | `done`

## To‑Dos

| ID | Ask | Meaning | Suggested work (updates / solution / work) | Status | Where |
|---:|---|---|---|---|---|
| 10 | Keep a running decisions log | Prevent churn and accidental reversions | Append dated decisions/changes here when a wording choice is locked | in_progress | this file |
| 3 | Use formal voice; remove 1st person | Improve professionalism; reduce “class project” vibe | Remove “I/my/our/we”; rewrite as “this work/the project” | done | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |
| 9 | Clean up proposal wording/labels | Reduce jargon and tighten phrasing | Apply the agreed wording changes (CMAB/iCMAB phrasing $\rightarrow$ context-aware MABs, acronym shorthand at first mention $\rightarrow$ iC-/C-MABs, remove “required” and “(not optional)”, “template” $\rightarrow$ “framework”, “For the DSCI 601/602 …” $\rightarrow$ “For this project …”, “two required testbeds” $\rightarrow$ “two testbeds”, timeline $\rightarrow$ Phase 1/Phase 2) | done | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |
| 2 | Define what “diagnostics” means per domain | Avoid ambiguity (clinical vs system/runtime vs “decision workflow”) | Add 1–2 explicit sentences: define “diagnostic-like” as sequential test/model selection; explicitly *not* system debugging | done | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |
| 4 | Remove obvious admin/meta statements | Reduce fluff; keep the proposal content-focused | Remove statements that are obvious or add no technical value (e.g., “This is an individual project”, “class project” wording, or other administrative/meta phrasing). Leave timeline label decisions to Task 9. | done | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |
| 8 | Justify fairness need in quantum setting | Anticipate advisor pushback (“why fairness in quantum?”) | Add 2–3 sentences: fairness as service equity across user/flow groups under limited qubits; tie to allocation policies | done | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |
| 5 | Establish fairness metric(s) per testbed | Fairness has to be measurable before “mitigation” claims are credible | Diagnostic: pick 1–2 (e.g., equal opportunity via FNR gap, equalized odds via FNR/FPR gaps). Quantum: define “service equity” precisely (e.g., disparity in mean success probability/latency across flow groups) | done | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` + experiment notes |
| 7 | Propose methods X/Y/Z (context → fairness) | Avoid sounding like “we’ll magically make it fair” | Enumerate 2–3 concrete methods: (a) context enrichment/features, (b) fairness penalty/constraint, (c) calibration/thresholding policy | done | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |
| 1 | Emphasize the generic product/framework (domain-agnostic) | Make the contribution clear even if domains change | Rewrite the opening and recurring phrasing so the work is framed as a generic, reusable framework for fairness-aware sequential decision-making under missing/uneven context; iCMABs are an included model family, not the entire product | done | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |
| 6 | Show baseline unfairness, then improvements | Strong story: “problem → evidence → fix” | Run baseline policies and report disparities under missing context/shift; then show improvements with contextual + mitigation | todo | experiments + results log |
| 11 | Separate and scope the two domains throughout the proposal | Remove confusion from mixing domain terms; make sections parallel and explicit | Restructure Goal/Background/Scientific Merit/Broader Impacts/Approach so each domain has clearly labeled, parallel statements (clinical/diagnostic-like vs quantum routing/qubit allocation), with consistent terminology and minimal cross-domain leakage | done | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |
| 12 | Build a clean code review repository | Meet the code review assignment with a reviewer-safe, reproducible repo | Rebuild `Semester5/DSCI601/implementation/dsci601_experiments` as a CRISP+ML-oriented pipeline with explicit stage commands, tests, docs, and merge validation | done | `Semester5/DSCI601/implementation/dsci601_experiments` |
| 13 | Prepare architecture assignment materials | Ensure the architecture writeup is grounded in the cleaned implementation repo | Use the code review repo as the implementation baseline; document system layers, stage interactions, storage decisions, and reproducibility flow | in_progress | `Semester5/DSCI601/implementation/dsci601_experiments/docs/ARCHITECTURE.md` + assignment submission files |

## Change Log (Shareable)

- 2026-04-12: Cleaned for sharing; working notes are kept local-only.
- 2026-04-18: Code review repository rebuild completed, committed, and pushed; architecture assignment is now the active next deliverable.
