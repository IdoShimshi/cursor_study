# 2026-06-05_Lecture 6 - 03_06 - page-02

> Gemini gemini-3.1-flash-lite transcription.

FP: $y=0, x=0, \pm 1$

$$DF(x,y) = \begin{pmatrix} 0 & 1 \\ 1-3x^2 & 0 \end{pmatrix}$$

$$DF(0,0) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \quad \psi(\lambda) = \begin{vmatrix} -\lambda & 1 \\ 1 & -\lambda \end{vmatrix} = \lambda^2 - 1$$
$$\lambda_{1,2} = \pm 1 \quad \text{saddle}$$

$$DF(\pm 1, 0) = \begin{pmatrix} 0 & 1 \\ -2 & 0 \end{pmatrix} \quad \psi(\lambda) = \begin{vmatrix} -\lambda & 1 \\ -2 & -\lambda \end{vmatrix} = \lambda^2 + 2$$
$$\lambda_{1,2} = \sqrt{-2} = \pm i\sqrt{2} \quad \text{center}$$

[diagram: phase portrait showing a saddle point at the origin and two centers at $x=1$ and $x=-1$ with closed orbits around them]

we could analyze saddle to find stable and unstable manifolds
but we'll do something else, we'll use energy function

$\dot{x} = y$
$\dot{y} = \frac{1}{m} F(x)$

$E = \frac{m}{2} \dot{x}^2 + V(x)$
$V(x) = -\frac{1}{m} \int_{x_0}^x F(x) dx$

well take $m=1$ ?
why ?? $\int \dot{y} = \int x - x^3 = \frac{x^2}{2} - \frac{x^4}{4}$

$\dot{E} = 0$
$E = \frac{m}{2} \dot{x}^2 - \frac{1}{m} \int_{x_0}^x F(x) dx = \frac{y^2}{2} - \frac{x^2}{2} + \frac{x^4}{4}$
$V(x) = -\frac{x^2}{2} + \frac{x^4}{4}$

[diagram: phase portrait showing a "figure-eight" homoclinic orbit connecting the saddle at the origin, with closed orbits inside the loops]

lobe is homoclinic
it leaves a FP and returns to it

if we have $x_0 = a_1$, then $V(a_1)$ will be its max
potential energy
as it goes in the cycle it slides down in $V$
at $x=-1$, $V$ will be min, kinetic energy will be max.
it will roll around in the wall

[diagram: plot of the potential function $V(x) = -\frac{x^2}{2} + \frac{x^4}{4}$ showing a double-well shape with minima at $x=\pm 1$ and a local maximum at $x=0$]

very close to 0, it will also cycle and it cannot cross the $y=0$ line on $V$, since energy is conserved
