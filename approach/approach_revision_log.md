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
