# 2026-10-31_Lecture 1 - 18_10_2 - page-23

> Gemini gemini-3.5-flash-lite transcription.

# About the Discrete Transform

1. $f_d$ is a discrete sampling of the continuous $f(x)$ at gaps $\Delta x$  
$F_d$ is a discrete sampling of the continuous $F(u)$ at gaps $\Delta u = \frac{1}{N\Delta x}$  
[diagram: A box showing the mapping $f(x) \leftrightarrow F(u)$ with downward arrows labeled $\downarrow \Delta x$ and $\downarrow \Delta u = \frac{1}{N\Delta x}$ leading to $f_d(i) \leftrightarrow F_d(j)$]

2. **Periodicity of the discrete transform (both $f(x)$ and $F(u)$):**  
$$F(u+N) = F(u)$$  
$$f(x+N) = f(x)$$  
$$F(u+N) = \frac{1}{N} \sum_{0}^{N-1} f(x) \ e^{-\frac{2\pi i x (u+N)}{N}} = \frac{1}{N} \sum_{0}^{N-1} f(x) \ e^{-\frac{2\pi i x u}{N}} \underbrace{= 1}_{= F(u)}$$  
$$f(x+N) = f(x) \quad \text{can be shown using the inverse transform}$$

3. **Computational complexity:** $\mathcal{O}(N \cdot \log N)$  
(with FFT – the Fast Fourier Transform)

---
*lectures Page 23*
