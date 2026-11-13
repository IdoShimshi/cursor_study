# Dynamical Systems - Practice Exam

Here is a practice exam composed of questions taken directly from actual university final exams on Dynamical Systems. They heavily align with the topics of your course: non-linear equilibria, ruling out or proving the existence of limit cycles (Poincaré-Bendixson), and 3D dissipative systems.

---

### Question 1: Non-linear Equilibria & Stability
*(Source: [University of Utah - Differential Equations 2280 Final Exam, Spring 2016](http://www.math.utah.edu/~gustafso/s2019/2280/exams/final/2280final-S2016-solutions.pdf))*

Consider the nonlinear dynamical system:
$$
\dot{x} = 14x - 2x^2 - xy
$$
$$
\dot{y} = 16y - 2y^2 - xy
$$

**a)** Find the equilibrium points for the nonlinear system.
**b)** Classify the linearization at equilibrium point $(4, 6)$ as a node, spiral, center, or saddle.
**c)** What classification can be deduced for equilibrium $(4, 6)$ of this nonlinear system, according to the general nonlinear stability theory?

---

### Question 2: Ruling Out Closed Orbits
*(Source: [University of Pittsburgh - Math 1280 Final Exam, Spring 2016, Problem 5](https://sites.pitt.edu/~evt3/a/1280/2016_Spring/Exams/fe(1280)_2016_spring_sln.pdf))*

Consider the system:
$$
\dot{x} = -x + y^2
$$
$$
\dot{y} = y(1 + 2x)
$$

**a)** Use index theory to show that the system has no closed orbits.
**b)** Use a method different from index theory and Dulac’s criterion to show that the system has no closed orbits.
**c)** Use Dulac’s criterion to show that the system has no closed orbits. You may use the Dulac’s function $g(x, y) = \frac{1}{y}$.

---

### Question 3: Trapping Regions & Poincaré-Bendixson Theorem
*(Source: [University of Pittsburgh - Math 1280 Final Exam, Spring 2016, Problem 6](https://sites.pitt.edu/~evt3/a/1280/2016_Spring/Exams/fe(1280)_2016_spring_sln.pdf))*

Consider the system:
$$
\dot{x} = 4x - y - x(x^2 + 2y^2)
$$
$$
\dot{y} = x + 4y - y(4x^2 + y^2)
$$

**a)** Classify the fixed point at the origin.
**b)** Switch to polar coordinates and write an equation for $\dot{r}$.
**c)** Determine the circle of maximum radius $r_1$, centered at the origin such that all trajectories have a radially outward component on it.
**d)** Determine the circle of minimum radius $r_2$, centered at the origin such that all trajectories have a radially inward component on it.
**e)** Assume that there are no fixed points in the region $r_1 \le r \le r_2$. Then prove that the system has a limit cycle somewhere in the trapping region $r_1 \le r \le r_2$.

---

### Question 4: 3D Systems & Dissipation
*(Source: [University of Pittsburgh - Math 1280 Final Exam, Spring 2016, Problem 9](https://sites.pitt.edu/~evt3/a/1280/2016_Spring/Exams/fe(1280)_2016_spring_sln.pdf))*

Show that the system:
$$
\dot{x} = 2xy^2 + 4xyz - y^2z
$$
$$
\dot{y} = -x^4y - 2y - y^3 + 2yz^2
$$
$$
\dot{z} = x^2 + y^3 - yz^2 - z^3
$$
is dissipative.
