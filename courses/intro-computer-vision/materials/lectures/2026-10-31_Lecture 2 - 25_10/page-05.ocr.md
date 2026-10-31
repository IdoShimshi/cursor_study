# 2026-10-31_Lecture 2 - 25_10 - page-05

> Gemini gemini-2.5-flash transcription.

# Spatial Filtering Operations

[diagram: 3x3 grid representing a filter]
3x3 filter

$h(x,y) = f(x,y) * \frac{1}{9} \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$

Example 3x3 filter

$h(x,y) = \frac{1}{9} \sum_{(n,m)} f(n,m)$

Average of all pixels in the
3x3 neighborhood of $(x,y)$

lectures Page 5
