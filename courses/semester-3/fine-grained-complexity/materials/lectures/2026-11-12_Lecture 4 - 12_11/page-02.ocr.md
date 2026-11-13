# 2026-11-12_Lecture 4 - 12_11 - page-02

> Gemini gemini-3.6-flash transcription.

use weighted MM – $A[i,j] = \begin{cases} \dots & \dots \\ \text{inf} & \text{else} \end{cases}$

$C[i,j] = \min_{k=1}^n A[i,k] + B[k,j] \quad c = A \oplus B$

we want $A \oplus A [i,j] + A[i,j] < 0$

$MM(\min,+)$: given two $n \times n$ matrices $A, B$, compute $C = A \oplus B$ s.t.
$$C[i,j] = \min_{k=1}^n A[i,k] + B[k,j]$$

Alg ($\text{Neg-}\Delta \to (\min,+)\text{-MM}$):
- def $A$ to be the weighted adj matrix
$$A[i,j] = \begin{cases} w(i,j) & \text{if } (i,j) \in E \\ +\infty & \text{else} \end{cases}$$
- compute $A^2 = A \oplus A$
- return $\min_{i,j} w(i,j) + A^2[i,j]$

---

APSP: Given $G = (V, E), w$
$\swarrow (\min,+)$
return $dist[u,v] = \min \text{ weight } u \text{ to } v \text{ path in } G$ for all $u, v \in V$

Thm: If $(\min,+)\text{-MM}$ is in time $T(n)$ then APSP is in time $O(T(n) \cdot \log n)$

alg: 
- def $A$ adj weight – $A[i,j] = \begin{cases} w(i,j) & \\ 0 & i=j \\ +\infty & \text{else} \end{cases}$
- compute $A^n$ – via repeated squaring
- return $dist(i,j) = A^n[i,j]$

claim: $A^k[i,j] = \text{shortest path from } i \text{ to } j \text{ with } \le k \text{ edges}$

time: $\log n \cdot T(\min,+)(n)$

What about $(\min,+)\text{MM} \to \text{APSP}$

[diagram: Matrix boxes $A \cdot B = C$ pointing to nodes $i$, $k$, $j$ connected along a path, with a label $w(i,k) = A[i,k] + 2U$]
