# 2026-07-07_Lecture 5 - 20_05 - page-03

> Gemini gemini-2.5-flash transcription.

nullcline flow direction

$X=0 \implies \dot{Y} = -YC < 0$ so flows down
by continuity $a-bY=0$ when $X \ll \epsilon$, goes down
from $\dot{X} > 0 \implies YX > C \implies (-C+aX) > 0$, so $\dot{Y} > 0$

$Y=0 \implies \dot{X} = aX > 0$, so flows to the right
by cont $-C+aX=0$, when $Y \ll \epsilon$
when $Y > \frac{a}{b}X \implies \dot{Y} < 0 \implies (a-bY) < 0$ so $\dot{X} < 0$

to understand how the FP acts, analyze $\lambda$

$DF\begin{pmatrix} X \\ Y \end{pmatrix} = \begin{pmatrix} a-bY & -bX \\ cY & -c+aX \end{pmatrix}$

$DF\begin{pmatrix} 0 \\ 0 \end{pmatrix} = \begin{pmatrix} a & 0 \\ 0 & -c \end{pmatrix}$ $\det < 0 \implies$ saddle

$DF\begin{pmatrix} \frac{c}{a} \\ \frac{a}{b} \end{pmatrix} = \begin{pmatrix} 0 & -\frac{bc}{a} \\ \frac{ac}{b} & 0 \end{pmatrix}$ $\phi(\lambda) = \lambda^2 + ac$ $\lambda_2 = \pm i\sqrt{ac}$

pure imaginary $\lambda$, this is a cycle

$\frac{\dot{Y}}{Y} - \frac{\dot{X}}{X} = \frac{-C+aX}{X} - \frac{a-bY}{Y}$ this is not defined with $X=0$
[box: reminder $\ln \frac{Y(t)}{X(t)} = \frac{\dot{Y}(t)}{Y(t)}$]
read as:
$\frac{\dot{Y}(a-bY)}{Y} - X(-C+aX)$

$\frac{a\dot{Y}}{Y} - b\dot{Y} = -c\frac{\dot{X}}{X} + a\dot{X}$

integral both sides
$K + a \ln Y - bY = -c \ln X + aX$

$K = \underbrace{-c \ln X + aX}_{f(X)} + \underbrace{-a \ln Y + bY}_{g(Y)}$ since $K$ is a constant, this is like a conserved energy of the system
so all trajectories are orbits

lets analyze $f(X)$
$f'(X) = -\frac{c}{X} + a$
$f'(X)=0 \implies X = \frac{c}{a}$ min

[diagram: graph of $f(x)$ vs $x$, showing a minimum at $x=c/a$]

$g(Y)$ looks the same, its min is $\frac{b}{a}$
so the min $K$ is at $(\frac{c}{a}, \frac{a}{b})$
which is our FP

when we are close to $0$, $f(X)$ and $g(Y)$
expand, leading to orbits being weird.

[diagram: phase portrait with a central fixed point and an orbit around it, with arrows indicating flow direction, and axes labeled $X$ and $Y$. There are also labels A-E and F for different regions of fixed point types.]

For a $2 \times 2$ linearization, the Jacobian $J$ near a fixed point determines the local behavior.
Let
$\tau = tr(J)$, $\Delta = det(J)$.
Since
$\lambda_1 + \lambda_2 = \tau$, $\lambda_1 \lambda_2 = \Delta$.
you get:

| Determinant $\Delta$ | Trace $\tau$ | Fixed Point Type |
| :------------------- | :----------- | :-------------------------------------------------- |
| $\Delta < 0$         | any          | Saddle (always unstable)                            |
| $\Delta > 0$         | $\tau < 0$   | Stable node/spiral                                  |
| $\Delta > 0$         | $\tau > 0$   | Unstable node/spiral                                |
| $\Delta > 0$         | $\tau = 0$   | Center or special case (need more analysis)         |
| $\Delta = 0$         | any          | Non-isolated/degenerate (linearization inconclu...) |

To distinguish node vs spiral, look at
$D = \tau^2 - 4\Delta$.

| D      | Eigenvalues       | Type                  |
| :----- | :---------------- | :-------------------- |
| $D > 0$ | real, distinct    | Node                  |
| $D = 0$ | repeated real     | Improper/star node    |
| $D < 0$ | complex conjugates | Spiral (or center if $\tau = 0$) |

[diagram: a graph showing regions for different fixed point types based on $\tau$ and $\Delta$ values, with labels A-E and F]
A = stable spiral
B = unstable spiral
C = stable node
D = unstable node
E = F = saddle

lectures Page 3
