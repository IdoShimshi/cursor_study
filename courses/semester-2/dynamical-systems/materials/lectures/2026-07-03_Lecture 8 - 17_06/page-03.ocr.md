# 2026-07-03_Lecture 8 - 17_06 - page-03

> Gemini gemini-2.5-flash transcription.

$Y = h(\bar{x}) = \frac{\tan^{-1}(\frac{1}{2}\frac{4a^2}{B(A+1)})}{2\frac{4a^2}{B(A+1)}} = \frac{\alpha x (1+B+1)}{B a^2} - \frac{B(A+1)}{B a}$

if $Y > \bar{Y} = \frac{(2B+1)^2}{8a}$ then $L' < 0$. $Y > B > \bar{Y}$
the smallest $Y$ there, is $B$, so if $Y \ge B > \bar{Y}$, $L$ is negative
so the trajectories are bounded, so there must be an orbit within it

[diagram: Phase plane diagram with Y and X axes. A polygonal region is defined by lines $Y=B+x$ (from $(0,B)$ to $(A/2, A/2)$) and $Y=A-x$ (from $(A/2, A/2)$ to $(A,0)$). A point $A/2$ is marked on the X-axis, and $b/a$ on the Y-axis. A small circular trajectory is drawn near the origin.]

example: we have harmonic oscillator with friction
$\ddot{x} = -x - \mu \dot{x}$
lets look at $\mu(x)$ depends on $x$ and can be $<0$
$\mu(x) = x^2-1$

$\dot{x} = V$
$\dot{V} = -x - (x^2-1)V$

define
$Y = V + \int^x f(t)dt = V + \frac{x^3}{3} - x$

rewrite the system to $x, Y$
$\dot{x} = Y - F(x)$
$\dot{Y} = V + F'(x)\dot{x} = -x - F'(x)V + F'(x)V = -x$

[diagram: Graph of $\mu(x) = x^2-1$ vs x. A parabola opening upwards, intersecting the x-axis at -1 and 1. Regions are labeled $\mu(x)>0$, $\mu(x)<0$, $\mu(x)>0$. The points $x=-1, 1$ are labeled $\bar{\mu}(x)=0$.]

nullclines
$\dot{x}=0 \implies Y=F(x)$
$\dot{Y}=0 \implies x=0$

[diagram: Phase plane diagram with Y and X axes. The curve $Y=F(x) = \frac{x^3}{3}-x$ (green) and the line $x=0$ (red) are plotted. The curve $Y=F(x)$ intersects the x-axis at $-\sqrt{3}, 0, \sqrt{3}$. The line $x=0$ is the Y-axis. Arrows indicate the direction of trajectories in different regions. Points $B$ and $B'$ are marked on the Y-axis, and $-\sqrt{3}, \sqrt{3}$ on the X-axis.]
