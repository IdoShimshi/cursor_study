# 2026-11-12_Lecture 3 - 01_11 - page-16

> Gemini gemini-2.5-flash transcription.

# Geometry

* Geometry – Greek: earth measurement
* Geometry concerns with shape, size, relative positions, and properties of spaces
* Euclidean geometry:
    * Point, line, plane
    * Incidence – relation between lines and points
    * Preserved under rigid transformations
        * Angles, lengths, areas
        * Parallelism
        * Order, “between”

[diagram: two triangles, one translated and rotated from the other, with an arrow indicating the transformation]

# Euclidean geometry – rigid transformation

* Shapes, Lengths, angles, areas/volumes are preserved under a rigid transformation
* In 2D: (Rotation, 1 dof)
    $$
    \begin{pmatrix}
    \cos \theta & -\sin \theta \\
    \sin \theta & \cos \theta
    \end{pmatrix}
    \begin{pmatrix}
    x \\
    y
    \end{pmatrix}
    +
    \begin{pmatrix}
    t_x \\
    t_y
    \end{pmatrix}
    $$
* In 3D: (Rotation, 3 dof)
Rotation is represented by a $3 \times 3$ matrix $R$ with $R^T R = I$ and $\det(R) = 1$
    $$
    \begin{bmatrix}
    r_{11} & r_{12} & r_{13} \\
    r_{21} & r_{22} & r_{23} \\
    r_{31} & r_{32} & r_{33}
    \end{bmatrix}
    \begin{bmatrix}
    X \\
    Y \\
    Z
    \end{bmatrix}
    +
    \begin{bmatrix}
    t_x \\
    t_y \\
    t_z
    \end{bmatrix}
    $$

lectures Page 16
