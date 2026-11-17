# 2026-11-11_Lecture 3 - 05_11 - page-04

> Gemini gemini-3.5-flash-lite transcription.

$$\text{3SUM} \longrightarrow_2 \text{ 3 Points on a Line}$$

$$x^3 - y^3 = (x - y)(x^2 + xy + y^2)$$
$$x^2 - y^2 = (x - y)(x + y)$$

$$\begin{tabular}{|l|}
\hline
\textbf{3 Points on a Line} \\
\hline
Input: \quad $n$ two-dimensional points \\
Output: $\exists$ line through 3 points? \\
\hline
\end{tabular}$$

[diagram: A Cartesian coordinate system showing a curve $y = x^3$ with three points $(a, a^3)$, $(b, b^3)$, and $(c, c^3)$ lying on a single straight line.]

$$\begin{aligned}
&\iff \frac{b^3 - a^3}{b - a} = \frac{c^3 - b^3}{c - b} \\
&\iff a^2 + ab + b^2 = b^2 + bc + c^2 \\
&\iff a^2 + ab = bc + c^2 \\
&\iff a^2 - c^2 = b(c - a) \\
&\iff a + c = -b \\
&\iff a + b + c = 0
\end{aligned}$$

$$\text{3 Points on a Line} \longleftrightarrow_2 \text{ Point on 3 Lines}$$

$$\begin{tabular}{|l|}
\hline
\textbf{Point on 3 Lines} \\
\hline
Input: \quad $n$ two-dimensional lines \\
Output: $\exists$ point lying on 3 lines? \\
\hline
\end{tabular}$$

[diagram: Two graphs connected by a dashed circle labeled "point-line duality". The left graph (primal) shows three collinear points on a line $y = mx + n$. The right graph (dual) shows three lines intersecting at a single point $(m, -n)$.]

$$\text{lectures Page 4}$$
