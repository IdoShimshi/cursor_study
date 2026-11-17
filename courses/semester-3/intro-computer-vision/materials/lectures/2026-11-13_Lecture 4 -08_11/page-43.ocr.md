# 2026-11-13_Lecture 4 -08_11 - page-43

> Gemini gemini-3.5-flash-lite transcription.

The Fundamental matrix, $q^T F p = 0$

* Similar to the mapping obtained by the Essential matrix, the Fundamental matrix $F$ maps from a point in one image to a line in the second image
* $F \in \mathbb{R}^{3 \times 3}$ has $7$ dof
  * $F$ is defined up to scale
  * $\text{Rank } (F) = 2$ (null spaces contain epipoles)
* Recovering $F$:
  * Linear solution requires $8$ pairs of corresponding points
  * Non-linear solution requires $7$ pairs: rank $2$ is enforced by requiring $\text{Det}(F) = 0$
