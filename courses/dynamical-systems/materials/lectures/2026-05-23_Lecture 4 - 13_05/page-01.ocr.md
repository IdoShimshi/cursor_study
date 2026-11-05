# 2026-05-23_Lecture 4 - 13_05 - page-01

> Gemini gemini-2.5-flash transcription.

Lecture 4 - 13/05
Thursday, May 21, 2026 1:53 PM

linear systems - reminder
$\dot{X} = A(t)X$

1. fixed point $X^*=0$
- can happen also if there a $\lambda=0$ eigenvalue, $AV=0$, all the points on this eigenvector are FP.

2. for every initial condition $X(0)$, $t$ can be driven forwards or backwards
to get the trajectory, $-\infty < t < \infty$, this trajectory is unique

3. Same qualitative behavior everywhere. You can mult by constant but the
trajectory will act the same

1D $\dot{X} = rX(1 - \frac{X}{K})$ $r, K > 0$
FP: $X=0$, $X=K$

$\forall X_0$, $X(t) = \frac{X_0 K}{X_0 + (K-X_0)e^{-rt}}$

looking at the different regions
and how they act

[diagram: graph of X(t) vs t, showing trajectories converging to K from above and below, and diverging from 0]

how we can look at $\dot{X}$:

Phase portrait:
$(\dot{X})$
[diagram: phase portrait of $\dot{X}$ vs X, showing a parabola intersecting the x-axis at 0 and K, with arrows indicating direction of flow]

neurons: cells that fire electrical signals, action potential
You can define the state of a neuron by defining the firing rate $r(t)$

[diagram: neuron input/output diagram with J, $\Delta$, r(t) arrows]

a firing happens because other neuron activation
So we can say an neuron's activation depends on the sum
of the signal it receives times some $J_i$, the strength of
the connection, its input, call it $h$

lectures Page 1
