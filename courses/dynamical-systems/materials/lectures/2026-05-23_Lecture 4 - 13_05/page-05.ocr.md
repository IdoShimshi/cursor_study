# 2026-05-23_Lecture 4 - 13_05 - page-05

> Gemini gemini-2.5-flash transcription.

(a) $x^* = y^* = -1$
$DF_{(-1,-1)} = \begin{pmatrix} -1 & 1 \\ -1 & -1 \end{pmatrix}$
$\varphi(\lambda) = \begin{vmatrix} -1-\lambda & 1 \\ -1 & -1-\lambda \end{vmatrix} = \lambda^2 + 2\lambda + 2$

Since $\tau = -2$, $\Delta = 2$, FP is stable, so all points around it spiral inwards.

(it is possible to still have an orbit)
[diagram: spiral converging to a central point, with arrows indicating inward movement]

if $\tau = \text{trace}(A)$
$\Delta = \det(A)$
$\varphi(\lambda) = \lambda^2 - \tau\lambda + \Delta$
$\lambda = \frac{\tau \pm \sqrt{\tau^2 - 4\Delta}}{2}$

if $\tau < 0$ and $\Delta > 0$
the FP is stable since $\text{Re}(\lambda) < 0$
