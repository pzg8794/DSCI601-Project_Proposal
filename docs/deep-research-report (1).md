# Neurodivergent-Friendly Color Coding for Your Beamer Deck

## Why color-coding works best when it is consistent and not color-only

What you’re asking for is strongly aligned with established cognitive accessibility guidance: keeping **a consistent visual design** (including consistent use of colors, layout, and cues) reduces cognitive load because people can “learn” the interface once and then reuse that understanding across pages/slides. citeturn3search1turn0search0  W3C’s cognitive accessibility patterns also emphasize making the **purpose** of each page clear and helping people re-orient after distraction—which maps directly to “every slide has an obvious, consistent visual cue telling you what type of content this is.” citeturn3search3turn3search0

At the same time, accessibility standards caution that **color must not be the only way meaning is conveyed** (i.e., pair color with text labels/shapes/icons). That’s WCAG Success Criterion 1.4.1. citeturn1search4  This matters practically because color-vision deficiency is common (e.g., NEI notes “about 1 in 12 men” have color vision deficiency) and many people perceive colors differently. citeturn4search0turn1search4

So the “best of both worlds” approach for your deck is:

You get **strong color coding** (for fast recognition), but each color cue is always paired with **text labels + shapes** (for robustness and clarity). citeturn1search4

## The semantic color system I recommend for your slides

You already have a good palette. The biggest improvement is to treat it as a **semantic mapping** you reuse everywhere:

- **Fairness** → `FairOrange`
- **Context / measurement quality** → `ContextTeal`
- **Sequential learning / bandits / formalism** → `SeqPurple`
- **Clinical testbed** → `ClinicalGreen`
- **Quantum testbed** → `TealAccent`
- **Risk / caution / tradeoff** → `RiskRed`

To make it immediately recognizable on every slide, we’ll add three consistent cues:

A thin **left accent bar** (hard to miss), a **colored square in the title**, and a **topic strip** of labeled “chips” near the bottom showing which concepts are active on that slide. These cues provide consistent signposting, which is exactly what the cognitive accessibility “consistent design” guidance calls for. citeturn3search1turn3search3

## Accessibility guardrails for color-coding in slides

These are the constraints that keep the design “friendly” rather than visually noisy:

Text should remain highly readable by ensuring sufficient contrast. WCAG’s contrast guidance is a good benchmark: normal text should meet ~4.5:1 contrast (and large/bold text can be ~3:1). citeturn1search2turn1search4  For non-text graphical cues (like your bar, boxes, diagram edges), WCAG non-text contrast guidance suggests aiming for about **3:1** against adjacent colors for meaningful visual information. citeturn2search2

Color should never be the only indicator—so every colored chip will also contain a written label (“Fairness”, “Context”, etc.), and the slide title will include a shape (`■`) plus text. citeturn1search4

You already use comfortable typography and whitespace; maintaining readable spacing aligns with W3C guidance that some users benefit from increased spacing and clean visual presentation. citeturn2search0turn2search1

## Implementation in Beamer: add reusable color-coded components

Below is a **drop-in upgrade** to your existing LaTeX. It adds:

- `\leftbar{<color>}`: vertical slide stripe
- `\ticon{<color>}`: tiny colored square for titles
- “chips” (on/off) + `\topicstrip{...}`: consistent slide legend
- `cblock` environment: per-block color-coded blocks without messing up global theme
- term-highlighting macros (`\Fair{}`, `\Ctx{}`, etc.) so you can visually tag key words consistently

### Preamble additions (paste these after your `\newcommand{\refs}`)

