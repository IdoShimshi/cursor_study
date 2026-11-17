# 2026-11-12_Lecture 3 - 01_11 - page-29

> Gemini gemini-3.5-flash-lite transcription.

Projective transformation = Projectivity = Homography

Representation of homography

<u>Theorem.</u> A mapping $h: \mathbb{P}^2 \to \mathbb{P}^2$ is a projective transformation if and only if there exists a non-singular matrix $3 \times 3$ matrix $H$ such that for any point $\boldsymbol{x} \in \mathbb{P}^2$ it holds that $h(\boldsymbol{x}) = H\boldsymbol{x}$

<u>Proof.</u> (partial)

Let $\boldsymbol{x}_1, \boldsymbol{x}_2, \boldsymbol{x}_3$ lie on a line $\boldsymbol{l}$, i.e., $\boldsymbol{l}^T\boldsymbol{x}_i = 0$, for $i = 1, 2, 3$. Let $H$ be a non-singular $3 \times 3$ matrix. Since $\boldsymbol{l}^T H^{-1} H \boldsymbol{x}_i = 0 \Rightarrow$ the points $H\boldsymbol{x}_i$ lie on the line $H^{-T}\boldsymbol{l}$.

Homography transforms a line to a line
