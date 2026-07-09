# 2026-05-14_Lecture 3 - 06_05 - page-01

> Gemini gemini-2.5-flash transcription.

Lecture 3 - 06/05
Wednesday, May 13, 2026 9:03 AM

We saw some examples of dynamical system, we want to analyze them without solving them.
$\dot{X}(t) = f(X(t))$

We have a space
given any point, we know where it goes
we can integrate that, but that's hard / impossible, could simulate
or say things about the solutions without solving.
"what happens when $t \to \infty$", goes to $\infty$? goes to $0$? a fixed point? oscillates?

[diagram: A 2D coordinate system with an origin labeled 'cf'. An arrow points upwards labeled 'JA', and another curved arrow points downwards labeled '$\hat{r}\theta$'. A circle is drawn around the origin.]

A is a fixed point if $F=0$. if we begin in that point, it won't move.
finding it is easy, just solve $F(X)=0$
what happens around it? goes away (unstable)? converges (stable)? goes around?
in general, we can linearize the system near the fixed point, look what happens around it.

linear dynamical systems - $F(t)$ and $X(t)$ are linear

$$
\begin{cases}
\dot{X} = Y \\
\dot{Y} = -\omega^2 X - c X^3
\end{cases}
$$
this becomes non linear, this is harder to solve.
in general you can mostly drop/replace the non-linear component near a fixed point

$X$ is an $n$ dimensional vector
$X(t) = (X_1(t), ..., X_n(t))$
its linear if all $X_i$ are linear

$$
\begin{cases}
\dot{X_1}(t) = a_{11} X_1(t) + ... + a_{1n} X_n(t) \\
\vdots \\
\dot{X_n}(t) = a_{n1} X_1(t) + ... + a_{nn} X_n(t)
\end{cases}
$$
we can write $a_{ij}$ as a matrix
$\boxed{\dot{X}(t) = A \cdot X(t)}$

this is an easy case. $X = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$ is always a fixed point
given 2 solution $X^1(t)$, $X^2(t) \Rightarrow X(t) = C_1 X^1(t) + C_2 X^2(t)$
every linear combination of them is a solution

if we have $n$ solutions we can find all
$\{X^j(t)\}$, $j=1, ..., n$