```latex
% ===============================
% Neurodivergent-friendly color coding helpers
% (consistent cues: title icon + left bar + topic chips)
% ===============================

% A small colored square you can put in every frametitle
\newcommand{\ticon}[1]{\textcolor{#1}{\rule{0.95ex}{0.95ex}}}

% Left accent bar: a strong, consistent "where am I?" cue
\newcommand{\leftbar}[1]{%
  \begin{tikzpicture}[remember picture,overlay]
    \fill[#1] (current page.north west) rectangle ([xshift=5pt]current page.south west);
  \end{tikzpicture}%
}

% Topic chips: ON (colored) and OFF (muted)
\newcommand{\chipon}[2]{%
  \tikz[baseline=-0.6ex]{
    \node[
      rounded corners=4pt,
      draw=#1!75!black,
      fill=#1!14,
      text=DeepNavy,
      font=\scriptsize\bfseries,
      inner xsep=5pt,
      inner ysep=2.2pt
    ] {#2};
  }%
}
\newcommand{\chipoff}[1]{%
  \tikz[baseline=-0.6ex]{
    \node[
      rounded corners=4pt,
      draw=SoftGray!25,
      fill=PaleGray,
      text=SoftGray,
      font=\scriptsize,
      inner xsep=5pt,
      inner ysep=2.2pt
    ] {#1};
  }%
}

% Common chips (keep the labels explicit so color is never the only cue)
\newcommand{\FairOn}{\chipon{FairOrange}{Fairness}}
\newcommand{\CtxOn}{\chipon{ContextTeal}{Context}}
\newcommand{\SeqOn}{\chipon{SeqPurple}{Sequential}}
\newcommand{\ClinOn}{\chipon{ClinicalGreen}{Clinical}}
\newcommand{\QuantOn}{\chipon{TealAccent}{Quantum}}

\newcommand{\FairOff}{\chipoff{Fairness}}
\newcommand{\CtxOff}{\chipoff{Context}}
\newcommand{\SeqOff}{\chipoff{Sequential}}
\newcommand{\ClinOff}{\chipoff{Clinical}}
\newcommand{\QuantOff}{\chipoff{Quantum}}

% A consistent topic strip you can place near the bottom of each slide
\newcommand{\topicstrip}[5]{%
  \vspace{0.35em}
  \noindent
  #1\hspace{0.25em}#2\hspace{0.25em}#3\hspace{0.25em}#4\hspace{0.25em}#5
}

% Color-coded term emphasis (optional but very effective for explaining live)
\newcommand{\Fair}[1]{\textcolor{FairOrange}{\textbf{#1}}}
\newcommand{\Ctx}[1]{\textcolor{ContextTeal}{\textbf{#1}}}
\newcommand{\Seq}[1]{\textcolor{SeqPurple}{\textbf{#1}}}
\newcommand{\Clin}[1]{\textcolor{ClinicalGreen}{\textbf{#1}}}
\newcommand{\Quant}[1]{\textcolor{TealAccent}{\textbf{#1}}}
\newcommand{\Risk}[1]{\textcolor{RiskRed}{\textbf{#1}}}

% Colorized block environment (keeps your global theme intact)
\newenvironment{cblock}[2]{%
  \begingroup
  \setbeamercolor{block title}{fg=white,bg=#1}
  \setbeamercolor{block body}{fg=SoftInk,bg=#1!10}
  \begin{block}{#2}
}{%
  \end{block}
  \endgroup
}
```

## Slide-by-slide color coding: exact edits to your current slides

Below are your slides rewritten with **(a)** a left accent bar, **(b)** a colored title icon, **(c)** topic chips, and **(d)** selective color-coded blocks/diagrams.

You can paste these frame bodies directly over your existing Slides 2–9. (Slide 1 already has excellent pillbox coding; we leave it as-is.)

### Slide 2: Motivation (Fairness as primary)

```latex
% --- Slide 2: Motivation ---
\begin{frame}{\ticon{FairOrange}\; Motivation}
\leftbar{FairOrange}
\small
\textcolor{FairOrange}{\textbf{Key claim:}} unequal \Ctx{measurement} produces unequal \Fair{decisions}
before any model ``looks biased.''

\vspace{0.6em}
\begin{columns}[T,onlytextwidth]
  \column{0.6\textwidth}
    \begin{cblock}{DeepNavy}{Two domains, same \Seq{sequential} structure}
    \begin{itemize}
      \item \Clin{Clinical:} choose tests / escalation steps under partial feedback; context can be systematically missing by group.
      \item \Quant{Quantum routing:} choose paths + allocate scarce qubits; link success uncertain and conditions shift.
      \item In both: policies optimize reward under uncertainty, but \Fair{fairness must be monitored during learning}.
    \end{itemize}
    \end{cblock}

  \column{0.38\textwidth}
    \begin{cblock}{ClinicalGreen}{What ``fairness'' looks like (Clinical)}
      FNR/FPR gaps, time-to-escalation gaps.
    \end{cblock}
    \begin{cblock}{TealAccent}{What ``fairness'' looks like (Quantum)}
      success/latency gaps across flow/user groups.
    \end{cblock}
    \begin{cblock}{SeqPurple}{Why bandits?}
      Bandits model \Seq{partial feedback}: you only observe the outcome of what you chose.
    \end{cblock}
\end{columns}

\topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOn}{\QuantOn}
\refs{Fairness metrics: Hardt et al. (EqOpp), Joseph et al. (fair bandits).}
\end{frame}
```

