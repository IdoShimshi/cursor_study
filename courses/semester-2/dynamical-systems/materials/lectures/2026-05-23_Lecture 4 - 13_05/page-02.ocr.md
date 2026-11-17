# 2026-05-23_Lecture 4 - 13_05 - page-02

> Gemini gemini-2.5-flash transcription.

$$h(t) = \sum_{\text{neurons}} r_i J_i$$

$$\tau \dot{r} = -r + g(h)$$
some time constant

$g(h)$ is usually some monotonic inc func
e.g. $g(h) = \frac{1}{1 + e^{-\beta h}}$
[diagram: increasing sigmoid curve]

if we have 1 neuron that is connected to itself
[diagram: J with a self-loop]

$$\epsilon \dot{r} = -r + g(Jr) = -r + \frac{1}{1 + e^{-\beta Jr}}$$

more generically, it can get some hext from others
[diagram: J with a self-loop and an incoming arrow labeled 'hext']
$$\epsilon \dot{r} = -r + g(Jr + h_{\text{ext}}) = -r + \frac{1}{1 + e^{-\beta (Jr + h_{\text{ext}})}}$$
hext here controls where the sigmoid curve happens
[diagram: sigmoid curve with horizontal shift]

it has the linear $-r$ component
and a sigmoid one
[diagram: phase portrait showing a linear line, a sigmoid curve, and their intersections on an r-axis]

Without hext, stable point at 0, so it dies out
With hext, sigmoid is shifted and the stable point is positive
we should analyze the phase portrait to understand the interesting region

generalized in 2D
$$\begin{cases} \dot{x} = -x \\ \dot{y} = -2y + 2x^3 \end{cases}$$
[diagram: 2D phase portrait with x and y axes, nullclines $x=0$ (y-axis) and $y=x^3$, and flow arrows]
$y=0$ (label for the curve)
$x=0$ (label for the y-axis)

first, find fixed points
find lines where something changes about the flow, a generalization of a FP in 1D
is a line in 2D, where one component is 0, called nullcline
any point on $x=0$ line, the flow will be vertical
look at $\dot{y}$ where $x$ is $0$, so $y = x^3$, any point on this line will go horizontal,
only in x direction
now look at the direction of flow, on $x=0$, its $\dot{y} = -2y$, so it'll go towards $(0,0)$
on $y=0$, $\dot{x} = -x$, so it'll go towards $x=0$

lectures Page 2
