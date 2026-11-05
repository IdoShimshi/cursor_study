# 2026-10-31_Lecture 1 - 18_10 - page-23

> Gemini gemini-3-flash-preview transcription.

# About the Discrete Transform

1. $f_d$ is a discrete sampling of the continuous $f(x)$ at gaps $\Delta x$
$\Updownarrow$
$F_d$ is a discrete sampling of the continuous $F(u)$ at gaps $\Delta u = \frac{1}{N \Delta x}$

$$\begin{array}{|c|}
\hline
f(x) \leftrightarrow F(u) \\
\downarrow \Delta x \quad \downarrow \Delta u = \frac{1}{N \Delta x} \\
f_d(i) \leftrightarrow F_d(j) \\
\hline
\end{array}$$

2. **Periodicity of the discrete transform (both $f(x)$ and $F(u)$):**
$F(u+N) = F(u)$
$f(x+N) = f(x)$
$\color{red}{F(u+N) = \frac{1}{N} \sum_{0}^{N-1} f(x) e^{-\frac{2\pi i x (u+N)}{N}} = \frac{1}{N} \sum_{0}^{N-1} f(x) e^{-\frac{2\pi i x u}{N}} \cdot \underbrace{e^{-2\pi i x}}_{=1} = F(u)}$
$\color{red}{f(x+N) = f(x) \quad \text{can be shown using the inverse transform}}$

3. **Computational complexity: $O(N \cdot \log N)$**
(with FFT – the Fast Fourier Transform)
