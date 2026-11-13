# 2026-11-13_Lecture 4 -08_11 - page-06

> Gemini gemini-3.6-flash transcription.

Summary

# Perspective projection

- Perspective rule $P = \begin{bmatrix} X \\ Y \\ Z \end{bmatrix} \to p = \begin{bmatrix} x \\ y \end{bmatrix}$
$$x = \frac{fX}{Z} \qquad y = \frac{fY}{Z}$$

- Using matrix notations and **homogeneous coordinates**
$$p = \begin{bmatrix} fX \\ fY \\ Z \end{bmatrix} = \begin{bmatrix} f & & 0 \\ & f & 0 \\ & & 1 & 0 \end{bmatrix} \begin{bmatrix} X \\ Y \\ Z \\ 1 \end{bmatrix}$$

- **Camera matrix**$^* \ 3D \to 2D \ (P \to p)$
$$\begin{bmatrix} f & & 0 \\ & f & 0 \\ & & 1 & 0 \end{bmatrix}_{3 \times 4} = \begin{bmatrix} f & & \\ & f & \\ & & 1 \end{bmatrix} [I | \mathbf{0}]$$

$^*$Special case
