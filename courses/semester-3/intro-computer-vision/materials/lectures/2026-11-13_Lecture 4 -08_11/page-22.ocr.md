# 2026-11-13_Lecture 4 -08_11 - page-22

> Gemini gemini-3-flash-preview transcription.

# Calibration matrix $K$

* A $3 \times 3$ upper triangular matrix, $K$, that captures (linear) internal calibration parameters
$$K = \begin{pmatrix} \alpha_x & \gamma & x_0 \\ 0 & \alpha_y & y_0 \\ 0 & 0 & 1 \end{pmatrix}$$

* Parameters:
    * $(x_0, y_0)$ - image center (in pixel dimensions)
    * $(\alpha_x, \alpha_y) = (f m_x, f m_y)$
    * $f$ - focal length
    * [diagram: blue rectangle] $(m_x, m_y)$ – number of pixels per unit distance in $x$ and $y$ directions
    * [diagram: blue parallelogram] $\gamma$ – skew (for tilted pixels, typically 0)
* Radial distortions are treated separately
* Both linear and radial calibration parameters are available in Exif tags

lectures Page 22
