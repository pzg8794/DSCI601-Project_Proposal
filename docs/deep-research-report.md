# Deep Research Review and PhD-Level Upgrade for Your DSCI601 Presentation

## Sources and artifacts reviewed

Your current Beamer deck is stored in your GitHub repo at `DSCI601-Project_Proposal/presentation/DSCI601_Project_Proposal_Presentation_2026_beamer.tex`. fileciteturn33file0L1-L1

The deck references an external figure `proposal_framework_figure.pdf` via `\includegraphics`, but that PDF is not present in the scanned GitHub repo contents (so compilation will fail unless the figure exists locally or in Drive). fileciteturn33file0L1-L1

You already have a “shared evaluation stack” diagram implemented in TikZ inside your related-work survey (`survey-related-work.tex`) that can replace the missing PDF figure cleanly (and more “PhD-like,” because it is editable, reproducible, and source-controlled). fileciteturn29file0L1-L1

Your revised proposal document (`revised-project-proposal.tex`) is more explicit than the slides about: deliverables, the two-domain evaluation design, fairness metrics (clinical: FNR/FPR gaps; routing: success/latency gaps), and planned mitigation mechanisms (constraints/penalties, calibration, missingness-aware augmentation). fileciteturn30file0L1-L1

The `quantum_project` repo is a strong “anchor” source for making the quantum portion technically concrete. In particular:
- The Paper2 integration report specifies a 4-node/4-path topology, per-hop fidelity (0.95) with multiplicative cascading, fixed 35-qubit allocation, and a threat ladder (Baseline/Stochastic/Markov/Adaptive/OnlineAdaptive), with expected performance benchmarks and research questions (RQ1–RQ3). fileciteturn18file0L1-L1  
- The testbeds hub explains how the framework builds on Huang et al.’s EXPNeuralUCB formulation (paths as “groups” with EXP3; allocations as “arms” with NeuralUCB), and summarizes the Paper2 extensions (contextual/predictive variants, allocators, validation tests). fileciteturn31file0L1-L1  
- The repo README documents the multi-testbed architecture and points to Paper2 as production-ready, with shared experiment logging and a results “data lake” design. fileciteturn32file0L1-L1  

On Google Drive, a synced `DSCI601_Project_Proposal_Presentation_2026.pptx` exists, which *may* be the version containing the missing figure (or equivalent visuals). fileciteturn34file0L1-L1

External literature that your talk implicitly relies on (and should explicitly cite, for PhD-level polish) includes: UCB foundations (Auer et al.), contextual bandits / LinUCB (Li et al.), equality of opportunity (Hardt et al.), fairness in bandits (Joseph et al.), fair contextual bandits (Chen et al., UAI), non-stationary bandits (Besbes et al.; Garivier & Moulines), restricted-context bandits (Bouneffouf et al., IJCAI), offline fairness guarantees for contextual bandits (Metevier et al., NeurIPS), quantum internet constraints (Wehner et al.), and entanglement routing foundations (Pant et al.; Caleffi). citeturn7search0turn4view2turn4view0turn4view3turn6search3turn1search8turn13view0turn6search1turn5search6turn2search1turn0search0turn7search5


## Assessment of the current deck against PhD-level expectations

Your current deck is **strong for a 5–10 minute MS-level project proposal**: it has a coherent narrative, clean visual design, and it correctly frames the work as *sequential decision-making under partial feedback* with fairness concerns in two domains. fileciteturn33file0L1-L1

However, it is **not yet “PhD-level” in the way faculty typically mean it**, mainly because the presentation currently emphasizes *topic overview* more than *research precision*. The biggest gaps:

The talk does not explicitly state a **formal problem** (variables, objective, constraints, what “fairness” means operationally, what “context quality” means mathematically). In the research literature, fairness definitions (e.g., equality of opportunity) and sequential learning constraints in bandits are formal objects—not just concepts—and that formality is part of what makes a talk “doctoral.” citeturn4view0turn4view3

