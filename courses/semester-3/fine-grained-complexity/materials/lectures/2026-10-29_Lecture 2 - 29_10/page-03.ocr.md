# 2026-10-29_Lecture 2 - 29_10 - page-03

> Gemini gemini-3.5-flash-lite transcription.

correctness :
fix a sol $a,b,c \in S$
$Pr[\text{all } 3 \text{ sets distinct colors}] = \frac{3!}{3^3} = \frac{2}{9}$

"no" $\rightarrow$ always "no"
"yes" $\rightarrow$ "yes" w.p. $> 9/10$
$Pr[\text{all } 10 \text{ calls fail}] \le \left(\frac{7}{9}\right)^{10} < \frac{1}{20}$

col-$3\text{sum} \rightarrow 3\text{sum}$

$\underline{\text{Thm:}}$ if $3\text{sum}$ is in $T(n)$ then col-$3\text{sum}$ is in $O(T(n))$

[diagram: three horizontal rectangles labeled A, B, C with arrows pointing to $+60$, $-40$, $-20$]

$S = \{a+60 \mid a \in A\} \cup \{b-40 \mid b \in B\} \cup \{c-20 \mid c \in C\}$
"yes" $\rightarrow$ "yes"
"no" $\rightarrow$ "no" sum of any 3 with repetitions in $\{60, -40, -20\}$ is $\neq 0$

$3\text{sum}'$ : given set $S$, are there $a,b,c \in S$ s.t. $a+b=c$?

$$3\text{sum} \xrightarrow{+60} \text{col-}3\text{sum} \xleftrightarrow{} \text{col-}3\text{sum}' \xleftarrow{+60} 3\text{sum}'$$

$\underline{\text{this}}$ is easy, just do $C' = \{-c \mid c \in C\}$

$3\text{AVARAGE}$ : given set $S$, are there $a,b,c \in S$ s.t. $\frac{a+b}{2} = c$?

do same thing, go to colored

$$\text{col-AVG} \rightarrow \text{col-}3\text{sum} \xleftrightarrow{} \text{col-}3\text{sum}'$$
