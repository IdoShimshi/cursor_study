# Dynamical Systems Study Guide: Mock Exam & Practice

This file contains a collection of practice problems gathered from various academic sources to help you prepare for your final exam.

---

### **Problem 1**
Consider the linear system $\dot{\mathbf{x}} = A\mathbf{x}$ with:
$$ A = \begin{pmatrix} \mu & 1 \\ -1 & \mu \end{pmatrix} $$
1. Find the eigenvalues and eigenvectors of $A$ in terms of the parameter $\mu$.
2. Classify the fixed point at the origin for $\mu < 0$, $\mu = 0$, and $\mu > 0$.
3. Sketch the phase portrait for each of the three cases above.

### **Problem 2**
Consider the system $\dot{x} = r + x^2$.
1. Find the fixed points and determine their stability as a function of the parameter $r$.
2. Identify the bifurcation value $r_c$ and the type of bifurcation that occurs.
3. Draw the bifurcation diagram (fixed points $x^*$ vs. $r$), using solid lines for stable points and dashed lines for unstable ones.

### **Problem 3**
Consider the system:
$$ \begin{cases} \dot{x} = x(1 - x - y) \\ \dot{y} = y(a - x - y) \end{cases} $$
where $a > 0$ is a constant.
1. Find all fixed points in the first quadrant ($x \ge 0, y \ge 0$).
2. Sketch the nullclines for the case $a > 1$.
3. Determine the stability of the fixed point(s) on the axes using the Jacobian matrix.
4. Show that if $a \neq 1$, there is no fixed point where both species coexist ($x > 0, y > 0$).

### **Problem 4**
Consider the system in polar coordinates:
$$ \begin{cases} \dot{r} = r(1 - r^2)(4 - r^2) \\ \dot{\theta} = 1 \end{cases} $$
1. Identify all periodic orbits (limit cycles) of the system.
2. Determine the stability of each limit cycle by analyzing the sign of $\dot{r}$ in the neighboring regions.
3. Use the **Poincaré-Bendixson Theorem** to prove that any trajectory starting in the region $1 < r < 2$ must approach a limit cycle.

### **Problem 5**
Consider the system:
$$ \begin{cases} \dot{x} = y \\ \dot{y} = -x + x^3 \end{cases} $$
1. Show that this is a **Hamiltonian system** and find the Hamiltonian function $H(x, y)$ such that $H(0,0) = 0$.
2. Use the Hamiltonian to show that the origin is a stable (but not asymptotically stable) fixed point.
3. Now consider a modified system with friction: $\dot{y} = -x + x^3 - \gamma y$ where $\gamma > 0$. Show that $V(x, y) = H(x, y)$ is a **Lyapunov function** for the origin and determine if the origin becomes asymptotically stable.

### **Problem 6**
The Lorenz equations are given by:
$$ \begin{cases} \dot{x} = \sigma(y - x) \\ \dot{y} = rx - y - xz \\ \dot{z} = xy - bz \end{cases} $$
1. Show that the volume of a region in phase space contracts over time at a constant rate. (Hint: Compute the divergence of the vector field).
2. For $r < 1$, the origin is the only fixed point. Show that it is globally stable using the Lyapunov function $V = \frac{1}{\sigma}x^2 + y^2 + z^2$.
3. Briefly explain what is meant by **"Sensitive Dependence on Initial Conditions"** and how it relates to the Lyapunov exponents of the Lorenz attractor.

### **Problem 7**
Two species of bacteria, $x$ and $y$, are growing in a lab culture. 

1. Species $x$ grows logistically with growth rate $r_x$ and carrying capacity $K_x$ when alone.
2. Species $y$ grows logistically with growth rate $r_y$ and carrying capacity $K_y$ when alone.
3. They compete for the same space. This is modeled by subtracting a term proportional to the other's population from each species' per-capita growth rate (use competition coefficients $\alpha$ for species $x$ being inhibited by $y$, and $\beta$ for species $y$ being inhibited by $x$).
4. Additionally, species $y$ produces a chemical that is toxic specifically to species $x$. This is modeled by subtracting an additional term proportional to the population of $y$ from the per-capita growth rate of $x$ (let this proportionality constant be $\gamma$).

**(a)** Construct a system of two differential equations $\dot{x} = f(x,y)$ and $\dot{y} = g(x,y)$ that models this situation.
**(b)** Find all fixed points on the axes (where at least one species is zero).
**(c)** Determine the stability of the fixed point $(K_x, 0)$ using the Jacobian matrix. How does the presence of species $y$ and its toxin affect whether $y$ can "invade" a culture originally dominated by $x$?
**(d)** Explain qualitatively what happens to the coexistence of the species as the toxin potency $\gamma$ is increased to a very large value.

### **Problem 8**
Consider the following continuous-time dynamical system given in polar coordinates:
$$ \begin{cases} \dot{r} = r(1-r) \\ \dot{\theta} = 1 \end{cases} $$
Let $\Sigma$ be a section defined by the positive x-axis (where $\theta = 0$). Suppose a trajectory starts on $\Sigma$ at an initial radial distance $r_0 > 0$.

**(a)** By integrating the differential equations exactly, find an explicit closed-form expression for the return map $r_{n+1} = P(r_n)$, which maps the radial position of the trajectory after one full rotation back to $\Sigma$.
**(b)** Find all fixed points of your discrete map $P(r)$.
**(c)** Calculate the derivative $P'(r)$ at the positive fixed point to determine its discrete stability. How does this finding relate to the continuous-time dynamics of the original system?

### **Problem 9**
Consider the nonlinear system:
$$ \begin{cases} \dot{x} = x - y - x^3 \\ \dot{y} = x + y - y^3 \end{cases} $$

**(a)** Rewrite the system in polar coordinates $(r, \theta)$. (Hint: use $r\dot{r} = x\dot{x} + y\dot{y}$ and keep trigonometric functions in the $\dot{r}$ equation).
**(b)** Find two constant radii, $R_{min}$ and $R_{max}$ (where $0 < R_{min} < R_{max}$), such that all trajectories must eventually enter the annular region defined by $R_{min} \le r \le R_{max}$ and can never leave it. 
**(c)** Based on your finding in part (b), what can you conclusively state about the long-term behavior of a trajectory starting at $x(0)=2, y(0)=2$?

### **Problem 10**
Consider the following competing-species model for two populations $x(t) \ge 0$ and $y(t) \ge 0$:
$$ \begin{cases} \dot{x} = x(2 - x - y) \\ \dot{y} = y(3 - 2x - y) \end{cases} $$

**(a)** Determine all fixed points of the system in the region $x \ge 0, y \ge 0$.
**(b)** Compute the Jacobian matrix at each fixed point and determine its topological index (e.g., saddle, node, spiral). 
**(c)** Suppose you suspect there might be a periodic closed orbit somewhere in the first quadrant ($x>0, y>0$). Based on the indices calculated in part (b), which fixed point(s) must be enclosed by this hypothetical closed orbit?
**(d)** Now, multiply the vector field by the scalar function $g(x,y) = \frac{1}{xy}$. By analyzing the divergence of this new vector field, conclusively prove whether periodic closed orbits can or cannot exist anywhere in the first quadrant ($x>0, y>0$).
