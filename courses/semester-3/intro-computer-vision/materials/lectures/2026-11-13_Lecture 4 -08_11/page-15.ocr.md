# 2026-11-13_Lecture 4 -08_11 - page-15

> Gemini gemini-3.6-flash transcription.

Summary

#(A) Planar scene $\rightarrow$ homography

* A plane $aX + bY + cZ = d$
* In vector notation $\boldsymbol{n}^T \boldsymbol{P} = d$
* $\boldsymbol{Q} = \boldsymbol{R}\boldsymbol{P} + \boldsymbol{t}$
* $\frac{\boldsymbol{n}^T \boldsymbol{P}}{d} = 1$, so $\boldsymbol{Q} = \boldsymbol{R}\boldsymbol{P} + \boldsymbol{t} \frac{\boldsymbol{n}^T \boldsymbol{P}}{d}$
* Rearrange, $\boldsymbol{Q} = \left(R + \frac{1}{d} \boldsymbol{t} \boldsymbol{n}^T \right) \boldsymbol{P}$
* Project, $\boldsymbol{q} \propto \left(R + \frac{1}{d} \boldsymbol{t} \boldsymbol{n}^T \right) \boldsymbol{p}$
* So $\boldsymbol{q} \propto H\boldsymbol{p}$ , with $H = R + \frac{1}{d} \boldsymbol{t} \boldsymbol{n}^T$

[diagram: Two camera views (image 1 with point P and image 2 with point Q, related by rotation R and translation t) observing points X on a planar surface A.]
