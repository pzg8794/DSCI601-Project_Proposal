# Draft 2 revision notes

This file records the major revisions applied to the `draft2` architecture
package and the reason for each change. It is intentionally separate from the
report so that the report itself remains formal and assignment-focused.

## Revisions applied

### 1. Removed the abstract
Reason:
- this deliverable is an architecture report, not the final paper.

### 2. Removed commentary-style drafting language from the report
Reason:
- phrases describing what was "missing in the previous draft" or why a revision
  is better are not part of the final assignment deliverable.
- those explanations belong in a revision log, not in the report itself.

### 3. Removed the "Why This Version Better Satisfies the Requirements" section
Reason:
- requirement-tracking commentary is useful during drafting but should not
  appear in the final report body.

### 4. Removed the conclusion section
Reason:
- the report already closes naturally after the workflow description and figure.
- for this assignment, repeating the same architectural claims in a conclusion
  did not add technical value.

### 5. Added a stage-to-component master mapping table
Reason:
- each stage needed to be explicitly linked to quantum-side objects.
- the report now identifies the specific component, what it does, and how it is
  used inside the stage.

### 6. Tightened the stage descriptions
Reason:
- each stage now explicitly names the relevant components and explains how those
  components work together to build the stage.
- this makes the stage descriptions implementation-oriented rather than generic.

### 7. Added the fairness--performance synthesis layer
Reason:
- the architecture needed a dedicated layer that compares fairness criteria
  against inherited performance metrics rather than leaving that comparison
  implicit.
- this layer is built on top of allocator context, runner outputs, evaluator
  summaries, and state-analysis tables.

### 8. Revised the diagram spacing and routing
Reason:
- several arrows were crossing nodes or layer labels.
- horizontal spacing between control nodes and execution nodes was increased.
- band labels were moved away from major arrow traffic.
- the fairness--performance and artifacts layers were separated more clearly.

### 9. Kept the figure on its own landscape page
Reason:
- the architecture diagram contains enough detail that it should remain large and
  legible.
- the dedicated page avoids forcing the figure into the page budget for the
  narrative text.

### 10. Preserved the replication workflow
Reason:
- the report must still explain how another party recreates the system and
  replicates results through notebooks, local setup, and GCP execution.
- that workflow remains part of the architecture, not an optional appendix.
