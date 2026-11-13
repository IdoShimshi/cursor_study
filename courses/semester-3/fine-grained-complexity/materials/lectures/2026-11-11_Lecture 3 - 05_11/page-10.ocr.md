# 2026-11-11_Lecture 3 - 05_11 - page-10

> Gemini gemini-3.5-flash-lite transcription.

- define $h(x) = x \bmod p$
- set $A[i] = \begin{cases} \text{random } x \text{ in } S_i \\ +\infty \quad \text{if } S_i = \emptyset \end{cases}$ let $S_i = \{x \in S \mid h(x) = i\}$
  B, C same way
- if $\text{conv-3sum}(A,B,C) = \text{"yes"}$, return $\text{"yes"}$
"go"

$\underline{\text{correctness:}}$
$$\begin{aligned}
\text{def: } &- a \text{ is "good" if } |S_{h(a)}| \le 10 \\
&- a \text{ is "bad" o.w} \\
&- a \text{ is "chosen" if } A[h(x)] = a
\end{aligned}$$
same for $b, c$

$\underline{\text{claim:}}$ if $a+b=c$ and $a,b,c$ "chosen"
then $\text{conv-3sum}[A,B,C] = \text{yes}$

pf clear

$\underline{\text{lemma:}}$ $a \neq a' \Rightarrow \Pr[h(a) = h(a')] = \Pr[a - a' \equiv 0 \bmod p] \le \frac{\text{\# prime divisors}}{\text{\# primes}} \le \frac{\lg h^3}{n \lg^2 h} \le \frac{1}{10n}$
$\Pr[a \text{ is "bad"}] \le \frac{1}{10}$

$\Pr[a \text{ is "chosen"} \mid a \text{ is "good"}] \ge \frac{1}{10}$
$\Pr[a \text{ is "chosen"}] \ge \frac{9}{100}$

$\Pr[a,b,c \text{ "chosen"}] \ge \left(\frac{9}{100}\right)^3$

while not that small, its constant
we repeat $10^7$ times for that
