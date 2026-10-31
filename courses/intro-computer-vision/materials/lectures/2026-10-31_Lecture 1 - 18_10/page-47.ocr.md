# 2026-10-31_Lecture 1 - 18_10 - page-47

> Gemini gemini-3-flash-preview transcription.

# Fast Fourier Transform - FFT

$$F(u) = \frac{1}{N} \sum_{x=0}^{N-1} f(x) e^{-\frac{2\pi iux}{N}} \quad u = 0, 1, 2, \dots, N-1$$

$O(N^2)$ operations, if performed as is

### FFT

$$F(u) = \underbrace{\frac{1}{N} \sum_{x=0}^{N/2-1} f(2x) e^{-\frac{2\pi iu2x}{N}}}_{\text{even x}} + \underbrace{\frac{1}{N} \sum_{x=0}^{N/2-1} f(2x+1) e^{-\frac{2\pi iu(2x+1)}{N}}}_{\text{odd x}}$$

$$= \frac{1}{2} \left[ \underbrace{\frac{1}{N/2} \sum_{x=0}^{N/2-1} f(2x) e^{-\frac{2\pi iux}{N/2}}}_{\text{Fourier Transform of N/2 even points}} + e^{-\frac{2\pi iu}{N}} \underbrace{\frac{1}{N/2} \sum_{x=0}^{N/2-1} f(2x+1) e^{-\frac{2\pi iux}{N/2}}}_{\text{Fourier Transform of N/2 odd points}} \right]$$

The Fourier transform of N inputs, can be performed as 2 Fourier Transforms of N/2 inputs each + one complex multiplication and addition for each value. Thus, if F(N) is the computation complexity of FFT:

$$F(N) = F(N/2) + F(N/2) + O(N) \Rightarrow F(N) = N \log N$$

lectures Page 47
