# 2026-05-12_Lecture 2 - 29_04 - page-03

> Gemini gemini-2.5-flash transcription.

$f = -KX - b\dot{X}$
$m\ddot{X} = -KX - b\dot{X}$
$\begin{cases} \dot{X} = V \\ \dot{V} = -\frac{KX}{m} - \frac{bV}{m} \end{cases}$
$E = \frac{1}{2}mV^2 + \frac{1}{2}KX^2$
$\dot{E} = mV\dot{V} + KX\dot{X} = mV(-\frac{KX}{m} - \frac{bV}{m}) + KXV = -bV^2 \le 0$

it will never reach the origin again.
this trajectory is called Lyapunov stable
Stable fixed Point = trajectory will approach it
[diagram: spiral trajectory in X-V phase space, approaching the origin]

Fixed Points
Periodic orbits
stable focus
unstable focus
Phase Portraits
Orbits
vector field
flow
$\dot{\vec{X}} = f(\vec{X})$

Pendulum
[diagram: simple pendulum with mass m, length l, angle $\theta$, and forces mg and F=-mgsin$\theta$]
$s = l\Delta\theta$
$\dot{X} = \lim_{\Delta t \to 0} \frac{l\Delta\theta}{\Delta t} = l\dot{\theta}$
$\ddot{X} = \frac{d\dot{X}}{dt} = \frac{d(l\dot{\theta})}{dt} = l\frac{d\dot{\theta}}{dt} = l\ddot{\theta}$
$F = ma = m\ddot{X} = ml\ddot{\theta}$
$ml\ddot{\theta} = -mg\sin\theta$

lectures Page 3
