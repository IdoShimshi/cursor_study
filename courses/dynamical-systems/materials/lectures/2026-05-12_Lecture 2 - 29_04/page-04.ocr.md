# 2026-05-12_Lecture 2 - 29_04 - page-04

> Gemini gemini-2.5-flash transcription.

this is non linear
$\left\{ \begin{array}{l} \dot{\theta} = \omega \\ \dot{\omega} = -\frac{g}{\ell} \sin \theta \end{array} \right.$
[diagram: right-angled triangle with hypotenuse $\ell$, vertical side $\Delta h$, and angle $\theta$ at the top vertex]
$\Delta h = \ell - \ell \cos \theta$

$E = \frac{m \nu^2}{2} + m g \ell (1 - \cos \theta)$
$E = \frac{m (\ell \dot{\theta})^2}{2} + m g \ell (1 - \cos \theta)$
$E = \frac{m (\ell \omega)^2}{2} + m g \ell (1 - \cos \theta)$
$E' = m \ell^2 \omega \dot{\omega} + m g \ell \sin \theta \cdot \dot{\theta} = m \ell^2 \omega (-\frac{g}{\ell} \sin \theta) + m g \ell \sin \theta \omega = 0$

start by analyzing fixed points
$\left\{ \begin{array}{l} 0 = \omega \\ 0 = -\frac{g}{\ell} \sin \theta \end{array} \right.$ we have $\infty$ fixed points

$\textcircled{1} \quad \theta \ll 1 \quad \sin \theta \sim \theta$
$\left\{ \begin{array}{l} \dot{\theta} = \omega \\ \dot{\omega} = -\frac{g}{\ell} \theta \end{array} \right.$
this is a linear approximation to show what happens locally to $0$
[diagram: phase portrait with $\theta$ on the horizontal axis and $\omega$ on the vertical axis, showing concentric elliptical orbits around the origin and saddle points at $\theta = \pm \pi$ with trajectories passing through them]

$\textcircled{2} \quad (\theta + \pi) \ll 1 \quad$ change coordinates
$\left\{ \begin{array}{l} \dot{\theta} = \omega \\ \dot{\omega} = \frac{g}{\ell} \theta \end{array} \right.$
$X = -\frac{g}{\ell} \frac{\theta + \omega}{2}$
$Y = \frac{g}{\ell} \frac{\theta - \omega}{2}$
$\left\{ \begin{array}{l} \dot{X} = (X-Y)\frac{g}{\ell} \\ \dot{Y} = \frac{g}{\ell}(X+Y) \end{array} \right.$
$\left\{ \begin{array}{l} \theta = (X+Y)\frac{\ell}{g} \\ \omega = X-Y \end{array} \right.$
$\left\{ \begin{array}{l} \dot{X} = 2\frac{g}{\ell}X \\ \dot{Y} = -\frac{g}{\ell}Y \end{array} \right.$
