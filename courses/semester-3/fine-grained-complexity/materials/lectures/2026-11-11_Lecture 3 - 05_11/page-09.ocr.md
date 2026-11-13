# 2026-11-11_Lecture 3 - 05_11 - page-09

> Gemini gemini-3.5-flash-lite transcription.

return "yes" if one says "port"

correctness: "yes" $\Rightarrow$ "yes" w.p. $1$
$$a+b+c=0 \Rightarrow (a+b+c) \pmod p = 0$$

"no" $\Rightarrow$ "no" w.p. $\ge 9/10$

fix $a,b,c$ s.t. $a+b+c \ne 0$
$$\Pr[a+b+c=0 \pmod p] = \frac{\# \text{ prime divisors of } a+b+c \text{ in } [2, h^3 \lg^3 n]}{\# \text{ of primes in } [2, h^3 \lg^3 n]} \le \frac{\lg(h^3 \lg^3 n)}{\frac{h^3 \lg^3 n}{\lg h}}$$

$$= O\left(\frac{\lg h}{h^3 \lg^3 n}\right) = \frac{1}{h^3 \lg n}$$

$$\underline{\text{union bound: }} \Pr[\exists a,b,c \text{ s.t. } a+b+c=0 \pmod p] \le h^3 \cdot \frac{1}{h^3 \lg n} < \frac{1}{\lg h} < \frac{1}{10}$$

$$\underline{\text{strong 3sum conj: }} \text{3sum is hard with } U=n^2 \text{, not solved!}$$

$$\underline{\text{conv-3sum:}}$$ given arrays $A, B, C$ of length $n$ with numbers in $[1, U]$.
are there $i, j \in [n]$ s.t. $A[i] + B[j-i] = C[j]$?

[diagram: three horizontal arrays labeled A, B, C with indices, where $A[i] + B[j-i] = C[j]$]

$\underline{\text{Exercise (will be in HW):}}$ 3sum in time $T(n) \Rightarrow$ conv-3sum in time $O(T(n))$

$\underline{\text{Thm:}}$ conv-3sum in time $T(n) \Rightarrow$ 3sum in time $T(n \lg^3 n)$ w.h.p.

$$\begin{aligned}
\text{the idea}: &\quad \text{conv-3sum basically does 3sum, but it has to be ordered} \\
&\quad \text{how to reorder, put } a \text{ in } A[a], \dots \\
&\quad \text{how } i+j-i = j \text{ and } a+b=c \\
&\quad \text{but } a \text{ might be too big, so hash, } a \text{ in } A[h(a)], \dots
\end{aligned}$$

$\text{want } h(x):$
- $h(x) = O(h \lg^3 n)$
- $a+b+c=0 \Rightarrow h(a) + h(b) + h(c) = 0$
- few collisions

$\underline{\text{reduction:}}$
- repeat $10^7 \lg n$ times:
  - pick random $p \in [10 \lg^3 n, 20 \lg^3 n]$
  - define $h(x) = x \bmod p$
  - set $A'[i] = \bigcup_{\text{random } x \text{ in } S_i} \dots$ let $S_i = \{x \in S \mid h(x) = i\}$

lectures Page 9
