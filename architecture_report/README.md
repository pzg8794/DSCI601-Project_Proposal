Architecture deliverable for DSCI601
===================================

This directory holds the canonical architecture artifacts for the DSCI601 proposal.

Files
- `main.tex` — submission-ready architecture writeup for Overleaf / LaTeX compilation.
- `architecture_diagram.tex` — TikZ source for the architecture diagram (canonical copy).
- `components.md` — component responsibilities and interface notes used to support the writeup.

Why a separate folder
- The architecture diagram is a deliverable (like `presentation/` and `DSCI601-Project_Proposal/` documents) and should have its own canonical location so it can be referenced by slides, the proposal text, and future decisions.

Mapping to class deliverables
- See the project deliverables and construction map at [PAPER_CONSTRUCTION_MAP.md](PAPER_CONSTRUCTION_MAP.md) for the course's expected artifacts (proposal, presentation, survey, and reproducible experiments). This architecture folder is explicitly a top-level deliverable: it feeds figures for the proposal and slides and a short design doc for reviewers.

Current status
1. `main.tex` is now the canonical architecture assignment writeup.
2. `architecture_diagram.tex` is included directly by the writeup and remains the canonical diagram source.
3. `components.md` remains the supporting design note for implementation details and interfaces.
