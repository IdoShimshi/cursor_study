# 2026-11-13_Lecture 4 -08_11 - page-41

> Gemini gemini-3.5-flash-lite transcription.

The Essential matrix, $q^T E p = 0$
$\hfill\text{\textit{The calibrated case}}$

$\underline{\text{Estimating } E}$

* point matches between the two images are needed
    * Linear solution (DLT) requires (at least) 8 matches
    * Non-linear (polynomial) solution requires 5 matches

$\underline{\text{Recovering } t \text{ and } R \text{ from } E \text{ (camera pose)}}$

* 4 solutions (two orthogonal matrices - rotation and reflection, sign ambiguity for translation).
  Resolve ambiguity: positive depths in both images

> Recovering camera pose is an important step towards structure from motion problem
