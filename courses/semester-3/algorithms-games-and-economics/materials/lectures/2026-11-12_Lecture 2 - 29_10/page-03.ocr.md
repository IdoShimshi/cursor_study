# 2026-11-12_Lecture 2 - 29_10 - page-03

> Gemini gemini-3-flash-preview transcription.

but if it votes $\succ_i$, then $a$ is selected, but $a \succ_i b$

<u>Lemma 4</u>: consider an instance $p, (P = (\succ_1, \dots, \succ_n))$ where $f(P) = a$ for every profile $P'$ where $a \succ_i x \Rightarrow a \succ_i' x$ $\forall i, x$ then $f(P') = a$

<u>Proof</u>: same structure as 3

<u>Lemma 5</u>: suppose an instance $P$ where $f(P) = a$
if one voter values an alternative $b$ without changing anything else, the new winner belongs to $\{a, b\}$

<u>Proof</u>: suppose $c$ won, then it is not truthful, if it prefers $c$ to $a$, it should raise $b$, which isn't truthful

[diagram: a box containing the text "unanimous: in every $P$, if $a$ is at the top of every voter, it is selected"]

<u>Lemma 6</u>: $f$ is unanimous, moreover, it never selects an alternative $b$ if there is an alternative $c$ that is preferred by everyone else.

<u>Proof</u>: Unanimous -
start with an instance $P$ where $f(P) = a$
one by one, increase $a$, put it at the top of the ranking of each voter
by lemma 4, $a$ is still the winner.
using lemma 4 again, we can move to any instance where $a$ is at the top of all rankings, and claim that $a$ is still the winner.

contradicting lemma 4 proves the second part

[diagram: a PDF icon with the text "voting_notes GS"]
