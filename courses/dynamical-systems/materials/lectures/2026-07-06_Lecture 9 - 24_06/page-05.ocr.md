# 2026-07-06_Lecture 9 - 24_06 - page-05

> Gemini gemini-3.1-flash-lite transcription.

while it is a linear system, which should be simple, you need to solve the full trajectory in order to get $\alpha(t)$

so if you look at 
$$\dot{x} = f(x) \to x(t)$$
$$\delta\dot{x} = \underbrace{f'(x(t))}_{\alpha(t)} \cdot \delta x(t)$$
and look at the sign of $\alpha(t)$, if its mostly positive, you have a chaotic system

for the general case - we have $\varphi(t; \vec{x}_0)$ and $\vec{v}$ a direction
take $\vec{x}_s = \vec{x}_0 + s \cdot \vec{v}$
[diagram: a coordinate system with a curved trajectory starting at $x_0$ and another starting at $x_s$, with a vector $v$ between them labeled $V(t)$ and the distance labeled $\epsilon$]
after time $t$, we have $V(t)$, the vector between $\varphi(t; x_0)$ and $\varphi(t; x_s)$
$$f(\vec{x}) \simeq f(\vec{x}_0) + DF \cdot \delta \vec{x}_0 \text{ near } x_0$$

$\dot{x}(t) = f(x)$
$(x(t) + v(t) \cdot s) = f(x(t) + v(t) \cdot s) = f(x(t)) + s \cdot f(v(t) \cdot s) = f(x(t)) + s \cdot DF(x(t)) \cdot \vec{v}(t)$

$$\dot{v}(t) = \underbrace{DF(x(t))}_{\text{A(t) - a matrix that depends on } t} \cdot v$$
need to find $x(t)$ for it
so this tells us how $v(t)$ vector rotates and changes size
we care about $||v(t)||$

lets assume $||v(t)|| \sim e^{\lambda t}$
then we can say
$$\frac{\log ||v(t)||}{t} \xrightarrow{t \to \infty} \lambda \quad \text{this is a Lyapunov exponent}$$

there cannot be more than $n$ Lyapunov exponents (even if you can take infinite $\vec{v}$)
$\lambda_1, \dots, \lambda_n$
1 of these is $0$, that happens when $\vec{v}$ is the direction of the movement, its basically just like moving ahead in time

if any of $\lambda_1, \dots, \lambda_n$ is $>0$, then its a chaotic system, theres a direction which makes the volume expand.
we need to look at $\sum \lambda_i$, that controls if the volume shrinks or expands
for lorenz system, $\lambda_1 < 0, \lambda_2 = 0, \lambda_3 > 0$ while $\sum \lambda_i < 0$

picking a random $\vec{v}$ will almost always give the largest $\lambda$; (hitting the small one is like hitting the stable manifold of a saddle point, unlikely by accident)

lectures Page 5
