# 2026-05-14_Lecture 3 - 06_05 - page-02

> Gemini gemini-2.5-flash transcription.

$\{X^j(t)\} \quad j=1,...,h$

$M_{h \times h}(t) = \begin{pmatrix} X^1(t) & ... & X^h(t) \end{pmatrix}$

$\dot{M}(t) = AM(t)$, because

$\dot{M}(t) = (\dot{X}^1(t), ..., \dot{X}^h(t)) = (AX^1(t), ..., AX^h(t)) = A(X^1(t), ..., X^h(t)) = AM(t)$

Solving it gives a matrix solution

having a matrix is enough to solve any initial condition

Example:
If we have M, is constant vector
$M(t): C = C_1 M^1(t) + ... + C_h M^h(t)$, since the columns solve the system this is a linear combination of them, which is also a solution

Lets find $X^0$
$X(t): X(0) = X^0$ will look for $C$
$M(0)C = X^0 \implies C = M^{-1}(0)X^0$
, $M^{-1}$ needs to exist, det $M(0) \neq 0$
So for any $X(t)$:
$X(t) = M(t)M^{-1}(0)X^0$
$X^j(t)$ - fundamental set of solutions
$M(t)$ - fundamental matrix solution

det $M(0) \neq 0 \implies$ det $M(t) \neq 0$, inverse time or any future solution can be initial

1 dimension: $\dot{X}(t) = aX(t) \implies X(t) = X_0 e^{at}$
explaining why this derivative law is true
$e^{at} = \sum_{k=0}^\infty \frac{(at)^k}{k!} = 1 + ...$
$\frac{d}{dt}(e^{at}) = \sum_{k=1}^\infty \frac{a^k t^{k-1}}{(k-1)!} = a \sum_{k=1}^\infty \frac{a^{k-1} t^{k-1}}{(k-1)!} = a \sum_{m=0}^\infty \frac{(at)^m}{m!} = a e^{at}$

general case: $\dot{X} = AX \implies X(t) = e^{At} X_0$
$e^{At} \stackrel{def}{=} \sum_{k=0}^\infty \frac{A^k t^k}{k!}$
, this will act the same
we had
$X(t) = M(t)M^{-1}(0)X^0$

lectures Page 2
