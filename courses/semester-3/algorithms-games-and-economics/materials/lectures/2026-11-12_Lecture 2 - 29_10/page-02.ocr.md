# 2026-11-12_Lecture 2 - 29_10 - page-02

> Gemini gemini-2.5-flash transcription.

We'll show how this is not truthful, by showing a case where a voter should report untruthful ranking.
Fischer is wrong - ranked-choice voting is not truthful.

3 candidates: $a, b, c$
5 voters:
| \# of voters | Preferences |
|---|---|
| 2 | $a > c > b$ |
| 2 | $b > a > c$ |
| 1 | $c > b > a$ |

round 1:
| a | b | c |
|---|---|---|
| 2 | 2 | 1 | $\rightarrow$ c eliminated

round 2:
| a | b |
|---|---|
| 2 | 3 | $\rightarrow$ b won

.
| \# of voters | Preferences |
|---|---|
| 1 | $a > c > b$ |
| 2 | $b > a > c$ |
| 1 | $c > b > a$ |
| 1 | $c > a > b$ |

after misreporting

round 1:
| a | b | c |
|---|---|---|
| 1 | 2 | 2 | $\rightarrow$ a eliminated

round 2:
| b | c |
|---|---|
| 2 | 3 | $\rightarrow$ c wins

So voter with original preference of $a > c > b$, changed the outcome from b to c
by miss reporting its ranking.

Theorem: Let $f$ be a truthful voting rule. Suppose that there are
3 candidates that are sometimes selected,
then $f$ is a dictatorship.

Gibbard-Satterthwaite.

Fix $f$ to be as in the theorem.

Lemma 3: Suppose only voter $i$ changes its vote from $s_i$ to $s_i'$.
Suppose that the outcome changes from $a$ to $b$
then $a >_i A$ and $b >_i a$

Proof: Suppose that $a >_i b$ but $a >_i b$

Consider a voter with $s_i'$. if it reports truthfully, then $b$ is
is selected, but $a >_i b$ then $a$ is selected, but $a >_i b$

Lemma 4: Consider an instance $P = (s_1, ..., s_n)$ where $f(P) = a$ for every profile $P'$
