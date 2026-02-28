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
| 2 | Define what “diagnostics” means per domain | Avoid ambiguity (clinical vs system/runtime vs “decision workflow”) | Add 1–2 explicit sentences: define “diagnostic-like” as sequential test/model selection; explicitly *not* system debugging | done | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |
| 4 | Remove obvious admin/meta statements | Reduce fluff; keep the proposal content-focused | Remove statements that are obvious or add no technical value (e.g., “This is an individual project”, “class project” wording, or other administrative/meta phrasing). Leave timeline label decisions to Task 9. | done | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |
| 8 | Justify fairness need in quantum setting | Anticipate advisor pushback (“why fairness in quantum?”) | Add 2–3 sentences: fairness as service equity across user/flow groups under limited qubits; tie to allocation policies | done | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |
| 5 | Establish fairness metric(s) per testbed | Fairness has to be measurable before “mitigation” claims are credible | Diagnostic: pick 1–2 (e.g., equal opportunity via FNR gap, equalized odds via FNR/FPR gaps). Quantum: define “service equity” precisely (e.g., disparity in mean success probability/latency across flow groups) | done | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` + experiment notes |
| 7 | Propose methods X/Y/Z (context → fairness) | Avoid sounding like “we’ll magically make it fair” | Enumerate 2–3 concrete methods: (a) context enrichment/features, (b) fairness penalty/constraint, (c) calibration/thresholding policy | done | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |
| 1 | Emphasize the generic product/framework (domain-agnostic) | Make the contribution clear even if domains change | Rewrite the opening and recurring phrasing so the work is framed as a generic, reusable framework for fairness-aware sequential decision-making under missing/uneven context; iCMABs are an included model family, not the entire product | done | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |
| 6 | Show baseline unfairness, then improvements | Strong story: “problem → evidence → fix” | Run baseline policies and report disparities under missing context/shift; then show improvements with contextual + mitigation | todo | experiments + results log |
| 11 | Separate and scope the two domains throughout the proposal | Remove confusion from mixing domain terms; make sections parallel and explicit | Restructure Goal/Background/Scientific Merit/Broader Impacts/Approach so each domain has clearly labeled, parallel statements (clinical/diagnostic-like vs quantum routing/qubit allocation), with consistent terminology and minimal cross-domain leakage | done | `Semester5/DSCI601/DSCI601-Project_Proposal/main.tex` |

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
- 2026-02-22: Background (reduce repetition): changed the integration sentence to say the framework is evaluated “in both domains” instead of repeating the full environment names in the same section.
- 2026-02-22: Structure (Background $\rightarrow$ Merit): moved the citations/prior-work + novelty/integration paragraph (and the “Unlike prior work …” sentence) from Background into Scientific Merit so Background stays problem-focused and Merit carries the contribution framing.
- 2026-02-22: Merit (ordering): kept the core scientific question/challenges paragraph as the first Merit paragraph, followed by the citations/prior-work + novelty/integration paragraph for a more natural “challenges $\rightarrow$ novelty” flow.
- 2026-02-22: Merit (two-domain challenges): rewrote the opening scientific question/challenges sentence to explicitly attribute the bandit challenges (partial/delayed feedback, shifting conditions, fairness--utility tension) to both the clinical diagnostics and quantum-network domains.
- 2026-02-22: Structure (Background/Merit split): moved the “novelty is the integration …” and “Unlike prior work …” sentences from Scientific Merit back into Background, and moved the “key innovative component …” sentence to appear after the “diagnostic-relevant pipelines” sentence in Merit for a cleaner “challenges $\rightarrow$ prior work $\rightarrow$ innovation” flow.
- 2026-02-22: Opening (integration placement): placed the integration sentence immediately after the deliverables line that ends with the quantum-routing simulator, reworded as “This is a novel integration …”.
- 2026-02-22: Quantum domain naming (big picture): rephrased the quantum domain across the proposal as “quantum-routing” (instead of routing + qubit allocation) to keep the focus on fair routing outcomes, while leaving resource scarcity as supporting context.
- 2026-02-22: Merit (two-domain framing): rewrote the “key innovative component” sentence to emphasize the two-domain evaluation (quantum-routing environment alongside diagnostic-like simulation) and removed the redundant (i)/(ii) restatement.
- 2026-02-22: Background (quantum constraints): expanded the quantum-domain sentence to explicitly state routing constraints (probabilistic link success, limited entanglement/quantum-resource availability, time-varying congestion) while keeping the lead-in “In the quantum domain,”.
- 2026-02-22: Broader Impacts (domain-specific): rewrote the impacts paragraph to explicitly separate clinical diagnostic impacts (resource-limited diagnostics/test allocation) from quantum-domain impacts (service equity in quantum-routing under probabilistic links/congestion/scarce resources), while keeping the shared two-testbed evaluation harness outcome.
- 2026-02-22: Broader Impacts (integration emphasis): moved the “This is a novel integration …” sentence from the opening deliverables block to the end of Broader Impacts.
- 2026-02-22: Broader Impacts (flow): fixed sentence fragments and “And, …” phrasing by rewriting the paragraph as a clean clinical $\rightarrow$ quantum $\rightarrow$ shared-harness flow.
- 2026-02-22: Approach (two-domain scope): clarified the opening sentence so Approach explicitly frames the work as spanning two domains across two testbeds.
- 2026-02-22: Approach (reproducibility wording): removed the parenthetical about using a single notebook from the reproducibility bullet.
- 2026-02-23: Tracker cleanup: reworded this log entry to avoid repeating the removed parenthetical verbatim.
- 2026-02-23: Survey (DSCI601 related-work): tightened the cross-domain transfer sentence to clarify that transfer is at the level of fairness mechanisms/policy-update strategies (not domain-specific features).
- 2026-02-23: Survey figure caption: replaced “adapted from” with “following the evaluation stack described in …” to reflect that the cited source is prior work for this project.
- 2026-02-23: Related Work flow: added a bridge sentence after the two testbed subsections to signal the transition into the broader algorithmic + fairness literature survey.
- 2026-02-23: Survey figure layer text: updated wording to emphasize noise/threat regimes and utility+fairness logging/summaries; generalized algorithm labels to contextual/adversarial/hybrid families to avoid implying EXP3 is contextual.
- 2026-02-23: Survey intro: defined “diagnostic-like” (explicitly not system debugging), clarified missing context can be group-dependent due to resource constraints/allocation, and enumerated mitigation mechanism types (fairness-regularization, calibration/thresholding, missingness-aware context augmentation).
- 2026-02-23: Survey intro: explicitly named the clinical testbed pipeline as EQUITAS at first mention; split the Introduction into two paragraphs for readability.
- 2026-02-23: Survey figure: changed logging phrasing to “captures full layered run state” and aligned caption/paragraph to “logged run state” (enables downstream utility/fairness analysis); Background domain grounding now explicitly states the quantum fairness metric as group disparity in success probability/latency across flow groups.
- 2026-02-23: References: updated the two self-cite BibTeX author fields to “Garcia, Piter Z.” to match the author block and in-text “Garcia~\cite{...}” mentions.
- 2026-02-23: Title formatting: added a small subtitle “(Related Work Survey)” on its own line under the main title.
- 2026-02-27: Proposal (`proposal.tex`): updated the author name to “Piter Z. Garcia”, updated the program line to “MS Data Science / Decision-Making \& Algorithmic Fairness”, and standardized the two self-cite reference author names to “Garcia, P. Z.”.
- 2026-02-28: Proposal (`proposal.tex`): standardized the acronym formatting to “iCMABs/CMABs” and added a short, positive-only “diagnostic-like” definition immediately after the i/ii/iii deliverables block (keeps the deliverables list easy to scan while still defining the term early).
- 2026-02-28: Proposal (`proposal.tex`): made the quantum fairness metric explicit in Background by defining service equity as group disparities in routing success probability and latency across flow groups.
- 2026-02-28: Proposal (`proposal.tex`): made the mitigation methods explicit near the top by listing fairness-regularized updates, calibration/thresholding, and missingness-aware context augmentation (matches the survey phrasing and clarifies what “mitigation” means).
- 2026-02-28: Proposal (`proposal.tex`): made the Phase 1/Phase 2 plan explicitly follow “baseline disparities, then mitigation,” and noted an initial demo in Phase 1 to match the project execution expectations.
- 2026-02-28: Proposal (`proposal.tex`): removed class-specific wording in the header by changing “DSCI 601 Project Advisors” to “Research Advisors”.
- 2026-02-28: Proposal (`proposal.tex`): clarified the Approach metrics bullet so it explicitly lists both domain-specific fairness metrics (diagnostic FNR/FPR gaps; quantum service-equity gaps in success probability/latency).
- 2026-02-28: Proposal (`proposal.tex`): updated the opening sentence to include “limited context” and non-stationarity for a more academic, compact framing; “lack of context” remains the core motivating concept and is treated as a first-class driver of fairness risk throughout the proposal.
- 2026-02-28: Proposal (`proposal.tex`): anchored the quantum testbed in prior work by citing the threat-aware hybrid contextual-bandit routing study, and replaced the placeholder/internal quantum-routing reference with that citation for a cleaner, defensible provenance trail.
- 2026-02-28: Proposal (`proposal.tex`): terminology consistency pass (minimal): replaced “controllable context missingness/uneven measurement” with “controllable limited context” (no other rewording).
- 2026-02-28: Proposal (`proposal.tex`): restored the word “measurement” by updating the two “controllable limited context” phrases to “controllable limited context and measurement limitations”.
- 2026-02-28: Proposal (`proposal.tex`): terminology consistency follow-up: standardized to “measurement noise” (instead of “measurement limitations”), updated the Phase 1 line to match, and replaced “uneven” with “differ” in Broader Impacts to avoid “evenness” framing.
- 2026-02-28: Proposal (`proposal.tex`): terminology consistency pass (minimal): replaced “incomplete” with “limited” for context access in the clinical sentence to match the overall “limited context” framing.
- 2026-02-28: Proposal (`proposal.tex`): tightened “iCMABs/CMABs” formatting while preventing margin overflow by inserting an invisible break hint (`\\allowbreak{}`) after the slash.
- 2026-02-28: Proposal (`proposal.tex`): terminology consistency pass (minimal): updated the diagnostic-like definition to use “limited context” (instead of “missing context”) to match the paper-wide framing.
- 2026-02-28: Proposal (`proposal.tex`): adjusted the title layout by breaking before “Under Missing Context” to improve readability and alignment.
- 2026-02-28: Proposal (`proposal.tex`): updated the title to a shorter, one-line form (“Fair Contextual MABs for Equitable Diagnostics Under Missing Context”) to improve scanability while keeping the same project framing.
- 2026-02-28: Proposal (`proposal.tex`): added a second-line subtitle “(Research Proposal)” under the title for quick document-type clarity.
- 2026-02-28: Proposal (`proposal.tex`): changed the subtitle styling from bold to italic to match the intended visual hierarchy.
