# 2026-11-13_Lecture 4 -08_11 - page-24

> Gemini gemini-2.5-flash transcription.

Camera matrix

$C = K[R|t]$

* The camera matrix is of size $3 \times 4$
* How many degrees of freedom (dof)?
* $R \in \mathbb{R}^{3 \times 3}$ rotation matrix, $\textbf{3}$ dof
* $t \in \mathbb{R}^3$ translation vector, $\textbf{3}$ dof
* $K = \begin{pmatrix} \alpha_x & \gamma & x_0 \\ 0 & \alpha_y & y_0 \\ 0 & 0 & 1 \end{pmatrix}$ calibration matrix, $\textbf{5}$ dof

$\Rightarrow 11$ dof (out of 12 entries)
Any multiplication by a non-zero scalar results in an equivalent camera matrix

lectures Page 24