The deck also lacks **scholarly anchoring** (citations on slides). You reference UCB/Thompson/LinUCB verbally, but without citations you “look like you’re summarizing Wikipedia,” even if you aren’t. Citations are especially important here because the fairness-in-bandits literature explicitly shows that fairness constraints change achievable regret and can require qualitatively different learning behavior. citeturn4view3

The related-work section is **too slide-expensive** for a 5–10 minute slot. You currently spend multiple frames on related work categories (overview + several sub-slides). That is fine for a 15–20 minute seminar, but in 5–10 minutes, it crowds out the two things that most strongly signal doctoral-level thinking:
- a crisp **research gap + hypothesis**, and  
- a concrete **evaluation design** (what you will measure, how you will stress-test it, what would falsify your claim).

There’s a practical issue too: the “Shared Evaluation Framework” slide includes `proposal_framework_figure.pdf`, but that artifact is not in the repo scan—so reproducibility is currently brittle. fileciteturn33file0L1-L1

Finally, for “PhD-level” technical credibility, your quantum portion should include a **concrete toy instance** (topology + physics model assumptions + threat model), which you *do* have in the `quantum_project` documentation, but it’s not surfaced in the slides yet. fileciteturn18file0L1-L1


## What a PhD-standard version should do in a 5–10 minute format

A PhD-standard 5–10 minute research talk is less about breadth and more about **research compression**:

It should state one precise research question (or hypothesis) and identify the minimal set of claims you will test. In your revised proposal, the key question is essentially: *when does informative context reduce disparity under shift—and when does it fail?* fileciteturn30file0L1-L1

It should include a compact formalization: “Here is the sequential decision structure; here is fairness; here is the tradeoff.” This is where you can use a single equation and a single diagram.

It should include one concrete testbed “anchor” example (quantum Paper2) and one clinical environment design sketch, since your contribution is partly cross-domain transfer under the *same measurement logic*. fileciteturn30file0L1-L1

It should use citations **sparingly but strategically** (3–8 across the whole deck). For this talk, the highest-yield citations are:
- LinUCB/contextual bandits (Li et al.) citeturn4view2  
- fairness definition (Hardt et al.) citeturn4view0  
- fairness in bandits / fairness–regret tension (Joseph et al.) citeturn4view3  
- restricted context / feature acquisition framing (Bouneffouf et al.) citeturn6search1  
- non-stationarity / change regimes (Besbes et al.; Garivier & Moulines) citeturn1search8turn13view0  
- quantum routing domain grounding (Wehner; Pant; Caleffi; plus your EXPNeuralUCB foundation) citeturn2search1turn0search0turn7search5turn9view0  

If you do only these, the talk will *read* doctoral-level without becoming jargon-heavy.


## Recommended revisions and upgraded slide flow

A clean PhD-leaning structure for **5–10 minutes** is **8–9 slides total** (including title and closing). The principle change is: compress related work into **one “positioning” slide**, and use the “recovered time” to add (a) a formal problem statement and (b) one concrete testbed diagram.

Also: replace the missing `proposal_framework_figure.pdf` with an in-source TikZ diagram. You already have a modular evaluation framework figure in your survey that can be simplified for Beamer. fileciteturn29file0L1-L1

Key content upgrades drawn from `quantum_project` that materially raise technical depth:
- Paper2 topology and physics: per-hop fidelity (0.95), multiplicative success across hops, fixed qubit capacity (35), and explicitly defined threat regimes. fileciteturn18file0L1-L1  
- “Paths as groups, allocations as arms” conceptual mapping (EXPNeuralUCB framing), which helps unify “bandits” with “routing.” fileciteturn31file0L1-L1  
- Showing that multiple regimes exist (stochastic vs Markov vs adaptive) supports your central claim that *context/fairness behavior is regime-dependent*, not just “more data fixes it.” fileciteturn18file0L1-L1

If you want a single extra external quantum routing bandit citation beyond Wehner/Pant/Caleffi/Huang, Chaudhary et al. (ICC 2023) is directly aligned with “bandit route selection in noisy quantum communication networks.” citeturn14search1


## Revised Beamer LaTeX source with PhD-level upgrades

