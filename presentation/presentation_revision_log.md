# Presentation Revision Log

This document records how the DSCI 601 proposal presentation was constructed, which
feedback sources shaped it, and why each slide exists in the current deck.

Primary deck source:
- [DSCI601_Project_Proposal_Presentation_2026_beamer.tex](/Users/pitergarcia/DataScience/Semester5/DSCI601/DSCI601-Project_Proposal/presentation/DSCI601_Project_Proposal_Presentation_2026_beamer.tex)

Compiled deck:
- [DSCI601_Project_Proposal_Presentation_2026_beamer.pdf](/Users/pitergarcia/DataScience/Semester5/DSCI601/DSCI601-Project_Proposal/presentation/DSCI601_Project_Proposal_Presentation_2026_beamer.pdf)

Supporting framework figure:
- [proposal_framework_figure.tex](/Users/pitergarcia/DataScience/Semester5/DSCI601/DSCI601-Project_Proposal/presentation/proposal_framework_figure.tex)

## Design Goals

The final deck was designed to satisfy four goals at the same time:

1. Meet the official DSCI 601 proposal-presentation requirements.
2. Stay aligned with the revised proposal and related-work survey.
3. Read like a formal research talk rather than a classroom artifact.
4. Use a stable visual system that makes fairness, context, sequential learning, and the two
   domains easy to track from slide to slide.

## Main Feedback Sources Used

The presentation decisions were grounded in the following materials:

- [Project Proposal Presentation - DSCI.601.01 - Applied Data Science I.pdf](/Users/pitergarcia/DataScience/Semester5/DSCI601/course_materials/Project%20Proposal%20Presentation%20-%20DSCI.601.01%20-%20Applied%20Data%20Science%20I.pdf)
- [proposal.tex](/Users/pitergarcia/DataScience/Semester5/DSCI601/DSCI601-Project_Proposal/proposal.tex)
- [survey-related-work.tex](/Users/pitergarcia/DataScience/Semester5/DSCI601/DSCI601-Project_Proposal/survey-related-work.tex)
- [proposal_revision_log.md](/Users/pitergarcia/DataScience/Semester5/DSCI601/DSCI601-Project_Proposal/proposal_revision_log.md)
- [survey_revision_log.md](/Users/pitergarcia/DataScience/Semester5/DSCI601/DSCI601-Project_Proposal/survey_revision_log.md)
- [02-20 Refining a Research Proposal by Separating Core Methodology from Domain-Specific Applications-Meeting Minutes.md](/Users/pitergarcia/DataScience/Semester5/DSCI601/DSCI601-Project_Proposal/notes/02-20%20Refining%20a%20Research%20Proposal%20by%20Separating%20Core%20Methodology%20from%20Domain-Specific%20Applications-Meeting%20Minutes.md)
- [02-20 Refining a Research Proposal by Separating Core Methodology from Domain-Specific Applications-Meeting Summary.md](/Users/pitergarcia/DataScience/Semester5/DSCI601/DSCI601-Project_Proposal/notes/02-20%20Refining%20a%20Research%20Proposal%20by%20Separating%20Core%20Methodology%20from%20Domain-Specific%20Applications-Meeting%20Summary.md)
- [deep-research-report (2).md](/Users/pitergarcia/DataScience/Semester5/DSCI601/deep-research-report%20%282%29.md)

## Core Presentation Decisions

### 1. The deck uses a balanced 12-slide main talk

Reason:
- The course rubric requires a title slide, background, a related-work overview table,
  detailed related-work slides, proposed-project slides, and an approach slide for the next
  two semesters.
- The earlier shorter, more seminar-style versions were cleaner as talks, but they did not
  map as safely to the rubric.

Decision:
- The live talk ends on slide 12.
- Any additional references or checklist material is backup material, not part of the main
  narrated presentation.

### 2. The narrative starts generic, then introduces the two domains

Reason:
- Feedback repeatedly showed that earlier versions mixed fairness, diagnostics, quantum,
  and bandits too early, which made the story harder to follow.
- The deck therefore starts from the generic problem of fairness-aware sequential
  decision-making under degraded context, then introduces the clinical and quantum domains
  as parallel case studies.

Decision:
- The first three slides establish the general problem, why fairness can appear before a
  model "looks biased," and how bandit settings differ by context availability.

### 3. The talk treats clinical and quantum as co-equal testbeds

Reason:
- The proposal revision process moved away from the earlier framing where one domain felt
  primary and the other felt like a transfer appendix.
- The current research direction treats both domains as target settings for the same
  fairness-aware decision framework.

Decision:
- Clinical and quantum appear together as case studies, both in related work and in the
  proposed evaluation framework.

### 4. The deck includes an explicit related-work table

Reason:
- This is required by the DSCI 601 presentation assignment.
- The survey already organizes the literature into usable categories, so the presentation
  table should mirror those categories instead of inventing a new taxonomy.

Decision:
- One slide is reserved for the overview table.
- The next related-work slides unpack the most important gaps rather than trying to restate
  the full survey body.

### 5. The deck includes a compact formal problem slide

Reason:
- Combined feedback indicated the talk should sound more like a research pitch and less like
  a broad concept deck.
- The formal slide gives the deck a concrete mathematical center without turning the talk
  into a theory lecture.

Decision:
- The formalization focuses on group-skewed missingness, partial feedback, utility, and
  fairness tracked over time.

