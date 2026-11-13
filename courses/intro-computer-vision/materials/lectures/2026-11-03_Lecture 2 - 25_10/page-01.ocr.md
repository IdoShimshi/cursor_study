# 2026-11-03_Lecture 2 - 25_10 - page-01

> Gemini gemini-3.5-flash-lite transcription.

Lecture 2 - 25/10

Friday, October 30, 2026 1:12 PM

[diagram: 2D Image and Fourier Spectrum pairs showing a square, two horizontal bars, and a diagonal line, with their corresponding Fourier transforms]

# Convolution

[diagram: Red box with an arrow pointing to the 1D continuous convolution formula, with handwritten text: "Flip $g$ around $x$ and shift it: $x - \alpha$, (then take the inner product)"]

1D (continuous, discrete):

$$f * g\ (x) = \int_{-\infty}^{\infty} f(\alpha)g(x - \alpha) d\alpha$$

[yellow box with red text: "Good for:
- Pattern matching
- Filtering
- Understanding Fourier properties"]

2D (continuous, discrete):

$$f * g\ (x, y) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(\alpha, \beta)g(x - \alpha, y - \beta) d\alpha d\beta$$

$$= \sum_{\alpha=0}^{N-1} \sum_{\beta=0}^{N-1} f(\alpha, \beta) g(x - \alpha, y - \beta)$$
