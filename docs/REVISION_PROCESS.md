# Revision Process

This document defines the required process for revising the final paper. It is binding for all future revision work.

## Core Rule

Use the final-paper requirements as the source of truth. Do not invent a new section structure, subsection structure, or review framework unless the user explicitly approves it.

For each major paper section, the rubric bullets become the working subsection scaffold exactly. The scaffold may later be smoothed for final manuscript style, but only after the content has been reviewed and accepted.

## Required Workflow for Each Section

For every section, follow this order:

1. Read the exact requirement from `docs/FINAL_PAPER_REQUIREMENTS.md`.
2. Convert the requirement bullets into the working section/subsection scaffold without adding extra headings.
3. Show the current content in question.
4. Map the current content to the requirement bullets.
5. Identify what is wrong or missing relative to the requirement.
6. Propose the smallest correction.
7. Wait for user acceptance, revision, blocking, or deferral.
8. Document the decision in `docs/revision_decisions/`.
9. Only then commit the accepted revision.

## Prohibited Behavior

Do not:

- invent new subsections not present in the requirement;
- change the process between sections;
- reintroduce old draft text that was removed or rejected;
- replace accepted text with a different version without asking;
- move content between sections without first checking the requirement;
- add generic filler instead of concrete, paper-specific content;
- claim a manuscript edit was applied when only a scaffold or note was updated.

## Current Section Scaffolds

### Introduction

The Introduction requirement says it should include:

1. scientific merit, importance, and challenges;
2. overview of the work done and how it relates to similar work;
3. what the results were;
4. brief overview of the rest of the paper, at most one sentence per section.

The working Introduction scaffold must therefore follow those requirement nodes. Substructure inside the first node may be used only because the requirement itself contains three parts: Scientific Merit, Importance, and Challenges.

### Approach / Methodology

The Approach / Methodology requirement says:

1. include the domain model diagram and give a description of it;
2. explain why the work is being done this way;
3. explain why the approach is needed instead of something already done;
4. explain why the approach is better than prior approaches;
5. explain the different design and implementation decisions that were made.

The working Approach / Methodology scaffold must therefore be:

```tex
\section{Approach and Methodology}

\subsection{Domain Model Diagram and Description}

\subsection{Why This Approach}

\subsection{Why Existing Approaches Are Not Enough}

\subsection{Why This Approach Is Better}

\subsection{Design and Implementation Decisions}
```

No additional methodology subsections should be introduced unless the user explicitly approves them.

## Decision Log Rule

Every accepted decision must be recorded in `docs/revision_decisions/` with:

- requirement section;
- current issue;
- accepted change;
- reason;
- affected manuscript/scaffold file;
- status: accepted, revised, blocked, or deferred.
