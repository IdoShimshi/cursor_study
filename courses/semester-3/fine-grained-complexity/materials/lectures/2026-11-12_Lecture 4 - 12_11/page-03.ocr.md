# 2026-11-12_Lecture 4 - 12_11 - page-03

> Gemini gemini-3.6-flash transcription.

$$dist(i,j) = \min_k A[i,k] + B[k,j]$$

$\text{Thm: If } \text{Neg-}\Delta \text{ is in time } O(n^{3-\varepsilon}) \text{ then } (\min, +)\text{-MM (and APSP) in time } O(n^{3-\frac{\varepsilon}{3}})$

APSP $\leftrightarrow$ $(\min, +) \xrightarrow{\log n \text{ binary search}} \text{All pairs Neg-}\Delta \longrightarrow \text{Neg-}\Delta$

[diagram: box with C], [diagram: box with 1,0], 0/1

---

<u>All Pairs Neg-$\Delta$:</u> given tripartite graph $G=(V, E, w)$
$V = I \cup J \cup K$
return $\forall i \in I, j \in J \quad D[i,j] = \begin{cases} 1 & \exists k \text{ s.t. } w(i,j,k) < 0 \\ 0 & \text{else} \end{cases}$

[diagram: tripartite graph with vertices A, B, C forming a triangle] $\longleftarrow$ [diagram: tripartite graph with dashed edge at bottom]

$$C[i,j] = \min_k A[i,k] + B[k,j]$$

$\forall i, j \ \exists k' \text{ s.t.}$
$$A[i,k] + B[k,j]$$
$$+ C[i,j] < 0$$

done by binary search over all pairs

---

how do we do All Pairs neg-$\Delta \longrightarrow \text{Neg-}\Delta$ (finding)

[diagram: tripartite graph with vertex sets] $\longrightarrow$ [diagram: isolated vertex sets]
$n^{3-\frac{\varepsilon}{3}} \longleftarrow (n^{3-\varepsilon})$
