# 02-20 Working Session: Fairness via Context in Diagnostics and Resource Allocation

## Key Points
---
- Discussion of exploration–exploitation trade-off in reinforcement learning and evolutionary algorithms; analogy of local search getting stuck on local maxima and need for randomized exploration to find global optima.
- Clarification request on the term “diagnostics” and whether it refers to clinical diagnostics or system/runtime diagnostics.
- Speaker 3 explains “diagnostic” more broadly (resource allocation, decision-making by AIs missing context) with a focus on fairness rather than correctness; concern that missing context can lead to unfair decisions affecting certain groups.
- Suggestion to be explicit about domains and terminology to avoid confusion, as terms overlap across multiple fields.
- Proposal to structure the work as designing “fair contextual data/mandates” and then applying them to clearly defined target domains (e.g., clinical diagnostics, resource allocation), keeping domain discussions separate for clarity.
- Speaker 3 clarifies their goal: not to build a “fair algorithm” per se, but to demonstrate that with appropriate context, more fair algorithms can be built; aim is to measure existing fairness and show achievable improvements via context.
- In clinical domain, recommendation to define a fairness metric, run baseline methods to show unfair outcomes, then propose and test methods (X/Y/Z) to improve fairness.
- Organizational and writing guidance:
  - Resolve terminology conflicts across domains; be precise when a word has different meanings.
  - Justify why fairness is needed in each target domain; question raised about the necessity of “fair bandits” in quantum computing vs. classical settings.
  - Writing style: prefer third-person formal tone (avoid “I/we/my/our”); avoid class/course framing, write as for a conference/report.
  - Clarify references and acronyms (e.g., “UNWI ISTES 780,” “ISE 780”); provide context and cite works explicitly rather than relying on unclear abbreviations.
- Practical citation approach suggested: describe building on existing clusters and cite specific works (e.g., operationalizing fairness, bias mitigation guidelines for diagnostic algorithms).
- Closing acknowledgments and agreement to reorganize the document accordingly.
- Non-sequitur note: “The film was shot in the city of Kassel.”
## Decisions Made
---
- Focus the project on fairness measurement and improvement via contextual data, rather than claiming to build a singular “fair algorithm.”
- Structure the document to:
  - Define a generic fair contextual mandate/data approach.
  - Apply it to specific, clearly separated target domains (e.g., clinical diagnostics, resource allocation).
- Use precise, domain-specific terminology for “diagnostics” and other overlapping terms to reduce ambiguity.
- Adopt a formal, third-person writing style and avoid course-specific framing; clarify acronyms and references.
## Action Items
---
### Tasks
| Task | Responsible Party | Deadline | Notes |
| --- | --- | --- | --- |
| Define and document the specific meaning of “diagnostics” in each target domain (clinical vs. system/runtime) | Speaker 3 | 2026-02-27 | Include clear domain scoping to avoid ambiguity. |
| Identify and select fairness metrics for the clinical domain | Speaker 3 | 2026-03-06 | Examples: equal opportunity, demographic parity, calibration; justify selection. |
| Run baseline evaluations to demonstrate unfair outcomes with existing methods | Speaker 3 | 2026-03-13 | Use clinical data (if accessible) and resource allocation scenarios; record metrics and outcomes. |
| Propose and outline methods (X/Y/Z) to incorporate context and improve fairness | Speaker 3 | 2026-03-20 | Describe methodological changes (data access, feature context, policy adjustments). |
| Reorganize the paper/report to separate domains and clarify terminology | Speaker 3 | 2026-02-29 | Present a generic fair contextual mandate, then domain-specific applications. |
| Revise writing to third-person formal style and remove class/course framing | Speaker 3 | 2026-02-29 | Replace “I/we/my” with “this work/the project.” |
| Clarify and standardize references and acronyms (e.g., ISE 780, UNWI ISTES 780) | Speaker 3 | 2026-02-29 | Provide full names and proper citations to referenced works. |
| Justify the necessity (or non-necessity) of fair bandit approaches in quantum vs. classical domains | Speaker 3 | 2026-03-06 | Provide use cases (e.g., resource allocation) and rationale for each domain. |
| Document infrastructure context (e.g., building on existing clusters) and cite relevant operational fairness guidelines | Speaker 3 | 2026-02-29 | Include specific citations to fairness/bias mitigation guidelines for diagnostics. |
### Deadlines
- 2026-02-27: Define domain-specific meaning of “diagnostics.”
- 2026-02-29: Reorganize report; revise writing style; clarify references and acronyms; document infrastructure context and citations.
- 2026-03-06: Select clinical fairness metrics; justify fair bandit necessity across domains.
- 2026-03-13: Run baseline unfairness evaluations.
- 2026-03-20: Propose context-based fairness improvement methods (X/Y/Z).
### Follow-Up Actions
- Review the reorganized document for clarity across domains and terminology.
- Validate chosen fairness metrics with domain experts (clinical and resource allocation).
- Assess results from baseline evaluations and iterate on proposed methods.
- Confirm appropriateness of fair bandit approaches in quantum computing through literature review or expert consultation.
- Ensure references and citations are complete and consistent before external submission.