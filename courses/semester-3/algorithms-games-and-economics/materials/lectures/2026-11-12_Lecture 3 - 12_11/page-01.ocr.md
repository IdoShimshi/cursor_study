# 2026-11-12_Lecture 3 - 12_11 - page-01

> Gemini gemini-2.5-flash transcription.

Lecture 3 - 12/11
Thursday, 12 November 2026 9:28

Continuing with lecture Proof:
Theorem: Let $f$ be a truthful voting rule. Suppose that there are 3 candidates that are sometimes selected, then $f$ is a dictatorship.

Proof: Start with a ranking where everyone ranks $a$ first and $b$ last.
Winner is $a$.
Lets raise $b$ to the top of each preference, one by one. Let $r$ be the voter that changes the outcome from $a$ to $b$.

[diagram: a column of preferences with $a$ at the top, then $b$ at the bottom, then $a$ at the top, then $b$ at the bottom, then $a$ at the top, then $b$ at the bottom, with arrows indicating $b$ moving up]

| $j < r$ | $r$ | $j > r$ | Winner |
| :------ | :-- | :------ | :----- |
| $P^-$   | $b > a > ...$ | $a > b > ...$ | $a > ... > b$ | $a$ | $\leftarrow$ before $r$ change |
| $P^+$   | $b > a > ...$ | $b > a > ...$ | $a > ... > b$ | $b$ | $\leftarrow$ after $r$ change |

lower $a$ in the ranking:

| $j < r$ | $r$ | $j > r$ | Winner |
| :------ | :-- | :------ | :----- |
| $H^-$   | $b > ... > a$ | $a > b > ...$ | $... > a > b$ | $a$ | $\leftarrow$ compared to $P^+$ only $b$ increased above $a$, so $f(a,b)$ |
| $H^+$   | $b > ... > a$ | $b > ... > a$ | $... > a > b$ | $b$ | $\leftarrow$ but compared to $P^-$, $b$ and $a$ relationship didn't change |
|         |             |             |             |     | $\leftarrow$ because compared to $P^+$, $b$ and $a$ hasn't changed |

use a third alternative $c \neq a, b$

| $j < r$ | $r$ | $j > r$ | Winner |
| :------ | :-- | :------ | :----- |
| $Q$     | $... > c > b > a$ | $... > c > a > b$ | $... > c > a > b$ | $a$ | $\leftarrow$ compared to $H^-$, relation between $a$ and everyone else hasn't changed |
| $Q'$    | $... > c > b > a$ | $... > c > b > a$ | $... > c > b > a$ | $a$ | $\leftarrow$ compared to $Q$, only $b$ increased above $a$, so $f(a,b)$ but $c > b$ for every case, so $b$ can't win, so $a$ wins |

in $Q'$ $r$ ranks $a$ first and everyone else is ranking $a$ last, and $a$ is selected.
this means that we can move from $Q$-like instance, to any other instance where $r$ ranks $a$ first and make sure that in every step $a$ is the winner.

lectures Page 1
