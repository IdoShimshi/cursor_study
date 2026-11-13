# 2026-11-13_Lecture 4 -08_11 - page-50

> Gemini gemini-3-flash-preview transcription.

# Estimating the Fundamental matrix $F$

Issue:
* Resulting $F$ may not have $\det(F) = 0$

Solution:
* Pick the closest matrix $F$ with $\det(F) = 0$
* This can be done simply using SVD
    * $[U, S, V] = \text{svd}(F)$
    * $S(3,3) = 0$
    * $F = U * S * V^T$

lectures Page 50
