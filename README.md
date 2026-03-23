# DSCI601 Proposal Repo

This repo contains the proposal, related-work survey, and presentation materials for the
DSCI 601 project on fairness-aware sequential decision-making across clinical and quantum
testbeds.

## Primary documents

- `proposal.tex`: current project proposal source
- `survey-related-work.tex`: related-work survey aligned to the current proposal framing
- `presentation/DSCI601_Project_Proposal_Presentation_2026_beamer.tex`: Beamer deck source
- `presentation/presentation_revision_log.md`: presentation rationale, slide decisions, and
  rubric mapping
- `proposal_revision_log.md`: proposal revision history and source feedback synthesis
- `survey_revision_log.md`: survey sync history

## Compile

Proposal:

1. `pdflatex proposal.tex`
2. run `pdflatex proposal.tex` again for stable references/layout

Survey:

1. `pdflatex survey-related-work.tex`
2. run `pdflatex survey-related-work.tex` again if needed

Presentation:

1. `cd presentation`
2. `pdflatex DSCI601_Project_Proposal_Presentation_2026_beamer.tex`
3. run `pdflatex DSCI601_Project_Proposal_Presentation_2026_beamer.tex` again for stable output

## Notes

- The presentation deck is designed to satisfy the DSCI 601 proposal-presentation rubric
  while still reading like a research talk rather than a class artifact.
- Slide-level rationale and the decision history for the presentation live in
  `presentation/presentation_revision_log.md`.
