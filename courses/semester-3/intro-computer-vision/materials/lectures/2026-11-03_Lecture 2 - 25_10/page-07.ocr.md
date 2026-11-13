# 2026-11-03_Lecture 2 - 25_10 - page-07

> Gemini gemini-3.5-flash-lite transcription.

LPF in Image domain vs. Fourier domain

Computational complexity of convolution: $O(N\log N)$ via Fourier. But for filter with a small support $k$ $\implies$ $O(kN)$ in the Image domain.

1) $f(x, y) * k \times k\ \text{rect} \iff F(u, v)\ \text{sinc}(u, v)$
*Convenient* (small spatial support; no cyclic assumption)
*But not an ideal LPF...*

[diagram: A 3x3 grid representing a small spatial support rectangular filter]

2) $f(x, y) * \text{sinc}(x, y) \iff F(u, v)\ \text{rect}(u, v)$
*An ideal LPF*

3) $f(x, y) * \text{gaussian}(x, y) \iff F(u, v)\ \text{Gaussian}(u, v)$

---

# The Sampling Theorem

Developed on the board (also found in recording):
- Nyquist frequency
- Aliasing
- Ideal interpolation
- Discretization induces a Cyclic function

[diagram: A black and white photo of a man sitting in front of a window with a bouquet of flowers on a table.]

$$\text{function}\ f(x)$$
[diagram: A hand-drawn sketch of a continuous function curve over the x-axis, labeled $f(x)$]

$$\text{Fourier}\ F(u)$$
[diagram: A hand-drawn sketch of a Fourier spectrum curve centered at the origin, with $-\Omega_0$ and $\Omega_0$ marked on the u-axis]

$$\text{if } F(u) \text{ is band limited-}$$
there is a certain frequency, above which, all frequencies are $0$, then we can sample it correctly

$$\exists\ \Omega_0\ \text{s.t.}\ \forall |u| > \Omega_0, F(u) = 0$$

$$\text{sampling func}\ S(x) =$$
[diagram: A series of evenly spaced impulse arrows pointing upwards, labeled $S(u)$ below with similar arrows]

lectures Page 7
