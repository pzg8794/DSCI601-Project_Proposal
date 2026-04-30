# Revision Decision 001: Introduction Conference Tone

Date: 2026-04-28

## Task

Task 1 from docs/CONFERENCE_REVISION_TODO.md: rewrite the introduction for conference tone.

## Accepted first-pass decision

The first pass applies the agreed introduction edits only, not the larger rewrite.

1. Keep the current third introduction paragraph for now.
2. Remove the paragraph that begins: The current rough draft reports the mostly completed design and implementation foundation.
3. Remove the beginning of the following paragraph: This rough draft does not claim that the final fairness results are complete. Also remove the next two sentences about consolidating into a preliminary final-paper structure and the project being cross-domain.
4. Preserve the scientific content from the remainder of that paragraph: both domains are sequential routing systems; fairness risk emerges from unequal context quality; clinical routes diagnostic attention; quantum routes probabilistic network resources; both require learning under partial feedback, non-stationarity, and group/flow-level monitoring.
5. Move the research-question material from Section 3C to the end of the introduction.
6. Remove or later rewrite Section 3C to avoid duplicated research questions.

## Reason

The current introduction contains rough-draft and report-structure language. That language describes the document rather than the scientific contribution. The introduction should end by making the problem, research questions, and current claim boundary clear.

## Replacement text for the trimmed paragraph

Both domains are sequential routing systems whose fairness risk emerges from unequal context quality. The clinical system routes diagnostic attention, testing, retesting capacity, escalation, and model-assisted triage; the quantum system routes probabilistic network resources such as entanglement-generation effort, qubit allocation, and path capacity. Both require learning under partial feedback, non-stationarity, and subgroup- or flow-level performance monitoring.

## Research-question text to add at the end of the introduction

This study is organized around four research questions:

RQ1: How much does context improve utility and fairness relative to non-contextual bandit baselines when groups or flows have comparable context quality?

RQ2: How quickly do fairness gaps emerge when one group, site, cohort, or flow class receives noisier, delayed, or incomplete context?

RQ3: Do missingness-aware or fairness-regularized policy updates reduce outcome disparities without unacceptable utility loss?

RQ4: Do the same policy-update and evaluation strategies transfer between clinical routing and quantum routing, or are the fairness mechanisms domain-specific?

The current evidence supports a compatibility-preserving and reproducible fairness-evaluation methodology across the two target applications. The quantum path preserves legacy saved-state and testbed compatibility while adding governed fairness artifacts. The clinical path runs as an embedded evaluator with multiple model families, allocator-mediated actions, EQUITAS audit/mitigation context, model-stratified fairness summaries, and reproducible reporting artifacts. Stronger claims about active fairness-adjusted quantum learning require an explicit policy-update mechanism and full experimental validation.

## Application status

Decision documented on branch revision/task1-intro-conference-tone. The manuscript TeX body still needs the patch applied because the remote connector exposes truncated large-file content and does not provide a safe full-file replacement path for rough_draft_report/rough_draft_report.tex.
