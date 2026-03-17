# DSCI601 Proposal Revision Log

This document records:
- the feedback given on the current proposal framing
- the specific problems identified in the transcripts
- the reasons the proposal now needs revision
- the planned changes before editing `proposal.tex`

Proposal source:
- [proposal.tex](/Users/pitergarcia/DataScience/Semester5/DSCI601/DSCI601-Project_Proposal/proposal.tex)

Transcript sources:
- [02-20 Refining a Research Proposal by Separating Core Methodology from Domain-Specific Applications-transcript.txt](/Users/pitergarcia/DataScience/Semester5/DSCI601/transcripts/02-20%20Refining%20a%20Research%20Proposal%20by%20Separating%20Core%20Methodology%20from%20Domain-Specific%20Applications-transcript.txt)
- [03-04 Lecture_ Ethics_Fairness Report, Contextual Bandits in Clinical Workflows, and Capstone Guidance-transcript.txt](/Users/pitergarcia/DataScience/Semester5/DSCI601/transcripts/03-04%20Lecture_%20Ethics_Fairness%20Report,%20Contextual%20Bandits%20in%20Clinical%20Workflows,%20and%20Capstone%20Guidance-transcript.txt)

## Current Proposal State

Current title in `proposal.tex`:

```text
Fair Contextual Bandits for Equitable Diagnostic Decision-Making Under Limited Context
```

Current framing in `proposal.tex`:
- centers a generic contextual bandit framework
- describes a diagnostic-like environment plus a quantum transfer study
- uses `diagnostic-like` as a key term
- emphasizes `contextual multi-armed bandits (iCMABs/CMABs)`
- does not yet reflect the newer public/internal framing:
  - fairness-aware decision-making
  - quantum routing and clinical settings
  - multi-armed, contextual, and informative bandit methods

## Core Feedback From the Transcripts

### 1. The term "diagnostics" was unclear

Transcript evidence:
- 02-20, `00:01:27` to `00:02:05`
- 02-20, `00:04:34` to `00:04:51`

Direct issue:
- readers did not know whether `diagnostics` meant medical diagnostics, runtime/system diagnostics, or something else

Why this matters:
- the proposal title and opening paragraph still lean on diagnostic wording in a way that invites this confusion

Needed change:
- make `clinical settings` explicit
- reduce ambiguous diagnostic wording
- ground the clinical side in a concrete workflow instead of a floating label

### 2. The proposal was seen as straddling too many domains with overloaded terminology

Transcript evidence:
- 02-20, `00:04:09` to `00:04:27`
- 02-20, `00:08:45`

Direct issue:
- reviewers felt the proposal mixed multiple domains and reused terms that mean different things in different areas

Why this matters:
- the current proposal still mixes:
  - diagnostics
  - fairness
  - clinical settings
  - quantum routing
  - contextual/iCMAB language
- without enough staged explanation

Needed change:
- simplify the framing
- separate core methodology from domain examples more clearly
- define the domains in a way that a non-specialist class audience can follow

### 3. The fairness story in quantum was not clear enough

Transcript evidence:
- 02-20, `00:05:13` to `00:05:24`
- 02-20, `00:09:18` to `00:09:33`

Direct issue:
- reviewers did not understand where fairness shows up in quantum routing or why a fair bandit is needed there

Why this matters:
- the current proposal mentions `service equity`, but it still reads as a thin concept compared with the clinical fairness case

Needed change:
- state concretely what fairness means in the quantum setting
- explain the resource-allocation logic more clearly
- show why routing and allocation decisions can create group-dependent disparities

### 4. The project needed concrete motivating examples

Transcript evidence:
- 03-04, `00:12:14` to `00:15:36`
- 03-04, `00:16:55` to `00:17:06`

Direct issue:
- reviewers asked for a concrete clinical workflow example and a concrete quantum workflow example
- they explicitly said the current abstract framing was hard to follow

Why this matters:
- the current proposal moves quickly into technical goals
- it still does not include simple motivating examples before the project goals

Needed change:
- add one concise motivating clinical example
- add one concise motivating quantum example
- place them before or inside the background section so the technical goals make sense

### 5. The method framing needs to reflect the intended spectrum

Transcript evidence:
- 03-04, `00:17:32` to `00:19:14`

Direct issue:
- reviewers noticed mismatch between the wording and the intended method spectrum
- the explanation in class was that the project compares limited-context, contextual, and informative-context settings

Why this matters:
- the current proposal still foregrounds `contextual multi-armed bandits (iCMABs/CMABs)`
- this does not cleanly reflect the three-part method framing discussed later

Needed change:
- describe the methods more explicitly as:
  - multi-armed
  - contextual
  - informative
- make that spectrum visible in the title, summary, and approach

