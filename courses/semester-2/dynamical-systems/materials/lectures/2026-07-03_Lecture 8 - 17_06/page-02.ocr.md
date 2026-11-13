# 2026-07-03_Lecture 8 - 17_06 - page-02

> Gemini gemini-2.5-flash transcription.

$DF(a, \frac{b}{a}) = \begin{pmatrix} b-1 & a^2 \\ -b & -a^2 \end{pmatrix}$
$det = -a^2(b-1) + ba^2 = -a^2b + a^2 + ba^2 = a^2 > 0$
$tr = b-1-a^2 = b-(1+a^2)$
if $b > 1+a^2 \rightarrow$ repellar
if $b < 1+a^2 \rightarrow$ attractor

lets look at $b \gg 1+a$
if we show its bounded, then there will be a limit cycle the repelled trajectory will go to.
lets show its bounded

for $Y=0$, $\dot{Y} = bx > 0$
for $X=0$, $\dot{X} = a > 0$
so you stay in the first quadrant

lets guess the following boundary ~ $Y=B+x$, $Y=A-x$
where $B < A$

[diagram: A graph with X and Y axes. A line $Y=B+x$ starts from Y-axis at B, goes up. A line $Y=A-x$ starts from Y-axis at A, goes down, intersecting X-axis at A. The intersection point of $Y=B+x$ and $Y=A-x$ is marked as $(\frac{A-B}{2}, \frac{A+B}{2})$. A point $(a, b/a)$ is marked inside the region bounded by these lines and the axes. A dashed line from X-axis at A/2 goes up.]

for $Y=A-x$
define $L(x,y) = x+y-A$. Basically the distance from the line (below it is negative, above, positive)
$\dot{L} = \dot{x}+\dot{y} = a+x^2y -ax-x + bx -x^2y = a-x$
for $\frac{A-B}{2} < x < A$ for $L<0$, we need $a<x$, as $\frac{A-B}{2}$ is the smallest relevant $x$, $\boxed{\frac{A-B}{2} > a}$

for $Y=B+x$
$L(x,y) = Y-x-B$
$\dot{L} = \dot{Y}-\dot{X} = bx - x^2y - a - x^2y + bx + x = 2bx - 2x^2y + x - a = (2b+1)x - 2x^2y - a$
$\dot{L} < 0$, $(2b+1)x - 2x^2y - a < 0$
$\frac{(2b+1)x-a}{2x^2} < Y$
$h(x) \equiv \frac{(2b+1)x-a}{2x^2} < Y$

[diagram: A graph of h(x) vs X, showing a curve with a maximum point $(\bar{X}, \bar{Y})$.]

h(x) has some max, lets find it.
$h'(x) = \frac{-(2b+1)x+2a}{2x^3}$
$h'(x) = 0 \implies -(2b+1)\bar{X} + 2a = 0$
$\bar{X} = \frac{2a}{2b+1}$
$\bar{Y} = h(\bar{X}) = \frac{(2b+1)\frac{2a}{2b+1}-a}{2(\frac{2a}{2b+1})^2} = \frac{a}{\frac{8a^2}{(2b+1)^2}} = \frac{a(2b+1)^2}{8a^2} = \frac{(2b+1)^2}{8a}$

lectures Page 2
