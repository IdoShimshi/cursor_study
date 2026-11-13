# 2026-11-13_Lecture 4 -08_11 - page-19

> Gemini gemini-2.5-flash transcription.

[diagram: A 3D coordinate system with axes $e_x, e_y, e_z$ and a point $X$. Another 3D coordinate system with axes $e'_x, e'_y, e'_z$ representing a camera, with a point $x$ on its image plane. A dashed line connects $X$ to $x$ through the camera's origin. Text labels indicate "External parameters $[R \ t]$", "Inner parameters, from metric (length) units to pixels", "Reference (global) Coordinate system", and "Camera (local) Coordinate system."]

* Calibrated case, metric space

$$
\lambda \mathbf{x} = [R \ t] \begin{pmatrix} X_1 \\ X_2 \\ X_3 \\ 1 \end{pmatrix}
$$

$$
\underbrace{\lambda \mathbf{x}}_{C} = \underbrace{[R \ t]}_{X} \begin{pmatrix} X_1 \\ X_2 \\ X_3 \\ 1 \end{pmatrix}
$$

* $C = [R \ t]_{3 \times 4}$ calibrated camera matrix

* $\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ 1 \end{bmatrix}$ calibrated coordinates

lectures Page 19
