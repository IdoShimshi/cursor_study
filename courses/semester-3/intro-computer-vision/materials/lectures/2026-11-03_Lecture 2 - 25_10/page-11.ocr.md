# 2026-11-03_Lecture 2 - 25_10 - page-11

> Gemini gemini-3.5-flash-lite transcription.

# Image Pyramid

[diagram: A vertical stack of images of decreasing resolution showing hot air balloons, from high resolution at the bottom to low resolution at the top, alongside space complexity equations.]

Does not consume much space
For an $N \times M$ image:
$$NM + \frac{1}{4} NM + \frac{1}{16} NM + \dots$$
$$= \sum_{l} (\frac{1}{4})^l NM$$
$$\le 1 \frac{1}{3} NM$$

# The Gaussian Pyramid

[diagram: A flowchart showing the process of constructing a Gaussian pyramid with images of hot air balloons at different levels ($G_0$ to $G_4$), using blur and down-sample operations indicated by red arrows.]

$$G_4 = (G_3 * gaussian) \downarrow 2$$
$$G_3 = (G_2 * gaussian) \downarrow 2$$
$$G_2 = (G_1 * gaussian) \downarrow 2$$
$$G_1 = (G_0 * gaussian) \downarrow 2$$
$$G_0 = \text{Image}$$
