# 2026-11-13_Lecture 4 -08_11 - page-14

> Gemini gemini-3.6-flash transcription.

Summary

#(B) Camera rotation $\boldsymbol{\rightarrow}$ homography

$$\boldsymbol{Q} = \boldsymbol{RP} + \cancel{\boldsymbol{t}}$$

$\boldsymbol{p}, \boldsymbol{q}$ are perspective projections of $\boldsymbol{P}, \boldsymbol{Q}$

<span style="color:red">Aim: Find invertible $H$ s.t. $\boldsymbol{q} \propto H\boldsymbol{p}$</span>

$$\boldsymbol{p} = \frac{f}{Z} \boldsymbol{P} \Rightarrow \color{red}{\boldsymbol{P} = \frac{Z}{f} \boldsymbol{p}}$$

$$\boldsymbol{q} = \frac{f}{Z'} \boldsymbol{Q} \Rightarrow \color{red}{\boldsymbol{Q} = \frac{Z'}{f} \boldsymbol{q}}$$

Substitute in $\boldsymbol{Q} = \boldsymbol{RP}$

$$\frac{Z'}{f} \boldsymbol{q} = \frac{Z}{f} \boldsymbol{R} \boldsymbol{p}$$

$$\Rightarrow \boldsymbol{q} = \frac{Z}{Z'} \boldsymbol{R} \boldsymbol{p}$$

$$\Rightarrow \boldsymbol{q} \boldsymbol{\propto R p}, \text{ with } H = R$$

($\Rightarrow$The 3D information, i.e. the depth, cannot be recovered)

Rotation around the focal center (no translation)

[diagram: Perspective projection geometry showing camera rotation around the center of projection (labeled B) with two image planes (image 1 and image 2), 3D points P and Q, and image projections x and x'.]

$$\boldsymbol{P} = \begin{bmatrix} X \\ Y \\ Z \end{bmatrix} \quad \boldsymbol{Q} = \begin{bmatrix} X' \\ Y' \\ Z' \end{bmatrix}$$
