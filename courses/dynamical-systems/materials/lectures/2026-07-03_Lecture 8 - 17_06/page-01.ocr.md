# 2026-07-03_Lecture 8 - 17_06 - page-01

> Gemini gemini-2.5-flash transcription.

Lecture 8 - 17/06
Thursday, July 2, 2026 11:02 AM

limiting set -
for a trajectory $\psi(t, x_0)$
Let $t_n : t_n \to \infty$
$\psi(t_n, x_0) - X^* \to 0$ then $X^*$ is a limiting point
the set of limiting points is the limiting set $w(x_0)$

in a bounded trajectory there must be a limiting set
in 2D, it's either a FP or a cycle.

inside the cycle there must be a FP (or undefined area)
reason: going backwards in time, trajectories are spiraling inwards in a bounded
area, they must approach a FP, or another smaller cycle (then repeat the argument)

example:
chemical reaction, 2 chemicals, $X, Y$, and more constants (basically infinite) chemicals $A$
converts
$\begin{cases} A \to X \\ 2X+Y \to 3X \\ B+X \to Y \\ X \to \emptyset \end{cases}$
$\dot{X} = a + X^2Y - bX - X$
$\dot{Y} = bX - X^2Y$

$\dot{Y} = 0 = bX - X^2Y$
$Y = \frac{bX}{X^2} = \frac{b}{X}$

$\dot{X} = 0 = a + X^2Y - bX - X$
$a + X^2(\frac{b}{X}) - bX - X = 0$
$a + bX - bX - X = 0$
$a - X = 0$
$X = a$

FP at $(a, \frac{b}{a})$

DF = $\begin{pmatrix} 2XY - (b+1) & X^2 \\ b-2XY & -X^2 \end{pmatrix}$

DF$(a, \frac{b}{a})$ = $\begin{pmatrix} 2a(\frac{b}{a}) - (b+1) & a^2 \\ b-2a(\frac{b}{a}) & -a^2 \end{pmatrix}$
DF$(a, \frac{b}{a})$ = $\begin{pmatrix} b-1 & a^2 \\ -b & -a^2 \end{pmatrix}$

det = $\delta = -a^2(b-1) + ba^2 = -a^2b + a^2 + a^2b = a^2 > 0$

lectures Page 1
