# 2026-11-12_Lecture 3 - 01_11 - page-22

> Gemini gemini-3.5-flash-lite transcription.

# Projective plane $\mathbb{P}^2$

* The projective space $\mathbb{P}^2$ consists of all the elements that can be represented by vectors in $\mathbb{R}^3 - (0,0,0)^T$
* A point is identified with a ray through the origin, so $\boldsymbol{p}$ and $\alpha \boldsymbol{p}$ for $\alpha \neq 0$ represent the same point
* Projective geometry is a geometry of rays

[diagram: A 3D coordinate system showing the origin, a plane $z=1$, and rays passing through the origin intersecting both the plane and representing points in the projective space]

---

# Homogeneous representation of lines

A line and a point in $\mathbb{P}^2$ have the same algebraic representation

* A line in $\mathbb{R}^2$ is represented as
  $$ax + by + c = 0$$
  where $(a, b, c)^T \neq (0, 0, 0)^T$
* $\boldsymbol{l} = (a, b, c)^T$ is a representation of the line
* The correspondence between lines and vectors is not one-to-one
* $ax + by + c = 0$ and $(ka)x + (kb)y + (kc) = 0$ are the same lines for any $k \neq 0$
* Thus, $(a, b, c)^T$ and $k(a, b, c)^T$, $k \neq 0$, represents the same line
* $(0, 0, 0)^T$ does not correspond to any line and therefore is excluded
* A point $\boldsymbol{x} = (x_1, x_2, x_3)^T \in \mathbb{P}^2$ lies on the line $\boldsymbol{l} = (a, b, c)^T \in \mathbb{P}^2$
  $$\iff$$
  $$\boldsymbol{x}^T \boldsymbol{l} = 0$$
