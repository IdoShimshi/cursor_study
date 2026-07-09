# 2026-05-14_Lecture 3 - 06_05 - page-04

> Gemini gemini-2.5-flash transcription.

$\lambda V = AV$
$(A - \lambda I) V = 0$
for any $V$ that is non $0$, $\det(A - \lambda I) = 0$
$\varphi(\lambda) = \det(A - \lambda I) = 0$ - Characteristic polynomial $\Rightarrow \lambda$
finding $\lambda$, plug it in to $(A - \lambda I) V = 0 \Rightarrow V$
Plugging $\lambda$ and $V$ to $X(t) = e^{\lambda t} V$, we get a solution
there can be 2 complications:
1) the polynomial might have complex roots
2) might have degenerate roots (E.g. only 2 solutions to a power 3 polynomial)
how to deal with them?
Practical example
$\dot{X} = \begin{pmatrix} 1 & 3 \\ 3 & 1 \end{pmatrix} X$
$\varphi(\lambda) = \det \begin{pmatrix} 1-\lambda & 3 \\ 3 & 1-\lambda \end{pmatrix} = (1-\lambda)^2 - 9 = \lambda^2 - 2\lambda - 8$
$\lambda = -2, \lambda = 4$

reminder
$\det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$
$\det \begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix} = aei + bfg + cdh - ceg - bdi - afh$

reminder
$ax^2 + bx + c = 0$
$x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$

Plug into $(A - \lambda I) V = 0$
$V = \begin{pmatrix} V_1 \\ V_2 \end{pmatrix}$
For $\lambda = -2$:
$\begin{pmatrix} 1 & 3 \\ 3 & 1 \end{pmatrix} - \begin{pmatrix} -2 & 0 \\ 0 & -2 \end{pmatrix} V = \begin{pmatrix} 3 & 3 \\ 3 & 3 \end{pmatrix} V = \begin{pmatrix} 3V_1 + 3V_2 \\ 3V_1 + 3V_2 \end{pmatrix} = 0 \Rightarrow V_1 = -V_2$
$\begin{pmatrix} 1 \\ -1 \end{pmatrix}$

For $\lambda = 4$:
$\begin{pmatrix} 1 & 3 \\ 3 & 1 \end{pmatrix} - \begin{pmatrix} 4 & 0 \\ 0 & 4 \end{pmatrix} V = \begin{pmatrix} -3 & 3 \\ 3 & -3 \end{pmatrix} V = \begin{pmatrix} -3V_1 + 3V_2 \\ 3V_1 - 3V_2 \end{pmatrix} = 0 \Rightarrow V_1 = V_2$
$\begin{pmatrix} 1 \\ 1 \end{pmatrix}$

Plug these in to $X(t) = e^{\lambda t} V$, to get 2 solutions
$X^1 = e^{-2t} \begin{pmatrix} 1 \\ -1 \end{pmatrix}$
$X^2 = e^{4t} \begin{pmatrix} 1 \\ 1 \end{pmatrix}$
[diagram: phase portrait with two lines (eigenvectors) and arrows indicating trajectories moving away from the origin along one line and towards the origin along the other, forming a saddle point]

Complications:
1) complex solution
2)
