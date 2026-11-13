# 2026-11-12_Lecture 4 - 12_11 - page-04

> Gemini gemini-3-flash-preview transcription.

naive: find one $\Delta$ at a time $- n^{3-\epsilon} \cdot n^3$, can be $n^{3-\epsilon} \cdot n^2$

idea: run det alg on smaller graph on $s$ nodes $s^{3-\epsilon}$

what smaller $s$? idea: random subgraphs of size $s$

[diagram: a triangle with circles around its vertices]

$(\frac{n}{s})^3$ attempts guarantees that every $\Delta$ is formed
$(\frac{n}{s})^3 \cdot s^{3-\epsilon} = \frac{n^3}{s^\epsilon}$
the problem, when looking for a specific $\Delta$, you might find another

we want to get rid of the collision

Reduction:
split $I, J, K$ arbitrarily into $s$-sized subsets
$I'_1, \dots, I'_{n/s}$
$J'_1, \dots$
$K'_1, \dots$

- for all $(\frac{n}{s})^3$ triples of subsets $I', J', K'$ do (in arbitrary order):
$\circledast$ - if Find-Neg-$\Delta$ $(I', J', K') = (i, j, k)$
- set $D[i, j] = 1$, remove edge $(i, j)$ from $E$, set $w(i, j) = +\infty$
- go to $\circledast$
- o.w. continue to next triple

correctness: if $(i, j)$ is in $\Delta$, we will find it in some triple

time: naive - $(\frac{n}{s})^3 \cdot s^{3-\epsilon} \cdot s^2$
better
$[(\frac{n}{s})^3 + K] \cdot s^{3-\epsilon}$
$\uparrow$
# pairs $(i, j)$
s.t. $D[i, j]$ in the end $\le n^2$

so $[(\frac{n}{s})^3 + n^2] \cdot s^{3-\epsilon} = \frac{n^3}{s^\epsilon} + n^2 \cdot s^{3-\epsilon} = n^{3-\frac{\epsilon}{3}}$
$\uparrow$
$s = n^{\frac{1}{3}}$

lectures Page 4
