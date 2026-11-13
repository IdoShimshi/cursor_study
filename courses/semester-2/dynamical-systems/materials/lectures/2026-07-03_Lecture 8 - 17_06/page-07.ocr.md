# 2026-07-03_Lecture 8 - 17_06 - page-07

> Gemini gemini-3.1-flash-lite transcription.

weakly stable $\Rightarrow$ supercritical $\Rightarrow$ PO appear after bifurcation
weakly unstable $\Rightarrow$ subcritical $\Rightarrow$ PO appear before "

example
$$\begin{cases} \dot{x} = y \\ \dot{y} = -x - x^3 + \mu y + k x^2 y \end{cases}$$

FP at $(0,0)$
taking partial derivative of linear part
$$A = \begin{pmatrix} 0 & 1 \\ -1 & \mu \end{pmatrix}$$
$-\lambda(\mu - \lambda) + 1 = 0$
$\lambda^2 - \mu\lambda + 1 = 0$
$\lambda_{1,2} = \frac{\mu \pm \sqrt{\mu^2 - 4}}{2} \xrightarrow{\text{when } \mu \to 0} = \frac{\mu}{2} \pm i \cdot 2$ we have a Hopf bifurcation, but which one?

look at the system at bifurcation point $\mu = 0$
$$\begin{cases} \dot{x} = y \\ \dot{y} = -x - x^3 + k x^2 y \end{cases}$$
$$L(x,y) = \frac{x^2}{2} + \frac{x^4}{4} + \frac{y^2}{2}$$
$$\dot{L} = x\dot{x} + x^3 \cdot \dot{x} + y\dot{y} = (x + x^3)y + y(-x - x^3 + k x^2 y) = k x^2 y^2 \ge 0$$

so FP is weakly unstable $\Rightarrow$ subcritical Hopf

so there is an unstable PO at $\mu < 0$

lectures Page 7
