---
name: Interactive Practice Exam App
overview: Create a local, interactive web interface for taking the 225-question practice exam with progress saving and slide image integration.
todos:
  - id: generate-json-data
    content: Create generate_app_data.py to aggregate YAMLs and image paths.
    status: completed
  - id: build-web-app
    content: Develop index.html with filtering and LocalStorage persistence.
    status: completed
  - id: verify-images-and-ux
    content: Verify slide image paths and "Show Slide" toggle functionality.
    status: completed
  - id: relaunch-conceptual-agents
    content: Update subagent prompt and relaunch all lecture agents for conceptual/integrated questions.
    status: completed
isProject: false
---

# Behavioral Neuroscience Practice Exam System

This document outlines the strategy for generating and taking the Behavioral Neuroscience practice exam.

## 1. Generation Strategy (Subagents)

Each of the 15 lectures is processed by a dedicated subagent with the following instructions:

### Master Subagent Prompt
> You are an expert TA for the Behavioral Neuroscience course. Your task is to generate 15 practice exam questions for the lecture provided.
>
> **Exam Context & Constraints:**
> 1. **Understanding over Memorization**: Focus on application, prediction, and synthesis. Do NOT ask for direct text recall if the answer can be found by just searching the PDF. 
> 2. **Conceptual Mastery**: Some questions should cover overarching concepts that span multiple slides or are inferred from the lecture as a whole.
> 3. **Vision & Diagrams**: At least 7 questions MUST require analyzing a specific graph, neural pathway, or experimental diagram from the slides.
> 4. **Strategic Referencing**: 
>    - DO NOT mention slide numbers in the question text for general conceptual questions.
>    - YOU MUST mention the slide number in the question text ONLY IF the question requires the student to analyze a specific diagram/graph (e.g., "Referring to the graph on Slide 10...").
>    - EVERY question must have a 'reference' field in the YAML.
> 5. **YAML Output ONLY**: Your entire response must be a single YAML code block.
>
> **CRITICAL: Referencing Rules**
> 1. **How to read Page Markers**: The PDF text markers (like `-- 31 of 51 --`) act as **FOOTERS**. This means the text of **Page 31** is found **ABOVE** the marker `-- 31 of 51 --`. The text found **BELOW** that marker belongs to **Page 32**.
> 2. **The Assets folder is the Ground Truth**: ALWAYS verify your references by looking at the `.png` filenames in the provided Assets folder. If you see a concept in the text, find the image that contains that exact content. The number in the filename (e.g., `page-32.png`) is the **Slide Number** you must use in your `reference` field.
> 3. **Title-Data Verification**: Professors often use a "Title Slide" (text only) followed by a "Data Slide" (graph only). If you reference a graph described on Page 31, check `page-32.png` to see if the actual graph is there. Reference the filename number that contains the visual.

## 2. Interactive Web App (Frontend)

The practice exam is taken via a standalone HTML application located at `practice/index.html`.

### Key Features:
- **Filtering**: Filter by Lecture, Difficulty (Easy/Medium/Hard), Question Type (MCQ/Open), and Status (Answered/Unanswered).
- **Ordering**: Logical ordering by lecture, sort by difficulty/type, or a stable Shuffle mode.
- **Persistence**: Answers are saved in real-time to the browser's **LocalStorage**.
- **Slide Integration**: "Show/Hide Slide" reveals the source material directly below the question.
- **Feedback**: Instant "Correct/Incorrect" feedback for MCQs and rubrics for open-ended questions.

## 3. Data Pipeline
The `generate_app_data.py` script consolidates the subagent YAML outputs into `exam_data.js`.

**Note on Offsets**: 
Because most questions were generated under the assumption that page markers were headers, the script currently applies a global **+1 offset** (Slide 31 -> `page-32.png`) to align the data correctly, with Lecture 2 being the only exception.
