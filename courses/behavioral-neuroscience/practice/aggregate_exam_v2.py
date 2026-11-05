import os
import random
import yaml
import re

def clean_yaml_content(content):
    # Subagents might wrap YAML in triple backticks
    if "```yaml" in content:
        content = re.search(r"```yaml\n(.*?)\n```", content, re.DOTALL).group(1)
    elif "```" in content:
        content = re.search(r"```\n(.*?)\n```", content, re.DOTALL).group(1)
    return content

temp_dir = '/home/ido/code/msc/cursor_study/courses/behavioral-neuroscience/practice/temp_questions'
all_questions = []

for filename in sorted(os.listdir(temp_dir)):
    if filename.endswith('.yaml'):
        with open(os.path.join(temp_dir, filename), 'r') as f:
            try:
                raw_content = f.read()
                clean_content = clean_yaml_content(raw_content)
                data = yaml.safe_load(clean_content)
                
                lecture_name = data.get('lecture_name', filename.replace('.yaml', ''))
                for q in data.get('questions', []):
                    q['lecture_source'] = lecture_name
                    all_questions.append(q)
            except Exception as e:
                print(f"Error parsing {filename}: {e}")

# Shuffle
random.shuffle(all_questions)

# Write Exam
with open('/home/ido/code/msc/cursor_study/courses/behavioral-neuroscience/practice/practice_exam.md', 'w') as f:
    f.write("# Behavioral Neuroscience Practice Exam\n\n")
    f.write(f"Total Questions: {len(all_questions)}\n\n")
    f.write("---")
    for i, q in enumerate(all_questions, 1):
        difficulty = q.get('difficulty', 'Medium')
        q_text = q.get('question', '')
        
        f.write(f"\n\n### Question {i} [{difficulty}]\n\n")
        f.write(f"{q_text}\n\n")
        
        if q.get('type') == 'MCQ' and 'options' in q:
            opts = q['options']
            for key in sorted(opts.keys()):
                f.write(f"{key}. {opts[key]}\n\n")
        
        f.write("\n---")

# Write Answers
with open('/home/ido/code/msc/cursor_study/courses/behavioral-neuroscience/practice/practice_exam_answers.md', 'w') as f:
    f.write("# Behavioral Neuroscience Practice Exam - Answer Key\n\n")
    for i, q in enumerate(all_questions, 1):
        f.write(f"## Question {i}\n")
        f.write(f"**Lecture Source**: {q.get('lecture_source')}\n")
        f.write(f"**Reference**: {q.get('reference')}\n")
        f.write(f"**Difficulty**: {q.get('difficulty')}\n\n")
        
        correct = q.get('correct_answer', '')
        f.write(f"**Correct Answer/Rubric**:\n{correct}\n\n")
        
        reasoning = q.get('reasoning', '')
        f.write(f"**Reasoning**:\n{reasoning}\n\n")
        f.write("---\n\n")

print(f"Successfully processed {len(all_questions)} questions from {len(os.listdir(temp_dir))} files.")
