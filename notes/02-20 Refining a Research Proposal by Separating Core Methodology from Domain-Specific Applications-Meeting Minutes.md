# 02-20 Discussion: AI Fairness and Presentation Structure

## Action Items
- @[Speaker 3] - Implement the suggested organizational structure for the project presentation to improve clarity. - [No Due Date Mentioned].
## Key Decisions
- No key decisions were explicitly recorded in the notes.
## Detailed Minutes
[00:20-01:36] **The concepts of exploration versus exploitation trade-offs in machine learning were explained.**
- This trade-off is common in reinforcement learning (RL) and evolutionary algorithms.
- Backpropagation in neural networks is a form of "local search," analogous to climbing a mountain and finding the nearest peak, which may not be the highest one (the global optimum).
- To find the global optimum, methods need some randomization or broader searching. This creates a trade-off:
  - **Exploration:** Searching for new, potentially better areas of the search space that have not yet been investigated.
  - **Exploitation:** Spending more time refining and leveraging known good areas of the search space.
- Reinforcement learning inherently deals with this exploration-exploitation balance.
[01:27-04:08] **The term "diagnostics" was clarified to encompass various applications beyond just medical contexts.**
- Speaker 1 initially asked for clarification on what Speaker 3 meant by "diagnostics," questioning if it was specifically about medical diagnostics.
- Speaker 3 clarified that it is not strictly medical and can apply to areas like resource allocation.
- The concept involves using AI to make decisions based on patterns. A lack of context can cause these AIs to "jeopardize or erase certain groups."
- The primary goal of Speaker 3's work is to measure fairness in AI decisions, particularly regarding the impact of including or omitting context, rather than determining the absolute correctness of the AI's decision.
- This fairness analysis could be expanded to include clinical data, testing how AI decisions are impacted by context and how certain groups might be unfairly treated in diagnostics or resource allocation.
[04:09-05:03] **Speaker 3's presentation was critiqued for using ambiguous terminology across multiple domains, making it difficult to understand.**
- Speaker 2 pointed out that Speaker 3 is straddling multiple domains and using terminology that exists in all of them without providing clear definitions or context.
- Specific feedback was given on the term "diagnostics," which could mean clinical diagnostics or system diagnostics—two entirely different concepts.
- Speaker 3 acknowledged the feedback, agreeing that the use of "diagnostics" and other terminology needed to be more specific.
[05:03-08:30] **A structured approach was proposed for Speaker 3's project to improve clarity by separating the core methodology from its domain-specific applications.**
- Speaker 1 and Speaker 2 identified that Speaker 3's project combined three things: using fairness as a decision-making tool, clinical settings, and a "Parkview" reference, creating confusion.
- Speaker 2 proposed a clearer structure:
  1. Start by defining the core goal, such as designing a generic, fair, contextual model (or "bandit").
  2. Then, discuss applying this generic model to specific target domains (e.g., clinical, quantum computing) in separate sections.
  3. This separation helps the audience understand the general concept before diving into domain-specific applications.
- Speaker 3 agreed with this feedback, stating the goal was to measure and prove that context can build fairer algorithms, not to build a "perfect" fair algorithm from scratch.
- Speaker 2 outlined a narrative: first, define the fairness metric for a domain (e.g., clinical), show that existing methods are unfair, and then propose new methods (X, Y, Z) to improve fairness.
- Action Item: @[Speaker 3] - Implement the suggested organizational structure for the project presentation to improve clarity. - [No Due Date Mentioned].
[08:45-09:57] **The importance of defining terminology was reinforced, especially when the same words have different meanings in different domains.**
- Speaker 2 emphasized that using the same terminology (e.g., "fairness") with different meanings across multiple domains (e.g., data science, quantum computing) is highly confusing for an audience, especially for experts from one of those domains.
- Speaker 3 agreed that the proposed organizational structure makes the explanation easier.
- Speaker 2 noted that while the need for a "fair bandit" is understandable in classical computing spaces, the rationale for needing one in quantum computing is not immediately clear and requires explanation.
- Speaker 3 confirmed there are use cases for fairness in quantum resource allocation.
- The recommended presentation flow is: show existing methods, demonstrate they are unfair, and then propose the new strategy to improve them.
[09:58-12:39] **Recommendations were given for improving the professionalism and formality of research writing.**
- Speaker 2 advised against using first-person pronouns (I, my, me, our) in research papers, suggesting a more formal third-person perspective is generally preferred.
  - Example: Instead of "My goal was," use "The goal of this project was."
- It is unnecessary to state that a project is an "individual project" or to include obscure course codes like "UNWI I S T E S 780" that are meaningless to a general audience.
- When referencing prior work, instead of just using an acronym and a citation number, it's better to describe the work explicitly.
  - Example: "This work builds on existing work operationalizing fairness, bias, and mitigation for diagnostic algorithm guidelines [citation]."
- The overall presentation should be framed as a formal conference submission or technical report, not as a class assignment.