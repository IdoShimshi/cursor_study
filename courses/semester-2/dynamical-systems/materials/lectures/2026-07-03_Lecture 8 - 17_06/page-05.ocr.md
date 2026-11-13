# 2026-07-03_Lecture 8 - 17_06 - page-05

> Gemini gemini-3.1-flash-lite transcription.

$x_0 \xrightarrow{T} \varphi(T; x_0) = x_0$
take a plane that is perpendicular to the flow $\Sigma$
take a point close to the cycle, because its close and continuous
it'll travel with the cycle, so after $T$-period, it'll cross the plane

$x \in \Sigma \xrightarrow{T \approx T} P(T; x) = x' \in \Sigma = P(x)$ called a Poincaré map

this function is of dim $D-1$

in 2D we can draw it, and the $P'(x^*)$ determines if its stable or not

$P(x_0) = x_0$
$x = x_0 + \delta x \to x' = P(x_0 + \delta x) = P(x_0) + P'(\delta x) = x_0 + DP(x_0) \cdot \delta x$
$\quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \uparrow$
$\quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \text{partial derivative matrix}$

in 2D, this is $P'(x) \delta x$, if $P'(x) < 1$, it'll shrink
in other, all eigen values need to be $< 1$

[diagram: a circle with a small arc segment marked on the right side, with a line segment perpendicular to the flow crossing the circle]

### Bifurcation

our systems have parameters, usually a slight change in them leads to a small change in the systems;
sometimes crossing some value can lead to dramatic changes

before we saw 2 chemicals $a, b$, and we said $A > 1-a$
so crossing this creates the cycle, basically the system has the cycle potential, but without
the right params, its not realized, it has an imaginary part eigenvalue
this is called Hopf bifurcation

example:
$$\dot{x} = \mu x + kx(x^2 + y^2)$$
$$\dot{y} = \omega x + \mu y + ky(x^2 + y^2)$$
linearizing, we get $A_{(0,0)} = \begin{pmatrix} \mu & -\omega \\ \omega & \mu \end{pmatrix}$

$$(\mu - \lambda)^2 + \omega^2 = \lambda^2 - 2\mu\lambda + \omega^2$$
$$\lambda_{1,2} = \mu \pm \sqrt{\mu^2 - \omega^2}$$
look at $\mu \approx 0$
$$\lambda_{1,2} \approx \mu \pm i\omega$$
raising $\mu$ makes it cross from negative to positive
so critical point is $\mu_{cr} = 0$

[diagram: a complex plane graph with a vertical axis labeled "Im $\lambda$" and a horizontal axis labeled "Re $\lambda$". Two arrows point toward the origin on the real axis, indicating the eigenvalues crossing from the left half-plane to the right half-plane.]

Lectures Page 5
