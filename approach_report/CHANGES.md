# CHANGES.md — Approach Writeup Revision History
**Project:** Fairness-Aware Routing in Quantum Networks and Clinical Settings
**Course:** DSCI 601.01 — Applied Data Science I
**Author:** Piter Z. Garcia

---

## File Index (Shareable)

| File | Description |
|---|---|
| `approach-writeup.tex` | Current approach writeup source (v5) |
| `approach-writeup.pdf` | Compiled PDF for review |
| `CHANGES.md` | Revision history (this file) |

Note: older intermediate drafts were used during editing but are kept local-only and are
not tracked in the shareable repo view.

---

## Original → v1: Formal Tone Fix

**Problem:** Several section openers used narrative or meta-documentary
framing — referring to the related-work survey to justify the approach
write-up's own existence, or describing "what this document does" rather
than asserting methodology directly.

**Changes:**
- `§1 Approach Overview` — rewritten to open with the problem and
  methodological contribution, not a description of the document's purpose
- `§2 Motivating Workflows opener` — removed "The survey introduces..."
  replaced with direct workflow framing
- `§3 Shared Domain Model` — removed "follows from the survey framing";
  domain model now stands on its own
- `§4 Method Comparison Logic opener` — removed "The survey argues...";
  replaced with direct assertion of the design requirement
- `§5 Implementation Plan opener` — removed reference to external docs
- `§6 Connection to the Survey` — removed entire section; replaced with
  `§6 Research Contribution` containing direct methodological statements

---

## v1 → v2: Routing Reframe + Rubric Alignment

**Problem:** The common ground between the two domains was framed too
generically ("repeated decisions under uncertainty"). The rubric's four
"why" questions were not explicitly or individually answered.

**Changes:**

### Core reframe
- Both domains are now explicitly identified as **routing problems**:
  clinical routing routes diagnostic/treatment resources among patients;
  quantum routing routes entanglement among competing flows
- Key claim added: *unfair routing is not merely an equity problem —
  it is a performance problem*
- Title updated: "Decision-Making" → "Routing" to reflect the reframe

### Domain model diagram
- Boxes are now **color-coded by phase**:
  - Phase 1 (blue)   — Environment / Input
  - Phase 2 (green)  — Context Observation
  - Phase 3 (orange) — Routing Decision
  - Phase 4 (purple) — Evaluation and Mitigation
- Phase background shading added behind each group of nodes
- Phase labels added below each band
- Figure caption expanded to describe each phase by color and content
- Node label updated: "Action" → "Routing Action"

### §4 renamed and restructured
- Section title changed from "Method Comparison Logic"
  to "Design Rationale and Novelty"
- Four subsections added, each answering a rubric question:
  1. Why this approach — novelty claim (no prior cross-domain routing
     fairness framework exists)
  2. Why better than others — explicit comparison to single-domain and
     post-hoc alternatives
  3. Design decisions — bandit choice, simulation-first, quantum env
     extension, three-level context spectrum
  4. Decisions vs. domain model — each decision mapped to a phase

### Quantum frontier framing
- Added to §1 and §6: quantum networking is a proven emerging technology;
  pairing with clinical settings is a deliberate positioning at the
  intersection of present necessity and future breakthrough

---

## v2 → v3: Q-Labeled Subsections + Figure Moved to End

**Problem:** The four rubric-answer subsections in §4 were titled
descriptively but not explicitly flagged as answers to rubric questions.
The domain model figure was placed mid-document, risking layout overflow
beyond two pages.

**Changes:**

### §4 subsection labels
Subsection titles now carry explicit Q-prefixes for rubric traceability:
- `Q1: Why do it this way, and why has it not been done before?`
- `Q2: Why is this approach better than others?`
- `Q3: What design and implementation decisions were made, and why?`
- `Q4: How do these decisions connect to the domain model?`

### Figure placement
- Figure moved from mid-document (§3) to **end of document**, just before
  the bibliography, using `\begin{figure*}[!b]`
- This ensures the two-page text body compiles cleanly before the figure
  page, satisfying the 1–2 page requirement (excluding diagrams)
- §3 Shared Domain Model retains a forward reference to Figure 1 and
  a prose description of all four phases — no content is lost

---

## Rubric Alignment — Final Status (v3)

| Rubric requirement | Status |
|---|---|
| 1–2 pages (excl. diagram) | Satisfied — figure at end, text fits two columns |
| Domain diagram present | Yes — color-coded, four phases |
| Diagram components described | Yes — in §3 prose + figure caption |
| Explain your approach | Yes — §1 and §2 |
| Why done this way | Yes — Q1 in §4 |
| Why better than others | Yes — Q2 in §4 |
| Design and implementation decisions | Yes — Q3 in §4 |
| How decisions relate to domain model | Yes — Q4 in §4 |
| Novelty claim | Yes — Q1, supported by literature gap |
| Common ground coherent + defensible | Yes — routing as shared structure |

---

## v3 → v5: Formatting + Full-Width Domain Model (IEEE two-column)

**Goal:** Improve readability and IEEE-style layout while keeping the writeup within the
expected page constraints (excluding the diagram page).

**Changes:**
- Updated the author/title block so names and affiliations present cleanly in a two-column
  layout.
- Implemented a full-width `figure*` domain-model diagram and ensured stable placement on
  its own page.
- Tightened cross-references so the figure label (`fig:domain_model`) resolves correctly
  after rebuild.
