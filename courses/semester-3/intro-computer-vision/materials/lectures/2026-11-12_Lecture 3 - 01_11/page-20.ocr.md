# 2026-11-12_Lecture 3 - 01_11 - page-20

> Gemini gemini-3.5-flash-lite transcription.

# Projective plane $\mathbb{P}^2$

* A **projective plane** is a geometric structure that extends the concept of the Euclidean plane
* In the **Euclidean plane**, two lines are typically intersect a single point, excluding parallel lines that do not intersect
* A projective plane can be considered as an ordinary plane equipped with additional points at infinity, **ideal points**, where parallel lines intersect
    * Given any two distinct points, there is exactly one line incident with both of them
    * Given any two distinct lines, there is exactly one point incident with both of them

---

# Homogeneous coordinates

* In projective geometry we use homogeneous coordinates
* The homogeneous coordinates of a point $\begin{pmatrix} x \\ y \end{pmatrix} \in \mathbb{R}^2$ are
$$\begin{pmatrix} \alpha x \\ \alpha y \\ \alpha \end{pmatrix} \in \mathbb{P}^2, \alpha \neq 0$$
* Example
$$\begin{pmatrix} 3 \\ 2 \\ 1 \end{pmatrix}, \begin{pmatrix} 6 \\ 4 \\ 2 \end{pmatrix}, \begin{pmatrix} 9 \\ 6 \\ 3 \end{pmatrix}, \dots \text{ are homogeneous coordinates of } \dots$$
$$\begin{pmatrix} 3 \\ 2 \end{pmatrix}$$

$$\begin{pmatrix} 3 \\ 2 \\ 1 \end{pmatrix}, \begin{pmatrix} 6 \\ 4 \\ 2 \end{pmatrix}, \begin{pmatrix} 9 \\ 6 \\ 3 \end{pmatrix}, \dots \text{ are the same element in } \mathbb{P}^2$$

[diagram: A 3D coordinate system showing a plane $z=1$ with a red dot representing the point $(3, 2, 1)^T$. Multiple dotted lines pass through the origin $(0,0,0)$ and intersect the line/ray corresponding to scalar multiples $\alpha$, illustrating that points on a single ray in $\mathbb{R}^3$ represent a single point in $\mathbb{P}^2$. Red text notes: "We add a dimension", "All points on a single ray are the same point", "Boil down to a single point in $\mathbb{R}^2$"]

---
lectures Page 20
