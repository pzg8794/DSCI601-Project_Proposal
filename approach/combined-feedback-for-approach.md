# Combined Feedback for the DSCI601 Approach Writeup

Primary raw inputs:

- `Semester5/DSCI601/transcripts/2026-02-20 Refining a Research Proposal by Separating Core Methodology from Domain-Specific Applications-transcript.txt`
- `Semester5/DSCI601/transcripts/2026-03-04 Lecture_ Ethics_Fairness Report, Contextual Bandits in Clinical Workflows, and Capstone Guidance-transcript.txt`
- `Semester5/DSCI601/transcripts/2026-03-23 Lecture_ Fairness-Aware Sequential Decision-Making-transcript.txt`

Supporting synthesis aids:

- `notes/02-20 ... Meeting Minutes.md`
- `notes/02-20 ... Meeting Summary.md`
- `notes/02-20 ... Summary.md`
- `proposal/proposal_revision_log.md`
- `PROJECT_TODO.md`

## Core diagnosis

The proposal and presentation struggled not because the project was weak, but because the methodology, domains, and motivating examples were introduced in the wrong order. The audience kept encountering domain language before understanding the shared method, and the project therefore sounded like several partly connected ideas instead of one coherent research design.

The approach section has to repair that. It must show that the work is a single fairness-aware sequential decision framework with two case-study testbeds, not a vague transfer story between unrelated domains.

## What reviewers still do not understand

- What the core contribution is if the two domains are set aside
- Why fairness is central rather than decorative
- Why fairness in quantum routing is a serious research question
- Why the method family is a comparison spectrum instead of one chosen algorithm
- Why the clinical and quantum settings belong in the same framework
- Why the design choices are better than simpler alternatives

## What the approach section must prove

- The shared framework is the main contribution.
- The domains are structurally similar enough to justify one methodology.
- Uneven context quality is the central fairness driver being studied.
- Partial feedback and distribution shift are part of the problem, not side conditions.
- The method spectrum is necessary because the project studies how different levels of available context change fairness and utility.
- The evaluation design is strong enough to show baseline unfairness before claiming any mitigation benefit.

## What must come before the task list

Before any implementation tasks appear, the writeup must establish:

1. one concrete clinical workflow example
2. one concrete quantum workflow example
3. the shared domain model connecting them
4. the reason this framework is needed instead of a simpler single-domain or post-hoc-fairness design

If the text starts with a task list first, it will repeat the same failure mode as the earlier proposal drafts.

## Clinical case-study guidance

The clinical side should be described as a sequential diagnostic workflow, not as a vague “diagnostic-like” idea. Good examples include:

- diagnostic test selection
- triage escalation
- follow-up escalation
- model or pipeline choice when patient context is incomplete or delayed

The writeup should state clearly that fairness in this setting concerns subgroup outcome disparities such as false-negative gaps or delayed-escalation gaps when some groups systematically have weaker observed context.

This domain should be grounded in prior clinical/bio fairness work rather than introduced as a hypothetical add-on.

## Quantum case-study guidance

The quantum side should be described as routing and resource allocation under probabilistic link success, scarce qubits, and changing threat or congestion conditions.

The writeup should define fairness here as service equity, for example:

- success-rate disparities across flow groups
- latency disparities across flow groups
- repeated disadvantage in resource allocation under limited capacity

The key point is that fairness in quantum must be explained through allocation consequences, not through analogy alone.

This domain is credible because it builds on existing routing/testbed work rather than proposing an entirely new simulation from scratch.

## Method-spectrum guidance

The approach must make the comparison spectrum explicit:

- non-contextual / multi-armed baseline
- contextual bandit baseline
- informative or restricted-context extension

The spectrum is not a naming preference. It is the mechanism that lets the project ask whether better or richer context actually improves fairness, when it fails, and when mitigation is still needed.

The writeup should make clear that the project is not only selecting one best model. It is studying how the amount and quality of context change fairness and utility behavior.

## Diagram/domain-model guidance

The domain model diagram should show one generic decision framework with two explicit testbed branches.

Required entities:

- environment / testbed
- observed context
- missing/noisy/delayed context mechanism
- policy family
- action
- partial feedback / reward
- fairness and utility logging
- mitigation / comparison loop

The text must explain how these entities interact and why this architecture justifies the chosen implementation plan.

## Writing-style guidance

- Use formal third-person voice.
- Avoid class framing.
- Avoid ambiguous terms such as plain `diagnostics`.
- Do not assume the reader knows the prior coursework or internal acronyms.
- Describe prior work explicitly instead of relying on shorthand.
- Use a research-facing title and explicit references.

## Top failure modes to avoid

- starting with technical goals before motivating examples
- using one term to mean different things across domains
- presenting quantum as a weak transfer add-on
- describing the method family without explaining why the spectrum matters
- listing tasks without explaining why this design is better than:
  - a single-domain study
  - contextual-only modeling
  - post-hoc fairness auditing
  - two unrelated domain projects
