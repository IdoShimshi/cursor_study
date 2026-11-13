# 2026-11-03_Lecture 2 - 25_10 - page-03

> Gemini gemini-3.5-flash-lite transcription.

Spatial Filtering Operations

[diagram: 3x3 filter grid]

Example 3x3 filter
$$h(x, y) = f(x, y) * \frac{1}{9} \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$$

$$h(x, y) = 1/9 \sum_{(n, m)} f(n, m)$$

Average of all pixels in the 3x3 neighborhood of $(x, y)$

[diagram: Salt & Pepper Noise image at top center, surrounded by 3x3 Average (middle-left), 5x5 Average (middle-right), 7x7 Average (bottom-left), and Median filter (bottom-right) images, with a red diagonal banner stating: Local averaging: Removes noise but blurs edges]

lectures Page 3
