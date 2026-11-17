# 2026-10-31_Lecture 1 - 18_10_2 - page-45

> Gemini gemini-3.5-flash-lite transcription.

# Fourier Properties

1. **Separability of the 2D transform:**
   $$2D\ Transform = \text{successive applications of 1D transforms}$$

2. **Linearity:**
   $$f + g \leftrightarrow F + G$$
   $$af \leftrightarrow aF$$

3. **Image average:**
   $$F(0,0) = \text{avg}(f(x, y)) \quad \text{(continuous)}$$

4. **Shift $\Leftrightarrow$ phase-change:**
   $$g(x) = f(x + a) \leftrightarrow G(u) = F(u)e^{2\pi iua}$$
   $$G(u) = F(u)e^{2\pi iua / N} \quad \text{(discrete)}$$

[diagram: red downward arrow between continuous and discrete equations]

* Same magnitude; only phase shift. $\quad |G(u)| = |F(u)|$
* Can be used to recover shift $(a,b)$ between two images $f(x,y)$ \& $g(x,y)$:
  $$G(u,v) / F(u,v) = e^{2\pi i \left(\frac{ua}{N} + \frac{vb}{M}\right)}$$ [diagram: green right-pointing arrow labeled $\text{FFT}^{-1}$] $\delta(x + a, y + b)$
