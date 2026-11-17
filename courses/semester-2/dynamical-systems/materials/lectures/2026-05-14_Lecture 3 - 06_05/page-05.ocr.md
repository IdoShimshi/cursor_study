# 2026-05-14_Lecture 3 - 06_05 - page-05

> Gemini gemini-2.5-flash transcription.

1) complex solution. Z
$\dot{Z} = AZ$, $Z(t) = u(t) + iw(t)$ this still fine, since we can look at u and w
every complex solution $\lambda = \alpha + i\beta$ $ax^2+bx+c=0$
will have its twin solution $\bar{\lambda} = \alpha - i\beta$ $a\bar{x}^2+b\bar{x}+c=0$
so $\bar{Z}(t) = u(t) - iw(t)$ is also a solution
in complex, these are 2 solutions, but in real, these are the same

Example
$\dot{X} = \begin{pmatrix} 0 & 1 \\ -4 & 0 \end{pmatrix} X$
$\varphi(\lambda) = \lambda^2+4=0 \implies \lambda = \pm 2i$
$\lambda = \alpha + i\beta$, $\alpha=0, \beta=2$
$(A-\lambda I)V = \begin{pmatrix} -2i & 1 \\ -4 & -2i \end{pmatrix} \begin{pmatrix} V_1 \\ V_2 \end{pmatrix} = 0$
$-2iV_1 + V_2 = 0$
$-4V_1 - 2iV_2 = 0$
$\implies V_1 = \frac{1}{2i} V_2$
$V = \begin{pmatrix} 2 \\ i \end{pmatrix} = \begin{pmatrix} 2 \\ 0 \end{pmatrix} + i \begin{pmatrix} 0 \\ 1 \end{pmatrix}$
$u = \begin{pmatrix} 2 \\ 0 \end{pmatrix}$ $w = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$
($\lambda = \alpha + i\beta$)
$e^{\lambda t}(u+iw) = e^{\alpha t} [ (u\cos(\beta t) - w\sin(\beta t)) + i (u\sin(\beta t) + w\cos(\beta t)) ]$
$e^{i\theta} = \cos(\theta) + i\sin(\theta)$
$e^{\lambda t}(u+iw) = e^{(\alpha+i\beta)t}(u+iw) = e^{\alpha t} \cdot e^{i\beta t}(u+iw) = e^{\alpha t}(\cos(\beta t)+i\sin(\beta t))(u+iw)$
$= e^{\alpha t} [ (u\cos(\beta t) - w\sin(\beta t)) + i (u\sin(\beta t) + w\cos(\beta t)) ]$
We take separately the real and complex parts

in our case
real part $X^1(t) = \begin{pmatrix} 2 \\ 0 \end{pmatrix} \cos(2t) - \begin{pmatrix} 0 \\ 1 \end{pmatrix} \sin(2t)$
imaginary $X^2(t) = \begin{pmatrix} 2 \\ 0 \end{pmatrix} \sin(2t) + \begin{pmatrix} 0 \\ 1 \end{pmatrix} \cos(2t)$
[diagram: phase portrait with two concentric ellipses and arrows indicating rotation]
both are real solutions

Example
$\dot{X} = \begin{pmatrix} -4 & 5 \\ -5 & 2 \end{pmatrix} X$
$\begin{vmatrix} -4-\lambda & 5 \\ -5 & 2-\lambda \end{vmatrix} = \lambda^2 + 2\lambda + 17 = 0$
$\lambda = -1 \pm 4i$
$\alpha = -1$, $\beta = 4$
$V = \begin{pmatrix} 3-i \\ 5 \end{pmatrix} = \begin{pmatrix} 3 \\ 5 \end{pmatrix} + i \begin{pmatrix} -1 \\ 0 \end{pmatrix}$
$u = \begin{pmatrix} 3 \\ 5 \end{pmatrix}$ $w = \begin{pmatrix} -1 \\ 0 \end{pmatrix}$

lectures Page 5
