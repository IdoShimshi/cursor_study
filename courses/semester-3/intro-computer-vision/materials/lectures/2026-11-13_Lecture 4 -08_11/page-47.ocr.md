# 2026-11-13_Lecture 4 -08_11 - page-47

> Gemini gemini-2.5-flash transcription.

Estimating the Fundamental (Essential) matrix by Direct Linear Transform (DLT) algorithm
Linear solution of $\{q^T F p = 0\}$
$$
\begin{pmatrix}
q_1^1 p_1^1 & q_1^1 p_2^1 & \dots & q_3^1 p_3^1 \\
q_1^2 p_1^2 & q_1^2 p_2^2 & \dots & q_3^2 p_3^2 \\
\vdots & & & \vdots \\
q_1^8 p_1^8 & q_1^8 p_2^8 & \dots & q_3^8 p_3^8
\end{pmatrix}
\begin{pmatrix}
F_{11} \\
\vdots \\
F_{33}
\end{pmatrix}
= 0
$$
* Find null space with SVD (Singular Value Decomposition)
* Data normalization is an essential step in the DLT algorithm, it must not be considered optional
* $n > 8$ point correspondences we use homogeneous least squares solution

lectures Page 47
