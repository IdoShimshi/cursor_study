# 2026-10-31_Lecture 2 - 25_10 - page-14

> Gemini gemini-2.5-flash transcription.

The Sampling Theorem
Developed on the board (also found in recording):
* Nyquist frequency
* Aliasing
* Ideal interpolation
* Discretization induces a Cyclic function

[image: A black and white portrait of a man with flowers, sitting in front of arched windows overlooking a landscape.]

function
[diagram: Graph of a continuous function $f(x)$ in the time domain, centered around the origin.]

sampling func $S(x)=$
[diagram: Graph of an impulse train $S(x)$ in the time domain, with impulses spaced by $\Delta x$.]

$f(x) \cdot S(x) =$
[diagram: Graph of the sampled function, showing impulses at the sampling points of $f(x)$.]

Fourier
if $F(\omega)$ is band limited-
[diagram: Graph of the Fourier transform $F(\omega)$, showing a band-limited spectrum from $-\Omega_0$ to $\Omega_0$.]

there is a certain frequency, above which all frequencies are 0, then we can sample it decently

$\exists \Omega_0 \text{ s.t. } \forall |\omega| > \Omega_0, F(\omega)=0$

$S(\omega)$
[diagram: Graph of an impulse train $S(\omega)$ in the frequency domain, with impulses spaced by $\Delta \omega = \frac{1}{\Delta x}$.]

$f(\omega) * S(\omega) =$
[diagram: Graph of the convolution of $F(\omega)$ and $S(\omega)$, showing periodic repetitions of the $F(\omega)$ spectrum.]

convolution with many shifted duplicates

lets look at cases
the "Nyquist frequency"
case 1: no overlap, if $\Delta \omega \ge 2 \Omega_0 \Rightarrow \Delta x < \frac{1}{2\Omega_0}$

lectures Page 14
