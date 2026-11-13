# 2026-07-07_Lecture 10 - 01_07 - page-02

> Gemini gemini-3.5-flash transcription.

$$\underbrace{\dots}_{A(t)}$$

if $\|\vec{v}(t)\| \underset{t \to \infty}{\longrightarrow} e^{\lambda t}$

$\lambda(x_0, \vec{v}_0) = \frac{\log \|\vec{v}(t)\|}{t} \quad (t \to \infty)$

### simple example

$$\dot{x} = F(x), \quad \text{FP} - x^*$$
$$F(x^*) = 0$$

$$x = x^* + u \quad \text{we can linearize at } x^*$$
$$\dot{u} = F(x^* + u) = \underbrace{DF(x^*)}_{A} \cdot u = Au$$

$A$ has:
$$Av_1 = \lambda_1 v_1$$
$$Av_2 = \lambda_2 v_2$$

so
$$u(0) = c_1 v_1 + c_2 v_2$$
$$u(t) = c_1 v_1 e^{\lambda_1 t} + c_2 v_2 e^{\lambda_2 t}, \quad \text{if } \lambda_1 > \lambda_2, \quad \|u\| \sim e^{\lambda_1 t}$$

so
$\lambda(x^*, v_1) = \lambda_1$, $\lambda(x^*, v_2) = \lambda_2$ \qquad in general case, there will be only real part of $\lambda$

---

lets say we dont know how to find $v_1, \lambda_1$ and $v_2, \lambda_2$, what can we do
do the same as before, without knowing these (since it is true for some values)

$$u(0) = c_1 v_1 + c_2 v_2$$
$$u(t) = c_1 v_1 e^{\lambda_1 t} + c_2 v_2 e^{\lambda_2 t}$$

look at $\frac{\log \|\vec{u}(t)\|}{t}$ and look when $t \to \infty$ this will equal $\lambda_1$, the largest $\lambda(x^*, \vec{u}_0)$

---

how do we find $\lambda_2$ ?
take 2 diviations
$$\vec{u}^1(0) = c_1^1 v_1 + c_2^1 v_2 \qquad \vec{u}^2(0) = c_1^2 v_1 + c_2^2 v_2$$
$$\vec{u}^1(t) = c_1^1 v_1 e^{\lambda_1 t} + c_2^1 v_2 e^{\lambda_2 t} \qquad \vec{u}^2(t) = c_1^2 v_1 e^{\lambda_1 t} + c_2^2 v_2 e^{\lambda_2 t}$$

both are still dominated by $\lambda_1$, if you go to large $t$, they go to it
they will rotate to point in similar direction

at $t=0$
[diagram: two vectors $u^1$ and $u^2$ pointing in different directions]

at $t \gg 0$
[diagram: two vectors $u^1$ and $u^2$ pointing in almost the same direction]
