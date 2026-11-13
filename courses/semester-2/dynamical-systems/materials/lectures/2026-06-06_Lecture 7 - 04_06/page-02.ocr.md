# 2026-06-06_Lecture 7 - 04_06 - page-02

> Gemini gemini-3.1-flash-lite transcription.

$\dot{L} = y\dot{y} - x\dot{x} + 2x^3\dot{x} = y(x - x^3 + y(x^2 - y^4)) + (2x^3 - x) \cdot y = y^2(-y^2 + x^2 - x^4) =$
$$= 2y^2 \cdot \left(\frac{y^2 - x^2 + x^4}{2}\right) = -2y^2L$$

notice $\begin{cases} L > 0, \dot{L} \le 0 \\ L < 0, \dot{L} \ge 0 \\ L = 0, \dot{L} = 0 \end{cases}$

so $L$ goes to $0$, $0$ is like a FP for it

$L = 0 : y^2 = x^2(1 - x^2)$
$y = \pm |x|\sqrt{1 - x^2}$

[diagram: A graph showing a figure-eight shape centered at the origin on an x-y plane. A green curve outlines the figure-eight, labeled $L=0$. Inside the left loop of the figure-eight, a blue spiral trajectory is drawn, labeled $L<0$. Outside the figure-eight, a green trajectory is drawn, labeled $L>0$.]

so any trajectory on $L=0$ will go to $0$
for any $x_0$ on it, $0$ is the $\omega$-set of it

inside it $L < 0$, outrid $L > 0$ and it goes towards $L=0$

what is the $\omega$-set of $x_0$ ? any point on the $L=0$ figure 8
for blue $x_0$, $\omega$-set is left part of $L=0$

limiting set -
1) if You start on some $\omega(x_0)$ limiting set, you will stay on it
$y_0 \in \omega(x_0) \implies \varphi(t, y_0) \in \omega(x_0)$

$\exists \{t_n\} : \varphi(t_n, x_0) \to y_0$. we want to show that $\varphi(t, y_0) \in \omega(x_0)$

[diagram: A curved line representing a trajectory. A point $y_0$ is marked on the curve. A blue segment of the curve is labeled $\omega(x_0)$. Two points on the curve are labeled $\varphi(t_n, x_0)$ and $\varphi(t_n + t, x_0)$.]

2) if a trajectory is bounded (there some area $C$
that once you enter it, you do not leave)
there must be a limiting set within it

$\varphi(t, x_0)$ is bounded $\implies \omega(x_0) \neq \emptyset$

proof - lets look at one dim of $x$

[diagram: A graph of a function $x(t)$ over time $t$. The curve oscillates with several peaks. Red dots are placed on the local maxima of the curve.]

discretize it, we need to find a monotonically inc or dc
set of $t, x(t)$
pick any point and continue to the next higher point
if there is none, this is a peak, we have 2 cases

lectures Page 2
