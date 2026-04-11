# Approach Revision Log

## 2026-04-10

Documented the standalone `approach/` package and synced the draft contents to the current
proposal framing.

### Scope

- Established `approach/` as a dedicated package for iterating on the approach section
  outside the main proposal file.
- Updated the approach draft to foreground the shared fairness-aware sequential decision
  framework before the domain-specific examples.
- Added explicit clinical and quantum workflow examples so the sequential decisions are
  concrete before the technical details.
- Clarified the method spectrum as multi-armed, contextual, and informative-context
  bandits.
- Strengthened the reproducibility story with configuration, seed, and per-step logging
  expectations.
- Expanded the combined feedback notes so the writing brief, cleaned transcripts, and
  implementation/reproducibility expectations are visible in one place.

### Why

- The course feedback repeatedly asked for the shared method to be defined before
  discussing domains.
- The proposal materials needed a concrete explanation of why clinical and quantum belong
  inside one framework instead of reading like two loosely related applications.
- The approach section needed concrete workflow examples and a clearer fairness rationale
  in the quantum setting.
- The repository needed a local revision log so future proposal edits can reference the
  approach-package decisions directly.

### Notes

- The compiled draft lives at `approach/draft/approach-writeup.pdf`.
- Cleaned transcript companions that informed this pass live in the parent workspace
  `../transcripts/`.
- This log is package-specific; proposal-wide revisions should continue to be tracked in
  `proposal/proposal_revision_log.md`.

## 2026-04-10 (style sync pass)

Reformatted and rewrote the approach draft so it reads like a companion document to the
survey instead of an internal memo.

### Scope

- Converted the draft from an `article`-style note into the same IEEE-style document format
  used by the survey.
- Matched the survey title pattern, author block, package usage, and section-based
  structure.
- Rewrote the opening so the approach explicitly identifies itself as the survey's
  methodological companion for the same paper/project.
- Added a closing section that states how the survey and approach document fit together.
- Tightened the wording so the clinical and quantum explanations parallel the survey's
  language and priorities.

### Why

- The survey is currently the strongest writing artifact in the repo and should be the style
  benchmark for proposal-facing materials.
- The previous approach draft sounded more like a planning note than part of the same
  paper, which weakened the perceived coherence of the project.
- Matching the survey's formatting and rhetorical structure makes the approach package more
  defensible as part of one unified research narrative.

### Notes

- This pass focused on style, structure, and cross-document coherence rather than changing
  the underlying research claims.
- The next polish step should be to mirror any future title or framing adjustments across the
  survey, approach draft, and proposal text together.
