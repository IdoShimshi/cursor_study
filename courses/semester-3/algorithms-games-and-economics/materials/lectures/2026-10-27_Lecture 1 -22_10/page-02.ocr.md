# 2026-10-27_Lecture 1 -22_10 - page-02

> Gemini gemini-2.5-flash transcription.

Pure Nash equilibrium - a set of strategies $(S_1, ..., S_n)$ s.t. each $S_i$ is the best response to $S_{-i}$.

Theorem: If $n \ge 2$, then the only equilibrium is $(\frac{1}{2}, \frac{1}{2})$.

Proof: denote the strategies of the players by $X_1, X_2$.
$X_1 < X_2$: Suppose that $X_1 \le \frac{1}{2}$, Player 1 is better off by playing $X_1 + \epsilon$, as long as $X_1 + \epsilon < X_2$.
$X_1 = X_2 \ne \frac{1}{2}$: Suppose that $X_1 < \frac{1}{2}$, $X_1 + \epsilon < \frac{1}{2}$, Player 1 is better off playing $X_1 + \epsilon$.
$X_1 = X_2 = \frac{1}{2}$: $U_1 = U_2 = \frac{1}{2}$, by moving right or left each player decreases the utility.

This model, with as simple as it is, turned out to be useful for US politics, with their 2 party system and winner takes it all.
It models the sure votes - anyone to the left of x1, and the middle between x1 and x2 are the swing votes. Until the 90s, candidates followed the best strategies, of try to be as close as possible to the opinion of the medium voter.
From the 90s, the strategy moved towards "go to the base" approach, basically just saying whatever the other side is doing is always wrong.
This model doesn't capture this new approach, so its not as useful. People found other strategies that the model doesn't capture.

As oppose to most theoretical courses, here we need to think if a model represents life well.

Theorem: for $n=3$, there is no equilibrium.

Lemma: let $(t_1, ..., t_n)$ be the position of the players $t_1 < ... < t_n$.
In every Nash equilibrium at least 2 players are at $t_2$ and $t_n$.

Proof:
[diagram: line segment with $t_1$ and $t_2$ marked]
if only one is at $t_1$,
moving to $t_2 - \epsilon$ is better for the player at $t_1$.

Corollary: there is no Nash equilibrium for $n=3$.

Proof: if $t_1 \ne t_n$ then two players have to be at every extreme point but we only have 3, not 4.
if $t_1 = t_n = t$, then the utility of each player is $\frac{1}{3}$, so every player can move and increase $u$.

What about $n=4$?
[diagram: line segment with $x_1, x_2$ and $x_3, x_4$ marked]

lectures Page 2
