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
  Final approach writeup package for review (single source, PDF, and change log).
- `presentation/`
  Beamer deck source and compiled slides.
- `ethics_fairness_report/`
  One-page DSCI601 ethics/fairness report and submission checklist.

Notes:
- Working materials (drafts, notes, archived docs) are kept locally and are not tracked.
- The repo root `main.tex` is set to compile the latest approach writeup for easy sharing.

## Primary Documents

- `proposal/proposal.tex`: current project proposal source
- `survey/survey-related-work.tex`: related-work survey aligned to the current proposal framing
- `approach/approach-writeup.tex`: final approach writeup source
- `approach/CHANGES.md`: approach writeup change log
- `ethics_fairness_report/ethics_fairness_report.tex`: one-page DSCI601 ethics/fairness report
- `presentation/DSCI601_Project_Proposal_Presentation_2026_beamer.tex`: Beamer deck source

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

1. `cd approach`
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

- The presentation deck is designed to satisfy the DSCI 601 proposal-presentation rubric
  while still reading like a research talk rather than a class artifact.
- The ethics/fairness report is mirrored here as a course-deliverable copy; the longer
  drafting lineage and foundation archive remain in the public `IDAI700` repo.
