# 2026-05-23_Lecture 4 - 13_05 - page-03

> Gemini gemini-3.1-flash-lite transcription.

how look at the direction of flow, at $x=0$, its $\dot{y}=-2y$, so it'll go towards $(0,0)$
oh $\dot{y}=0$, $\dot{x}=-x$, so it'll go towards $x=0$

how we can divide the phase portrait into regions

[diagram: A Cartesian coordinate system with a saddle point at the origin. Four regions $R_1, R_2, R_3, R_4$ are defined by the axes. A vertical green line labeled $\dot{x}=0$ and a curved blue line labeled $\dot{y}=0$ are shown. Trajectories are drawn with arrows indicating flow, including points labeled A, B, and C.]

look at A, by continuity, we can guess it'll go diagonal towards $(0,0)$.
intuition - why is this true? A couldnt go to the right
if it did, there would be a point where it goes between $\dot{x}>0$
it must be $\downarrow$, but thats $\dot{x}=0$.

looking at $R_2$, flow should be $\downarrow$, since there is a line pointing away from the region on $\dot{y}=0$
some points (B) can go directly to $(0,0)$, and some (C) can cross to $R_3$.
$R_3$ is mirror of $R_1$, $R_4$ is mirror of $R_2$ (maybe B is fake and there only C, he wasnt sure)

another example
$$\begin{cases} \dot{x} = -x+y \\ \dot{y} = xy-1 \end{cases}$$

[diagram: A phase portrait with two fixed points at $(-1, -1)$ and $(1, 1)$. Nullclines are drawn: a straight line $y=x$ labeled $\dot{x}=0$ and a hyperbola $y=1/x$ labeled $\dot{y}=0$. Various trajectories and arrows indicate the flow in regions $R_1$ through $R_6$.]

1) find FP, $(-1, -1), (1, 1)$
2) look for nullcline, $\dot{x}=0 \Rightarrow y=x$, points go vertical
$\dot{y}=0 \Rightarrow y=\frac{1}{x}$, points go horizontal

3) put arrows, for $\dot{x}=0, y=x$, so $\dot{y}=x^2-1$, so when $x>1, \dot{y}$ is $+$
for $\dot{y}=0, y=\frac{1}{x}$, so $\dot{x}=-x+\frac{1}{x}$; if $x$ big, its $-x$, so towards 0
if $x$ small, its $\frac{1}{x}$, so away
notice it isnt symmetrical, on the bottom there's some rotation thing, but not on top

4) look at regions, $R_1 \to$ either go up to $R_2$ or down to $R_6$, by continuity, there's
some place that goes directly to FP $(1,1)$

$R_2 \to$ only goes up and right to $(\infty, \infty)$

$R_3 \to$ can cross to $R_1$, can cross to $R_6$ or go to FP $(1,1)$

$R_6 \to$ must go to $R_5$

there is some rotation... $R_1 \to R_6 \to R_3 \to R_1$

lectures Page 3
