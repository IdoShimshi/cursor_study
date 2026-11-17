# 2026-06-05_Lecture 6 - 03_06 - page-04

> Gemini gemini-3.1-flash-lite transcription.

back to the pendulum - lets add damping
$$\begin{cases} \dot{x} = y \\ \dot{y} = -\sin x - by \end{cases}$$
$$E = \frac{y^2}{2} + 1 - \cos x$$
$$\dot{E} = y\dot{y} + \sin x \cdot \dot{x} = y(-\sin x - by) + \sin x \cdot y = -by^2 \leq 0$$
so energy is not constant

definition: for dynamical system $\dot{\underline{x}} = f(\underline{x})$, with FP $\underline{x}^*$ if $\exists L(\underline{x})$ s.t.
$$L(\underline{x}) \geq L(\underline{x}^*) \quad \text{for } x \text{ close to } x^*$$
$$\dot{L}(\underline{x}) \leq 0$$
then this is a weak lyapunov function
if $\dot{L}(\underline{x}) < 0$, its strong
any energy is a WLF

define: FP $\underline{x}^*$ is lyapunov stable if for a small enough area around $\underline{x}^*$ all trajectories that start in that area, cannot leave another area
any $x_0$ in green will never leave blue
[diagram: a small circle labeled "green" inside a larger circle labeled "blue", with a point $x^*$ at the center]

1) if you find a WLF in neighborhood of FP, this FP is Lyapunov stable
- idea, it $\dot{L} \leq 0$, $L(x)$ cannot increase, so it is stuck in that area
2) if you find a SLF " " " " ", this FP is asymptotically stable

so the damped pendulum looks like
[diagram: a phase portrait showing spiral sinks at $(2n+1)\pi$ and centers/spirals at $2n\pi$, with trajectories flowing toward the sinks]

$Z_u: \{ \dot{L}(x) = 0 \mid x \in U \}$

another example, lets damp
