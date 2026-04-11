# Approach Writing Brief

This brief is the decision-complete specification for the standalone DSCI601 approach writeup.

## Target artifact

- `approach/draft/approach-writeup.tex`
- standalone 1-2 page writeup
- domain model diagram included
- research-facing tone

## Locked structure

1. `Approach Overview`
2. `Domain Model and Interaction Logic`
3. `Why This Design`
4. `Implementation Plan`

## Opening claim

The writeup should open by stating that the contribution is a **shared fairness-aware sequential decision framework** for two domain-distinct but structurally similar settings: clinical diagnostic workflows and quantum routing/resource allocation.

The opening must make clear that the work is not just “using bandits in two places.” The actual research target is fairness under uneven context quality, partial feedback, and shift.

## Required claims

The writeup must explicitly state:

- the contribution is a shared fairness-aware sequential decision framework, not only two applications
- fairness under uneven context and shift is the real research target
- simulation-first clinical design is intentional and justified
- the quantum testbed is credible because it builds on existing routing work
- the method family is a comparison spectrum:
  - multi-armed
  - contextual
  - informative
- fairness must be measured during learning, not only after it
- the shared framework is better than two unrelated single-domain studies

## Required examples

The writeup must include:

- one concrete clinical workflow example
- one concrete quantum workflow example

These examples must appear before or inside the design explanation, not after the task list.

## Domain model expectations

The writeup must explain a shared domain model with these entities:

- environment / testbed
- observed context
- degraded context mechanism
- policy family
- action selection
- partial feedback / reward
- fairness and utility logging
- mitigation / comparison loop

It must explain:

- what each entity is
- how the entities interact
- why the same interaction logic supports both domains
- why the domains remain distinct case studies rather than being collapsed into one

## Why-this-design section requirements

This section must justify these decisions:

- simulation-first clinical environment instead of requiring sensitive data
- existing quantum routing testbed instead of inventing a toy second domain
- comparison across non-contextual, contextual, and informative methods
- domain-specific fairness metrics under one shared evaluation framework
- reproducibility via fixed configs, seeds, modular runs, and explicit metric logging

It must also explain why this design is better than:

- a single-domain-only project
- contextual-only modeling without baseline spectrum
- post-hoc fairness auditing
- a vague generic framework plus weak transfer claim

## Implementation plan section requirements

The implementation plan should read as a consequence of the domain model, not a disconnected checklist.

It should describe:

- clinical testbed build
- quantum testbed integration
- shared policy interface
- metric and reward design
- fairness mitigation
- reproducibility packaging

The implementation plan should be concise and should follow logically from the earlier sections.

## Tone and citation rules

- use third-person formal voice
- avoid “class project” wording
- avoid unexplained acronyms on first mention
- cite key prior work explicitly
- cite the relevant self-foundation work as prior grounding, not as a substitute for argument

## Completion standard

The draft is ready only if a reader can answer all of these after one pass:

- What is the framework?
- Why do the two domains belong together?
- What does the diagram represent?
- Why is this approach better than simpler alternatives?
- What exactly will be implemented and measured?
