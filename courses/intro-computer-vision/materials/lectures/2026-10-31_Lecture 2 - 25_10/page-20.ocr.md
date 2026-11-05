# 2026-10-31_Lecture 2 - 25_10 - page-20

> Gemini gemini-2.5-flash transcription.

# Image Pyramid

Low resolution
[diagram: An arrow points upwards from "High resolution" to "Low resolution". Along the arrow, there is a stack of images of hot air balloons, decreasing in size from bottom to top, illustrating an image pyramid.]

Does not consume much space
For an $N \times M$ image:
$NM + \frac{1}{4} NM + \frac{1}{16} NM + ...$
$= \Sigma_l (\frac{1}{4})^l NM$
$\leq 1 \frac{1}{3} NM$

High resolution

lectures Page 20
