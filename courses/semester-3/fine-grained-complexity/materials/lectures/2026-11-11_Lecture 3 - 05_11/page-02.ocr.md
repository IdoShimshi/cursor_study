# 2026-11-11_Lecture 3 - 05_11 - page-02

> Gemini gemini-3.5-flash-lite transcription.

# Today: Some 3SUM-Hardness Reductions
[Gajentaan, Overmars '95] [Barequet, Har-Peled '99]

[diagram: Flowchart showing reductions starting from 3SUM to GeomBase and Segment Pattern Matching. GeomBase reduces to 3 Points on a Line, Segment Visibility, and Motion Planning. 3 Points on a Line reduces to Point on 3 Lines. Segment Pattern Matching reduces to Polygon Containment.]

---

## $3\text{SUM} \longleftrightarrow_2 \text{GeomBase}$

$$\text{GeomBase}$$
| | |
|---|---|
| **Input:** | $n$ two-dimensional points that lie on the horizontal lines with $y = 0, 1, 2$ |
| **Output:** | $\exists$ non-horizontal line through $3$ points? |

[diagram: A graph with three horizontal dotted lines at $y = 0$, $y = 1$, and $y = 2$, with multiple black dots representing points on each line. An oblique yellow line labeled "YES" passes through one point on $y = 0$, one point on $y = 1$, and one point on $y = 2$.]

---

## $3\text{SUM} \longleftrightarrow_2 \text{GeomBase}$

$$\text{GeomBase}$$
| | |
|---|---|
| **Input:** | $n$ two-dimensional points that lie on the horizontal lines with $y = 0, 1, 2$ |
| **Output:** | $\exists$ non-horizontal line through $3$ points? |
