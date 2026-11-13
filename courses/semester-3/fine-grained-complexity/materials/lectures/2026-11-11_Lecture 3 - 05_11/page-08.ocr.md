# 2026-11-11_Lecture 3 - 05_11 - page-08

> Gemini gemini-3.5-flash-lite transcription.

convolution: multiply with shift and sum
[diagram: two arrays of boxes aligned vertically, with zig-zag connection lines between them and a result array below showing red and blue dots]

input: arrays $A, B$ of len $U$
output: $C = A \circledast B$ s.t.
$\forall j \in [2U]: C[j] = \sum_{i=1}^{U} A[i] \cdot B[j-i]$

$\xrightarrow{\text{equivalent}}$ polynomial multiplication
input: polynomials $p(x) = \sum_{i=0}^{U-1} a_i x^i$
$q(x) = \sum_{i=0}^{U-1} b_i x^i$

output: $p \cdot q(x) = \sum_j (\sum_i a_i b_{i-j}) x^j$

naive: $O(U^2)$
FFT: $O(U \log U)$

$O(n + U \log U)$ for Positive-3sum':
- let $A[i] = B[i] = \begin{cases} 1 & i \in S \\ 0 & i \notin S \end{cases}$
- compute $C = A \circledast B$
- "yes" iff $\exists j$ s.t. $j \in S$ and $C[j] \ge 1$

correctness: $C[j] \ge 1 \iff \exists i: A[i] \ge 1 \quad B[j-i] \ge 1 \iff S: i \in S \text{ and } j-i \in S$

what about larger $U$?

$U = O(n^3 \log^3 n)$

Thm: if $3\text{sum}$ with $U = n^3 \log^3 n$ is in time $T(n)$, then there is an alg that solves $3\text{sum}$ with $U = n^{100}$ in time $O(T(n))$ and succeeds w.p. $\ge 9/10$

$h(x) = (x \bmod p)$

Alg: - pick a random prime $p$ in $[2, n^3 \log^3 n]$ uniformly
- $S' = \{h(x) \mid x \in S\}$
- if $3\text{sum}(S') = \text{"no"}$ return $\text{"no"}$
- return $\text{"yes"}$ [diagram: red arrow pointing from "if $3\text{sum}(S') = \text{"no"}$ return 'no'" to note "make 4 calls to $3\text{sum}(S', \text{target})$ with target $= 0, p, 2p, 3p$ return 'yes' if one says 'yes'"]

correctness: $\text{"no"}$ $\Rightarrow$ $\text{"yes"}$ w.p. $1$

[footer: lectures Page 8]
