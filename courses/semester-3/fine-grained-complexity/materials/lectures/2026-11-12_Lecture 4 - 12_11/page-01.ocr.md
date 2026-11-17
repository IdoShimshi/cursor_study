# 2026-11-12_Lecture 4 - 12_11 - page-01

> Gemini gemini-3.6-flash transcription.

Lecture 4 - 12/11
Thursday, 12 November 2026 13:19

$\underline{\text{Def:}}$ A triangle in a graph $G=(V,E)$ is a triple $\{a,b,c\} \subseteq V$ s.t. $\{a,b\}, \{b,c\}, \{a,c\} \in E$

$\Delta$-detection: given $G$, does it have a triangle

naive: $O(n^3)$

matrix multiplication
given two $n \times n$ matrices $A,B$
compute $C = A \cdot B$

$$C[i,j] = \sum_{k=1}^{n} A[i,k] \cdot B[k,j]$$

[diagram: matrix multiplication visual representation showing row i of matrix A times column j of matrix B resulting in entry (i,j) of matrix C]

$$A[i,j] = \begin{cases} 1 & \text{if } \{i,j\} \in E \\ 0 & \text{else} \end{cases}$$

$A^2[i,j] = \text{number of 2-paths}$

find $i,j$ s.t. (1) $A^2[i,j] > 0$, (2) $(i,j) \in E \equiv A[i,j] = 1$

$\text{def: } \omega \text{ is the smallest const s.t. } MM \text{ can be solved in } O(n^\omega) \text{ time}$

$\underline{\text{Thm:}} \quad \omega < 2.25$

$\Delta\text{-det. (unweighted)} \quad O(n^\omega) \quad \text{these can be tri colored}$

Graph Problem $\leftarrow \begin{cases} \text{negative-}\Delta \iff APSP \\ \text{min-}\Delta \\ \text{zero-}\Delta \underset{\text{S}}{\overset{\text{S}}{\curveleft}} \text{conv3sum} \iff 3\text{sum} \end{cases}$

[diagram: triangle graph with 3 vertices connected by edges]

$\underline{\text{negative-}\Delta:}$ given $G=(V,E,w)$
$w : E \to [-U, U]$, does it contain $\{a,b,c\} \subseteq V$ s.t. $w(a,b) + w(b,c) + w(a,c) < 0$

use weighted MM - $A[i,j] = \begin{cases} w(i,j) & \text{if } \{i,j\} \in E \\ \text{inf} & \text{else} \end{cases}$
