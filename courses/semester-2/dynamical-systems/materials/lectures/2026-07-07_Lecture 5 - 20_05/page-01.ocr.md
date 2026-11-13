# 2026-07-07_Lecture 5 - 20_05 - page-01

> Gemini gemini-3.5-flash transcription.

Lecture 5 - 20/05
Thursday, May 21, 2026 1:53 PM

### ecological systems

Population and the rate of its change

$$\lim_{\Delta t \to 0} \frac{1}{\Delta t} \frac{\Delta X}{X} = \frac{\dot{X}}{X}$$

if food is abundant $\frac{\dot{x}}{x} = c$, $c > 0$, population will grow
since there are no infinite food sources so, $\frac{\dot{x}}{x} = c - x$
this can be written as $\dot{x} = cx - x^2 = rx(1 - \frac{x}{K})$
this is one dim, but we can grow to see how species interact

$$
\begin{cases}
\frac{\dot{x}}{x} = f(x,y) \\
\frac{\dot{y}}{y} = g(x,y)
\end{cases}
$$

### Lotka-Volterra systems

$$
\begin{cases}
\frac{\dot{x}}{x} = c_x + a_{xx} x + a_{xy} y \\
\frac{\dot{y}}{y} = c_y + a_{yx} x + a_{yy} y
\end{cases}
$$

### competing populations

$$
\begin{cases}
\frac{\dot{x}}{x} = K - x - ay \\
\frac{\dot{y}}{y} = L - bx - y
\end{cases}
$$

$K/L$ are the rate of growth just given the food while they represent the same constant food source they control the rate of growth given that food which changes per species

$$
\begin{cases}
\dot{x} = x(K - x - ay) \\
\dot{y} = y(L - bx - y)
\end{cases}
$$

Parms: $K, L, a, b > 0$

[diagram: Phase portrait showing the nullclines for competing populations, with axes $x$ and $y$, lines representing $K-x-ay=0$ and $L-bx-y=0$ intersecting at $(x^*, y^*)$, and vector field arrows indicating flow directions.]

looking for nullclines:

$$0 = \dot{x} = x(K - x - ay)$$

*   $x = 0$
*   $K - x - ay = 0 \implies y = -\frac{1}{a}x + \frac{K}{a}$ (vertical)

$$0 = \dot{y} = y(L - bx - y)$$

*   $y = 0$
*   $L - bx - y = 0 \implies y = -bx + L$ (horizontal)

FP - $(0,0), (K,0), (0,L), (x^*, y^*)$ where $x^*, y^* > 0$

$(x^*, y^*)$ can be negative depending on params or not exist

lets look at different cases

① $L > \frac{K}{a}, K > \frac{L}{b}$

$$\dot{\begin{pmatrix} x \\ y \end{pmatrix}} = F\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} f(x,y) \\ g(x,y) \end{pmatrix}$$

$$DF\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} \frac{\partial f(x,y)}{\partial x} & \frac{\partial f(x,y)}{\partial y} \\ \frac{\partial g(x,y)}{\partial x} & \frac{\partial g(x,y)}{\partial y} \end{pmatrix}_{/FP}$$

$$DF\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} (K-x-ay)-x & -ax \\ -by & (L-bx-y)-y \end{pmatrix}$$

---

**reminder**
$$q(\lambda) = \begin{vmatrix} a-\lambda & b \\ c & d-\lambda \end{vmatrix} = (a-\lambda)(d-\lambda) - bc = \lambda^2 - \lambda(a+d) + ad - bc$$
$\lambda_1 \cdot \lambda_2 = \det M$
$\lambda_1 + \lambda_2 = \text{trace } M$
we can determine $\lambda_1, \lambda_2$ sign just with det and trace
if $\det M > 0$ and $\text{tr } M < 0$
$\lambda_1, \lambda_2 < 0$ and FP is stable
