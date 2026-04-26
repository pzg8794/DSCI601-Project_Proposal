# Rough Draft Report

Build from this directory:

```bash
latexmk -pdf -interaction=nonstopmode rough_draft_report.tex
```

The report uses IEEE conference style and the local bibliography file
`rough_draft_references.bib`.

## Current implementation addendum

The rough draft LaTeX source predates the latest embedded clinical/fairness
framework work. Read the update addendum before revising or compiling a final
version:

```text
rough_draft_report/fairness_framework_update_addendum.md
```

That addendum records the current implementation status, including:

- legacy quantum fairness sidecar smokes
- embedded clinical evaluator/runner/environment path
- EQUITAS mediation seam
- default and fairness reporting profiles
- report manifests
- fairness validation hub notebook
- CI smoke and reporting/validation workflow protection

The addendum should guide the next full LaTeX revision. It does not replace the
rough draft; it prevents the current draft from overstating the clinical path as
only planned or missing the new reporting/validation layer.
