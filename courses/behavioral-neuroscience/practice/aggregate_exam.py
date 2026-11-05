import os
import random
import re

def parse_md(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Split into Questions and Answer Key sections
    parts = re.split(r'#+\s*(?:Section\s*\d+:\s*)?(?:Questions|Answer Key|Answers|Answer\s*Key)', content, flags=re.IGNORECASE)
    
    if len(parts) >= 2:
        q_section = parts[1]
        a_section = parts[-1] if len(parts) > 2 else ""
    else:
        parts = re.split(r'(?m)^#+\s*Answer\s*Key', content, flags=re.IGNORECASE)
        if len(parts) >= 2:
            q_section = parts[0]
            a_section = parts[1]
        else:
            q_section = content
            a_section = ""

    # Split questions by common markers
    q_pattern = r'(?m)^(?:###\s*Q\d+|###\s*Question\s*\d+|\d+\.)'
    q_blocks = re.split(q_pattern, q_section)
    q_blocks = [q.strip() for q in q_blocks if q.strip()]
    
    # Split answers by common markers
    a_pattern = r'(?m)^(?:###\s*Q\d+|###\s*Question\s*\d+|\d+\.|##\s*\d+\.|#\s*\d+\.)'
    a_blocks = re.split(a_pattern, a_section)
    a_blocks = [a.strip() for a in a_blocks if a.strip()]

    return q_blocks, a_blocks

temp_dir = '/home/ido/code/msc/cursor_study/courses/behavioral-neuroscience/practice/temp_questions'
all_pairs = []

for filename in sorted(os.listdir(temp_dir)):
    if filename.endswith('.md'):
        qs, ans = parse_md(os.path.join(temp_dir, filename))
        print(f"File {filename}: found {len(qs)} questions and {len(ans)} answers")
        count = min(len(qs), len(ans))
        for i in range(count):
            all_pairs.append({
                'q': qs[i],
                'a': ans[i],
                'source': filename
            })

# Shuffle
random.shuffle(all_pairs)

# Write Exam
with open('/home/ido/code/msc/cursor_study/courses/behavioral-neuroscience/practice/practice_exam.md', 'w') as f:
    f.write("# Behavioral Neuroscience Practice Exam\n\n")
    f.write(f"Total Questions: {len(all_pairs)}\n\n")
    for i, pair in enumerate(all_pairs, 1):
        f.write(f"{i}. {pair['q']}\n\n---\n\n")

# Write Answers
with open('/home/ido/code/msc/cursor_study/courses/behavioral-neuroscience/practice/practice_exam_answers.md', 'w') as f:
    f.write("# Behavioral Neuroscience Practice Exam - Answer Key\n\n")
    for i, pair in enumerate(all_pairs, 1):
        f.write(f"## Question {i}\n")
        f.write(f"*Source Lecture: {pair['source'].replace('.md', '')}*\n\n")
        f.write(f"{pair['a']}\n\n---\n\n")

print(f"\nFinal exam created with {len(all_pairs)} questions.")
