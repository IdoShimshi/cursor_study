# 2026-11-13_Lecture 4 -08_11 - page-51

> Gemini gemini-3-flash-preview transcription.

# Estimating the Fundamental matrix $F$

### The 8-point algorithm:
* Extract at least 8 point correspondences
* Normalize the coordinates
* Form $A$ and solve using SVD:
$$\min_{\|v\|=1} \|Av\|^2$$
* Form the matrix $F$ (ensure that $\det(F) = 0$)
* Transform back to the original coordinates
