# AGENTS.md

## Rule 0: Canonical Paper Artifacts Only

This public repository contains canonical manuscript sources and intentional
submission outputs. It is not a workspace backup or analysis dump.

- Keep one canonical `.tex`/`.bib` source set and only intentional submission
  PDFs required for review, grading, or release.
- Do not keep archives, media recordings, conversation exports, data dumps,
  numbered copies, backup copies, or alternate exports.
- Do not keep LaTeX intermediates, Finder metadata, caches, temporary files,
  or local draft directories after validation.
- Keep a figure only when a current manuscript or presentation source uses it,
  or when its directory documents a specific submission requirement.
- Runtime data, model state, experiment state, and validation outputs belong in
  the external data layer or private implementation repo, never here.
- Before staging, run the required Git-root check and inspect every added or
  modified binary file individually.

## Repository Boundary

- Path: `/Users/pitergarcia/DataScience/Semester5/DSCI601/implementation/paper`
- Remote: `https://github.com/pzg8794/DSCI601-Project_Proposal.git`
- Purpose: paper, proposal, report, and presentation artifacts only.

Do not move implementation code or workflow outputs into this repository.
