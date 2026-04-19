# draft1 — Improved Architecture Write-Up and Diagram

This directory contains the PhD-level, CRISP-DM-aligned improvements to the
architecture report. These files are intended to be merged into (or replace)
the corresponding files in `architecture_report/`.

## Files

| File | Purpose |
|---|---|
| `architecture_report.tex` | Full improved IEEEtran write-up: adds explicit CRISP-DM mapping table, updated four-layer figure caption, and improved Conclusion paragraph |
| `architecture_diagram.tex` | Fully redrawn TikZ diagram: four layers (CRISP-DM phases → support → stages → manifest), cross-row arrow fix, control arrows, dotted phase-to-stage alignment, color legend |
| `components.md` | Component reference table: maps every class, CLI command, and workflow to its CRISP-DM phase and output artifact |

## What Changed

1. **CRISP-DM mapping table** (`\ref{tab:crispmap}`) — explicit table linking all 6 CRISP-DM phases to concrete stages and artifacts.
2. **Four-layer diagram** — added CRISP-DM phase row at top; fixed missing Explore→Mine arrow; added dashed control arrows from Config/CLI/Validation; added dotted phase-to-stage alignment arrows; added color legend.
3. **Figure caption** — updated to describe all four layers and arrow types.
4. **Architecture Overview** — rewritten to cite CRISP-DM and reference the new table.
5. **Conclusion** — added closing paragraph tying the diagram and table to the PhD-level traceability argument.
6. **Bibliography** — added Wirth & Hipp (2000) CRISP-DM reference.