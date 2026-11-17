# 2026-07-06_Lecture 9 - 24_06 - page-02

> Gemini gemini-3.5-flash transcription.

[diagram: two blobs representing a region $U$ with volume $V$ evolving over time to $\varphi(t, U)$ with volume $V(t)$]

for every point $\dot{\vec{x}} = \vec{F}(\vec{x})$
so the volume depends on the movement of the border
if it goes away, it expands, $V$ inc, if it goes inwards, it shrinks, $V$ dec

if the shape is $U$, its circumference is $\partial U$
take an area on the border $A$, it has $n$ normal and $F$ vector field (where it moves)

$$\dot{V} = \int_{\partial U} (\vec{F} \cdot \vec{n}) dA = \int_U (\nabla \cdot \vec{F}(\vec{x})) d\vec{x}$$

$$\frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \dots = \sum_i \frac{\partial F_i}{\partial x_i}$$

for 1D, 
[diagram: a line segment from A to B with an arrow pointing right]
it will be

$$\int_A^B \frac{\partial F(x)}{\partial x} dx = F(B) - F(A)$$

if $\sum_i \frac{\partial F_i}{\partial x_i} = c$ constant then $\dot{V} = cV$

***

### chaotic systems - Lorenz

$$\dot{x} = -\sigma x + \sigma y$$
$$\dot{y} = rx - y - xz \qquad \text{we assume params } > 0$$
$$\dot{z} = -b z + xy$$

$$\text{fix } \sigma = 10, \ b = \frac{8}{3}$$
$$r = 28$$

#### FPs
$$\dot{x} = 0, \quad y = x$$
$$\dot{z} = 0, \quad z = \frac{x^2}{b}$$
$$\dot{y} = 0, \quad (r-1)x - \frac{x^3}{b} = 0$$

$$x = 0 \implies (0,0,0)$$
$$x \neq 0 \implies x = \pm \sqrt{b(r-1)}, \text{ if } r > 1, \quad (\pm \sqrt{b(r-1)}, \pm \sqrt{b(r-1)}, r-1)$$
$$z = r-1$$

$$DF = \begin{pmatrix} -\sigma & \sigma & 0 \\ r-z & -1 & -x \\ y & x & -b \end{pmatrix}$$

$$DF(0,0,0) = \begin{pmatrix} -\sigma & \sigma & 0 \\ r & -1 & 0 \\ 0 & 0 & -b \end{pmatrix}$$

$$\lambda_s = -b < 0$$
$$\lambda_s = \quad < 0$$
$$\lambda_u = \frac{-(\sigma+1) + \sqrt{(\sigma+1)^2 + 4\sigma(r-1)}}{2}$$

for $r < 1$, $(0,0,0)$ is the only FP, and $\lambda_u < 0$. it is globally stable
for $r > 1$, $\lambda_u > 0$, which is unstable saddle point
