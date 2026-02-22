# Option 6 (DSCI601) — Project To‑Do Tracker

Source notes reviewed:
- `Semester5/DSCI601/DSCI601-Project_Proposal/notes/02-20 Refining a Research Proposal by Separating Core Methodology from Domain-Specific Applications-Summary.md`
- `Semester5/DSCI601/DSCI601-Project_Proposal/notes/02-20 Refining a Research Proposal by Separating Core Methodology from Domain-Specific Applications-Meeting Summary.md`
- `Semester5/DSCI601/DSCI601-Project_Proposal/notes/02-20 Refining a Research Proposal by Separating Core Methodology from Domain-Specific Applications-Meeting Minutes.md`

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
| 2 | Define what “diagnostics” means per domain | Avoid ambiguity (clinical vs system/runtime vs “decision workflow”) | Add 1–2 explicit sentences: define “diagnostic-like” as sequential test/model selection; explicitly *not* system debugging | todo | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |
| 4 | Remove obvious admin/meta statements | Reduce fluff; keep the proposal content-focused | Remove statements that are obvious or add no technical value (e.g., “This is an individual project”, “class project” wording, or other administrative/meta phrasing). Leave timeline label decisions to Task 9. | done | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |
| 8 | Justify fairness need in quantum setting | Anticipate advisor pushback (“why fairness in quantum?”) | Add 2–3 sentences: fairness as service equity across user/flow groups under limited qubits; tie to allocation policies | todo | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |
| 5 | Establish fairness metric(s) per testbed | Fairness has to be measurable before “mitigation” claims are credible | Diagnostic: pick 1–2 (e.g., equal opportunity via FNR gap, equalized odds via FNR/FPR gaps). Quantum: define “service equity” precisely (e.g., disparity in mean success probability/latency across flow groups) | todo | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` + experiment notes |
| 7 | Propose methods X/Y/Z (context → fairness) | Avoid sounding like “we’ll magically make it fair” | Enumerate 2–3 concrete methods: (a) context enrichment/features, (b) fairness penalty/constraint, (c) calibration/thresholding policy | todo | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |
| 1 | Emphasize the generic product/framework (domain-agnostic) | Make the contribution clear even if domains change | Rewrite the opening and recurring phrasing so the work is framed as a generic, reusable framework for fairness-aware sequential decision-making under missing/uneven context; iCMABs are an included model family, not the entire product | todo | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |
| 6 | Show baseline unfairness, then improvements | Strong story: “problem → evidence → fix” | Run baseline policies and report disparities under missing context/shift; then show improvements with contextual + mitigation | todo | experiments + results log |
| 11 | Separate and scope the two domains throughout the proposal | Remove confusion from mixing domain terms; make sections parallel and explicit | Restructure Goal/Background/Scientific Merit/Broader Impacts/Approach so each domain has clearly labeled, parallel statements (clinical/diagnostic-like vs quantum routing/qubit allocation), with consistent terminology and minimal cross-domain leakage | todo | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |

## Decisions Log

- 2026-02-22: Created this tracker from the 02-20 notes.
- 2026-02-22: Locked workflow: propose changes first; apply edits only after explicit approval.
- 2026-02-22: Reset statuses to `todo` to review and apply updates one-by-one (Option A workflow).
- 2026-02-22: Reordered tasks from easiest $\rightarrow$ hardest to support incremental edits with checkpoints.
- 2026-02-22: Moved Task 3 (remove first person) to the top; narrowed Task 9 to timeline label clarity (DSCI 601/602 $\rightarrow$ Phase/Term labels).
- 2026-02-22: Reverted unauthorized `main.tex` edits; Task 3 set back to `todo` until explicitly approved.
- 2026-02-22: Cleaned task scopes: Task 1 = generic product only; Task 9 = ISTE780 + timeline labels (optionally iCMAB naming); domain separation moved to Task 11 (hardest).
- 2026-02-22: Refined Task 4 to “remove obvious admin/meta statements” (distinct from Task 3 voice changes).
- 2026-02-22: Applied Task 3 (approved): removed first-person voice in `main.tex` with minimal wording changes (our/we/my $\rightarrow$ neutral third-person phrasing).
- 2026-02-22: Migrated Option 6 assets into `Semester5/DSCI601/DSCI601-Project_Proposal` (git repo): merged `main.tex`, added `.gitignore`, and moved meeting notes + `PROJECT_TODO.md`.
- 2026-02-22: Applied Task 4: removed the “This is an individual project.” admin/meta sentence from the Approach paragraph.
- 2026-02-22: Applied Task 9 (approved change list):
  - Replace “fairness-aware CMAB/iCMAB” with “fairness aware and contextual MABs” in the evaluation/approach phrasing.
  - Replace “evaluating CMAB/iCMAB” with “evaluating context aware MABs”.
  - Remove “(not optional)”.
  - Replace “reproducible template” with “reproducible framework”.
  - Replace “For the DSCI 601/602 …” with “For this project …”.
  - Replace “(two required testbeds + …)” with “(two testbeds + …)”.
  - Replace “Timeline: DSCI 601/DSCI 602 …” with “Phase 1 includes …; Phase 2 includes …”.
  - Remove all remaining uses of the word “required”.
- 2026-02-22: Updated acronym order at first mention: (CMAB / iCMAB) $\rightarrow$ (iC-/C-MABs).
- 2026-02-22: Updated prior-work wording: replaced “ISTE780” mentions with {\it Equitable Bioinformatics} and updated the reference entry to an “unpublished paper” style.
- 2026-02-22: Wording refinement (readability): replaced “fairness and context aware” with “fairness aware and contextual” across the proposal (commit `9f4fbbb`).
- 2026-02-22: Acronym refinement (clarity): revised the first-mention shorthand from (iC-/C-) to (iC-/C-MABs) after feedback that dropping “MAB(s)” made the acronym confusing (commits `637469d`, `cada8ed`).
- 2026-02-22: Two-domain clarity (opening summary, before deliverables): kept Option 1 wording for later reporting — “Although this framework is generic in nature, this work focuses on measuring and improving fairness across two domains—clinical (diagnostic-like) decision-making and quantum-network routing/qubit allocation—through the following deliverables.” Applied Option 2 as the more suitable proposal phrasing by adding: “The work on this generic framework focuses on measuring and improving fairness across the clinical (diagnostic-like) and quantum domains, through the following deliverables:” immediately before the deliverables list in `main.tex`.
- 2026-02-22: Background (two-domain opening): rewrote the first sentence to explicitly cover both domains — “Many real-world workflows in both clinical diagnostics and quantum networking require sequential choices under uncertainty, resource constraints, and distribution shift.”
- 2026-02-22: Background (wording cleanup): removed the parenthetical “(context)” from “side information (context)” for cleaner reading.
- 2026-02-22: Background (domain framing): changed “Multi-armed bandits …” to start with “In both domains, …” to make it clear the bandit framing applies to both the clinical and quantum domains before expanding the clinical diagnostic context.
- 2026-02-22: Background (transition): changed “In diagnostics, …” to “However, in clinical diagnostics, …” to smooth the transition from the cross-domain bandit framing to the clinical-specific context example.
- 2026-02-22: Background (risk sentence): rewrote “This creates both performance risk and fairness risk …” to “These limitations create performance and fairness risks …” to avoid the rigid “both … and …” phrasing and to tie the risk explicitly to aggregate optimization hiding subgroup error spikes.
- 2026-02-22: Background (two domain problems): added a quantum-network domain context sentence (link-quality/load/qubit signals; delayed/noisy/partial observation) before the clinical diagnostic context sentence to make the two domain problem statements explicit.
- 2026-02-22: Background (integration sentence): updated the novelty sentence to state the framework is evaluated in both the diagnostic-like and quantum-network environments while tracking fairness disparities over time.
- 2026-02-22: Background (prior-work wording): changed “and on prior work,” to “and previous work on …” to improve flow into the {\it Equitable Bioinformatics} reference.