### Slide 3: Formal problem (Sequential/formal as primary)

```latex
% --- Slide 3: Formal problem + metrics ---
\begin{frame}{\ticon{SeqPurple}\; Formal problem (compressed)}
\leftbar{SeqPurple}
\small
\textcolor{SeqPurple}{\textbf{Goal:}} learn a policy that is \Seq{high utility} and \Fair{low disparity},
under \Ctx{missing context} and shift.

\vspace{0.4em}
\begin{cblock}{ContextTeal}{Contextual bandit with groups and degraded context}
At round $t$: observe group $g_t\in\mathcal{G}$ and \emph{observed} context $\tilde{x}_t$ (possibly missing),
choose action $a_t\in\{1,\dots,K\}$, observe reward $r_t(a_t)$ (bandit feedback).
\[
\tilde{x}_t = M_t(g_t)\odot x_t \quad \text{(group-dependent missingness / noise)}
\]
\end{cblock}

\vspace{0.3em}
\begin{columns}[T,onlytextwidth]
  \column{0.52\textwidth}
    \begin{cblock}{SeqPurple}{Utility objective}
    \[
      \max_{\pi}\; \mathbb{E}\Big[\sum_{t=1}^{T} r_t\Big] \quad
      \text{(or minimize regret)}
    \]
    \end{cblock}
  \column{0.46\textwidth}
    \begin{cblock}{FairOrange}{Fairness monitoring}
    Example (clinical): \textbf{EqOpp gap}
    \[
      \Delta^{\text{TPR}}(t) = \text{TPR}_{g=0}(t) - \text{TPR}_{g=1}(t)
    \]
    Track $\Delta(t)$ in sliding windows (not just end-of-run).
    \end{cblock}
\end{columns}

\topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOff}{\QuantOff}
\refs{Contextual bandits: Li et al.; EqOpp: Hardt et al.; non-stationarity: Besbes et al., Garivier \& Moulines.}
\end{frame}
```

### Slide 4: Quantum testbed (Quantum as primary)

This version colors the diagram and the blocks consistently in the quantum color.

```latex
% --- Slide 4: Quantum testbed concretely (Paper2) ---
\begin{frame}{\ticon{TealAccent}\; Quantum testbed anchor (Paper2)}
\leftbar{TealAccent}
\small
\textcolor{TealAccent}{\textbf{Concrete example:}}
(from \texttt{quantum\_project}) 4 nodes, 4 paths, per-hop fidelity, threat regimes.

\vspace{0.2em}
\begin{columns}[T,onlytextwidth]
  \column{0.55\textwidth}
  \centering
  \begin{tikzpicture}[
    node/.style={circle, draw=TealAccent!85!black, fill=TealAccent!12, minimum size=8mm, inner sep=0pt},
    edge/.style={-Stealth, line width=0.9pt, draw=TealAccent!85!black},
    lab/.style={font=\scriptsize, color=SoftGray}
  ]
    \node[node] (n1) {1};
    \node[node, right=2.2cm of n1] (n2) {2};
    \node[node, below=1.6cm of n1] (n3) {3};
    \node[node, below=1.6cm of n2] (n4) {4};

    \draw[edge] (n1) -- (n2);
    \draw[edge] (n1) -- (n3);
    \draw[edge] (n2) -- (n4);
    \draw[edge] (n3) -- (n4);

    \node[lab, above=0.1cm of n1] {Src};
    \node[lab, above=0.1cm of n4] {Dst};

    \node[lab, right=0.2cm of n2] {$0.95$ per hop};
  \end{tikzpicture}

  \vspace{0.35em}
  \begin{cblock}{TealAccent}{Physics (toy numbers)}
    2-hop success: $0.95^2=0.9025$ \\
    3-hop success: $0.95^3\approx 0.8574$
  \end{cblock}

  \column{0.43\textwidth}
  \begin{cblock}{TealAccent}{Why this matters}
    Longer paths degrade; attacks create non-stationarity.\\
    The decision policy must adapt \emph{and} we must track \Fair{service equity}.
  \end{cblock}

  \begin{cblock}{SeqPurple}{Threat ladder (examples)}
    Baseline $\rightarrow$ Stochastic $\rightarrow$ Markov $\rightarrow$ Adaptive $\rightarrow$ OnlineAdaptive
  \end{cblock}

  \begin{cblock}{FairOrange}{Bandit mapping}
    Paths $\approx$ arms (or groups of arms); qubit allocations $\approx$ structured actions.
  \end{cblock}
\end{columns}

\topicstrip{\FairOn}{\CtxOff}{\SeqOn}{\ClinOff}{\QuantOn}
\refs{Quantum routing context: Wehner et al.; Pant et al.; Caleffi; EXPNeuralUCB: Huang et al.}
\end{frame}
```

