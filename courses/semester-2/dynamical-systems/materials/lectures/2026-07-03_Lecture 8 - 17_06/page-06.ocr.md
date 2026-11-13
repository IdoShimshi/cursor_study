# 2026-07-03_Lecture 8 - 17_06 - page-06

> Gemini gemini-3.1-flash-lite transcription.

to critical point is $r=0$

lets switch to polar coords
$x = r \cos \theta$
$y = r \sin \theta$
$\begin{cases} \dot{x} = \dot{r} \cos \theta - r \dot{\theta} \sin \theta \\ \dot{y} = \dot{r} \sin \theta + r \dot{\theta} \cos \theta \end{cases}$
$\Downarrow$ in our case (after some substitutions)
$\dot{r} = \mu r + K r^3$
$\dot{\theta} = \omega$

because $\dot{\theta} = \omega$, we are rotating clockwise
to know spiral direction, look at $\dot{r}$

1) $K < 0$ supercritical Hopf
[diagram: three graphs of $\dot{r}$ vs $r$. (a) $\mu < 0$: curve passes through origin with negative slope, labeled "stable FP". (b) $\mu = 0$: curve is tangent to r-axis at origin, labeled "weakly stable FP". (c) $\mu > 0$: curve crosses r-axis at origin and at $r = \sqrt{-\mu/K}$, labeled "unstable FP", "stable PO"]

2) $K > 0$ subcritical Hopf
[diagram: three graphs of $\dot{r}$ vs $r$. (a) $\mu < 0$: curve crosses r-axis at origin and at $r^*$, labeled "stable FP", "$r^*$ unstable PO". (b) $\mu = 0$: curve tangent to r-axis at origin, labeled "weakly unstable". (c) $\mu > 0$: curve crosses r-axis only at origin, labeled "unstable FP"]

this is a general thing

if $\lambda_{1,2} = \alpha_\mu \pm i \omega_\mu$

1) $\alpha_{\mu^*} = 0$ the real part crosses from negative to positive
$\alpha'_{\mu^*} > 0$

look at it when $\mu = \mu^*$ ($\mu = 0$ in our case)
weakly stable $\Rightarrow$ supercritical $\Rightarrow$ PO appear after bifurcation
weakly unstable $\Rightarrow$ subcritical $\Rightarrow$ PO appear before [illegible]
