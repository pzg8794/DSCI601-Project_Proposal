# Domain Model Plan for the Approach Writeup

## Purpose

The domain model diagram must explain the shared decision architecture behind the project and make the relationship between the two domains legible before the implementation plan is introduced.

## Required entities

The diagram must include these entities:

1. `Environment / Testbed`
2. `Observed Context`
3. `Context Degradation Mechanism`
4. `Policy Family`
5. `Action`
6. `Partial Feedback / Reward`
7. `Utility and Fairness Logger`
8. `Mitigation / Comparison Loop`

## Domain branches

The `Environment / Testbed` component must branch into two explicitly labeled settings:

- `Clinical diagnostic workflow`
- `Quantum routing / resource allocation`

The diagram should show that both branches feed the same decision logic, but remain separate domains with different operational meanings and fairness metrics.

## Entity meanings

### Environment / Testbed

Represents the task setting in which decisions occur.

- Clinical branch: diagnostic test selection, triage escalation, or pipeline/model choice
- Quantum branch: path selection and qubit/resource allocation under uncertain network conditions

### Observed Context

Represents the information available before the decision is made.

- Clinical: symptoms, vitals, history, prior tests, operational constraints
- Quantum: link-quality estimates, congestion signals, current allocation state, threat indicators

### Context Degradation Mechanism

Represents the missing, noisy, delayed, or uneven quality of context that can create fairness risk.

This must be shown as a distinct entity because it is central to the project’s research question.

### Policy Family

Represents the method spectrum under comparison:

- non-contextual / multi-armed baseline
- contextual bandit baseline
- informative or restricted-context extension

### Action

Represents the chosen intervention at each round.

- Clinical: select test, escalate, retest, choose model/pipeline
- Quantum: choose path, allocate scarce resources

### Partial Feedback / Reward

Represents the fact that only the chosen action reveals its immediate outcome.

This node should make clear that the project is studying sequential decisions under bandit-style feedback rather than full-information supervision.

### Utility and Fairness Logger

Represents the shared evaluation layer where both performance and disparity are tracked over time.

Examples:

- utility / regret / latency / cost
- clinical fairness gaps such as FNR or delayed-escalation disparities
- quantum fairness gaps such as success-rate or latency disparities across flow groups

### Mitigation / Comparison Loop

Represents the stage where the framework:

- compares policy families
- evaluates fairness-aware mitigation
- measures utility-fairness tradeoffs

## Required interaction logic

The text accompanying the diagram must explain this flow:

1. the testbed generates a decision state
2. the system observes degraded context
3. the policy family selects an action
4. the environment returns partial feedback and reward
5. the logger records utility and fairness over time
6. the mitigation/comparison loop evaluates whether richer context or fairness-aware mechanisms improve outcomes

## What the diagram must prove

The diagram is not only decorative. It must support four claims:

- the project is one framework with two case studies
- uneven context quality is central to the problem
- fairness is measured during decision-making, not only after it
- the implementation plan follows directly from the architecture

## Common failure modes to avoid

- drawing only a generic pipeline without the two domain branches
- omitting the degraded-context mechanism
- omitting the logger / evaluation layer
- showing methods without making the policy spectrum explicit
- presenting the two domains as disconnected projects instead of one shared decision architecture
