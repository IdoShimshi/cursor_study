# 2026-10-29_Lecture 2 - 29_10 - page-02

> Gemini gemini-3.5-flash-lite transcription.

Thm: ("finding $\to$ decision"):

if 3-sum is in time $T(n)$ then 3-sum finding is in $O(T(n))$ time

- split randomly, call 3-sum, keep doing untill 3 are in your split, $(\frac{1}{2})^3 = \frac{1}{8}$ its in the smaller split

$O(1) \cdot T_{\text{dec}}(n) + T_{\text{find}}(n)$ this works but rand

- Partition to 4 sets, check every set of 3 of them
[diagram: A rectangle divided into 4 vertical sections labeled $S_1, S_2, S_3, S_4$]

let $S_i' = S / S_i$
note: $|S_i'| = \frac{3}{4}n$
- call 3-sum($S_i'$) for each $i$
- recurse on first find else, return false.
- if $|S|=O(1)$, solve in $|S|^3$ time

correctness: $\checkmark$
time: $T_{\text{find}}(n) \le 4\, T_{\text{dec}}(n) + T_{\text{find}}\left(\frac{3}{4}n\right) + O(n) = O\left(n + \sum_{i=0}^{\log n} \left(T_{\text{dec}}\left(\frac{3}{4}\right)^i \cdot n\right)\right) =$
$\le O\left(n + \left(\sum_{i=0}^{\log n} \left(\frac{3}{4}\right)^i\right) \cdot T_{\text{dec}}(n)\right) = O(T_{\text{dec}}(n))$

colorful-3sum: Given 3 sets of $n$ numbers, $A, B, C \subseteq [-U, U]$
are there $a \in A, b \in B, c \in C$ s.t. $a+b+c = 0$
[diagram: Three rectangles labeled $A$ (with element $a$), $B$ (with element $b$), and $C$ (with element $c$) next to $a+b+c=0$]

Thm 2: if col-3sum is in $T(n)$ then there is an alg that solve 3-sum in time $O(T(n))$ and succeeds w.p. $\frac{9}{10}$

Pf: - repeat 10 times independently w.p. $\frac{2}{3}$
- $\forall x \in S$ let $\text{col}(x) = \begin{cases} 1 \\ 2 \\ 3 \end{cases}$
- let $A = \{x \in S \mid \text{col}(x) = 1\}$
$B = \{\dots 2\}$
$C = \{\dots 3\}$
- if $\text{col-3sum}(A, B, C) = \text{"yes"}$ return "yes"

- return "no"
