# 2026-10-31_Lecture 1 - 18_10 - page-18

> Gemini gemini-3-flash-preview transcription.

# Some Fourier Transforms

| Function | Fourier Transform |
| :--- | :--- |
| $f(x) = \text{rect}(x) = \begin{cases} k & -c \le x \le c \\ 0 & \text{otherwise} \end{cases}$ | $F(u) = 2kc \cdot \text{sinc}(2\pi cu)$ |
| $f(x) = \delta(x)$ | $F(u) \equiv 1$ |
| $f(x) = \dots$ | $F(u) = \int_{-\infty}^{\infty} f(x) e^{-2\pi iux} dx$ |
| $f(x) = \dots$ | $= (e^{i\alpha x} + e^{-i\alpha x}) \dots$ |
| $f(x) = \dots$ | [diagram: hand-drawn plot of a rectangular function $f(x) = \text{rect}(x)$ with height $k$ and width from $-c$ to $c$] |
| | [diagram: hand-drawn plot of a sinc function] |
| | $\text{Sinc}(x) = \sin(x)/x$ |
| Gaussian | [diagram: hand-drawn plot of a sinc function labeled $F(u)$ with peak value $2kc$ and zero crossings at $\frac{1}{2c}, \frac{2}{2c}, \frac{3}{2c}$] |
| | $F(u)$ |

lectures Page 18
