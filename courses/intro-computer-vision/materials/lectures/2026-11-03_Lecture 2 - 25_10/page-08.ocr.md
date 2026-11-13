# 2026-11-03_Lecture 2 - 25_10 - page-08

> Gemini gemini-3.5-flash-lite transcription.

sampling func $s(x) =$
[diagram: a series of evenly spaced vertical arrows representing a Dirac comb with spacing $\Delta x$]

$f(x) \cdot s(x) =$
[diagram: a series of arrows of varying heights representing the sampled function]

$\exists \Omega_0 \text{ s.t. } \forall |u| > \Omega_0, F(u) = 0$

$S(u)$
[diagram: frequency domain representation of the sampling function with spacing $\Delta u = \frac{1}{\Delta x}$]

$f(u) * S(u) =$
[diagram: repeated smooth curves representing convolution with many delta duplicates]

convolution with many delta duplicates

lets look at cases

the "Nyquist frequency"

case 1: no overlap, if $\Delta u > 2\Omega_0 \Rightarrow \Delta x < \frac{1}{2\Omega_0}$

[diagram: two overlapping wave lobes]

from here, take a LPF that captures one of the duplicates, thats the original $F(u)$, then go to $f(x)$
so if we sample more densely than $2\Omega_0$, we can reconstruct

case 2: overlap
[diagram: two overlapping bell-shaped curves with significant intersection]

now if we take a LPF of this we get [diagram: a single bell curve with distorted overlapping tails]
this causes aliasing

# Examples of **Temporal** Aliasing

A **“fast”** dynamic event imaged by **a “slow camera”**

**Motion aliasing**

[diagram: an image of a ceiling fan with wooden blades]

lectures Page 8
