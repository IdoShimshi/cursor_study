# 2026-06-05_Lecture 6 - 03_06 - page-01

> Gemini gemini-3.1-flash-lite transcription.

Lecture 6 - 03/06
Thursday, June 4, 2026 2:56 PM

last time we saw -
$$\begin{cases} \dot{x} = x(a-by) \\ \dot{y} = y(-c+ex) \end{cases}$$
$$\frac{\dot{y}}{\dot{x}} = \frac{y(-c+ex)}{x(a-by)}$$
$$\dot{y} \left(\frac{a}{y} - b\right) = \dot{x} \left(-\frac{c}{x} + e\right)$$
integrating both sides give us
$$K = (ex - c \ln x) + (by - a \ln y) = f(x, y) = \text{const}$$
[diagram: a graph of a function $f(x)$ with a minimum at $x = c/e$, and a phase portrait showing a closed orbit around a fixed point]

$$m\ddot{x} = F(x)$$
$$\begin{cases} \dot{x} = v \\ \dot{v} = \frac{1}{m} F(x) \end{cases}$$
$$m\ddot{x} = F(x)$$
$$m\dot{x}\ddot{x} = \dot{x}F(x)$$
$$m\dot{x}\ddot{x} - \dot{x}F(x) = 0$$
$$\frac{d}{dt} \left[ \frac{1}{2} m\dot{x}^2 - \int_{x_0}^x F(s) ds \right] = 0$$
so this is conserved over time, we call it energy
$$E = \frac{1}{2} m\dot{x}^2 - \int_{x_0}^x F(s) ds = \frac{1}{2} m\dot{x}^2 + V(x)$$
notice $V(x)$ depends on $x_0$
$$V(x) = - \int_{x_0}^x F(s) ds$$

[diagram: a box containing a derivation and a graph. The derivation is:
$$\lim_{\Delta t \to 0} \frac{\int_{x_0}^{x(t+\Delta t)} F(s) ds - \int_{x_0}^{x(t)} F(s) ds}{\Delta t} = \lim_{\Delta t \to 0} \frac{\int_{x(t)}^{x(t+\Delta t)} F(s) ds}{\Delta t}$$
Below this is a graph of $F(s)$ vs $s$ with a shaded area between $x(t)$ and $x(t+\Delta t)$.
Text notes: "for $\Delta t$ small enough, this will be $F(x(t)) \cdot \dot{x} \cdot \Delta t$", "the value at $x(t)$", "the slope there", and "for our case, $\dot{x}F(x) = \int_{x_0}^x F(s) ds$"]

$$\begin{cases} \dot{x} = y &= f(x, y) \\ \dot{y} = x - x^3 &= g(x, y) \end{cases}$$
FP: $y=0, x=0, \pm 1$
