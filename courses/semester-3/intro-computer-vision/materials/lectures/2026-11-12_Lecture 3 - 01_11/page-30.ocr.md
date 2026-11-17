# 2026-11-12_Lecture 3 - 01_11 - page-30

> Gemini gemini-3.5-flash-lite transcription.

Projective transformation = Projectivity = Homography

- An invertible linear transformation of rays
$$\begin{pmatrix} x' \\ y' \\ 1 \end{pmatrix} = q \propto H p = \begin{pmatrix} h_{11} & h_{12} & h_{13} \\ h_{21} & h_{22} & h_{23} \\ h_{31} & h_{32} & h_{33} \end{pmatrix} \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}$$

- Non-linear transformation of points
$$x' = \frac{h_{11}x + h_{12}y + h_{13}}{h_{31}x + h_{32}y + h_{33}}, \quad y' = \frac{h_{21}x + h_{22}y + h_{23}}{h_{31}x + h_{32}y + h_{33}}$$

- Homography has 9 entries, only 8 DOFs, why?
- $H$ is determined up to scale
- Homography can be calculated by Direct Linear Transform
- How many points are needed to determine homography?
  - 4 points: each point determines two equations

---

Examples of projective transformation

[diagram: Two illustrations showing homography setups. Diagram A shows rays from a planar surface intersecting two image planes via perspective projection (camera motion R,t). Diagram B shows two image planes sharing a camera center with camera rotating about its center, no translation.]

(A) The projective transformation between two images induced by a world plane
(B) The projective transformation between two images with the same camera center (camera rotating about its center, no translation)
- Proof in a few slides

lectures Page 30
