# 2026-07-06_Lecture 9 - 24_06 - page-03

> Gemini gemini-3.1-flash-lite transcription.

for $r < 1$, $(0,0,0)$ is the only FP and $\lambda < 0$. it is globally stable
for $r > 1$, $\lambda > 0$, which is unstable saddle point

$$L_2(x,y,z) = \frac{x^2+y^2+(z-r-\sigma)^2}{2}$$
You can prove there is some ellipse where $\dot{L}_2(x,y,z) = 0$
and some sphere $U$ around it that is a trapping region, $\dot{L}_2 \leq 0$

[diagram: a sphere $U$ with a vertical ellipse inside it, labeled $p$ and $p^*$, with axes $x, y, z$]

the sphere $U$ has some volume
we can look at $V(t)$
$$\dot{V} = \int_{V(t)} \nabla F \, dx = (-\sigma - 1 - b) \cdot V$$
$$V(t) = V_{sp} \, e^{-(\sigma + 1 + b)t} \xrightarrow{t \to \infty} 0$$

[diagram: a box containing the text: "note: a unstable manifold of a saddle FP that is within a trapping region is in the attractor $A$. why? if we go forward in time, it is trapped. if we go back, it only goes to FP, which is inside $U$." and a small circle with a saddle point inside]

definition: sensitive dependence on initial conditions
let $x_0$ be some initial condition
$\exists \, r > 0, \forall \, \delta > 0, \exists \, y_0 \in B_\delta(x_0), \exists \, \tau \geq 0$
$$\| \varphi(\tau; y_0) - \varphi(\tau; x_0) \| \geq r$$
in words, for any small $x_0$, there is a $y_0$ that can be as close as $\delta$, after some time $\tau$ they will be as far as $r$

for lorenz attractor, every point has this property

lets look at trivial examples
$\dot{r} = r(1-r^2)$
$\dot{\theta} = 1$

[diagram: a graph of $\dot{r}$ vs $r$ showing a curve crossing the $r$-axis at 1, and a spiral diagram showing trajectories converging to a unit circle]

the attractor here is an unstable orbit - the unit cycle
- within it, its not sensitive, points converge to 0
- take $x_0$ on it, if you can pick $y_0$ out of it, it is sensitive
- if you can only pick $y_0$ on the circle, it isnt, so the usual case the attractor is not sensitive

a chaotic system is when we have sensitivity on the attractor

lectures Page 3
