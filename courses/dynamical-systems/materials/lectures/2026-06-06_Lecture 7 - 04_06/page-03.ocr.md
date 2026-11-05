# 2026-06-06_Lecture 7 - 04_06 - page-03

> Gemini gemini-3.1-flash-lite transcription.

pick any point and continue to the next higher point
if there is none, this is a peak, we have 2 cases
1. there is a finit number of peaks, so we can go past them, then there's just a monotonic inc set (since there are no more peaks)
2. there's an infinite set of peaks, which are decrising, so that's our monotonically dec set

how look at another dim, take the set we found as the descrite points, so
how we find a subset of this subset where this direction is also dec/inc, by the same arguments, we can find it

in 2D, if a system is bounded, the options are
1. $\omega(x_0) = \{x^*\}$, a FP
2. $\omega(x_0) = \Gamma$, a limit cycle

[diagram: a phase portrait showing a spiral trajectory moving outward from a central point towards a closed loop (limit cycle) labeled $\Gamma$, with a point $x^*$ marked outside the loop]

so it the bounded area doesn't contain a FP, there is a cycle

example:
$$\dot{x} = y$$
$$\dot{y} = -x + y(4 - x^2 - 4y^2)$$
$$L(x,y) = \frac{x^2 + y^2}{2} \quad L \text{ is the distance from } (0,0)$$
$$\dot{L} = x\dot{x} + y\dot{y} = xy + y(-x + y(4 - x^2 - 4y^2)) = y^2(4 - x^2 - 4y^2) = \begin{cases} \ge 0 & x^2 + 4y^2 \le 4 \\ \le 0 & x^2 + 4y^2 \ge 4 \end{cases}$$

look at unit cycle $x^2 + y^2 = 1$
$$x^2 + y^2 = 1 \implies x^2 + 4y^2 = 1 - y^2 + 4y^2 = 1 + 3y^2 \le 4$$
since $-1 \le y \le 1$ here $\to$
so $\dot{L} \ge 0$

look at $x^2 + y^2 = 4$
$$x^2 + y^2 = 4 \implies x^2 + 4y^2 = 4 - y^2 + 4y^2 = 4 + 3y^2 \ge 4$$
so $\dot{L} \le 0$

[diagram: a coordinate plane with two concentric circles centered at the origin. The inner circle is labeled $x^2 + y^2 = 1$ with arrows pointing outward ($\dot{L} \ge 0$). The outer circle is labeled $x^2 + y^2 = 4$ with arrows pointing inward ($\dot{L} \le 0$)]
