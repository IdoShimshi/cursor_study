# 2026-11-12_Lecture 3 - 01_11 - page-40

> Gemini gemini-3.5-flash-lite transcription.

# Hierarchy of transformations

| Transformation | Matrix | Properties |
| :--- | :--- | :--- |
| Rigid | $\begin{pmatrix} \cos\theta & -\sin\theta & t_x \\ \sin\theta & \cos\theta & t_y \\ 0 & 0 & 1 \end{pmatrix}$ | Preserves angles, lengths, area, parallelism |
| Similarity | $\begin{pmatrix} a & -b & t_x \\ b & a & t_y \\ 0 & 0 & 1 \end{pmatrix}$ | Preserves angles, parallelism |
| Affine | $\begin{pmatrix} a & b & t_x \\ c & d & t_y \\ 0 & 0 & 1 \end{pmatrix}$ | Preserves parallelism |
| Homography | $\begin{pmatrix} h_{11} & h_{12} & h_{13} \\ h_{21} & h_{22} & h_{23} \\ h_{31} & h_{32} & h_{33} \end{pmatrix}$ | (up to scale) <br> Preserves cross ratio |

lectures Page 40
