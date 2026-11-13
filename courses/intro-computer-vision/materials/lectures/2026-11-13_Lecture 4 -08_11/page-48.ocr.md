# 2026-11-13_Lecture 4 -08_11 - page-48

> Gemini gemini-3-flash-preview transcription.

# Direct Linear Transform (DLT) algorithm

Matrix formulation
$$M\boldsymbol{v} = 0$$
We are interested in $0 \neq \boldsymbol{v} \in null(M)$ (arbitrary scale)
In general, due to <u>noise</u> in the measurements, we will not have an exact solution
We look for a solution for the optimization problem
<u>Homogeneous least-squares problem</u>
$$\min_{\|\boldsymbol{v}\|=1} \|M\boldsymbol{v}\|$$
<u>Solution</u>
$\boldsymbol{v}$ is the last column of $V$, where $M = UDV^T$ is the SVD of $M$
