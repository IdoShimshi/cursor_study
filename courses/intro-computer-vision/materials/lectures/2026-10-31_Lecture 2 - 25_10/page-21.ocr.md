# 2026-10-31_Lecture 2 - 25_10 - page-21

> Gemini gemini-2.5-flash transcription.

The Gaussian Pyramid

[diagram: A vertical arrow indicates increasing resolution from top to bottom. A series of images of hot air balloons are arranged in a pyramid structure, with the largest, highest resolution image at the bottom and progressively smaller, lower resolution images upwards. Arrows and labels describe the process of creating the pyramid levels.]

Low resolution
$\uparrow$
$G_4 = (G_3 * \text{gaussian}) \downarrow 2$
$\xrightarrow{\text{blur}}$
$\xrightarrow{\text{down-sample}}$

$G_3 = (G_2 * \text{gaussian}) \downarrow 2$
$\xrightarrow{\text{blur}}$
$\xrightarrow{\text{down-sample}}$

$G_2 = (G_1 * \text{gaussian}) \downarrow 2$
$\xrightarrow{\text{blur}}$
$\xrightarrow{\text{down-sample}}$

$G_1 = (G_0 * \text{gaussian}) \downarrow 2$
$\xrightarrow{\text{blur}}$
$\xrightarrow{\text{down-sample}}$

$G_0 = \text{Image}$

High resolution

lectures Page 21
