# 2026-11-12_Lecture 2 - 29_10 - page-01

> Gemini gemini-3-flash-preview transcription.

Lecture 2 - 29/10
Thursday, 29 October 2026 10:14

<u>Voting rules</u>

Two candidates: $a, b$

$n$ voters: $>_i$ (preference, if it prefer $a$ or $b$)

we want voting rules which are nonstrategic / "truthful"

examples:
- truthful voting rule: majority, most of the time, vote doesn't change, if there's a tie the vote will change to what $i$ prefer

- choose $a$ iff $\sum w_i v_i \geq 100$ (not anonymous)


non truthful rule: minority


Theorem: a voting rule for <u>two candidates</u> is truthful iff it is monotone.

A voting rule $f$ is monotone if every voter $i$, and preferences of other $v_{-i}$
$f(1, v_{-i}) \geq f(0, v_{-i})$ $f$ is outcome

$(f(0, v_{-i}), f(1, v_{-i}))$
$\begin{matrix} 0 & 0 \\ 1 & 1 \end{matrix} \Big\}$ if the majority was selected without me - non pivotal

$\times \quad 1 \quad 0$ - not truthful, not monotonic

$\quad 0 \quad 1$ - my vote is the pivot.


Truthful $\Rightarrow$ monotonicity clear

monotonicity $\Rightarrow$ Truthful some, just looking at the different options


3 candidates?


<u>Ranked-choice voting</u>

each voter fully submits its ranking of the candidates
if there is a majority of first ranked alternative, then choose it.

otherwise "delete" the candidate that got the least amount of first place ranking, and repeat
