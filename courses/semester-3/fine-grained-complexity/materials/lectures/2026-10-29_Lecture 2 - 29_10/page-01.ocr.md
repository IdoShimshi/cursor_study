# 2026-10-29_Lecture 2 - 29_10 - page-01

> Gemini gemini-3.5-flash-lite transcription.

Lecture 2 - 29/10

News
Last time we did reductions to SETH, APSP, 3Sum and that last 2 are broken.
2 days ago SETH is broken

Our reduction was $\text{SETH} \to \text{OV} \to \text{things}$

Doesn't apply OV yet, so for now they stand.

3Sum

Given a set $S$ of $n$ integers in $[-U, +U]$, are there $a,b,c \in S$ s.t. $a+b+c = 0$?

Algs:
- naive: $O(n^3)$, try every triplet

- $O(n^2 \log n)$ - sort, go over pairs, binary search last one

- $O(n^2)$ rand - hash sum of all pairs

- $O(n^2)$ sort, have 2 indexs, one at start, one at end, move if it's small or big

- $O(n^{2.999})$

K-Sum: $a_1 + a_2 + \dots + a_k = 0$

hash sum of $k/2$, select $k/2$, look for its

$$O(n^{\lceil k/2 \rceil})$$

$$2 \to n$$
$$3 \to n^2$$
$$4 \to n^2$$
$$5 \to n^3$$
$$6 \to n^3$$

this is not broken yet

Variants

3-sum finding: given $S \dots$ return $a,b,c \in S$ s.t. $a+b+c=0$ if it exists