### 6. The current proposal still reads too much like a generic framework plus transfer study

Transcript evidence:
- 02-20, `00:06:08`
- 03-04, `00:20:19` to `00:20:33`

Direct issue:
- the class advice suggested a cleaner framing:
  - define the fair bandit methodology clearly
  - then apply it to target domains
- current text still sounds like:
  - one generic framework
  - one main domain
  - one transfer validation

Why this matters:
- your later framing treats quantum routing and clinical settings as co-important parts of the research direction
- the current wording still preserves the earlier confusion

Needed change:
- reduce `generic framework` and `transfer study` phrasing
- present both domains more clearly as target settings for the same fairness-aware decision-making agenda

## Why the Proposal Must Be Updated

The proposal now needs revision because the transcript criticism is not fully reflected in the current draft.

Specifically:
- the title still uses old wording
- the opening summary still depends on terminology that confused readers
- the role of fairness in quantum routing is still underexplained
- the motivating examples requested in class are still missing
- the method spectrum is not presented the way it was discussed in feedback

This is not just polish.
These changes are required to bring the written proposal into alignment with:
- the actual transcript criticism
- the revised title direction
- the clearer framing already being used in resume/email materials

## Planned Revision Targets

The next edits to `proposal.tex` should focus on:

1. Title
- Replace the old title with the current direction centered on fairness-aware decision-making in quantum routing and clinical settings.

2. Opening summary paragraph
- Remove stale language that still causes diagnostic/context confusion.
- Reflect the updated method spectrum and domain framing.

3. Background
- Add one concrete clinical example.
- Add one concrete quantum example.
- Explain fairness/service-equity in both more plainly.

4. Scientific Merit
- Reframe the core question so it is easier to understand.
- Reduce the sense that quantum is just a transfer add-on.

5. Approach
- Make the method spectrum explicit:
  - multi-armed
  - contextual
  - informative

## Editing Rule

Before modifying `proposal.tex`, changes should be handled section by section with:
- exact target section
- why the change is needed
- before
- after

This log should be updated as changes are approved and applied.

## Applied Changes

### Item 1. Title

Status:
- approved and applied

Before:

```text
Fair Contextual Bandits for Equitable Diagnostic Decision-Making
Under Limited Context
```

After:

```text
Fairness-Aware Decision-Making in Quantum Routing and Clinical Settings
via Multi-Armed, Contextual, and Informative Bandit Methods
```

Why this change was made:
- removes the older title language that contributed to confusion around `diagnostics`
- removes `Under Limited Context`, which no longer reflects the preferred framing
- makes both domains explicit
- reflects the intended method spectrum discussed in transcript feedback

### Item 2. Opening summary paragraph

Status:
- approved and applied

Before:

```text
This project will develop a practical, reproducible framework for contextual multi-armed bandits (iCMABs/CMABs) to support sequential decision-making under uncertainty, limited context, and non-stationarity while treating algorithmic fairness as a first-class objective.
The work on this generic framework focuses on measuring and improving fairness across the clinical (diagnostic-like) and quantum-network routing domains through the following deliverables:
i) a simulation-first diagnostic-like sequential decision environment with controllable limited context, measurement noise, and distribution shift,
ii) a fairness-aware contextual MAB evaluation stack (baselines + contextual policies) with time-evolving group disparity reporting and at least one mitigation mechanism,
and iii) a transfer study demonstrating the same policy stack in a quantum-network routing simulator.

Here, ``diagnostic-like'' refers to clinical diagnostic sequential decision workflows such as diagnostic test selection, triage or follow-up escalation, and model/pipeline selection under partial feedback and non-stationarity. It also includes cases where key diagnostic components (tests, instruments, or patient information) are unavailable or delayed due to resource constraints or allocation policies, creating group-dependent limited context.

Mitigation mechanisms considered include fairness-regularized policy updates (constraints/penalties), group-aware calibration or thresholding, and missingness-aware context augmentation (e.g., feature acquisition or imputation policies).
```

After:

```text
This project develops a practical, reproducible framework for fairness-aware sequential decision-making in two target settings: clinical diagnostic workflows and quantum-network routing. The methodological focus is a spectrum of bandit methods ranging from non-contextual to contextual to informative contextual bandits, designed to study how different levels of available context affect fairness, equity, and performance under uncertainty, non-stationarity, and resource constraints.

On the clinical side, the project focuses on sequential workflows such as diagnostic test selection, triage, follow-up escalation, and model or pipeline choice when patient context may be incomplete, delayed, noisy, or unevenly available across groups. On the quantum side, the project focuses on routing and resource-allocation decisions under probabilistic link success, scarce resources, and time-varying congestion, where service-equity gaps can emerge across flow or user groups.

The initial deliverables are: i) a simulation-first clinical decision environment with controllable missing context, measurement noise, and distribution shift; ii) a shared evaluation stack for non-contextual, contextual, and informative bandit policies with time-evolving disparity reporting, baseline unfairness assessment, and at least one mitigation mechanism; and iii) a quantum-routing implementation of the same decision-making framework to study fairness, robustness, and cross-domain transfer. Mitigation mechanisms considered include fairness-regularized policy updates, group-aware calibration or thresholding, and missingness-aware context augmentation.
```

