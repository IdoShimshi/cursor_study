# 2026-11-13_Lecture 4 -08_11 - page-23

> Gemini gemini-2.5-flash transcription.

The role of the calibration matrix $K$ of a camera $C$

$$
K = \begin{pmatrix}
\alpha_x & \gamma & x_0 \\
0 & \alpha_y & y_0 \\
0 & 0 & 1
\end{pmatrix}
$$

* $K$ transforms from the image plane (calibrated) to the real image (pixels)
* $K^{-1}$ maps from the real image (pixels) to the image plane
* Calibration parameters are available in EXIF tags

lectures Page 23
