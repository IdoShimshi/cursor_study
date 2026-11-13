# 2026-11-13_Lecture 4 -08_11 - page-11

> Gemini gemini-3.6-flash transcription.

Summary

# Projective transformation = Projectivity = Homography

- An invertible linear transformation of rays
$$\begin{pmatrix} x' \\ y' \\ 1 \end{pmatrix} = \boldsymbol{q} \propto H\boldsymbol{p} = \begin{pmatrix} h_{11} & h_{12} & h_{13} \\ h_{21} & h_{22} & h_{23} \\ h_{31} & h_{32} & h_{33} \end{pmatrix} \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}$$

- Non-linear transformation of points
$$x' = \frac{[H\boldsymbol{p}]_1}{[H\boldsymbol{p}]_3} = \frac{h_{11}x + h_{12}y + h_{13}}{h_{31}x + h_{32}y + h_{33}}, \quad y' = \frac{[H\boldsymbol{p}]_2}{[H\boldsymbol{p}]_3} = \frac{h_{21}x + h_{22}y + h_{23}}{h_{31}x + h_{32}y + h_{33}}$$

- H is determined up to scale, 8 DOFs

- The unknowns are the 9 entries of the homography

- Homography can be calculated by Direct Linear Transform (DLT)

- How many points are needed to determine homography?
  - 4 point matches: each point match determines two equations
