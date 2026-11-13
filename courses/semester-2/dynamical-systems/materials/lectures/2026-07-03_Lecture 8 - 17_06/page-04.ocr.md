# 2026-07-03_Lecture 8 - 17_06 - page-04

> Gemini gemini-3.1-flash-lite transcription.

$\dot{y}=0, \quad x=0$
$L(x,y) = \frac{x^2}{2} + \frac{y^2}{2} \quad$ distance from origin
$\dot{L} = x\dot{x} + y\dot{y} = x(-f(x)) - yx = -xf(x)$

[diagram: A graph showing a curve in the first quadrant with a point $Y_1$ on the y-axis, a point $B$ on the curve, and labels indicating regions where $\dot{L} > 0$ and $\dot{L} < 0$.]

So if we start at $Y$, we'll get to $Y_1$. We want to see if $L(Y_1) \lesseqgtr L(Y)$ then we'll know the shape of the cycle (or spiral).

$\Delta L(Y) = L(Y_1) - L(Y)$
for small $Y$, $\Delta L(Y) > 0$, if the whole way from $Y$ to $Y_1$ is within $(-\sqrt{3}, \sqrt{3})$
for other $Y$, we have 3 parts, start from $\dot{L} > 0$, cross to $\dot{L} < 0$, then again $\dot{L} > 0$
lets say at $t_y$ we hit $x(t_y) = \sqrt{3}$, lets call that point $B$

so $\Delta L(Y) = L(Y_1) - L(Y) = \underbrace{L(B) - L(Y)}_{>0} + \underbrace{L(B') - L(B)}_{<0} + \underbrace{L(Y_1) - L(B')}_{>0}$
$L(B) - L(Y) = \int_0^{t_y} \dot{L} dt = \int_0^{t_y} -xf(x) dt = \int_0^{y_B} \frac{\dot{x}}{\dot{y}} f(x) = \int_0^{y_B} \frac{-x}{y-f(x)} f(x) \xrightarrow{Y \to \infty} 0$
$\frac{dy}{dx} = \frac{\dot{y}}{\dot{x}} \cdot dx = \frac{-x}{y-f(x)}$
$L(Y_1) - L(B') = \text{similar to above} \xrightarrow{X \to \infty} 0$
$|L(B') - L(B)|$ increases with greater $Y$ (bad explanation)

[diagram: A graph of $P(Y)$ vs $Y$. The curve $P(Y)$ starts at the origin, increases, and levels off to a horizontal asymptote. A dashed line $P(Y)=Y$ intersects the curve at $Y^*$.]

so there is some point $Y^*$ where we end up where we started, thats a cycle.
anything below it, spiral outwards to it and vice versa
$P(Y^*) = Y^*$
if $P'(Y^*) < 1 \to$ stable periodic orbit

in the general case we have a cycle flow (can be more then 2D)
$x_0 \xrightarrow{T} \phi(T; x_0) = x_0$
take a plane that is perpendicular to the flow $\Sigma$

[diagram: A 3D sketch showing a closed loop (cycle) passing through a small flat surface (plane) labeled $\Sigma$.]
