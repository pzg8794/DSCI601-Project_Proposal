# DSCI601 Proposal Repo

This repo contains the proposal package for the DSCI 601 project on fairness-aware
sequential decision-making across clinical and quantum testbeds. The materials are now
organized by deliverable so each document family keeps its own source, compiled output,
and revision history together.

## Repository Structure

- `proposal/`
  Current project proposal source, compiled PDF, and proposal revision log.
- `survey/`
  Related-work survey materials aligned to the current proposal framing.
- `approach/`
  Standalone approach package used to isolate and iterate on the approach section before
  merging it into the full proposal. Includes the writing brief, domain model plan,
  feedback synthesis, revision log, and draft writeup/PDF.
- `presentation/`
  Beamer deck source, compiled slides, figure assets, and presentation revision log.
- `ethics_fairness_report/`
  One-page DSCI601 ethics/fairness report and submission checklist.
- `docs/`
  Supporting reference documents and archived deep-research notes.

## Primary Documents

- `proposal/proposal.tex`: current project proposal source
- `proposal/proposal_revision_log.md`: proposal revision history and source feedback synthesis
- `survey/survey-related-work.tex`: related-work survey aligned to the current proposal framing
- `survey/survey_revision_log.md`: survey sync history
- `approach/draft/approach-writeup.tex`: standalone approach-section draft
- `approach/approach_revision_log.md`: approach-package revision history and rationale
- `ethics_fairness_report/ethics_fairness_report.tex`: one-page DSCI601 ethics/fairness report
- `presentation/DSCI601_Project_Proposal_Presentation_2026_beamer.tex`: Beamer deck source
- `presentation/presentation_revision_log.md`: presentation rationale, slide decisions, and
  rubric mapping

## Compile

Proposal:

1. `cd proposal`
2. `pdflatex proposal.tex`
3. run `pdflatex proposal.tex` again for stable references/layout

Survey:

1. `cd survey`
2. `pdflatex survey-related-work.tex`
3. run `pdflatex survey-related-work.tex` again if needed

Approach package:

1. `cd approach/draft`
2. `pdflatex approach-writeup.tex`
3. run `pdflatex approach-writeup.tex` again if needed for stable output

Ethics and Fairness Report:

1. `cd ethics_fairness_report`
2. `latexmk -xelatex ethics_fairness_report.tex`

Presentation:

1. `cd presentation`
2. `pdflatex DSCI601_Project_Proposal_Presentation_2026_beamer.tex`
3. run `pdflatex DSCI601_Project_Proposal_Presentation_2026_beamer.tex` again for stable output

## Notes

- The `approach/` directory is the active workspace for refining the shared methodology
  before folding that language back into `proposal/proposal.tex`.
- The approach package is intentionally paired with cleaned transcript companions stored in
  the parent workspace under `../transcripts/`.
- The presentation deck is designed to satisfy the DSCI 601 proposal-presentation rubric
  while still reading like a research talk rather than a class artifact.
- Slide-level rationale and the decision history for the presentation live in
  `presentation/presentation_revision_log.md`.
- The ethics/fairness report is mirrored here as a course-deliverable copy; the longer
  drafting lineage and foundation archive remain in the public `IDAI700` repo.
