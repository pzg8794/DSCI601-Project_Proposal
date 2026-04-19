# draft2 architecture package

This directory contains a revised architecture package prepared as a stronger
draft of the canonical `architecture_report/` deliverable.

## Files

- `architecture_report.tex` - revised full writeup with CRISP-DM-aligned framing
- `architecture_diagram.tex` - revised TikZ diagram with connected stage flow and explicit control/provenance layers
- `components.md` - synchronized component note matching the current repo structure
- `rewrite_package.md` - working notes describing the problems fixed and the rewrite logic

## What changed

- replaced the older `CRISP+ML` framing with a clearer `CRISP-DM-aligned` framing
- made the mapping from CRISP-DM phases to executable review stages explicit
- fixed the diagram so the stage flow is fully connected
- made the support layer visibly connected to the executable pipeline
- kept the artifact/provenance layer explicit
- aligned the component note with the current implementation repository

## Intent

This draft keeps the original architecture directory untouched while providing a
submission-ready alternative that is more consistent with the code-review
assignment, the implementation docs, and the broader proposal-writing standards.
