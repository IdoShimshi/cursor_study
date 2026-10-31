# 2026-10-31_Lecture 2 - 25_10 - page-10

> Gemini gemini-2.5-flash transcription.

Going back to the “noise cleaning” example...

[diagram: image with salt & pepper noise]
$* \frac{1}{9} \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$
rect
[diagram: image after 3x3 averaging]
$3 \times 3$ Average
Salt & Pepper Noise

Convolution with a rect $\square \square$ Multiplication with a sinc in the Fourier domain
$= \text{LPF}$ (Low-Pass Filter)
$\square$ blurs the image

[diagram: image after 5x5 averaging]
[diagram: image after 7x7 averaging]
$5 \times 5$ Average
$7 \times 7$ Average

Wider rect $\square \square$ Narrower sinc $=$ Stronger LPF $\square$ Stronger blur

lectures Page 10
