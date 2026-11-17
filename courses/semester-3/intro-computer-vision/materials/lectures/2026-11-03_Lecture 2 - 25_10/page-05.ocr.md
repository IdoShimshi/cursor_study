# 2026-11-03_Lecture 2 - 25_10 - page-05

> Gemini gemini-3.5-flash-lite transcription.

The Convolution Theorem

$$\mathcal{F}\{f(x) * g(x)\} = \mathcal{F}\{f(x)\} \cdot \mathcal{F}\{g(x)\}$$

and similarly:

$$\mathcal{F}\{f(x)g(x)\} = \mathcal{F}\{f(x)\} * \mathcal{F}\{g(x)\}$$

[diagram: Red handwritten text overlay on the first box reading "Proof: Homework"]

$\rightarrow$ Computational complexity of Discrete Convolution: 
$$O(N\log N)$$
Take $f$ and $g \rightarrow \text{FFT} \rightarrow F \cdot G \rightarrow \text{FFT}^{-1} \rightarrow f * g$

Going back to the "noise cleaning" example...

[diagram: Image showing an equation: an image with salt & pepper noise, multiplied by (1/9) times a 3x3 matrix of ones labeled "rect", equals a smoother 3x3 Average image]

Salt & Pepper Noise

$3 \times 3$ Average

Convolution with a $\text{rect}$ $\iff$ Multiplication with a $\text{sinc}$ in the Fourier domain
$= \text{LPF}$ (Low-Pass Filter)
$\implies$ blurs the image

[diagram: Two images showing the result of $5 \times 5$ Average and $7 \times 7$ Average filters on the noisy image]

$5 \times 5$ Average
$7 \times 7$ Average

Wider $\text{rect}$ $\iff$ Narrower $\text{sinc}$ $= \text{Stronger LPF}$ $\implies$ Stronger blur

---
lectures Page 5
