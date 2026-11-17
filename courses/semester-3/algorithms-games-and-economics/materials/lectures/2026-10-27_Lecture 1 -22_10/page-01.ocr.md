# 2026-10-27_Lecture 1 -22_10 - page-01

> Gemini gemini-3-flash-preview transcription.

Lecture 1 - 22/10
Tuesday, October 27, 2026 6:32 PM

HW - pass/fail, AI OK, 20%
Before - take home exam - now, find something new - should take a few days

Hotelling model

[diagram: A horizontal line segment from 0 to 1, with points $x_1$ and $x_2$ marked such that $0 < x_1 < x_2 < 1$.]

- every point is a voter (infinite voters)
- 2 candidates
- every candidate wants to maximize its vote share

suppose that the locations of the candidates are $x_1 < x_2$

voters vote for the closest candidate
$u$ for utility
$u_1(x_1, x_2) = x_1 + \frac{x_2 - x_1}{2} = \frac{x_2 + x_1}{2}$
$u_2(x_1, x_2) = 1 - x_2 + \frac{x_2 - x_1}{2} = 1 - \frac{x_2 + x_1}{2}$

if $x_1 = x_2$ then $u_1(x_1, x_2) = u_2(x_1, x_2) = \frac{1}{2}$

picking to have $\frac{1}{2}$ as your choice is optimal, at worse you get $\frac{1}{2}$

now the same game with 3 candidates - not as simple

Game: a set $N$ of players $(1, \dots, n)$
for each player $i$ there is a nonempty set of strategies $S_i$.
Each player $i$ has a utility function $u_i: S_1 \times \dots \times S_n \to \mathbb{R}$.

A strategy profile $s = (s_1, \dots, s_n)$ specifies how each player played
we sometimes write $s_{-i} = (s_1, \dots, s_{i-1}, s_{i+1}, \dots, s_n)$

The best response of player $i$ given strategies $s_{-i}$ is a strategy $s_i$ that max $u_i(s_i, s_{-i})$

Pure Nash equilibrium - a set of strategies $(s_1, \dots, s_n)$ s.t. each $s_i$ is [illegible] [illegible] [illegible]
