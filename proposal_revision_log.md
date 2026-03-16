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
