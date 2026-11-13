# 2026-11-12_Lecture 3 - 01_11 - page-37

> Gemini gemini-2.5-flash transcription.

(A) Planar scene $\rightarrow$ homography
- A plane $aX + bY + cZ = d$
- In vector notation $\mathbf{n}^T \mathbf{P} = d$
- $\mathbf{Q} = \mathbf{RP} + \mathbf{t}$
- $\frac{\mathbf{n}^T \mathbf{P}}{d} = 1$, so $\mathbf{Q} = \mathbf{RP} + \mathbf{t} \frac{\mathbf{n}^T \mathbf{P}}{d}$
- Rearrange, $\mathbf{Q} = \left(\mathbf{R} + \frac{1}{d} \mathbf{tn}^T\right) \mathbf{P}$
- Project, $\mathbf{q} \propto \left(\mathbf{R} + \frac{1}{d} \mathbf{tn}^T\right) \mathbf{p}$
- So $\mathbf{q} \propto \mathbf{Hp}$, with $\mathbf{H} = \mathbf{R} + \frac{1}{d} \mathbf{tn}^T$

[diagram: Two cameras viewing a planar surface, showing corresponding points x and x' in image 1 and image 2 respectively. The transformation between the cameras is denoted by R,t. A blue arrow indicates the direction of projection from the 3D point X to the 2D point x. Below the diagram, the letter A is shown.]

$$
\mathbf{P} = \begin{bmatrix} X \\ Y \\ Z \end{bmatrix} \quad \mathbf{Q} = \begin{bmatrix} X' \\ Y' \\ Z' \end{bmatrix}
$$

lectures Page 37
