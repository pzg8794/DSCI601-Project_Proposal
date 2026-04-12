# Approach Revision Log Addendum — 2026-04-12

This addendum documents the final approach-writeup refinement pass completed after the earlier package setup and style-sync work.

## Scope

- Finalized the approach draft around a shared routing formulation linking clinical and quantum settings.
- Centered missing context as the common failure mode that connects fairness and performance across both testbeds.
- Strengthened the motivating clinical examples to reflect both uneven routing of scarce diagnostic resources and under-representative calibration contexts.
- Clarified the quantum rationale so the iCMAB advantage is framed as recovery and use of missing or weakly represented context rather than as complexity alone.
- Integrated explicit cross-references to Figure 1(a) and Figure 1(b) throughout the prose so the conceptual model and operational pipeline are each referenced where they do real work.
- Converted Figure 1 into a combined visual: Figure 1(a) as the shared domain model and Figure 1(b) as a horizontal zoom-in of the shared evaluation pipeline.
- Preserved the two-page writeup target by tightening wording, compressing line breaks, and treating the figure page as non-counted support material per the course requirement.

## Why

- The instructor prompt requires the approach section to explain the domain model, design decisions, rationale, and component interaction clearly and cohesively.
- The revised framing makes the project read as one fairness-aware routing study rather than two loosely related applications.
- The integrated Figure 1 structure improves readability by separating the conceptual four-phase model from the concrete execution harness while keeping both inside one coherent figure.
- The tightened prose preserves the stronger argument without letting formatting overhead push the narrative beyond the intended two pages of writeup text.

## Final Document Characteristics

- The approach draft now explicitly distinguishes:
  - Figure 1(a): shared domain model
  - Figure 1(b): shared evaluation pipeline zoom-in
- The implementation section points directly to the shared pipeline in Figure 1(b).
- The shared-domain section uses Figure 1(a) for the conceptual phases and ties Phase 4 to the operational expansion in Figure 1(b).
- The current draft is intended as the polished course submission version of the standalone approach package.

## Files

- `approach/draft/approach-writeup.tex`
- `approach/draft/approach-writeup.pdf`

## Notes

- This addendum records the final refinement decisions without overwriting the earlier revision log entries.
- Proposal-wide narrative changes should still be synchronized separately in `proposal/proposal_revision_log.md` when the standalone approach language is folded back into the full proposal.
