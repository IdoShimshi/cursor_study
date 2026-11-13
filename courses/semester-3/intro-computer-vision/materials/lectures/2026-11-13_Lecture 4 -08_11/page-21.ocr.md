# 2026-11-13_Lecture 4 -08_11 - page-21

> Gemini gemini-2.5-flash transcription.

Camera matrix $C_{3 \times 4} = K[R|t]$
- Camera matrix $C_{3 \times 4}$ captures camera translation $t$, orientation $R$, and (linear) internal calibration parameters $K$

$$
\mathbf{x} \propto K[R|t]\mathbf{X}
$$

$$
\begin{pmatrix} x \\ y \\ 1 \end{pmatrix} \propto \underbrace{\begin{pmatrix} \alpha_x & \gamma & x_0 \\ 0 & \alpha_y & y_0 \\ 0 & 0 & 1 \end{pmatrix}}_{\text{Internal calibration}} \underbrace{\begin{pmatrix} r_{11} & r_{12} & r_{13} & t_x \\ r_{21} & r_{22} & r_{23} & t_y \\ r_{31} & r_{32} & r_{33} & t_z \end{pmatrix}}_{\text{external calibration}} \begin{pmatrix} X \\ Y \\ Z \\ 1 \end{pmatrix}
$$

The linear mapping $K_{3 \times 3}$ is an invertible upper triangular matrix

- As before, '$\propto$' means "up to (non-zero) scale factor"
Scale is different for every point

lectures Page 21
