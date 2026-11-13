# 2026-06-06_Lecture 7 - 04_06 - page-01

> Gemini gemini-2.5-flash transcription.

Lecture 7 - 04/06
Saturday, June 6, 2026 2:40 PM

limiting Point
[diagram: A trajectory $\phi(t, x_0)$ starting from $x_0$ and approaching a point $x^*$. Points $t_1, t_2, ..., t_n$ are marked along the trajectory, getting closer to $x^*$.]
we have seen trajectories that approach the FP $x^*$ (either a stable point, or a saddle, where
There is still a few such trajectories.

taking a Point on the trajectory $\phi(t, x_0)$,
we can discretize the trajectory to $\{t_n\}_{n \to \infty}$
so $\phi(t_n, x_0) \to x^*$

for a limiting Point $\exists \{t_n\}$ an infinite set of time points so $\phi(t_n, x_0) \to x^*$
but it doesn't mean its true for all $\{t_n\}$

simple example - limit cycle
[diagram: A closed loop representing a limit cycle, with $x^*$ marked on the loop.]

take a Point a shift
the distance from $x^*(\phi-x^*)$
changes
[diagram: A graph of $\phi-x^*$ versus $t$, showing an oscillating function that periodically touches the t-axis (where $\phi-x^*=0$). Points $t_1, t_2, t_3, t_4$ are marked on the t-axis where the function is zero.]

taking $t_1, t_2, ...$ is a set of infinite points where $\phi=x^*=0$, so $\phi(t_n, x_0) \to x^*$
but between those times, it can move away

another case can be -
trajectory just gets closer to the cycle, but never reaches
so any point on it is a limiting point
[diagram: A spiral trajectory starting from $x_0$ and asymptotically approaching a limit cycle.]

So $x^*$ is a $\omega$-limit Point of $x_0$
All $\omega$-limiting Points are called the $\omega$ set of $x_0$
in reverse time, we'd call it $\alpha$-limit point

Example -
$\dot{x} = y$
$\dot{y} = x - 2x^3 + y(x^2 - x^4 - y^2)$
$L(x,y) = \frac{y^2}{2} + \frac{-x^2 + x^4}{2}$
$\dot{L} = y\dot{y} - x\dot{x} + 2x^3\dot{x} = y(x - 2x^3 + y(x^2 - x^4 - y^2)) + (2x^3 - x)y = y^2(-y^2 + x^2 - x^4)$