### Slide 5: Clinical testbed (Clinical as primary)

```latex
% --- Slide 5: Clinical testbed design sketch ---
\begin{frame}{\ticon{ClinicalGreen}\; Clinical testbed design (simulation-first)}
\leftbar{ClinicalGreen}
\small
\textcolor{ClinicalGreen}{\textbf{DSCI601 deliverable:}}
a diagnostic-like sequential environment with controllable missingness + shift.

\vspace{0.4em}
\begin{columns}[T,onlytextwidth]
  \column{0.55\textwidth}
    \begin{cblock}{ClinicalGreen}{Workflow abstraction}
    \begin{itemize}
      \item State: patient context $x_t$ (symptoms, vitals, history) + \Ctx{missingness mask}.
      \item Action: choose next test / model / escalation step.
      \item Reward: utility minus cost/latency; penalize unsafe delay.
      \item Outcome fairness: \Fair{FNR gap, TPR gap}, time-to-escalation gap (by group).
    \end{itemize}
    \end{cblock}

    \begin{cblock}{ContextTeal}{Why simulation-first?}
      Enables controlled \Ctx{missingness} + \Seq{shift} experiments without protected clinical datasets.
    \end{cblock}

  \column{0.43\textwidth}
  \centering
  \begin{tikzpicture}[
    box/.style={rounded corners=6pt, draw=ClinicalGreen!85!black, fill=ClinicalGreen!10,
      align=center, minimum width=4.2cm, minimum height=0.8cm},
    arr/.style={-Stealth, line width=0.9pt, draw=ClinicalGreen!85!black},
    note/.style={font=\scriptsize, color=SoftGray, align=center}
  ]
    \node[box] (ctx) {Observed context $\tilde{x}_t$};
    \node[box, below=0.35cm of ctx] (act) {Choose action $a_t$\\(test / escalate)};
    \node[box, below=0.35cm of act] (fb) {Bandit feedback\\(only chosen outcome)};
    \node[box, below=0.35cm of fb] (met) {Update + log\\utility \& disparity};

    \draw[arr] (ctx) -- (act);
    \draw[arr] (act) -- (fb);
    \draw[arr] (fb) -- (met);

    \node[note, right=0.2cm of ctx] {missingness\\depends on group};
  \end{tikzpicture}
\end{columns}

\topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOn}{\QuantOff}
\refs{Clinical bias motivation: Obermeyer et al. (proxy targets); fairness definition: Hardt et al.}
\end{frame}
```

### Slide 6: Methods (Sequential as primary, with fairness mechanisms highlighted)

