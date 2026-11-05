# 2026-10-31_Lecture 1 - 18_10 - page-22

> Gemini gemini-3-flash-preview transcription.

# The Finite Discrete Fourier Transform

**1D Finite Discrete Fourier Transform:**

$$F(u) = \frac{1}{N} \sum_{x=0}^{N-1} f(x)e^{\frac{-2\pi iux}{N}}$$
$$(u = 0, \dots, N-1)$$

$$f(x) = \sum_{u=0}^{N-1} F(u)e^{\frac{+2\pi iux}{N}}$$
$$(x = 0, \dots, N-1)$$

**2D Finite Discrete Fourier Transform:**

$$F(u, v) = \frac{1}{N} \frac{1}{M} \sum_{x=0}^{N-1} \sum_{y=0}^{M-1} f(x, y)e^{-2\pi i(\frac{ux}{N} + \frac{vy}{M})}$$
$$(u = 0, \dots, N-1; v = 0, \dots, M-1)$$

$$f(x, y) = \sum_{u=0}^{N-1} \sum_{v=0}^{M-1} F(u, v)e^{+2\pi i(\frac{ux}{N} + \frac{vy}{M})}$$
$$(x = 0, \dots, N-1; y = 0, \dots, M-1)$$

lectures Page 22
