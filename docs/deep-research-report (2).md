# Accessible, Color-Coded DSCI601 Beamer Deck With Semantic Slide Cues and TikZ Diagrams

## Executive summary

You shared two constraints that **conflict**: the earlier “9 slides / 5–10 minutes” target and the **official DSCI601 presentation requirements** that specify the presentation should be **~10–15 slides** and **~10 minutes**, with specific required slide categories (background, related-work table + detailed related-work slides, proposed project slides, and a two-semester approach slide). fileciteturn41file1L1-L1  
This response prioritizes meeting the **course rubric and required structure** while preserving your neurodivergent-friendly color system and keeping timing tight.

Deliverable included below: a **single complete `.tex` Beamer document** that:

- Preserves your **Madrid theme + your color palette** (DeepNavy, TealAccent, FairOrange, ContextTeal, SeqPurple, ClinicalGreen, RiskRed, etc.). fileciteturn37file0L1-L1  
- Implements a **semantic color-coding system** with reusable macros: `\ticon`, `\leftbar`, `\chipon/\chipoff`, `\topicstrip`, `\cblock`, and **term highlighting** macros, and uses them consistently on **every slide**. (Design is aligned with the W3C cognitive guidance principle of **consistent visual design**, which reduces relearning and cognitive load across screens.) citeturn1search2  
- Uses **TikZ-only** figures to replace external images (quantum testbed diagram, clinical workflow diagram, shared evaluation pipeline), with **colored nodes/edges + explicit labels/shapes** so meaning is never conveyed by color alone. (WCAG explicitly requires that color not be the only visual means of conveying information.) citeturn1search0  
- Incorporates **contrast targets** and a simple pre-submit contrast-check step guided by WCAG contrast criteria for text and meaningful graphics (4.5:1 for normal text; 3:1 for large text; and 3:1 for meaningful non-text graphics). citeturn0search3turn1search3  
- Includes **concise speaker notes** on every slide and ends with a combined **Key References + Accessibility Checklist** slide (you can keep it as a “backup/checklist” slide and not present it live).

## Information needs and how they were resolved

To do this well, I needed to verify:

- The **official DSCI601 presentation structure and rubric** (slides required, timing, scoring emphasis). fileciteturn41file1L1-L1  
- Your **existing slide narrative and style** so the upgraded deck stays consistent with your visual identity. fileciteturn37file0L1-L1  
- The **quantum testbed specifics** (topology, fidelity, qubit allocations, threat ladder) so the quantum diagram and claims are concrete and aligned with your primary repo. fileciteturn38file0L1-L1  
- The “foundation mapping” for quantum routing as a structured bandit problem (paths as groups / allocations as arms) to strengthen the cross-domain argument. fileciteturn39file0L1-L1  
- The **accessibility constraints** most relevant to color-coding (color-not-only, contrast for text and meaningful graphics, consistent design cues, spacing). citeturn1search0turn0search3turn1search3turn1search2turn1search1  

## Connector scan findings used to ground the deck

GitHub (project materials):

- Your prior Beamer deck in `DSCI601-Project_Proposal` establishes the design language (theme, colors, pillbox styling) and the original narrative structure. fileciteturn37file0L1-L1  
- The `quantum_project` “Paper2 Integration Report” provides exactly the parameters needed to make a credible quantum diagram: 4-node/4-path topology, per-hop fidelity 0.95 with multiplicative path success, total 35 qubits with fixed allocation (8,10,8,9), and a five-level threat ladder (Baseline → OnlineAdaptive). fileciteturn38file0L1-L1  
- The `quantum_project` testbeds hub frames the conceptual mapping we rely on in the talk: **paths as groups** selected via EXP3 and **allocations as arms** inside groups with NeuralUCB (EXPNeuralUCB-style), plus the testbed family context. fileciteturn39file0L1-L1  
- Your EQUITAS writeup is available (useful as a domain testbed / fairness audit framing), though the final presentation keeps it concise to fit 10 minutes and to align with your current cross-domain bandit research thrust. fileciteturn40file0L1-L1  

Google Drive (course requirements and artifacts):

- The course’s “Project Proposal Presentation” instructions explicitly specify **10–15 slides**, **10 minutes**, and require: 1–3 background slides, a related-work overview table slide, 2–5 detailed related-work slides, 3–5 proposed project slides, and a next-two-semesters approach slide. fileciteturn41file1L1-L1  
- Your PPT version of the original deck exists in Drive, confirming the baseline content and structure you were working from. fileciteturn41file7L1-L1  

## Accessibility research synthesis for color-coded slide systems

A color-coded slide system is most accessible when it is **semantic + consistent + redundant**:

Color must not be the only way meaning is conveyed. WCAG SC 1.4.1 requires that color not be used as the only visual means of conveying information; the recommended fix is to add **text labels, shapes, or other cues** in addition to color. citeturn1search0  
In this deck, that redundancy is implemented by: (a) a labeled chip strip (“Fairness / Context / Sequential / Clinical / Quantum”), (b) a title icon square plus explicit title text, and (c) labels inside all diagrams.