Why this change was made:
- replaces the ambiguous `diagnostic-like` framing with clearer clinical language
- makes the method spectrum explicit in the way discussed in transcript feedback
- removes stale `generic framework` and `transfer study` language from the opening
- strengthens the fairness/equity/performance framing at the top of the proposal
- signals baseline unfairness assessment rather than only post-mitigation reporting

### Item 5. Broader Impacts

Status:
- approved and applied

Before:

```text
If successful, this work provides a concrete, reproducible framework for fairness-aware contextual sequential decision systems in both clinical diagnostics and quantum-network routing. In the clinical diagnostic domain (diagnostic-like test/model/retesting selection, including COVID-style test allocation), the framework supports measuring and mitigating disparities that can arise when resources and context quality differ across patient groups. In quantum-network routing, it advances trustworthy routing by adding explicit service-equity monitoring and disparity-aware constraints to online routing policies under probabilistic link success, time-varying congestion, and scarce quantum resources across user/flow groups. The result is a reusable evaluation harness (two testbeds + shared policy API) for benchmarking fairness-aware contextual MAB policies, while reporting and mitigating fairness disparities over time rather than only post-hoc.
```

After:

```text
If successful, this project provides a concrete and reproducible way to study fairness-aware sequential decision-making in settings where limited context, scarce resources, and shifting conditions can produce unequal outcomes. In clinical diagnostic workflows, the work supports measuring and mitigating disparities that arise when some patient groups receive weaker context, delayed information, or lower-quality decision support. In quantum-network routing, it supports more trustworthy resource allocation by making service-equity gaps visible and testable rather than leaving them hidden inside aggregate routing performance.

More broadly, the project contributes a reusable evaluation framework for comparing bandit methods under fairness, equity, and performance objectives across more than one domain. That matters not only for this proposal's two testbeds, but also for the larger principle behind the work: fairness should be treated as part of the design and evaluation of sequential decision systems, not as a post-hoc audit added after optimization is already complete.
```

Why this change was made:
- makes the section read like broader impacts rather than a second technical summary
- keeps both domains visible while emphasizing practical/public consequences
- reframes fairness as a design principle rather than a post-hoc evaluation step
- preserves the reusable-evaluation-framework contribution without dropping into implementation detail

### Item 6. Approach

Status:
- approved and applied

Before:

```text
The goal is to implement and evaluate fairness-aware contextual MAB policies in two domains across two testbeds (diagnostic-like sequential decision simulation + quantum-network routing simulator), and to report utility--fairness tradeoffs under shift. The work is structured to be feasible without sensitive clinical data access (simulation-first), while remaining extensible to approved open datasets. The tasks are:
- Build diagnostic testbed
- Build quantum testbed
- Implement bandit policies
- Define reward + metrics
- Add fairness mitigation
- Package for reproducibility
Phase 1 establishes baseline performance and group disparities under controlled limited context and measurement noise, evaluates an initial mitigation mechanism, and produces an initial demo; Phase 2 tests robustness under distribution shift and finalizes packaging for the final report/demo.
```

After:

```text
The goal is to implement and evaluate fairness-aware bandit methods across two testbeds: a simulation-first clinical diagnostic decision environment and a quantum-network routing simulator. The comparison is organized as a spectrum from non-contextual to contextual to informative contextual bandit methods, with the aim of measuring utility--fairness tradeoffs under limited context, missing information, and distribution shift. The work is structured to remain feasible without sensitive clinical data access while still being extensible to approved open datasets. The tasks are:
- Build clinical testbed
- Build quantum testbed
- Implement bandit methods
- Define reward + metrics
- Add fairness mitigation
- Package for reproducibility
Phase 1 establishes baseline performance and baseline unfairness under controlled missing context and measurement noise, evaluates an initial mitigation mechanism, and produces an initial demo. Phase 2 tests robustness under distribution shift and finalizes packaging for the final report and demo.
```

Why this change was made:
- makes the method spectrum explicit in the approach section, as requested in transcript feedback
- replaces stale `diagnostic-like` framing with clearer clinical wording
- keeps the clinical and quantum testbeds parallel and easier to understand
- adds baseline unfairness language explicitly
- preserves the original task structure while aligning it to the revised project framing
