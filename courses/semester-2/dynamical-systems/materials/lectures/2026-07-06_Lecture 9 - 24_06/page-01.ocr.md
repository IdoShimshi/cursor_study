# 2026-07-06_Lecture 9 - 24_06 - page-01

> Gemini gemini-3.5-flash transcription.

Lecture 9 - 24/06
Sunday, July 5, 2026   8:36 AM

trapping region

a closed shape that at its borders trajectories can only move inwards - never leave

[diagram: A circular region U containing a smaller green-shaded region A, with red arrows on the boundary of U pointing inwards]

$\varphi(t; U) = \{\varphi(t, x_0) \mid x_0 \in U\} \in \text{interior}(U) \quad t > 0$

$$\boxed{A = \bigcap_{t \ge 0} \varphi(t; U)} - \text{attractor for } U$$

$x \in A$, means $\forall t \ge 0 \quad x \in \varphi(t; U) \quad ; \quad \exists y \in U : x = \varphi(t, y) \quad ; \quad \varphi(-t; x) \in U$

so for a trajectory that reaches $x \in A$, no matter how far you go back, stays in $U$
since that is true for every point on that trajectory, so every point must be inside $A$,
so the whole trajectory is fully inside $A$.

this is not the whole $U$, for many points, going back in time leaves $U$

lets look at previous attractors -

$\dot{x} = y$
$\dot{y} = x - 2x^3 + y(x^2 - x^4 - y)$
$L(x,y) = \frac{-x^2 + x^4}{2} + \frac{y^2}{2}$
$\dot{L} = -2y^2 L$

[diagram: A yellow double-lobed (peanut-shaped) region U enclosing two fixed points labeled with '+' and '-']

take $U$, an outer cycle without the FPs
lets call the figure $\Gamma$ ($\Gamma^+$ for $x > 0$, $\Gamma^-$ for $x < 0$)
remember, things outside the $\Gamma$ shrink to it, so $U$ is a trapping region

$A = \Gamma$ is invariant set (also $\Gamma^+, \Gamma^-$)

what if $U$ doesnt exclude FP? $A = \Gamma \cup \{FP_1\} \cup \{FP_2\}$

---

if we have region $U$ of volume $V$

define $\varphi(t; U)$ (where $U$ moves after $t$) and its volume is $V(t)$

for every point $\dot{\vec{x}} = \vec{F}(\vec{x})$

[diagram: A region U, V transforming over time t to a region \varphi(t; U), V(t)]

so the volume depends on the movement of the border
