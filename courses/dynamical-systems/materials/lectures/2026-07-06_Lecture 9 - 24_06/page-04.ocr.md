# 2026-07-06_Lecture 9 - 24_06 - page-04

> Gemini gemini-3.5-flash transcription.

... attractor is not sensitive

a chaotic system is when we have sensitivity on the attractor

[diagram: 3D sketch of the Lorenz attractor with two lobes containing points $p^-$ and $p^+$]

in lorenz the the attractor has 2 sides
and flows move between them.
we cannot know how long they stay in each.
so take $X_0, Y_0$ in one, after some time, one
will jump to the other side, while the other one
doesnt

looking at just $x$ over time

[diagram: Plot of $x$ over time $t$ showing two nearby trajectories diverging over time]

another classical example - rossler attractor

$$\dot{x} = -y - z$$
$$\dot{y} = x + ay$$
$$\dot{z} = b + z(x - )$$

[diagram: 3D trajectory of the Rössler attractor spiraling outwards and escaping upwards before returning]

so it spirals inwards, then escapes and comes back to the spiral
we dont know how many cycles around the spiral it will do before escaping

---

For $\dot{x} = F(x)$ \qquad FP $x^*$
we can linearize if $y$ is close to $x^*$
$$x(t) = x^* + y(t)$$
$$\dot{y} = DF(x^*) \cdot y$$

we can do this for any point, not just FP

$$x(t) = \varphi(t, x_0)$$
$$x(t) + \delta x(t) = \varphi(t, x_0 + \delta x) \quad , \quad \text{in 1D} \quad \dot{x} = F(x)$$

[diagram: Plot of two trajectories $x(t)$ and $x(t) + \delta x(t)$ over time $t$, showing the deviation $\delta x(t)$ between them]

so $\delta x(t)$ is the deviation

$$\dot{(x + \delta x)} = F(x + \delta x)$$
$$\cancel{\dot{x}} + \dot{\delta x} = \cancel{F(x(t))} + \delta x \cdot F'(x(t))$$

$$\dot{\delta x} = \underbrace{F'(x(t))}_{\alpha(t)} \cdot \delta x(t) = \alpha(t) \cdot \delta x(t) \qquad \text{this is a linear system}$$
$$\qquad\qquad\qquad\qquad\qquad\qquad\text{this assumes } \delta x(0) \text{ is very small}$$

while it is a linear system, which should be simple, you need to solve the full trajectory in order
to [illegible]
