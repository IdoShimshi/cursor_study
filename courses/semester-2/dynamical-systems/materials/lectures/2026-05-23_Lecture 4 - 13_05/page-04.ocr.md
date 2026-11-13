# 2026-05-23_Lecture 4 - 13_05 - page-04

> Gemini gemini-2.5-flash transcription.

R6 - mwi yu to R5

then there is some rotation $R_f \rightarrow R_4 \rightarrow R_5 \rightarrow R_6$
within the spiral, it can't spiral outwards (it'll hit $R_2 / R_f$), so it either
spirals in to $FR(-1,1)$, or there is some ellipse that is a stable orbit
and out of it it spirals inwards to it. within it it spirals outwards, to it

Definitions
- Asymptotically stable FP - if all points around it, go to it
- Basin of attraction - the region from which trajectories go to FP
  - for a stable FP, $BA=R^2$ (the full space)
- stable manifold of a FP $X^*$ is defined:
  - $\{P_0: \varphi(t;P_0) \xrightarrow{t \rightarrow \infty} X^* \} = W_s(X^*)$
  where $\varphi(t,P_0)$ is trajectory with $P_0$ starting point
- unstable manifold - $W_u(X^*) = \{P_0: \varphi(t;P_0) \xrightarrow{t \rightarrow -\infty} X^* \}$

FP $(-1,1)$ is stable
FP $(1,1)$ is unstable, if you are not directly on a the stable manifold, you will go away

5) To decide what happens around FP, we can approximately linearly
$\dot{X} = F(X)$ FP $X^*: F(X^*)=0$
near $X^*$, we can look at $X(t) = X^* + U(t)$, $U$ is very small
$\dot{U}(t) = F(X^*+U(t)) = F(X^*) + DF_{(X^*)} \cdot U$, where $D$ is a matrix, $D_{ij} = \frac{\partial F_i}{\partial X_j}(X^*)$
$\dot{U}(t) = DF_{(X^*)} U$
$n \times 1 \quad n \times n \quad n \times 1$
if the system is nice and differentiable, and $D$ is not degenerate, $U$ acts like $\dot{X}$

a) $X^*=Y^*=1$
$X=1+u$
$Y=1+v$
for any $(x,y)$, $DF_{(x,y)} = \begin{pmatrix} -1 & 1 \\ y & x \end{pmatrix}$
for $(1,1)$, $DF_{(1,1)} = \begin{pmatrix} -1 & 1 \\ 1 & 1 \end{pmatrix}$
$\begin{pmatrix} \dot{u} \\ \dot{v} \end{pmatrix} = \begin{pmatrix} -1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} u \\ v \end{pmatrix}$
A
$\varphi(\lambda) = \begin{vmatrix} -1-\lambda & 1 \\ 1 & 1-\lambda \end{vmatrix} = \lambda^2 - 2$
it is -trace(A)
$\lambda_{1,2} = \pm \sqrt{2}$ - saddle FP
$(-1,1)$

lectures Page 4