```latex
% --- Slide 6: Methods (spectrum + fairness integration) ---
\begin{frame}{\ticon{SeqPurple}\; Method spectrum and fairness integration}
\leftbar{SeqPurple}
\small
\textcolor{SeqPurple}{\textbf{Compare policies}} by \Ctx{context quality} and how \Fair{fairness} enters learning.

\vspace{0.4em}
\begin{columns}[T,onlytextwidth]
  \column{0.33\textwidth}
  \begin{cblock}{SeqPurple}{Non-contextual baselines}
    $\epsilon$-greedy, UCB, Thompson sampling.\\
    \textcolor{SoftGray}{Blind to group-dependent missing context.}
  \end{cblock}

  \column{0.33\textwidth}
  \begin{cblock}{ContextTeal}{Contextual baselines}
    LinUCB-style policies.\\
    \textcolor{SoftGray}{Can amplify inequities if context quality differs by group.}
  \end{cblock}

  \column{0.33\textwidth}
  \begin{cblock}{ContextTeal}{Informative / restricted context}
    Choose which features to observe (feature acquisition / restricted context).\\
    \textcolor{SoftGray}{Makes “context quality” an explicit experimental variable.}
  \end{cblock}
\end{columns}

\vspace{0.35em}
\begin{cblock}{FairOrange}{Fairness mechanisms (what makes it ``PhD-level'' here)}
\begin{itemize}
  \item \textbf{Monitoring:} time-evolving disparity curves, worst-group metrics.
  \item \textbf{Mitigation in-loop:} constraints/penalties or fairness-aware calibration during learning.
  \item \textbf{Shift robustness:} evaluate under stochastic + adversarial regimes.
\end{itemize}
\end{cblock}

\topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOff}{\QuantOff}
\refs{Bandits: Auer et al.; contextual bandits: Li et al.; fair bandits: Joseph et al.; restricted context: Bouneffouf et al.; fair CMAB constraints: Chen et al.}
\end{frame}
```

### Slide 7: Shared evaluation framework (Framework slide with “colored pipeline”)

Here, each pipeline box is semantically colored (context → sequential policy → fairness metrics → mitigation).

```latex
% --- Slide 7: Shared evaluation framework (TikZ) ---
\begin{frame}{\ticon{ContextTeal}\; Shared evaluation framework (reproducible)}
\leftbar{ContextTeal}
\small
\textcolor{ContextTeal}{\textbf{One evaluation logic:}}
configure $\rightarrow$ run policies $\rightarrow$ log $\rightarrow$ measure fairness over time.

\vspace{0.25em}
\centering
\begin{tikzpicture}[
  box/.style={rounded corners=7pt, align=center, minimum width=3.2cm, minimum height=0.92cm},
  arr/.style={-Stealth, line width=0.9pt, draw=DeepNavy},
  small/.style={font=\scriptsize, color=SoftGray}
]
  \node[box, draw=ContextTeal!85!black, fill=ContextTeal!10, text=DeepNavy] (cfg)
    {Config\\\small{shift + missingness}};
  \node[box, right=0.55cm of cfg, draw=DeepNavy, fill=PaleGray, text=DeepNavy] (env)
    {Testbed\\\small{\Clin{clinical} + \Quant{quantum}}};
  \node[box, right=0.55cm of env, draw=SeqPurple!85!black, fill=SeqPurple!10, text=DeepNavy] (pol)
    {Policy\\\small{MAB/CMAB/iCMAB}};
  \node[box, right=0.55cm of pol, draw=SoftGray!60, fill=PaleGray, text=DeepNavy] (log)
    {Logger\\\small{full run state}};
  \node[box, below=0.55cm of pol, draw=FairOrange!85!black, fill=FairOrange!10, text=DeepNavy] (met)
    {Metrics\\\small{utility + disparity(t)}};
  \node[box, right=0.55cm of met, draw=RiskRed!85!black, fill=RiskRed!10, text=DeepNavy] (mit)
    {Mitigation\\\small{constraints/penalty}};

  \draw[arr] (cfg) -- (env);
  \draw[arr] (env) -- (pol);
  \draw[arr] (pol) -- (log);
  \draw[arr] (log) -- (met);
  \draw[arr] (met) -- (mit);

  \node[small, below=0.1cm of met] {Report time-evolving gaps (windows), worst-group, and tradeoffs};
\end{tikzpicture}

\vspace{0.35em}
\begin{cblock}{DeepNavy}{Why this is the contribution}
A reusable harness that makes \Fair{fairness visible during learning} and comparable across domains.
\end{cblock}

\topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOn}{\QuantOn}
\refs{Offline/partial-feedback evaluation tools: Dud\'ik et al.; offline fairness guarantees: Metevier et al.}
\end{frame}
```