This is a **drop-in replacement** for the current Beamer file (keeps your theme/colors) but:
- reduces to a **9-slide** 5–10 minute structure,
- adds a **formal problem + metrics** slide,
- adds a **concrete Paper2 quantum testbed diagram** (TikZ, no external PDF),
- replaces the missing `proposal_framework_figure.pdf` with a **reproducible evaluation-pipeline diagram** (TikZ),
- adds **lightweight citations per slide** (as short footers; no BibTeX required).

```latex
\documentclass[aspectratio=169,professionalfonts]{beamer}

\usetheme{Madrid}
\usecolortheme{default}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}[frame number]
\setbeamertemplate{blocks}[rounded][shadow=false]

\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{booktabs}
\usepackage{array}
\usepackage{ragged2e}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{positioning,arrows.meta,calc}
\usepackage{amsmath,amssymb}

\definecolor{DeepNavy}{RGB}{11,26,51}
\definecolor{TealAccent}{RGB}{0,201,167}
\definecolor{FairOrange}{RGB}{245,166,35}
\definecolor{ContextTeal}{RGB}{52,190,255}
\definecolor{SeqPurple}{RGB}{126,87,194}
\definecolor{ClinicalGreen}{RGB}{45,176,150}
\definecolor{SoftGray}{RGB}{86,100,126}
\definecolor{RiskRed}{RGB}{214,74,74}
\definecolor{PaleGray}{RGB}{244,248,252}
\definecolor{SoftInk}{RGB}{33,42,62}
\definecolor{HeaderLine}{RGB}{115,232,255}

\setbeamercolor{title}{fg=white}
\setbeamercolor{subtitle}{fg=PaleGray}
\setbeamercolor{titlelike}{fg=white,bg=DeepNavy}
\setbeamercolor{frametitle}{fg=white,bg=DeepNavy}
\setbeamercolor{normal text}{fg=SoftInk,bg=white}
\setbeamercolor{block title}{fg=white,bg=DeepNavy}
\setbeamercolor{block body}{fg=SoftInk,bg=PaleGray}
\setbeamercolor{itemize item}{fg=DeepNavy}
\setbeamercolor{itemize subitem}{fg=DeepNavy}
\setbeamercolor{structure}{fg=TealAccent}
\setbeamercolor{palette primary}{fg=white,bg=DeepNavy}
\setbeamercolor{palette secondary}{fg=white,bg=SeqPurple}
\setbeamercolor{palette tertiary}{fg=white,bg=DeepNavy}
\setbeamercolor{footline}{fg=SoftInk,bg=PaleGray}

\setbeamerfont{title}{series=\bfseries,size=\Large}
\setbeamerfont{subtitle}{series=\mdseries,size=\large}
\setbeamerfont{frametitle}{series=\bfseries,size=\large}
\setbeamerfont{block title}{series=\bfseries}

\title{Fairness-Aware Sequential Decision-Making}
\subtitle{Limited Context, Bandit Learning, and Two Testbeds (Clinical + Quantum Routing)}
\author{Piter Z. Garcia Bautista}
\institute{MS Data Science / Decision-Making \& Algorithmic Fairness, RIT\\Advisors: Dr. Daniel Krutz, Travis Desell}
\date{DSCI 601 • Applied Data Science I • Spring 2026}

\newcommand{\pillbox}[3]{%
  \begin{tikzpicture}
    \node[
      rounded corners=10pt,
      fill=#1!14,
      draw=#1!80!black,
      text width=0.92\linewidth,
      minimum height=1.25cm,
      align=center,
      inner sep=5pt
    ] {
      {\bfseries\small\color{DeepNavy} #2}\\[2pt]
      {\footnotesize\color{SoftGray} #3}
    };
  \end{tikzpicture}
}

\newcommand{\refs}[1]{%
  \vspace{0.2em}
  \begin{flushright}
    \scriptsize\color{SoftGray}{#1}
  \end{flushright}
}

\begin{document}

% --- Slide 1: Title ---
\begin{frame}[plain]
  \begin{beamercolorbox}[wd=\paperwidth,ht=3.15cm,dp=0ex,leftskip=0.8cm,rightskip=0.8cm]{titlelike}
    \vspace{0.35cm}
    {\centering\fontsize{18}{21}\selectfont\bfseries
    \parbox{0.94\paperwidth}{\centering Fairness-Aware Sequential Decision-Making}\par}
    \vspace{0.15cm}
    {\centering\usebeamerfont{subtitle}
    Limited context, bandit learning, and two testbeds (Clinical + Quantum Routing)\par}
    \vspace{0.18cm}
    {\color{HeaderLine}\rule{0.62\paperwidth}{1.4pt}}
  \end{beamercolorbox}

  \vspace{0.45cm}
  {\centering\large\color{DeepNavy} Piter Z. Garcia Bautista\par}
  \vspace{0.15cm}
  {\centering\small\color{SoftInk} MS Data Science / Decision-Making \& Algorithmic Fairness, RIT\par}
  {\centering\small\color{SoftGray} Advisors: Dr. Daniel Krutz, Travis Desell\par}
  \vspace{0.25cm}
  {\centering\normalsize\color{DeepNavy} DSCI 601 • Applied Data Science I • Spring 2026\par}

  \vspace{0.3cm}
  \begin{columns}[T,onlytextwidth]
    \column{0.33\textwidth}
      \pillbox{FairOrange}{Fairness}{Track outcome gaps over time, not just averages.}
    \column{0.33\textwidth}
      \pillbox{ContextTeal}{Context Quality}{Missing/noisy/delayed context is a fairness driver.}
    \column{0.33\textwidth}
      \pillbox{SeqPurple}{Sequential Effects}{Each decision shapes future evidence + outcomes.}
  \end{columns}
\end{frame}

% --- Slide 2: Motivation ---
\begin{frame}{Motivation}
\small
\textcolor{TealAccent}{Key claim: unequal \emph{measurement} produces unequal \emph{decisions} before any model ``looks biased.''}

\vspace{0.6em}
\begin{columns}[T,onlytextwidth]
  \column{0.6\textwidth}
    \begin{block}{Two domains, same structure}
    \begin{itemize}
      \item \textbf{Clinical:} choose tests / escalation steps under partial feedback; context can be systematically missing by group.
      \item \textbf{Quantum routing:} choose paths + allocate scarce qubits; link success uncertain and conditions shift.
      \item In both: policies optimize reward under uncertainty, but \textbf{fairness must be monitored as the policy learns}.
    \end{itemize}
    \end{block}
  \column{0.38\textwidth}
    \begin{block}{What ``fairness'' looks like}
      \textbf{Clinical:} FNR/FPR gaps, time-to-escalation gaps.\\
      \textbf{Routing:} success/latency gaps across flow/user groups.
    \end{block}
    \begin{block}{Why bandits?}
      Bandits model \textbf{partial feedback}: you only observe the outcome of what you chose.
    \end{block}
\end{columns}

\refs{Fairness metrics: Hardt et al. (EqOpp), Joseph et al. (fair bandits).}
\end{frame}

% --- Slide 3: Formal problem + metrics ---
\begin{frame}{Formal problem (compressed)}
\small
\textcolor{TealAccent}{Goal: learn a policy that is \emph{high utility} and \emph{low disparity}, under missing context and shift.}

\vspace{0.4em}
\begin{block}{Contextual bandit with groups and degraded context}
At round $t$: observe group $g_t\in\mathcal{G}$ and \emph{observed} context $\tilde{x}_t$ (possibly missing),
choose action $a_t\in\{1,\dots,K\}$, observe reward $r_t(a_t)$ (bandit feedback).
\[
\tilde{x}_t = M_t(g_t)\odot x_t \quad \text{(group-dependent missingness / noise)}
\]
\end{block}

\vspace{0.3em}
\begin{columns}[T,onlytextwidth]
  \column{0.52\textwidth}
    \begin{block}{Utility objective}
    \[
      \max_{\pi}\; \mathbb{E}\Big[\sum_{t=1}^{T} r_t\Big] \quad
      \text{(or minimize regret)}
    \]
    \end{block}
  \column{0.46\textwidth}
    \begin{block}{Fairness monitoring}
    Example (clinical): \textbf{EqOpp gap}
    \[
      \Delta^{\text{TPR}}(t) = \text{TPR}_{g=0}(t) - \text{TPR}_{g=1}(t)
    \]
    Track $\Delta(t)$ in sliding windows (not just end-of-run).
    \end{block}
\end{columns}

\refs{Contextual bandits: Li et al.; EqOpp: Hardt et al.; non-stationarity: Besbes et al., Garivier \& Moulines.}
\end{frame}

% --- Slide 4: Quantum testbed concretely (Paper2) ---
\begin{frame}{Quantum testbed anchor (Paper2)}
\small
\textcolor{TealAccent}{Concrete example (from \texttt{quantum\_project}): 4 nodes, 4 paths, per-hop fidelity, threat regimes.}

\vspace{0.2em}
\begin{columns}[T,onlytextwidth]
  \column{0.55\textwidth}
  \centering
  \begin{tikzpicture}[
    node/.style={circle, draw=DeepNavy, fill=ContextTeal!10, minimum size=8mm, inner sep=0pt},
    edge/.style={-Stealth, line width=0.9pt, draw=DeepNavy},
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

  \vspace{0.4em}
  \begin{block}{Physics (toy numbers)}
    2-hop success: $0.95^2=0.9025$ \\
    3-hop success: $0.95^3\approx 0.8574$
  \end{block}

  \column{0.43\textwidth}
  \begin{block}{Why this matters}
  Longer paths degrade; attacks create non-stationarity.\\
  The decision policy must adapt \emph{and} we must track service equity.
  \end{block}

  \begin{block}{Threat ladder (examples)}
  Baseline $\rightarrow$ Stochastic $\rightarrow$ Markov $\rightarrow$ Adaptive $\rightarrow$ OnlineAdaptive
  \end{block}

  \begin{block}{Bandit mapping}
  Paths $\approx$ arms (or groups of arms); qubit allocations $\approx$ structured actions.
  \end{block}
\end{columns}

\refs{Quantum routing context: Wehner et al.; Pant et al.; Caleffi; EXPNeuralUCB: Huang et al.}
\end{frame}

% --- Slide 5: Clinical testbed design sketch ---
\begin{frame}{Clinical testbed design (simulation-first)}
\small
\textcolor{TealAccent}{DSCI601 deliverable: a diagnostic-like sequential environment with controllable missingness + shift.}

\vspace{0.4em}
\begin{columns}[T,onlytextwidth]
  \column{0.55\textwidth}
    \begin{block}{Workflow abstraction}
    \begin{itemize}
      \item State: patient context $x_t$ (symptoms, vitals, history) + \textbf{missingness mask}.
      \item Action: choose next test / model / escalation step.
      \item Reward: utility minus cost/latency; penalize unsafe delay.
      \item Outcome fairness: FNR gap, TPR gap, time-to-escalation gap (by group).
    \end{itemize}
    \end{block}

    \begin{block}{Why simulation-first?}
      Enables fairness experiments without protected clinical datasets; shift + missingness can be injected transparently.
    \end{block}

  \column{0.43\textwidth}
  \centering
  \begin{tikzpicture}[
    box/.style={rounded corners=6pt, draw=DeepNavy, fill=PaleGray, align=center, minimum width=4.2cm, minimum height=0.8cm},
    arr/.style={-Stealth, line width=0.9pt, draw=DeepNavy},
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

\refs{Clinical bias motivation: Obermeyer et al. (proxy targets); fairness definition: Hardt et al.}
\end{frame}

% --- Slide 6: Methods (spectrum + fairness integration) ---
\begin{frame}{Method spectrum and fairness integration}
\small
\textcolor{TealAccent}{Compare policies by \emph{how much} and \emph{what quality} context they exploit, and how fairness enters learning.}

\vspace{0.4em}
\begin{columns}[T,onlytextwidth]
  \column{0.33\textwidth}
  \begin{block}{Non-contextual baselines}
    $\epsilon$-greedy, UCB, Thompson sampling.\\
    \textcolor{SoftGray}{Strong regret baselines, but blind to group-dependent missing context.}
  \end{block}

  \column{0.33\textwidth}
  \begin{block}{Contextual baselines}
    LinUCB-style policies.\\
    \textcolor{SoftGray}{Good when context is reliable; can amplify measurement inequities if context quality differs by group.}
  \end{block}

  \column{0.33\textwidth}
  \begin{block}{Informative / restricted context}
    Choose which features to observe (feature acquisition / restricted context).\\
    \textcolor{SoftGray}{Key for studying “context quality” as a fairness lever.}
  \end{block}
\end{columns}

\vspace{0.35em}
\begin{block}{Fairness mechanisms (what makes it ``PhD-level'' here)}
\begin{itemize}
  \item \textbf{Monitoring:} time-evolving disparity curves, worst-group metrics (not only averages).
  \item \textbf{Mitigation in-loop:} constraints/penalties or fairness-aware calibration during learning (not just post-hoc audits).
  \item \textbf{Shift robustness:} evaluate under stochastic + adversarial regimes.
\end{itemize}
\end{block}

\refs{Bandits: Auer et al.; contextual bandits: Li et al.; fair bandits: Joseph et al.; restricted context: Bouneffouf et al.; fair CMAB constraints: Chen et al.}
\end{frame}

% --- Slide 7: Shared evaluation framework (TikZ, no missing PDF) ---
\begin{frame}{Shared evaluation framework (reproducible)}
\small
\textcolor{TealAccent}{One evaluation logic across both domains: configure $\rightarrow$ run policies $\rightarrow$ log $\rightarrow$ measure fairness over time.}

\vspace{0.25em}
\centering
\begin{tikzpicture}[
  box/.style={rounded corners=7pt, draw=DeepNavy, fill=PaleGray, align=center, minimum width=3.2cm, minimum height=0.92cm},
  arr/.style={-Stealth, line width=0.9pt, draw=DeepNavy},
  small/.style={font=\scriptsize, color=SoftGray}
]
  \node[box] (cfg) {Config\\\small{shift + missingness}};
  \node[box, right=0.55cm of cfg] (env) {Testbed\\\small{clinical or quantum}};
  \node[box, right=0.55cm of env] (pol) {Policy\\\small{MAB/CMAB/iCMAB}};
  \node[box, right=0.55cm of pol] (log) {Logger\\\small{full run state}};
  \node[box, below=0.55cm of pol] (met) {Metrics\\\small{utility + disparity(t)}};
  \node[box, right=0.55cm of met] (mit) {Mitigation\\\small{constraints/penalty}};

  \draw[arr] (cfg) -- (env);
  \draw[arr] (env) -- (pol);
  \draw[arr] (pol) -- (log);
  \draw[arr] (log) -- (met);
  \draw[arr] (met) -- (mit);

  \node[small, below=0.1cm of met] {Report time-evolving gaps (windows), worst-group, and tradeoffs};

\end{tikzpicture}

\vspace{0.35em}
\begin{block}{Why this is the contribution}
A reusable harness that makes fairness visible \emph{during learning} and comparable across domains.
\end{block}

\refs{Offline/partial-feedback evaluation tools: Dud\'ik et al.; offline fairness guarantees: Metevier et al.}
\end{frame}

% --- Slide 8: Contributions + 601/602 timeline ---
\begin{frame}{Deliverables and timeline}
\small
\textcolor{TealAccent}{What is new (and testable) vs. what is background.}

\vspace{0.4em}
\begin{columns}[T,onlytextwidth]
  \column{0.5\textwidth}
  \begin{block}{DSCI 601 (now)}
    \begin{itemize}
      \item Implement clinical environment (simulation-first).
      \item Baselines: non-contextual + contextual.
      \item Define reward + fairness metrics (time-evolving).
      \item One mitigation mechanism + ablation of missingness.
    \end{itemize}
  \end{block}

  \column{0.48\textwidth}
  \begin{block}{DSCI 602 (next)}
    \begin{itemize}
      \item Integrate quantum routing testbed (Paper2-style regimes).
      \item Add informative/restricted-context policies.
      \item Stress-test under shift/adversarial regimes.
      \item Cross-domain comparison + reproducible packaging.
    \end{itemize}
  \end{block}
\end{columns}

\vspace{0.25em}
\begin{block}{Expected research outcome}
Identify when “more context” reduces disparity, when it \emph{does not}, and when explicit fairness constraints are required.
\end{block}

\refs{Project framing: your revised proposal + survey; quantum testbed scaffold: \texttt{quantum\_project}.}
\end{frame}

% --- Slide 9: Closing ---
\begin{frame}{Takeaway}
\small
\begin{block}{Main message}
Fairness should be part of how sequential decision systems are \textbf{designed and evaluated}—especially when \textbf{context quality differs by group} and environments \textbf{shift over time}.
\end{block}

\vspace{0.35em}
\begin{columns}[T,onlytextwidth]
  \column{0.6\textwidth}
  \begin{block}{One-sentence thesis}
Context is not just “more features”; it is a \textbf{resource} whose unequal quality can create persistent outcome gaps unless fairness is monitored and mitigated during learning.
  \end{block}
  \column{0.38\textwidth}
  \begin{block}{Questions?}
  \textcolor{DeepNavy}{pizg8794@g.rit.edu}
  \end{block}
\end{columns}

\refs{Core refs: Auer (UCB); Li (LinUCB); Hardt (EqOpp); Joseph (fair bandits); Chen (fair CMAB); Huang (EXPNeuralUCB); Wehner/Pant/Caleffi (quantum routing).}
\end{frame}

\end{document}
```

