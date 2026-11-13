# 2026-05-14_Lecture 3 - 06_05 - page-03

> Gemini gemini-2.5-flash transcription.

we had
$X(t) = M(t) M^{-1}(0) X^0$
how we have also
$X(t) = e^{At} X^0$
[diagram: arrow pointing up and then curving right]
this relies on the uniqueness of the solution, 2 different solutions must emerge from the same point
so $e^{At} = M(t) M^{-1}(0) = \tilde{M}(t)$

Examples
1) Simplest case, diagonal matrix
$\dot{X} = ax$
$\dot{Y} = by$
$A = \begin{pmatrix} a & 0 \\ 0 & b \end{pmatrix}$
$e^{At} = 2$
just need to solve for 2 initial conditions
$X^1 = \begin{pmatrix} e^{at} \\ 0 \end{pmatrix}$
$X^2 = \begin{pmatrix} 0 \\ e^{bt} \end{pmatrix}$
$M(t) = \begin{pmatrix} e^{at} & 0 \\ 0 & e^{bt} \end{pmatrix} = \tilde{M}(t) = e^{At}$
[diagram: x-y axis with $X^1$ and $X^2$ labels]

2) harmonic oscillator
$A = \begin{pmatrix} 0 & -\omega \\ \omega & 0 \end{pmatrix}$
$\dot{X} = -\omega Y$
$\dot{Y} = \omega X$
[diagram: x-y axis with a point on the y-axis]
$X(t) = \begin{pmatrix} \cos(\omega t) \\ \sin(\omega t) \end{pmatrix}$
$X^2(t) = \begin{pmatrix} -\sin(\omega t) \\ \cos(\omega t) \end{pmatrix}$
$\implies M = \begin{pmatrix} \cos \omega t & -\sin \omega t \\ \sin \omega t & \cos \omega t \end{pmatrix}$
$e^{\begin{pmatrix} 0 & -\omega \\ \omega & 0 \end{pmatrix} t} = \begin{pmatrix} \cos \omega t & -\sin \omega t \\ \sin \omega t & \cos \omega t \end{pmatrix}$

3)
$C = \begin{pmatrix} a & 0 \\ 0 & a \end{pmatrix} + \begin{pmatrix} 0 & -\omega \\ \omega & 0 \end{pmatrix}$
A B
$e^{Ct} = 2$
(for numbers $e^{a+b} = e^a e^b$)
(proving this was $a+b=b+a$)
(not true for matrix)

general case algorithm
$\dot{X} = AX \implies X(t) = e^{At} X^0$
let's look for a solution of shape ($V$ is constant)
$X(t) = e^{\lambda t} V$
$\dot{X}(t) = \lambda e^{\lambda t} V$
$\lambda e^{\lambda t} V = A X = A e^{\lambda t} V$

lectures Page 3
