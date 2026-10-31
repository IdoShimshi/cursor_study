---
description: Guidance on visualizing mathematical graphs, phase portraits, and data
applyTo: "**"
---

# Mathematical visualizations

Never use AI image generation for mathematical graphs, phase portraits, or data visualizations unless the user explicitly says "generate using the model" or "DALL-E style".

Instead, follow these priorities:
1. **Compute and plot:** use Python (Matplotlib, Seaborn) to generate a precise, high-quality image file.
2. **Web search:** find existing high-quality educational diagrams or interactive tools.
3. **Markdown/Mermaid:** use Mermaid diagrams for simple flowcharts or architectural diagrams.

When plotting phase portraits:
- Use `streamplot` or `quiver` for vector fields.
- Ensure axes are labeled and the scale is appropriate.
- Save the result to the `assets/` folder and embed it in the response.
