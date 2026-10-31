# 2026-10-31_Lecture 2 - 25_10 - page-02

> Gemini gemini-2.5-flash transcription.

# Convolution

Flip g around x and shift it: $x \square 0$,
(then take the inner product)
$\downarrow$

1D (continuous, discrete):
$$f * g (x) = \int_{-\infty}^{\infty} f(\alpha)g(x - \alpha)d\alpha$$
Good for:
- Pattern matching
- Filtering
- Understanding Fourier properties

1D continuous
1D discrete

2D (continuous, discrete):
$$f * g (x,y) = \int_{\alpha=-\infty}^{\infty} \int_{\beta=-\infty}^{\infty} f(\alpha,\beta)g(x - \alpha, y - \beta)d\alpha d\beta$$
2D continuous
$$= \sum_{N-1}^{N-1} \sum_{N-1}^{N-1} f(\alpha.\beta)a(x - \alpha. v - \beta)$$
2D discrete

lectures Page 2
