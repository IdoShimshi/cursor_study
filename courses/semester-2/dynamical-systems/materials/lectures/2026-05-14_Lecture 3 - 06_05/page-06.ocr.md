# 2026-05-14_Lecture 3 - 06_05 - page-06

> Gemini gemini-2.5-flash transcription.

$V = \begin{pmatrix} 3-4i \\ s \end{pmatrix} = \begin{pmatrix} 3 \\ s \end{pmatrix} + i\begin{pmatrix} -4 \\ s \end{pmatrix}$
$\underline{u}$ $\underline{w}$

$X^1(t) = e^{-t} \left( \cos 4t \begin{pmatrix} 3 \\ s \end{pmatrix} - \sin 4t \begin{pmatrix} -4 \\ s \end{pmatrix} \right)$
$X^2(t) = e^{-t} \left( \sin 4t \begin{pmatrix} 3 \\ s \end{pmatrix} + \cos 4t \begin{pmatrix} -4 \\ s \end{pmatrix} \right)$

[diagram: A 2D coordinate system with x and y axes. A spiral path starts from a point in the first quadrant and spirals inwards towards the origin, indicating decay. An arrow shows the direction of the spiral.]

$e^{-t}$ will win, so it decays toward $0$.
Somehow analyze system of $\begin{pmatrix} 3 \\ s \end{pmatrix}$, $\begin{pmatrix} -4 \\ s \end{pmatrix}$ to understand direction.

Problem 2, if we don't have enough solutions.
$\psi(\lambda) = (\lambda - \lambda_1)(\lambda - \lambda_2)^2$
Here we have 2 solutions $V^1 e^{\lambda t}$, $V^2 e^{\lambda t}$, but this is 3 dimensional.

[diagram: A 3D coordinate system with axes labeled $v_1$ and $v_2$ (and an implied third axis), with a vector shown originating from the origin.]

We can solve things on that plane.
Here is another vector $W$ that satisfies
$(A-\lambda I)W = V_2$
$(A-\lambda I)^2 W = 0$
$AW = \lambda W + V_2$

$X(t) = (W + tV_2) e^{\lambda t}$ will be another solution.
Only $V_2$, since it is the one with a degenerate $\lambda$.

$X'(t) = W \cdot \lambda e^{\lambda t} + V_2 e^{\lambda t} + tV_2 \cdot \lambda e^{\lambda t} = e^{\lambda t} (\lambda W + V_2 + tV_2\lambda) =$
$= AX = A(W + tV_2) e^{\lambda t} = \underbrace{AW}_{\lambda W + V_2} e^{\lambda t} + \lambda t V_2 e^{\lambda t} = e^{\lambda t} (\lambda W + t\lambda V_2)$
