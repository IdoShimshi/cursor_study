# 2026-07-07_Lecture 10 - 01_07 - page-04

> Gemini gemini-3.5-flash transcription.

$$ \|v(t)\|^2 = (B(t)v(0), B(t)v(0)) = (v_0, B^T(t)B(t)v_0) $$

$$ \underset{n \times n}{B^T(t)B(t)} \xrightarrow{\quad t \quad} \underset{n \times n}{\Omega^{2t}} $$

so $l_1, \dots, l_n$ are $\lambda_1, \dots, \lambda_n$ of $\Omega$

---

### Example

$$ \begin{cases} \dot{x} = -y + x(1-x^2-y^2) \\ \dot{y} = x + y(1-x^2-y^2) \end{cases} $$

[diagram: A circle of radius 1 centered at the origin in the 2D plane, with an arrow indicating counterclockwise flow, and a point labeled '1' on the positive x-axis.]

$$ \begin{cases} x(t) = r(t) \cos \theta(t) \\ y(t) = r(t) \sin \theta(t) \end{cases} \qquad \begin{aligned} x(t) &= \cos t \\ y(t) &= \sin t \end{aligned} $$

$$ \downarrow $$

$$ \begin{aligned} \dot{\theta} &= 1 \\ \dot{r} &= r(1-r^2) \end{aligned} $$

What are the Lyapunov exponents?

We had a Poincaré map $P(x) = x'$ where:
* if $P'(x) < 1$, its stable,
* $P'(x) = 1$ its a orbit
* $P'(x) > 1$ its unstable

[diagram: Two concentric circles representing a Poincaré map, with a radial line segment showing a mapping from $x$ to $x'$.]

$$ P'(x) = 1 \quad \text{(for } d \ge 2, \text{ this is a matrix and you find its eigenvalues)} $$

$$ r^* = 1 $$

$$ \begin{aligned} r(0) &= 1 + u \\ r(t) &= 1 + u(t) \\ \dot{u}(t) &= (1+u)(-2u) \\ \dot{u} &= -2u \\ u(t) &= u_0 e^{-2t} \\ l_1 &= \frac{\log u(t)}{t} = -2 \\ l_2 &= 0 \end{aligned} $$