### Slide 8: Deliverables (Clinical “now” + Quantum “next”)

This is a very direct, neurodivergent-friendly mapping: DSCI 601 is green (clinical build), DSCI 602 is teal (quantum integration).

```latex
% --- Slide 8: Contributions + 601/602 timeline ---
\begin{frame}{\ticon{SeqPurple}\; Deliverables and timeline}
\leftbar{SeqPurple}
\small
\textcolor{SeqPurple}{\textbf{What is new (testable)}} vs. what is background.

\vspace{0.4em}
\begin{columns}[T,onlytextwidth]
  \column{0.5\textwidth}
  \begin{cblock}{ClinicalGreen}{DSCI 601 (now)}
    \begin{itemize}
      \item Implement \Clin{clinical} environment (simulation-first).
      \item Baselines: non-contextual + contextual.
      \item Define reward + fairness metrics (time-evolving).
      \item One mitigation mechanism + ablation of missingness.
    \end{itemize}
  \end{cblock}

  \column{0.48\textwidth}
  \begin{cblock}{TealAccent}{DSCI 602 (next)}
    \begin{itemize}
      \item Integrate \Quant{quantum routing} testbed (Paper2-style regimes).
      \item Add informative/restricted-context policies.
      \item Stress-test under shift/adversarial regimes.
      \item Cross-domain comparison + reproducible packaging.
    \end{itemize}
  \end{cblock}
\end{columns}

\vspace{0.2em}
\begin{cblock}{FairOrange}{Expected research outcome}
Identify when \Ctx{“more context”} reduces \Fair{disparity}, when it \emph{does not}, and when explicit fairness constraints are required.
\end{cblock}

\topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOn}{\QuantOn}
\refs{Project framing: your revised proposal + survey; quantum testbed scaffold: \texttt{quantum\_project}.}
\end{frame}
```

### Slide 9: Takeaway (Fairness as primary)

```latex
% --- Slide 9: Closing ---
\begin{frame}{\ticon{FairOrange}\; Takeaway}
\leftbar{FairOrange}
\small
\begin{cblock}{FairOrange}{Main message}
Fairness should be part of how sequential decision systems are \textbf{designed and evaluated}—especially when
\Ctx{context quality differs by group} and environments \Seq{shift over time}.
\end{cblock}

\vspace{0.35em}
\begin{columns}[T,onlytextwidth]
  \column{0.6\textwidth}
  \begin{cblock}{DeepNavy}{One-sentence thesis}
\Ctx{Context} is not just “more features”; it is a resource whose unequal quality can create persistent
\Fair{outcome gaps} unless fairness is monitored and mitigated during learning.
  \end{cblock}

  \column{0.38\textwidth}
  \begin{cblock}{SeqPurple}{Questions?}
  \textcolor{DeepNavy}{pizg8794@g.rit.edu}
  \end{cblock}
\end{columns}

\topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOff}{\QuantOff}
\refs{Core refs: Auer (UCB); Li (LinUCB); Hardt (EqOpp); Joseph (fair bandits); Chen (fair CMAB); Huang (EXPNeuralUCB); Wehner/Pant/Caleffi (quantum routing).}
\end{frame}
```

## Final checklist to keep the deck both calming and “lecture-proof”

Because you’re using color coding to reduce cognitive effort, the goal is that the scheme stays stable and never becomes a new thing to decode.

Keep the mapping consistent across slides (W3C cognitive guidance explicitly calls out consistent use of colors and visual cues as helpful). citeturn3search1turn0search0

Make sure every color cue is paired with text/shape labels (WCAG 1.4.1: don’t use color as the only means). citeturn1search4

If you ever darken a box fill, keep an eye on text contrast; WCAG contrast guidance is a good benchmark (4.5:1 for normal text; meaningful non-text cues ~3:1). citeturn1search2turn2search2

If you want an even stronger “orientation cue,” you already have slide numbers; pairing them with the consistent left bar + chips supports the “make steps clear / re-orient after distraction” goal from cognitive accessibility patterns. citeturn3search0turn3search3