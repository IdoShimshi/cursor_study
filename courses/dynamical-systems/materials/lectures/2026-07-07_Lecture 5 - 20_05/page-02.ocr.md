# 2026-07-07_Lecture 5 - 20_05 - page-02

> Gemini gemini-2.5-flash transcription.

$\frac{dx}{dt} = x(K-x-\alpha y)$
$\frac{dy}{dt} = y(L-y-\beta x)$

$DF(x,y) = \begin{pmatrix} K-2x-\alpha y & -\alpha x \\ -\beta y & L-2y-\beta x \end{pmatrix}$

$DF(0,0) = \begin{pmatrix} K & 0 \\ 0 & L \end{pmatrix}$
$\lambda_1 = K, \lambda_2 = L$
If $K,L>0 \implies$ Unstable FP

$DF(K,0) = \begin{pmatrix} -K & -\alpha K \\ 0 & L-\beta K \end{pmatrix}$
$\lambda_1 = -K, \lambda_2 = L-\beta K$
If $L-\beta K > 0 \implies det < 0 \implies$ Saddle FP

$DF(0,L) = \begin{pmatrix} K-\alpha L & 0 \\ -\beta L & -L \end{pmatrix}$
$\lambda_1 = K-\alpha L, \lambda_2 = -L$
If $K-\alpha L > 0 \implies det < 0 \implies$ Saddle FP

$DF(x^*,y^*) = \begin{pmatrix} -x^* & -\alpha x^* \\ -\beta y^* & -y^* \end{pmatrix}$
$det = x^*y^*(1-\alpha \beta)$
$tr = -(x^*+y^*)$
If $1-\alpha \beta > 0 \implies det > 0$. $tr < 0 \implies$ Stable

we can determine the sign of the det and trace
if $det M > 0$ and $tr M < 0$
$\lambda_1, \lambda_2 < 0$ and FP is stable
if $det M < 0$
$\lambda_1 < 0, \lambda_2 > 0$ and FP is saddle point

[diagram: Phase portrait with fixed points at (0,0), (K,0), (0,L) and (x*,y*). Stable manifolds of saddles at (K,0) and (0,L) are shown. Trajectories spiral towards (x*,y*).]

There are two stable manifold $W^s$
on these the populations can coexist
Anything above $W^s$ will go to $(0,L)$, meaning
$X$ population is extinct
Anything below $W^s$, will go to $(K,0)$, meaning
$Y$ population is extinct

② $\frac{K}{a} > L$, $\frac{L}{b} > K$

$(0,0)$ is still unstable

[diagram: Phase portrait with fixed points at (0,0), (K,0), (0,L) and (x*,y*). Trajectories go towards (K,0) and (0,L). (x*,y*) is a saddle point.]

$DF(K,0) = \begin{pmatrix} -K & -\alpha K \\ 0 & L-BK \end{pmatrix}$
$L-BK > 0$
$det < 0 \implies$ saddle

$DF(0,L) = \begin{pmatrix} K-\alpha L & 0 \\ -\beta L & -L \end{pmatrix}$
$K-\alpha L > 0$
$det < 0 \implies$ saddle

$DF(x^*,y^*) = \begin{pmatrix} -x^* & -\alpha x^* \\ -\beta y^* & -y^* \end{pmatrix}$
$det = x^*y^*(1-\alpha \beta) > 0$
$tr < 0 \implies$ stable
$\begin{cases} K < \frac{L}{\alpha} \\ L < \frac{K}{\beta} \\ 1 < \frac{1}{\alpha \beta} \\ 1 < 1 \end{cases}$

So in this case, no matter the start
as long as neither population is 0, they
will co-exist

Predator - Prey
Prey: $\dot{x} = x(a-by)$
Predator: $\dot{y} = y(-c+ex)$
a-prey natural growth without predators
-c-predators natural death without prey
a,b,c,e > 0

$\dot{x} = x(a-by)$
$\dot{y} = y(-c+ex)$

nullclines
$\dot{x}=0 \implies x=0$ or $a-by=0 \implies y=\frac{a}{b}$
$\dot{y}=0 \implies y=0$ or $-c+ex=0 \implies x=\frac{c}{e}$

FP
There are 2 FP, $(0,0)$ and $(\frac{c}{e}, \frac{a}{b})$
(where green and red meet)

[diagram: Phase portrait for predator-prey. X-axis is prey, Y-axis is predator. Nullclines are $x=0$, $y=a/b$, $y=0$, $x=c/e$. Fixed points at (0,0) and (c/e, a/b). Arrows indicate a counter-clockwise flow around (c/e, a/b).]