### 6. The deck uses a shared evaluation pipeline as the main framework slide

Reason:
- A simple list of deliverables was not enough to show how the project actually works.
- The shared evaluation pipeline makes the framework visible: configuration, testbed,
  policy, logging, metrics, and mitigation.

Decision:
- The framework slide is one of the core contribution slides.
- It is intentionally reusable across both clinical and quantum domains.

### 7. The deck uses semantic visual cues instead of generic theme decoration

Reason:
- The visual system needed to do actual work, not just look polished.
- The deck also needed to remain readable when projected and when viewed by people who do
  not rely on color alone for meaning.
- The guidance summarized in [deep-research-report (2).md](/Users/pitergarcia/DataScience/Semester5/DSCI601/deep-research-report%20%282%29.md)
  strongly supported redundant semantic cues, contrast, and consistent visual structure.

Decision:
- The deck uses:
  - a left accent bar
  - a title marker square
  - a topic chip strip
  - repeated color semantics across slides
  - explicit labels in diagrams so color is never the only cue

## Slide-by-Slide Rationale

### Slide 1. Title

Purpose:
- Establish the project identity, speakership, and three central pillars:
  fairness, context quality, and sequential effects.

Why this slide looks this way:
- The title slide needed to feel more deliberate than the original PowerPoint version.
- The three bottom boxes immediately state the thesis-level ideas that recur through the
  rest of the talk.

### Slide 2. Motivation

Purpose:
- State the central claim in plain language: unequal measurement can create unequal decisions
  before a model looks obviously biased.

Why it exists:
- Earlier project feedback said the problem motivation was too abstract.
- This slide fixes that by showing the fairness problem before any heavy technical framing.

### Slide 3. Background: bandits, context, and partial feedback

Purpose:
- Define the decision framework that the rest of the talk depends on.

Why it exists:
- The audience needs a compact explanation of non-contextual, contextual, and
  informative/restricted-context bandits before the research gap makes sense.

Design note:
- The slide is intentionally comparative rather than encyclopedic.

### Slide 4. Related work overview table

Purpose:
- Satisfy the assignment requirement and orient the audience to the literature categories.

Why it exists:
- The table makes the project’s novelty legible as a combination:
  fairness over time, degraded context, shift, and two-domain evaluation.

### Slide 5. Related work: partial feedback, limited context, and shift

Purpose:
- Explain what the bandit literature already gives the project.

Why it exists:
- This slide turns the overview table into a real research gap:
  strong utility methods exist, but fairness under degraded context and shift remains weaker.

### Slide 6. Related work: fairness in sequential learning

Purpose:
- Show that fairness is not being added decoratively; it changes the learning problem.

Why it exists:
- This is where equality of opportunity and fair-bandit work become relevant to the
  project’s fairness-over-time framing.

### Slide 7. Related work: domain testbeds

Purpose:
- Ground the talk in one clinical anchor and one quantum anchor.

Why it exists:
- Prior feedback said the quantum fairness case was underexplained and that the project
  needed concrete examples.
- This slide supplies those anchors without expanding into full domain lectures.

### Slide 8. Proposed project: research question and hypotheses

Purpose:
- State what is being tested rather than only what will be built.

Why it exists:
- The talk needed a sharper research identity, not just a list of tasks or tools.
- This slide turns the project into a falsifiable set of claims.

### Slide 9. Proposed project: formal setup and metrics

Purpose:
- Show the minimum mathematical structure needed to evaluate the hypotheses.

Why it exists:
- This is the slide that connects the research question to implementation and evaluation.

### Slide 10. Proposed project: shared evaluation pipeline

Purpose:
- Make the framework visible.

Why it exists:
- This slide clarifies expectations for what the implementation actually produces:
  a reusable harness, not just one domain-specific experiment.

### Slide 11. Approach for the next two semesters

Purpose:
- Meet the assignment requirement for forward planning.

Why it exists:
- The course expects a concrete path across DSCI 601 and DSCI 602.
- This slide also shows that the scope is intentionally staged.

### Slide 12. Takeaway and questions

Purpose:
- End on the main thesis, not on logistics.

Why it exists:
- The closing slide reframes context quality as a resource and fairness as part of system
  design rather than an audit added at the end.

## Rubric Mapping

The current live deck maps to the course requirements as follows:

- Title slide: slide 1
- Background slides: slides 2-3
- Related-work overview table: slide 4
- Detailed related-work slides: slides 5-7
- Proposed-project slides: slides 8-10
- Next-two-semesters approach slide: slide 11
- Closing synthesis: slide 12

## Presentation Source Decisions

### Beamer over PowerPoint

Reason:
- The Beamer version is easier to version, discuss, and revise alongside the proposal and
  survey sources in Git.

Decision:
- The PowerPoint deck served as an adaptation source.
- The Beamer deck is now the authoritative source for the presentation.

### Speaker notes were kept in-source

Reason:
- The deck needed to stay rehearseable without requiring a separate script file.

Decision:
- Short speaker notes remain embedded directly in the Beamer source.

## Operational Notes

- For live presentation, stop on slide 12.
- If needed, a references or accessibility-check slide can exist as backup material, but it
  should not weaken the main ending.
- If the deck changes substantially, update this file together with the deck so the repo
  preserves both the artifact and the rationale.
