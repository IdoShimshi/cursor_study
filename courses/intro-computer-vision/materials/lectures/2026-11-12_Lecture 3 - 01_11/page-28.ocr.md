# 2026-11-12_Lecture 3 - 01_11 - page-28

> Gemini gemini-3.5-flash-lite transcription.

# Vanishing lines and vanishing points

* Any set of parallel lines on the plane define **a vanishing point**

* The union of all vanishing points from lines **on the same plane** is the vanishing line

* For the **ground plane**, this is called the **horizon**

[diagram: Two images showing perspective projection. Top image shows parallel grid lines converging to two vanishing points $v_1$ and $v_2$ on a dashed horizontal line. Bottom image shows two cubes in perspective with lines extending to vanishing points on the horizon.]

---

# Projective transformation = Projectivity = Homography

A projectivity is an invertible mapping from points in $\mathbb{P}^2$ (homogeneous $3$-vectors) to points in $\mathbb{P}^2$ that maps lines to lines.

<u>Def.</u> A <u>projective transformation</u> is an invertible mapping $h: \mathbb{P}^2 \to \mathbb{P}^2$ such that three points $x_1, x_2$ and $x_3$ lie on the same line if and only if $h(x_1), h(x_2)$ and $h(x_3)$ are on the same line

---
<sub>lectures Page 28</sub>
