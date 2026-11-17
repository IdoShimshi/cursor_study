import os
import yaml
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
YAML_DIR = BASE_DIR / "temp_questions"
LECTURES_DIR = BASE_DIR.parent / "materials" / "lectures"
OUTPUT_FILE = BASE_DIR / "exam_data.json"


def get_lecture_dir_map():
    mapping = {}
    for d in LECTURES_DIR.iterdir():
        if d.is_dir():
            # Match "lectureX" or "lectureXX"
            match = re.search(r"lecture(\d+)", d.name, re.IGNORECASE)
            if match:
                lecture_num = int(match.group(1))
                mapping[lecture_num] = d.name
    return mapping


def parse_reference(ref_str):
    # Example: "Lecture 2, Slide 6" or "Lecture 2, Slides 41-42"
    match = re.search(
        r"Lecture\s+(\d+),\s+(?:Slide|Slides|Page)\s+(\d+)", ref_str, re.IGNORECASE
    )
    if match:
        return int(match.group(1)), int(match.group(2))
    return None, None


# Dictionary to handle inconsistent slide numbering across lectures.
# Default is +1 for most lectures (due to title page offset).
# Set to 0 if a lecture is perfectly aligned (e.g. Lecture 2).
LECTURE_OFFSETS = {
    1: 1,
    2: 0,  # Confirmed 0
    3: 1,
    4: 1,
    5: 1,  # Confirmed 1
    6: 1,
    7: 1,
    8: 1,
    9: 1,
    10: 1,
    11: 1,
    12: 1,
    13: 1,  # Confirmed 1
    14: 1,
    15: 1,
}


def generate_data():
    lecture_dir_map = get_lecture_dir_map()
    all_questions = []

    yaml_files = sorted(
        list(YAML_DIR.glob("*.yaml")),
        key=lambda p: (
            int(re.search(r"lecture_(\d+)", p.name).group(1))
            if re.search(r"lecture_(\d+)", p.name)
            else 0
        ),
    )

    for yaml_path in yaml_files:
        print(f"Processing {yaml_path.name}...")
        with open(yaml_path, "r") as f:
            try:
                # ... same logic as before ...
                content = f.read()
                if "```yaml" in content:
                    content = re.search(
                        r"```yaml\n(.*?)\n```", content, re.DOTALL
                    ).group(1)
                elif "```" in content:
                    content = re.search(r"```\n(.*?)\n```", content, re.DOTALL).group(1)

                data = yaml.safe_load(content)
                lecture_name = data.get(
                    "lecture_name", yaml_path.stem.replace("_", " ").capitalize()
                )

                # Get lecture index from filename if not elsewhere
                fname_match = re.search(r"lecture_(\d+)", yaml_path.name)
                lecture_idx = int(fname_match.group(1)) if fname_match else 0

                # Determine the shift for this specific lecture
                shift = LECTURE_OFFSETS.get(lecture_idx, 1)  # Default to 1

                for i, q in enumerate(data.get("questions", []), 1):
                    ref_str = q.get("reference", "")
                    l_num, p_num = parse_reference(ref_str)

                    # Fallback if reference doesn't match or refers to wrong lecture
                    if l_num is None:
                        l_num = lecture_idx

                    # Apply the lecture-specific shift
                    actual_p_num = p_num + shift if p_num is not None else None

                    # Create a unique ID
                    q_id = f"L{lecture_idx:02d}_Q{i:02d}"

                    image_path = None
                    if l_num in lecture_dir_map and actual_p_num:
                        dir_name = lecture_dir_map[l_num]
                        # Relative to index.html which will be in practice/
                        image_path = f"../materials/lectures/{dir_name}/page-{actual_p_num:02d}.png"

                    question_data = {
                        "id": q_id,
                        "lecture": lecture_name,
                        "lecture_num": lecture_idx,
                        "difficulty": q.get("difficulty", "Medium"),
                        "type": q.get("type", "MCQ"),
                        "question": q.get("question", ""),
                        "options": q.get("options", {}),
                        "correct_answer": q.get("correct_answer", ""),
                        "reasoning": q.get("reasoning", ""),
                        "reference": ref_str,
                        "image_path": image_path,
                    }
                    all_questions.append(question_data)

            except Exception as e:
                print(f"Error parsing {yaml_path.name}: {e}")

    with open(BASE_DIR / "exam_data.js", "w") as f:
        f.write(f"const EXAM_DATA = {json.dumps(all_questions, indent=2)};")

    print(f"Generated {len(all_questions)} questions in {BASE_DIR / 'exam_data.js'}")


if __name__ == "__main__":
    generate_data()
