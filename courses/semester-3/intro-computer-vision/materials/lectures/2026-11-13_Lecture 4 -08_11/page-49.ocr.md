# 2026-11-13_Lecture 4 -08_11 - page-49

> Gemini gemini-3-flash-preview transcription.

# Singular Value Decomposition (SVD)

*   <u>Theorem.</u> A matrix $M \in \mathbb{R}^{m \times n}$ can be factorized into
    $$M = UDV^T$$
    where $U \in \mathbb{R}^{m \times m}$ and $V \in \mathbb{R}^{n \times n}$ are orthogonal matrices and $D = diag(\sigma_1, ..., \sigma_p) \in \mathbb{R}^{m \times n}$ with $p = \min\{m, n\}$ where $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_p \ge 0$, called singular values.
*   It can be shown that if we define $r$ by
    $$\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > \sigma_{r+1} = \dots = \sigma_p = 0$$
    then
    $$\text{rank}(M) = r$$
    $$\text{null}(M) = \text{span}\{v_{r+1}, ..., v_n\}$$
    $$\text{Img}(M) = \text{span}\{u_1, ..., u_r\}$$

[diagram: Visual representation of SVD showing $M = U \Sigma V^*$. It illustrates the dimensions of the matrices $M$ ($m \times n$), $U$ ($m \times m$), $\Sigma$ ($m \times n$), and $V^*$ ($n \times n$). It also shows that $U U^* = I_m$ and $V V^* = I_n$, indicating $U$ and $V$ are orthogonal matrices.]
