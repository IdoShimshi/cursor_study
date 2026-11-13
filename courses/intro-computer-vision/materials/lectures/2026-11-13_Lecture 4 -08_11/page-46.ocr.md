# 2026-11-13_Lecture 4 -08_11 - page-46

> Gemini gemini-3.5-flash-lite transcription.

Estimating the Fundamental (Essential) matrix $F$

We have that if $\boldsymbol{p} \leftrightarrow \boldsymbol{q}$ are corresponding points
$$\Rightarrow \boldsymbol{q}^T F \boldsymbol{p} = 0$$

If $\boldsymbol{p} = (p_1, p_2, p_3)^T$, $\boldsymbol{q} = (q_1, q_2, q_3)^T$

$$\boldsymbol{q}^T F \boldsymbol{p} = (q_1, q_2, q_3) \begin{pmatrix} F_{11} & F_{12} & F_{13} \\ F_{21} & F_{22} & F_{23} \\ F_{31} & F_{32} & F_{33} \end{pmatrix} \begin{pmatrix} p_1 \\ p_2 \\ p_3 \end{pmatrix} =$$

$$F_{11} q_1 p_1 + F_{12} q_1 p_2 + F_{13} q_1 p_3 + F_{21} q_2 p_1 + F_{22} q_2 p_2 + F_{23} q_2 p_3$$
$$+ F_{31} q_3 p_1 + F_{32} q_3 p_2 + F_{33} q_3 p_3 = 0$$

A linear equation in $F$'s elements
