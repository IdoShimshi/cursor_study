# 2026-11-03_Lecture 2 - 25_10 - page-12

> Gemini gemini-3.5-flash-lite transcription.

# The Laplacian Pyramid

$$L_i = G_i - \text{expand}(G_{i+1})$$
$$G_i = L_i + \text{expand}(G_{i+1})$$

[diagram: Diagram showing the construction of a Laplacian pyramid from a Gaussian pyramid. Gaussian pyramid levels $G_0, G_1, G_2, G_n$ are shown on the left. Arrows labeled "expand" point from higher levels to lower levels, where they are subtracted (-) from the Gaussian image to produce the Laplacian pyramid levels $L_0, L_1, L_2, L_n$ on the right using equals (=) signs.]

---

# Laplacian $\sim$ Difference of Gaussians

[diagram: 1D signal plots showing a narrow Gaussian minus a wider Gaussian equals a bandpass/Laplacian-like curve with a central positive peak and negative side lobes.]

$$\text{DOG} = \text{Difference of Gaussians}$$

More details on Gaussian and Laplacian pyramids can be found in the paper by Burt and Adelson (link will appear on the website).

lectures Page 12
