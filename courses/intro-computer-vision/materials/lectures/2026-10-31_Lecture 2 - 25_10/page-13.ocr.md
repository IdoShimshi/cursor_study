# 2026-10-31_Lecture 2 - 25_10 - page-13

> Gemini gemini-2.5-flash transcription.

LPF in _Image domain_ vs. _Fourier domain_

Computational complexity of convolution: $O(N \log N)$ via Fourier.
But for filter with a $\underline{small}$ support $k \quad \square \quad O(kN)$ in the Image domain.

1) $f(x,y) * $
[diagram: $k \times k$ grid representing a rect function]
$\leftrightarrow F(u,v) \text{ sinc}(u,v)$
_Convenient_
_But not an ideal LPF..._
(small spatial support;
no cyclic assumption)

2) $f(x,y) * \text{sinc}(x,y) \leftrightarrow F(u,v) \text{ rect}(u,v)$
_An ideal LPF_

3) $f(x,y) * \text{gaussian}(x,y) \leftrightarrow F(u,v) \text{ Gaussian}(u,v)$

lectures Page 13
