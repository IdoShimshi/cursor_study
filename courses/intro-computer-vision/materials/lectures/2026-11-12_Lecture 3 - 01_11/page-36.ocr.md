# 2026-11-12_Lecture 3 - 01_11 - page-36

> Gemini gemini-3.5-flash-lite transcription.

Camera motion model

$$\begin{bmatrix} X_1' \\ X_2' \\ X_3' \end{bmatrix} = R \begin{bmatrix} X_1 \\ X_2 \\ X_3 \end{bmatrix} + t$$

$R \in \mathbb{R}^{3 \times 3}$ rotation matrix
$R^T R = I, \ \det(R) = 1$
$\Rightarrow R^{-1} = R^T$
$t \in \mathbb{R}^3$ translation vector

$$\begin{bmatrix} X_1'/X_3' \\ X_2'/X_3' \\ 1 \end{bmatrix} = \begin{bmatrix} X_1' \\ X_2' \\ X_3' \end{bmatrix} = [R \ t] \begin{bmatrix} X_1 \\ X_2 \\ X_3 \\ 1 \end{bmatrix}$$
*[diagram: Camera coordinate system and Global coordinate system with projection rays]*

The rows of $R$ encodes the $x'$ axis, $y'$ axis and $z'$ axis of the local coordinate system, as expressed in the global coordinate system

(B) Camera rotation $\rightarrow$ homography

$$Q = RP + \cancel{t}$$

$p, q$ are perspective projections of $P, Q$

$$p = \frac{f}{Z} P \Rightarrow P = \frac{Z}{f} p$$
$$q = \frac{f}{Z'} Q \Rightarrow Q = \frac{Z'}{f} q$$

Substitute in $Q = RP$

$$\frac{Z'}{f} q = \frac{Z}{f} Rp$$
$$\Rightarrow q = \frac{Z}{Z'} Rp$$
$$\Rightarrow q \propto Rp$$

(need to verify that the scaling is free of 3D information)

*[diagram: Rotation around the focal center (no translation) showing image 1 and image 2]*

$$P = \begin{bmatrix} X \\ Y \\ Z \end{bmatrix} \ Q = \begin{bmatrix} X' \\ Y' \\ Z' \end{bmatrix}$$

lectures Page 36
