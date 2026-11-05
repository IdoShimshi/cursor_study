# 2026-10-31_Lecture 2 - 25_10 - page-22

> Gemini gemini-2.5-flash transcription.

The Laplacian Pyramid

$L_i = G_i - \text{expand}(G_{i+1})$
$G_i = L_i + \text{expand}(G_{i+1})$

Useful for image compression
Laplacian Pyramid

Gaussian Pyramid
[diagram: A pyramid structure showing the construction of a Laplacian pyramid from a Gaussian pyramid.
On the left, a Gaussian pyramid is shown with levels $G_n$, $G_2$, $G_1$, and $G_0$, each represented by a progressively larger, blurred image of Lena.
Arrows labeled "expand" point from each $G_{i+1}$ level to an expanded version of that image.
A minus sign indicates that the expanded $G_{i+1}$ is subtracted from the corresponding $G_i$ image.
The results of these subtractions are shown on the right as the Laplacian pyramid levels $L_2$, $L_1$, and $L_0$. These images highlight edges and details.
The top level of the Laplacian pyramid is $L_n = G_n$, which is the smallest image from the Gaussian pyramid.]

lectures Page 22
