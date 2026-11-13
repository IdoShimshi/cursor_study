# 2026-07-07_Lecture 10 - 01_07 - page-01

> Gemini gemini-2.5-flash transcription.

Lecture 10 - 01/07
Monday, July 6, 2026 7:49 PM

We had trapping region U
[diagram: A region U with a smaller region A inside, and a point x with an arrow indicating flow]

$\forall t \ge 0: \psi(t, U) = \bigcup_{x \in U} \psi(t, x) \in U$

$A = \bigcap_{t \ge 0} \psi(t, U)$ which is an invariant set in U

$x \in A \iff \forall t \ge 0 \ \exists y \in U: x = \psi(t, y)$
to show its invariant: show that $x' = \psi(t', x)$ for $t' > 0$ and $x \in A$
$t' \ge 0:$
Since $x \in A$, $\forall t \ge 0 \ \exists y \in U: x = \psi(t, y)$, let $y' = \psi(t', y) \in U$

Since $x' = \psi(t', x)$ and $x = \psi(t, y)$, $x' = \psi(t', \psi(t, y)) = \psi(t' + t, y) = \psi(t, \psi(t', y)) = \psi(t, y')$
So $\forall t \ge 0 \ \exists y' \in U: x' = \psi(t, y')$

$t' < 0: x' = \psi(t', x)$
take $t$ s.t. $t + |t'| \ge 0$ so $\exists y \in U: \psi(t + |t'|, y) = x$
$(* + t' = t)$
$x' = \psi(t', x) = \psi(t', \psi(t + |t'|, y)) = \psi(t' + t + |t'|, y) = \psi(t, y)$

LYAPUNOV EXPONENTS

$\dot{X} = F(X)$
We want to know if there sensitivity at $X_0 \to \psi(t; X_0) = X(t)$
take small step from $X_0$ in direction $\vec{v}$, get to $X_0' \to \psi(t; X_0') = X'(t)$
$V(t) = |X(t) - X'(t)|$
if $V(t) \underset{t \to \infty}{\longrightarrow} \infty$, $X_0$ is sensitive

$V(t) = DF(X(t)) \vec{v}$
$\underset{A(t)}{\text{}}$
[diagram: A flow line with a point X0 and a vector v, then another flow line slightly perturbed from the first, showing divergence.]

lectures Page 1
