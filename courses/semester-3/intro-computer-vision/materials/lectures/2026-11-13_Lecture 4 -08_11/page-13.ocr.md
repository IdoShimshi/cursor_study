# 2026-11-13_Lecture 4 -08_11 - page-13

> Gemini gemini-3.6-flash transcription.

# Camera motion model
## external parameters

[diagram: Summary illustration showing two coordinate systems: "Camera coordinate system" on the left and "Global coordinate system" on the right, connected by projection lines to a 3D point.]

Global coordinate system
$$R = I, \boldsymbol{t} = \mathbf{0}$$

$$\begin{bmatrix} X_1' \\ X_2' \\ X_3' \end{bmatrix} = R \begin{bmatrix} X_1 \\ X_2 \\ X_3 \end{bmatrix} + \boldsymbol{t}$$

$R \in \mathbb{R}^{3 \times 3}$ rotation matrix
$R^T R = I, \ \det(R) = 1$
$\Rightarrow R^{-1} = R^T$
$\boldsymbol{t} \in \mathbb{R}^3$ translation vector

$$X_3' \begin{bmatrix} X_1' / X_3' \\ X_2' / X_3' \\ 1 \end{bmatrix} = \begin{bmatrix} X_1' \\ X_2' \\ X_3' \end{bmatrix} = [R \ \boldsymbol{t}] \begin{bmatrix} X_1 \\ X_2 \\ X_3 \\ 1 \end{bmatrix} \leftarrow \text{homogeneous coordinates of a 3D point}$$

$[R \ \boldsymbol{t}]_{3 \times 4}$ is called camera matrix

The rows of $R$ encodes the $x'$ axis, $y'$ axis and $z'$ axis of the local coordinate system, as expressed in the global coordinate system