### Notes on how this specifically addresses the weaknesses

This version directly fixes the broken external figure dependency by replacing it with a TikZ-drawn evaluation framework (and you can optionally reuse/condense your more detailed diagram from the survey). fileciteturn33file0L1-L1 fileciteturn29file0L1-L1

It brings in the “quantum routing is real and specific” credibility by using the Paper2 topology and physics assumptions (per-hop fidelity, hop-based success) and mentioning the threat ladder explicitly, aligned with your `quantum_project` documentation. fileciteturn18file0L1-L1

It aligns the “two-domain” promise with the wording in your revised proposal: simulation-first clinical environment, time-evolving fairness metrics, at least one mitigation mechanism, then transfer to quantum routing. fileciteturn30file0L1-L1


## Speaker notes and 5–10 minute timing

This slide count is designed so you can hit **~7–9 minutes** at a calm pace, or **~5–6 minutes** if needed by tightening explanations.

A workable pacing:

Title (15–20s): One sentence: “I’m studying when better context actually reduces fairness gaps in sequential decision-making, and when it doesn’t.”

Motivation (45–60s): Give one concrete “unequal measurement” sentence; name the two domains; state what fairness metrics look like.

Formal problem (70–90s): Walk through the timeline: observe (possibly missing) context → choose action → observe partial feedback → log disparity(t). State that fairness is monitored over time, not only at the end.

Quantum testbed (60–75s): Explain 4-node/4-path toy example and why hop length matters; say “this comes from our production-ready Paper2 testbed.” fileciteturn18file0L1-L1

Clinical testbed (60–75s): Explain simulation-first environment and what “missingness that depends on group” means; name the fairness metrics.

Methods (60–75s): Explain spectrum: bandit → contextual → restricted-context; then one sentence on fairness mechanism classes.

Evaluation framework (50–70s): Explain the pipeline: configure shift/missingness → run policies → log → compute fairness curves and tradeoffs.

Timeline (45–60s): DSCI601 deliverables vs DSCI602 transfer/stress tests.

Takeaway/Q (20–30s): Repeat thesis; stop.

If you want an even more PhD-style close, add a single “falsifiable hypothesis” sentence on Slide 8, like: “Hypothesis: under group-skewed missingness, contextual bandits can reduce regret while worsening $\Delta^{\text{TPR}}(t)$ unless fairness enters the learning objective.” That’s consistent with the fairness-in-sequential-learning motivation from the literature. citeturn4view3turn4view0