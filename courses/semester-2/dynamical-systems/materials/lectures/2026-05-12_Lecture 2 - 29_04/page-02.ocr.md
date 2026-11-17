# 2026-05-12_Lecture 2 - 29_04 - page-02

> Gemini gemini-2.5-flash transcription.

2) $E \ge 0$ , if we move E equation around, we get
$\frac{V^2}{(2E/m)} + \frac{X^2}{(2E/K)} = 1 \leftarrow$ an ellipse
smaller E, smaller ellipse
We know the direction by looking
at $\dot{x}$ and V at some points
the arrow map is the vector field
the trajectory are called orbits

notice $\vec{X}(t) = \vec{X}(t+T)$
smallest T is period

lets introduce friction (Put it in air)
[diagram: spring-mass system with friction, and a block experiencing friction from particles with velocity u]
$F=ma = m\dot{v} = \dot{p}$

$\left\{ \begin{array}{l} mu + Mv = -mu' + Mv' \\ \frac{mu^2}{2} + \frac{Mv^2}{2} = \frac{mu'^2}{2} + \frac{Mv'^2}{2} \end{array} \right.$
div $m(u^2-u'^2) = M(V'^2-V^2)$
$\rightarrow u-u' = v+v'$
$(a^2-b^2) = (a-b)(a+b)$

$u' = -v' - v + u$
$V' = \frac{(M-m)v - 2mu}{M+m}$
$u' = \frac{2Mv + (M-m)u}{M+m}$

We want to calc, what is big mass experiencing
average
$\langle \Delta P \rangle = M \langle V' - V \rangle \ge M \langle \frac{(M-m)v - 2mu}{M+m} - V \rangle$
$= M \langle \frac{(M-m)v - 2mu - V(M+m)}{M+m} \rangle$
$= M \langle \frac{Mv - mv - 2mu - MV - mv}{M+m} \rangle$
$= M \langle \frac{-2mv - 2mu}{M+m} \rangle$
$= M \langle \frac{-2m(v+u)}{M+m} \rangle$
$\ge \frac{-2m}{M+m} M \langle v+u \rangle$
$= \frac{-2mM}{M+m} (\langle v \rangle + \langle u \rangle)$

$\langle u \rangle$ is 0
Since for every collision
there an opposite one

$F = \frac{\langle \Delta P \rangle}{\Delta t} \cdot \# \text{collisions} \sim -V$

So now