Text contrast matters (especially for small slide text). WCAG guidance for contrast (SC 1.4.3) recommends at least **4.5:1** for normal text and **3:1** for large text. citeturn0search3  
To help meet this, the deck avoids “white text on bright accent colors” for most elements. Accent colors are used as **tints** behind dark text, and when a dark title bar is used, it is DeepNavy with white text (high contrast).

Non-text elements that carry meaning (lines, arrows, diagram edges) also need contrast. WCAG non-text contrast guidance (SC 1.4.11) calls for **3:1** contrast for meaningful graphical objects against adjacent colors. citeturn1search3  
This is why the left accent bar and diagram strokes are drawn with a darkened version of the semantic color (e.g., `FairOrange!85!black`) rather than the pure bright color.

Consistent visual design reduces cognitive load. W3C’s Cognitive Accessibility “Use a Consistent Visual Design” pattern directly supports the approach of repeating the same slide-cues (left bar, title icon, chips) across slides so the viewer doesn’t have to re-learn the interface each time. citeturn1search2  

Finally, color-vision deficiency is common enough that you should assume some viewers will not perceive your hues accurately; NEI notes “about 1 in 12 men” have color vision deficiency. citeturn0search6  
That is another reason the deck’s semantics are never color-only: everything is labeled.

## Implementation details and design decisions

Semantic mapping used consistently throughout the deck:

- **Fairness** → `FairOrange`
- **Context quality / missingness** → `ContextTeal`
- **Sequential learning / bandits** → `SeqPurple`
- **Clinical domain** → `ClinicalGreen`
- **Quantum domain** → `TealAccent`
- **Risk / caution / tradeoffs** → `RiskRed`

To meet DSCI601 requirements, the deck is **13 slides** total: it fits the required slide categories while keeping talkable content to ~10 minutes; the final slide is a combined “References + Accessibility Checklist” slide you can keep as a backup/checklist and optionally skip live. fileciteturn41file1L1-L1  

A recommended “last-mile” contrast check step is also included (end slide + report guidance): after compiling the PDF, spot-check a few representative slides with a contrast tool and confirm the WCAG target ratios for text and meaningful lines/diagram elements. citeturn0search3turn1search3  

## Complete LaTeX Beamer `.tex` file

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
\usetikzlibrary{positioning,arrows.meta,calc,fit}
\usepackage{amsmath,amssymb}

% Speaker notes (hidden by default; can be shown for rehearsal)
\usepackage{pgfpages}
\setbeameroption{hide notes}
% Uncomment to show notes on a second screen:
% \setbeameroption{show notes on second screen=right}

% =========================
% User palette (unchanged)
% =========================
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

% =========================
% Beamer colors (unchanged)
% =========================
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

% =========================
% Beamer fonts (unchanged)
% =========================
\setbeamerfont{title}{series=\bfseries,size=\Large}
\setbeamerfont{subtitle}{series=\mdseries,size=\large}
\setbeamerfont{frametitle}{series=\bfseries,size=\large}
\setbeamerfont{block title}{series=\bfseries}

% =========================
% Title metadata (unchanged)
% =========================
\title{Fairness-Aware Sequential Decision-Making}
\subtitle{Limited Context, Bandit Learning, and Two Testbeds (Clinical + Quantum Routing)}
\author{Piter Z. Garcia Bautista}
\institute{MS Data Science / Decision-Making \& Algorithmic Fairness, RIT\\Advisors: Dr. Daniel Krutz, Travis Desell}
\date{DSCI 601 • Applied Data Science I • Spring 2026}

% =========================
% Existing pillbox macro (title slide)
% =========================
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
  \vspace{0.15em}
  \begin{flushright}
    \scriptsize\color{SoftGray}{#1}
  \end{flushright}
}

% ==========================================================
% Semantic color-coding helpers (accessibility-aware)
% ==========================================================

