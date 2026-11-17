# 2026-07-07_Lecture 10 - 01_07 - page-03

> Gemini gemini-3.1-flash-lite transcription.

[diagram: two vectors $u_1$ and $u_2$ originating from the same point, with a dashed vector $u_2^\perp$ representing the component of $u_2$ orthogonal to $u_1$]

how look at
$$u_2^\perp = u_2 - u_1 \frac{(u_1, u_2)}{\|u_1\|^2} \sim e^{\lambda_2 t}$$

at FP, $l$ are $\lambda$

so $\frac{\log \|u_2^\perp\|}{t} \xrightarrow{t \to \infty} \lambda_2$

[diagram: arrow from "DF" pointing to the right, with a curved arrow from "DF" pointing to the $A(t)$ term below]

recap, You got $\dot{x} = F(x) \longrightarrow x(t) = \varphi(t; x_0) \longrightarrow A(t)$
$$v_0 \to \dot{v} = A(t)v$$
$$\|v(t)\| \sim e^{l_1 t} \to l_1(x_0, v_0) \text{ the largest } l$$
how take $v_0, v_0^\perp$ find $v_1^\perp$ with graham schmidt,
$$\frac{\log \|v_1^\perp\|}{t} \xrightarrow{t} l_2(x_0, t)$$
continue to find the rest

graham schmidt -

You got $\vec{v}_1, \dots, \vec{v}_n$, we want to find $\vec{w}_1, \dots, \vec{w}_n$ that are orthogonal
$\vec{w}_1 = \vec{v}_1$
[diagram: vector $v_2$ with a vector $w_2$ pointing perpendicular to $w_1$]
how
$$\vec{w}_2 = \vec{v}_2 - \vec{w}_1 \frac{(\vec{w}_1, \vec{v}_2)}{\|\vec{w}_1\|^2}$$
$$\vec{w}_3 = \vec{v}_3 - \vec{w}_1 \frac{(\vec{w}_1, \vec{v}_3)}{\|\vec{w}_1\|^2} - \vec{w}_2 \frac{(\vec{w}_2, \vec{v}_3)}{\|\vec{w}_2\|^2}$$
$$\vdots$$
$$\vec{w}_n$$

why are there $l_1, \dots, l_n$? why not more or less
we have $A(t) = DF(x(t)) \cdot v$ and $\dot{v} = A(t) \cdot v$
the length of $v$ is $\|v(t)\| = (v(t), v(t))$
$$v(t) \sim \underbrace{e^{\int A(t) dt}}_{B(t)} v(0)$$
$$v(t) = B(t) \cdot v(0)$$

lectures Page 3
