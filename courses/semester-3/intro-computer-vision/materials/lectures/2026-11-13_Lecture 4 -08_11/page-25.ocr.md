# 2026-11-13_Lecture 4 -08_11 - page-25

> Gemini gemini-3.5-flash-lite transcription.

# Camera matrix

## Calibrated camera

* Camera equations
  $$\lambda x = CX$$

* Def. A camera $C = K[R \;\mathbf{t}]$ is called calibrated if the inner parameters $K$ are known.
* We can multiply the camera equations from both sides by $K^{-1}$, yielding
  $$\lambda K^{-1}x = [R \;\mathbf{t}]X$$
  $$\lambda \tilde{x} = [R \;\mathbf{t}]X$$
  with $\tilde{x} = K^{-1}x$

* Def. The camera matrix $[R \;\mathbf{t}]$ is called normalized (calibrated) camera and $\tilde{x}$ are called the normalized (calibrated) image points

---
lectures Page 25