% Small colored square (paired with text in frametitle, not color-only)
\newcommand{\ticon}[1]{\textcolor{#1}{\rule{0.95ex}{0.95ex}}}

% Left accent bar (darkened for non-text contrast against white)
\newcommand{\leftbar}[1]{%
  \begin{tikzpicture}[remember picture,overlay]
    \fill[#1!85!black] (current page.north west) rectangle ([xshift=6pt]current page.south west);
  \end{tikzpicture}%
}

% Topic chips (text + shape, not color-only)
\newcommand{\chipon}[2]{%
  \tikz[baseline=-0.6ex]{
    \node[
      rounded corners=4pt,
      draw=#1!75!black,
      fill=#1!14,
      text=DeepNavy,
      font=\scriptsize\bfseries,
      inner xsep=5pt,
      inner ysep=2.1pt
    ] {#2};
  }%
}
\newcommand{\chipoff}[1]{%
  \tikz[baseline=-0.6ex]{
    \node[
      rounded corners=4pt,
      draw=SoftGray!30,
      fill=PaleGray,
      text=SoftGray,
      font=\scriptsize,
      inner xsep=5pt,
      inner ysep=2.1pt
    ] {#1};
  }%
}

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

\newcommand{\topicstrip}[5]{%
  \vspace{0.25em}
  \noindent #1\hspace{0.25em}#2\hspace{0.25em}#3\hspace{0.25em}#4\hspace{0.25em}#5
}

% Term-highlighting macros (paired with text; avoid low-contrast on light backgrounds)
\newcommand{\Fair}[1]{\textcolor{FairOrange!85!black}{\textbf{#1}}}
\newcommand{\Ctx}[1]{\textcolor{ContextTeal!85!black}{\textbf{#1}}}
\newcommand{\Seq}[1]{\textcolor{SeqPurple!85!black}{\textbf{#1}}}
\newcommand{\Clin}[1]{\textcolor{ClinicalGreen!85!black}{\textbf{#1}}}
\newcommand{\Quant}[1]{\textcolor{TealAccent!85!black}{\textbf{#1}}}
\newcommand{\Risk}[1]{\textcolor{RiskRed!85!black}{\textbf{#1}}}

% Color-coded block:
% - Title bar stays DeepNavy (high contrast with white text)
% - Category color appears as icon + tinted body (readable dark text)
\newenvironment{cblock}[2]{%
  \begingroup
  \setbeamercolor{block title}{fg=white,bg=DeepNavy}
  \setbeamercolor{block body}{fg=SoftInk,bg=#1!8}
  \begin{block}{\ticon{#1}\; #2}
}{%
  \end{block}
  \endgroup
}

% ==========================================================
% Document
% ==========================================================
\begin{document}

% ----------------------------------------------------------
% Slide 1: Title (required)
% ----------------------------------------------------------
\begin{frame}[plain]
\leftbar{DeepNavy}

  \begin{beamercolorbox}[wd=\paperwidth,ht=3.15cm,dp=0ex,leftskip=0.8cm,rightskip=0.8cm]{titlelike}
    \vspace{0.30cm}
    {\centering\fontsize{18}{21}\selectfont\bfseries
    \parbox{0.94\paperwidth}{\centering Fairness-Aware Sequential Decision-Making}\par}
    \vspace{0.12cm}
    {\centering\usebeamerfont{subtitle}
    Limited context, bandit learning, and two testbeds (Clinical + Quantum Routing)\par}
    \vspace{0.15cm}
    {\color{HeaderLine}\rule{0.62\paperwidth}{1.4pt}}
    \vspace{0.05cm}

    {\centering\scriptsize
      \ticon{FairOrange}\;Fairness \quad
      \ticon{ContextTeal}\;Context \quad
      \ticon{SeqPurple}\;Sequential \quad
      \ticon{ClinicalGreen}\;Clinical \quad
      \ticon{TealAccent}\;Quantum
    \par}
  \end{beamercolorbox}

  \vspace{0.40cm}
  {\centering\large\color{DeepNavy} Piter Z. Garcia Bautista\par}
  \vspace{0.12cm}
  {\centering\small\color{SoftInk} MS Data Science / Decision-Making \& Algorithmic Fairness, RIT\par}
  {\centering\small\color{SoftGray} Advisors: Dr. Daniel Krutz, Travis Desell\par}
  \vspace{0.20cm}
  {\centering\normalsize\color{DeepNavy} DSCI 601 • Applied Data Science I • Spring 2026\par}

  \vspace{0.25cm}
  \begin{columns}[T,onlytextwidth]
    \column{0.33\textwidth}
      \pillbox{FairOrange}{Fairness}{Track outcome gaps over time, not just averages.}
    \column{0.33\textwidth}
      \pillbox{ContextTeal}{Context Quality}{Missing/noisy/delayed context is a fairness driver.}
    \column{0.33\textwidth}
      \pillbox{SeqPurple}{Sequential Effects}{Each decision shapes future evidence + outcomes.}
  \end{columns}

  \vspace{0.25cm}
  \topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOn}{\QuantOn}

\note{
\begin{itemize}\itemsep0.2em
  \item (0:15–0:20) One-sentence opener: I study when “more context” reduces fairness gaps in sequential decisions—and when it fails.
  \item Point to the chip strip: these colors will repeat on every slide for quick orientation.
\end{itemize}
}
\end{frame}

% ----------------------------------------------------------
% Slide 2: Background 1 (required: 1–3 background slides)
% ----------------------------------------------------------
\begin{frame}{\ticon{FairOrange}\; Motivation: fairness begins before modeling}
\leftbar{FairOrange}
\small
\textcolor{FairOrange!85!black}{\textbf{Core idea:}}
unequal \Ctx{measurement} produces unequal \Fair{decisions} before any model “looks biased.”

\vspace{0.4em}
\begin{columns}[T,onlytextwidth]
  \column{0.62\textwidth}
    \begin{cblock}{FairOrange}{Why this is a sequential decision problem}
    \begin{itemize}\itemsep0.25em
      \item Many systems decide repeatedly under uncertainty (choose a test, route traffic, allocate scarce capacity).
      \item \Seq{Partial feedback}: you only observe outcomes for the action you chose.
      \item If we optimize only average utility, \Fair{worst-group failures} can remain hidden.
    \end{itemize}
    \end{cblock}

  \column{0.36\textwidth}
    \begin{cblock}{ClinicalGreen}{Clinical example}
      Test selection / escalation when context is missing or delayed for some groups.
    \end{cblock}
    \begin{cblock}{TealAccent}{Quantum example}
      Path choice + qubit allocation under uncertain links and shifting threats.
    \end{cblock}
\end{columns}

\topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOn}{\QuantOn}
\refs{Accessibility cue: color is paired with text labels (WCAG Use of Color).}
\note{
\begin{itemize}\itemsep0.2em
  \item (0:50–1:10) Define “fairness” in plain terms: we track outcome gaps over time, not just overall averages.
  \item Emphasize: this is about \emph{decision-making} (what we do next), not only prediction accuracy.
\end{itemize}
}
\end{frame}

% ----------------------------------------------------------
% Slide 3: Background 2
% ----------------------------------------------------------
\begin{frame}{\ticon{SeqPurple}\; Background: bandits, context, and partial feedback}
\leftbar{SeqPurple}
\small
\textcolor{SeqPurple!85!black}{\textbf{Bandits}} model online decisions with \Seq{explore/exploit} tradeoffs and \Seq{partial feedback}.

\vspace{0.25em}
\begin{columns}[T,onlytextwidth]
  \column{0.33\textwidth}
    \begin{cblock}{SeqPurple}{MAB (non-contextual)}
      Choose using reward history.\\
      \textcolor{SoftGray}{UCB, Thompson, $\epsilon$-greedy.}
    \end{cblock}
  \column{0.33\textwidth}
    \begin{cblock}{ContextTeal}{CMAB (contextual)}
      Observe features $x_t$ before acting.\\
      \textcolor{SoftGray}{Example: LinUCB.}
    \end{cblock}
  \column{0.33\textwidth}
    \begin{cblock}{ContextTeal}{iCMAB / restricted context}
      Decide what context to acquire when context is costly/uneven.
    \end{cblock}
\end{columns}

\vspace{0.3em}
\begin{cblock}{FairOrange}{Why context quality is a fairness lever}
If group $A$ systematically has noisier/missing $\tilde{x}$ than group $B$, the policy can look “optimal” on average while producing persistent \Fair{gap trajectories}.
\end{cblock}

\topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOff}{\QuantOff}
\refs{Refs (talk): UCB (Auer), LinUCB (Li), fair bandits (Joseph).}
\note{
\begin{itemize}\itemsep0.2em
  \item (1:10–2:20) Define CMAB in one sentence; define iCMAB as “choosing what you know before you choose what you do.”
  \item Transition: now that the decision framework is set, I’ll position the project relative to prior work.
\end{itemize}
}
\end{frame}

% ----------------------------------------------------------
% Slide 4: Related work table (required)
% ----------------------------------------------------------
\begin{frame}{\ticon{ContextTeal}\; Related work overview table}
\leftbar{ContextTeal}
\scriptsize
\begin{cblock}{ContextTeal}{How the literature maps to this project (table required by rubric)}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{p{0.19\linewidth} p{0.26\linewidth} p{0.25\linewidth} p{0.26\linewidth}}
\toprule
\textbf{Subtopic} & \textbf{Representative works} & \textbf{Key contribution} & \textbf{Gap this project targets} \\
\midrule
Bandit foundations & UCB, Thompson sampling & Regret-optimal exploration baselines & Typically optimize utility only (fairness not tracked during learning) \\
\addlinespace[0.2em]
Contextual bandits & LinUCB / linear bandits & Uses side-information $x_t$ to improve decisions & Can amplify inequities when context quality differs by group \\
\addlinespace[0.2em]
Restricted / informative context & Feature acquisition / restricted-context bandits & Models missing/costly/uneven context & Limited work on fairness under group-skewed missingness \\
\addlinespace[0.2em]
Non-stationarity / shift & Non-stationary bandits & Policies under drift / changing rewards & Few integrate shift + fairness + partial feedback together \\
\addlinespace[0.2em]
Fairness in sequential learning & Equality of opportunity; fair bandits & Makes fairness constraints explicit & Many notions are simplified; less emphasis on time-evolving outcome gaps \\
\addlinespace[0.2em]
Domain testbeds & EQUITAS (clinical audit); quantum routing bandits & Realistic settings where bias/robustness matters & Need a shared fairness-aware evaluation harness across both domains \\
\bottomrule
\end{tabular}
\end{cblock}

\topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOn}{\QuantOn}
\refs{Slide purpose: meet “overview table” requirement; details next.}
\note{
\begin{itemize}\itemsep0.2em
  \item (2:20–3:10) Spend ~30–40s: “Here’s the map; next two slides zoom into the key gaps.”
  \item Point out your novelty: fairness over time + uneven context + transfer across domains.
\end{itemize}
}
\end{frame}

% ----------------------------------------------------------
% Slide 5: Related work detail 1 (required 2–5 detailed related work slides)
% ----------------------------------------------------------
\begin{frame}{\ticon{SeqPurple}\; Related work: learning under partial feedback and limited context}
\leftbar{SeqPurple}
\small

\begin{columns}[T,onlytextwidth]
  \column{0.33\textwidth}
    \begin{cblock}{SeqPurple}{Bandit baselines}
      Strong online-learning baselines (UCB, Thompson).\\
      \textcolor{SoftGray}{Useful comparisons for any new policy.}
    \end{cblock}

  \column{0.33\textwidth}
    \begin{cblock}{ContextTeal}{Contextual improvements}
      LinUCB-style policies improve efficiency when context is reliable.\\
      \textcolor{SoftGray}{Risk: “better use of bad context.”}
    \end{cblock}

  \column{0.33\textwidth}
    \begin{cblock}{ContextTeal}{Restricted context}
      Models “what you’re allowed to know” or “what you can afford to observe.”\\
      \textcolor{SoftGray}{Matches missing/unequal context reality.}
    \end{cblock}
\end{columns}

\vspace{0.25em}
\begin{cblock}{RiskRed}{Where the gap shows up}
Most work optimizes \emph{utility under uncertainty}; fewer track \Fair{disparity trajectories} as the policy adapts under shift.
\end{cblock}

\topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOff}{\QuantOff}
\refs{Refs (talk): UCB/TS; LinUCB; restricted-context bandits; non-stationary bandits.}
\note{
\begin{itemize}\itemsep0.2em
  \item (~0:40) One sentence per column. Emphasize the “restricted context” connection to fairness.
  \item One key phrase: “we don’t assume more features fixes fairness.”
\end{itemize}
}
\end{frame}

% ----------------------------------------------------------
% Slide 6: Related work detail 2
% ----------------------------------------------------------
\begin{frame}{\ticon{FairOrange}\; Related work: fairness in sequential learning}
\leftbar{FairOrange}
\small

\begin{columns}[T,onlytextwidth]
  \column{0.52\textwidth}
    \begin{cblock}{FairOrange}{Outcome-based fairness (example)}
      Equality of opportunity motivates monitoring gaps in true-positive rates across groups.\\[0.4em]
      \[
        \Delta^{\text{TPR}}(t)=\text{TPR}_{g=0}(t)-\text{TPR}_{g=1}(t)
      \]
      \textcolor{SoftGray}{Key idea: measure over time, not only at the end.}
    \end{cblock}

  \column{0.46\textwidth}
    \begin{cblock}{SeqPurple}{Fairness changes learning}
      Fair bandit results show that adding constraints can change what can be learned efficiently.\\
      \textcolor{SoftGray}{Fairness is not “free,” so we quantify tradeoffs.}
    \end{cblock}
\end{columns}

\vspace{0.25em}
\begin{cblock}{ContextTeal}{What is still missing (for this project)}
Few frameworks jointly handle: \Ctx{unequal context quality} + \Seq{partial feedback} + \Seq{shift} + \Fair{fairness over time}, and then test transfer across domains.
\end{cblock}

\topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOff}{\QuantOff}
\refs{Refs (talk): EqOpp (Hardt); fair bandits (Joseph); fair contextual bandits (Chen).}
\note{
\begin{itemize}\itemsep0.2em
  \item (~0:50) Define EqOpp in plain language: “equal chance to catch positives across groups.”
  \item Transition: now show the two grounding testbeds and why they’re complementary.
\end{itemize}
}
\end{frame}

% ----------------------------------------------------------
% Slide 7: Related work detail 3 (domain testbeds + quantum TikZ)
% ----------------------------------------------------------
\begin{frame}{\ticon{TealAccent}\; Related work: domain testbeds (Clinical + Quantum)}
\leftbar{TealAccent}
\scriptsize

\begin{columns}[T,onlytextwidth]
  \column{0.50\textwidth}
    \begin{cblock}{ClinicalGreen}{Clinical audit perspective (EQUITAS-style)}
      Emphasizes that predictive performance and fairness auditing should be evaluated together; many clinical audits are primarily offline/static rather than online sequential decisions.
    \end{cblock}

    \vspace{0.2em}
    \begin{cblock}{FairOrange}{What we take from this}
      Use audit-style thinking \emph{inside} the learning loop: log disparity(t), worst-group metrics, and escalation delays.
    \end{cblock}

  \column{0.48\textwidth}
    \begin{cblock}{TealAccent}{Quantum routing bandit testbed (Paper2 anchor)}
      4 nodes, 4 paths, per-hop fidelity 0.95 with multiplicative path success; fixed 35-qubit allocation; threats from Baseline to OnlineAdaptive.
    \end{cblock}

    \vspace{0.2em}
    \centering
    \begin{tikzpicture}[
      node/.style={circle, draw=TealAccent!85!black, fill=TealAccent!12, minimum size=8mm, inner sep=0pt},
      edge/.style={-Stealth, line width=0.9pt, draw=TealAccent!85!black},
      lab/.style={font=\scriptsize, color=SoftGray}
    ]
      \node[node] (n1) {1};
      \node[node, right=2.0cm of n1] (n2) {2};
      \node[node, below=1.35cm of n1] (n3) {3};
      \node[node, below=1.35cm of n2] (n4) {4};

      \draw[edge] (n1) -- node[lab, above] {hop} (n2);
      \draw[edge] (n1) -- node[lab, left] {hop} (n3);
      \draw[edge] (n2) -- node[lab, right] {hop} (n4);
      \draw[edge] (n3) -- node[lab, below] {hop} (n4);

      \node[lab, above=0.10cm of n1] {Src};
      \node[lab, above=0.10cm of n4] {Dst};

      \node[lab, below=0.10cm of n3] {$0.95$ per hop};
      \node[lab, below=0.42cm of n3] {$0.95^2=0.9025;\;0.95^3\approx0.8574$};
    \end{tikzpicture}
\end{columns}

\vspace{0.2em}
\topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOn}{\QuantOn}
\refs{Repo anchoring: Paper2 parameters + threat ladder; EXPNeuralUCB “paths as groups, allocations as arms.”}
\note{
\begin{itemize}\itemsep0.2em
  \item (~0:55) Quick left-to-right: clinical audit mindset + quantum realistic sequential testbed.
  \item Emphasize: the shared structure lets us test whether fairness-aware decision principles transfer.
\end{itemize}
}
\end{frame}

% ----------------------------------------------------------
% Slide 8: Proposed project 1 (required 3–5 proposed project slides)
% ----------------------------------------------------------
\begin{frame}{\ticon{FairOrange}\; Proposed project: research question and hypotheses}
\leftbar{FairOrange}
\small

\begin{cblock}{FairOrange}{Core research question}
\textbf{How do the amount and quality of decision context change the utility–fairness tradeoff under shift, and does the same logic transfer across clinical and quantum testbeds?}
\end{cblock}

\vspace{0.25em}
\begin{columns}[T,onlytextwidth]
  \column{0.50\textwidth}
  \begin{cblock}{ContextTeal}{Hypothesis family (context quality)}
    \begin{itemize}\itemsep0.2em
      \item Adding context helps only when context quality is comparable across groups.
      \item Under group-skewed missingness, “more context” can reduce regret while worsening disparity(t).
    \end{itemize}
  \end{cblock}

  \column{0.48\textwidth}
  \begin{cblock}{SeqPurple}{Hypothesis family (shift / adversary)}
    \begin{itemize}\itemsep0.2em
      \item Under shift/adversary, policies need robustness \emph{and} fairness monitoring.
      \item Transfer tests reveal which fairness methods are domain-general vs. domain-specific.
    \end{itemize}
  \end{cblock}
\end{columns}

\topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOn}{\QuantOn}
\refs{PhD-style framing: hypotheses are falsifiable via disparity(t) curves under controlled missingness + threat regimes.}
\note{
\begin{itemize}\itemsep0.2em
  \item (~1:00) Say the question once, then emphasize “falsifiable outcomes.”
  \item Preview: next slide formalizes; next after that shows evaluation harness.
\end{itemize}
}
\end{frame}

% ----------------------------------------------------------
% Slide 9: Proposed project 2 (formalization + metrics)
% ----------------------------------------------------------
\begin{frame}{\ticon{SeqPurple}\; Proposed project: formal setup and metrics}
\leftbar{SeqPurple}
\small

\begin{cblock}{ContextTeal}{Contextual bandit with group-skewed missingness}
At time $t$: observe group $g_t\in\mathcal{G}$ and observed context $\tilde{x}_t$, choose action $a_t$, observe reward $r_t(a_t)$.
\[
\tilde{x}_t = M_t(g_t)\odot x_t \qquad \text{(group-dependent missingness / noise)}
\]
\end{cblock}

\vspace{0.25em}
\begin{columns}[T,onlytextwidth]
  \column{0.52\textwidth}
  \begin{cblock}{SeqPurple}{Utility}
    \begin{itemize}\itemsep0.2em
      \item Reward / regret (standard bandit metrics)
      \item Cost-aware reward (latency/tests/qubits)
    \end{itemize}
  \end{cblock}

  \column{0.46\textwidth}
  \begin{cblock}{FairOrange}{Fairness (tracked over time)}
    \begin{itemize}\itemsep0.2em
      \item Clinical: $\Delta^{\text{TPR}}(t)$, FNR gap, time-to-escalation gap
      \item Quantum: success/latency gaps across flow/user groups
    \end{itemize}
  \end{cblock}
\end{columns}

\topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOn}{\QuantOn}
\refs{Key design choice: fairness is logged during policy learning, not only post-hoc.}
\note{
\begin{itemize}\itemsep0.2em
  \item (~1:00) Keep the math minimal. Emphasize “mask depends on group.”
  \item One sentence: same metrics interface across testbeds enables transfer comparisons.
\end{itemize}
}
\end{frame}

% ----------------------------------------------------------
% Slide 10: Proposed project 3 (shared evaluation pipeline TikZ)
% ----------------------------------------------------------
\begin{frame}{\ticon{ContextTeal}\; Proposed project: shared evaluation pipeline (TikZ)}
\leftbar{ContextTeal}
\small
\textcolor{ContextTeal!85!black}{\textbf{One harness across domains:}} configure missingness/shift $\rightarrow$ run policies $\rightarrow$ log $\rightarrow$ compute utility + disparity(t) $\rightarrow$ mitigation/ablations.

\vspace{0.25em}
\centering
\begin{tikzpicture}[
  box/.style={rounded corners=7pt, align=center, minimum width=3.15cm, minimum height=0.90cm},
  arr/.style={-Stealth, line width=0.9pt, draw=DeepNavy},
  small/.style={font=\scriptsize, color=SoftGray}
]
  \node[box, draw=ContextTeal!85!black, fill=ContextTeal!10, text=DeepNavy] (cfg)
    {Config\\\small{missingness + shift}};
  \node[box, right=0.55cm of cfg, draw=DeepNavy, fill=PaleGray, text=DeepNavy] (env)
    {Testbed\\\small{\Clin{clinical} / \Quant{quantum}}};
  \node[box, right=0.55cm of env, draw=SeqPurple!85!black, fill=SeqPurple!10, text=DeepNavy] (pol)
    {Policy\\\small{MAB/CMAB/iCMAB}};
  \node[box, right=0.55cm of pol, draw=SoftGray!60, fill=PaleGray, text=DeepNavy] (log)
    {Logger\\\small{full trajectories}};
  \node[box, below=0.55cm of pol, draw=FairOrange!85!black, fill=FairOrange!10, text=DeepNavy] (met)
    {Metrics\\\small{utility + disparity(t)}};
  \node[box, right=0.55cm of met, draw=RiskRed!85!black, fill=RiskRed!10, text=DeepNavy] (mit)
    {Mitigation\\\small{constraints/penalty}};

  \draw[arr] (cfg) -- (env);
  \draw[arr] (env) -- (pol);
  \draw[arr] (pol) -- (log);
  \draw[arr] (log) -- (met);
  \draw[arr] (met) -- (mit);

  \node[small, below=0.10cm of met] {Report disparity curves, windowed gaps, worst-group, and tradeoffs};
\end{tikzpicture}

\vspace{0.25em}
\begin{cblock}{FairOrange}{Deliverable logic (what you can grade)}
Same evaluation logic across both domains: configure $\rightarrow$ run $\rightarrow$ measure $\rightarrow$ compare $\rightarrow$ ablate.
\end{cblock}

\topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOn}{\QuantOn}
\refs{Non-text contrast reminder: meaningful shapes/lines should be \(\ge\) 3:1 vs background (WCAG 1.4.11).}
\note{
\begin{itemize}\itemsep0.2em
  \item (~1:05) Walk the pipeline once; don’t over-explain.
  \item Tie directly to grading: “shared framework + figures + related work + clear approach.”
\end{itemize}
}
\end{frame}

% ----------------------------------------------------------
% Slide 11: Approach (required: next two semesters)
% ----------------------------------------------------------
\begin{frame}{\ticon{SeqPurple}\; Approach for the next two semesters (DSCI601 → DSCI602)}
\leftbar{SeqPurple}
\small

\begin{columns}[T,onlytextwidth]
  \column{0.49\textwidth}
  \begin{cblock}{ClinicalGreen}{DSCI 601: build + baseline}
    \begin{itemize}\itemsep0.2em
      \item Implement clinical simulation environment.
      \item Baselines: MAB + CMAB policies.
      \item Define reward + time-evolving fairness metrics.
      \item First mitigation mechanism + ablations (missingness severity).
    \end{itemize}
  \end{cblock}

  \column{0.49\textwidth}
  \begin{cblock}{TealAccent}{DSCI 602: robustness + transfer}
    \begin{itemize}\itemsep0.2em
      \item Integrate Paper2 quantum routing testbed regimes.
      \item Add informative/restricted-context policies.
      \item Stress-test under shift/adversarial conditions.
      \item Package experiments + reproducibility (configs, seeds, plots).
    \end{itemize}
  \end{cblock}
\end{columns}

\vspace{0.15em}
\begin{cblock}{RiskRed}{Risk control (scope)}
Simulation-first for clinical domain; quantum testbed already production-ready—minimize data access risk while meeting two-testbed requirement.
\end{cblock}

\topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOn}{\QuantOn}
\refs{Rubric alignment: clear approach and deliverables across two semesters.}
\note{
\begin{itemize}\itemsep0.2em
  \item (~1:00) This slide should feel like a plan, not a wish list.
  \item Close with: “By end of 601 we have baselines + metrics; 602 adds robustness + transfer.”
\end{itemize}
}
\end{frame}

% ----------------------------------------------------------
% Slide 12: Closing (keep short)
% ----------------------------------------------------------
\begin{frame}{\ticon{FairOrange}\; Takeaway + Questions}
\leftbar{FairOrange}
\small

\begin{cblock}{FairOrange}{Takeaway}
In sequential decision systems, \Ctx{context quality} is a \emph{resource}. If it is uneven by group, then optimized policies can produce persistent \Fair{outcome gaps} unless fairness is monitored and mitigated during learning.
\end{cblock}

\vspace{0.25em}
\begin{columns}[T,onlytextwidth]
  \column{0.62\textwidth}
  \begin{cblock}{SeqPurple}{What you will get (deliverables)}
    \begin{itemize}\itemsep0.2em
      \item Two testbeds under one harness (clinical + quantum).
      \item Comparable plots: utility and disparity(t) under missingness + shift.
      \item Reproducible code structure (configs + logging + figures).
    \end{itemize}
  \end{cblock}

  \column{0.36\textwidth}
  \begin{cblock}{DeepNavy}{Questions?}
    \textcolor{white}{pizg8794@g.rit.edu}\\[0.2em]
    \textcolor{PaleGray}{Piter Z. Garcia Bautista}
  \end{cblock}
\end{columns}

\topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOn}{\QuantOn}
\refs{End here in the live talk; next slide is references + accessibility checklist (backup).}
\note{
\begin{itemize}\itemsep0.2em
  \item (~0:25–0:35) Stop here for Q\&A.
  \item If asked: the backup slide lists citations and an accessibility pre-submit check.
\end{itemize}
}
\end{frame}

% ----------------------------------------------------------
% Slide 13: Key references + accessibility checklist (end)
% ----------------------------------------------------------
\begin{frame}{\ticon{ContextTeal}\; Key references + accessibility checklist (pre-submit)}
\leftbar{ContextTeal}
\scriptsize

\begin{columns}[T,onlytextwidth]
  \column{0.52\textwidth}
  \begin{cblock}{SeqPurple}{Key references (examples)}
  \begin{itemize}\itemsep0.15em
    \item Auer et al. (UCB); Thompson (TS)
    \item Li et al. (LinUCB / contextual bandits)
    \item Hardt et al. (Equality of Opportunity)
    \item Joseph et al. (Fairness in bandits / learning under fairness constraints)
    \item Bouneffouf et al. (restricted/selected context)
    \item Besbes et al. (non-stationary bandits)
    \item Huang et al. (EXPNeuralUCB framing); Chaudhary et al. (quantum routing bandit testbed)
  \end{itemize}
  \end{cblock}

  \column{0.46\textwidth}
  \begin{cblock}{FairOrange}{Accessibility checklist (quick)}
  \begin{itemize}\itemsep0.15em
    \item \textbf{Color not only cue:} every color meaning also has text/shape labels.
    \item \textbf{Contrast targets:} normal text \(\ge\) 4.5:1; large text \(\ge\) 3:1.
    \item \textbf{Non-text contrast:} meaningful lines/edges \(\ge\) 3:1 vs background.
    \item \textbf{Consistent cues:} left bar + title icon + chip strip on every slide.
  \end{itemize}
  \end{cblock}

  \begin{cblock}{RiskRed}{Simple contrast-check step (before final PDF)}
  \begin{itemize}\itemsep0.15em
    \item Compile PDF, sample 2–3 slides with colored elements.
    \item Use a contrast checker to verify text and key diagram elements meet the targets above.
  \end{itemize}
  \end{cblock}
\end{columns}

\topicstrip{\FairOn}{\CtxOn}{\SeqOn}{\ClinOn}{\QuantOn}
\refs{WCAG anchors: 1.4.1 (color not only), 1.4.3 (contrast), 1.4.11 (non-text contrast).}
\note{
\begin{itemize}\itemsep0.2em
  \item Not intended for live narration (backup).
  \item Use it as your pre-submit checklist and as “references present” evidence for grading.
\end{itemize}
}
\end{frame}

\end{document}
```

### Notes on the requirement alignment and timing

This deck is intentionally **10–15 slides** (13 total) and structured to match the required categories listed in the course instructions (background slides, related-work overview table, 2–5 detailed related-work slides, 3–5 proposed project slides, and an approach slide for the next two semesters). fileciteturn41file1L1-L1  
You can present Slides 1–12 in ~10 minutes and keep Slide 13 as a backup/checklist.

### Practical contrast-check recommendation before final submission

WCAG guidance recommends minimum contrast for readable text (4.5:1 normal text; 3:1 large text). citeturn0search3  
It also recommends meaningful visual graphics have ~3:1 contrast against adjacent colors (non-text contrast). citeturn1search3  
A simple workflow is: compile the PDF, then use any contrast-check tool you trust to sample-check a few slides—especially the chip strip, block titles, and diagram edges.