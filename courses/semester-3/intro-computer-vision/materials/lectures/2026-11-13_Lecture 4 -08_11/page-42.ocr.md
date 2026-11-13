# 2026-11-13_Lecture 4 -08_11 - page-42

> Gemini gemini-3.5-flash-lite transcription.

# Epipolar geometry - the Fundamental matrix

The uncalibrated case

* The mapping between the image plane (Euclidean space) and the real image (pixels), is given by...
* Calibration matrix $K$
* The relation between the calibrated ($\tilde{p}, \tilde{q}$) and the uncalibrated coordinates ($p, q$) is given by

$$p = K\tilde{p}, \ q = K\tilde{q}$$

$$\Rightarrow 0 = \tilde{q}^T E\tilde{p} = q^T K^{-T} E K^{-1} p$$

* Let

$$F = K^{-T} E K^{-1}$$

* Then

$$q^T F p = 0$$

* $F$ is called the Fundamental matrix

---
lectures Page 42
