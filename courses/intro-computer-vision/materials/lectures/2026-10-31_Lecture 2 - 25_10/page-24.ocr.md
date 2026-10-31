# 2026-10-31_Lecture 2 - 25_10 - page-24

> Gemini gemini-3.6-flash transcription.

# Computerized Tomography (CT)

[diagram: Diagram illustrating computerized tomography showing parallel ray projections $p(x)$, $p_1(x)$, and $p_2(x)$ through a 2D object $f(x,y)$, alongside the Central Slice Theorem in the 2D frequency domain $(u,v)$ showing 1D Fourier transforms $P(u)=F(u,0)$, $P_1(u)$, and $P_2(u)$ along radial lines.]

$$P(u) = F(u,0)$$

**Radon transform:** $p(x) = \int_y f(x,y)dy$

$$P(u) = \int_x p(x) e^{-2\pi i u x} dx = \int_x \int_y f(x,y) dy \, e^{-2\pi i u x} dx =$$
$$= \iint_{xy} f(x,y) e^{-2\pi i (ux + 0y)} dy dx = F(u,0)$$
