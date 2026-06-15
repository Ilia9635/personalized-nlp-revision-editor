import json
import os
from pathlib import Path
from openai import OpenAI

client = OpenAI()

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = PROJECT_ROOT / "data" / "processed" / "dataset_b.jsonl"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def load_jsonl(path):
    examples = []
    with open(path, mode = "r", encoding = "utf-8") as file:
        for line in file:
            examples.append(json.loads(line))

    return examples

def get_text_field(row, possible_names):
    for name in possible_names:
        if name in row and row[name]:
            return row[name]
    return ""

def build_few_short_examples(examples, n=3):
    selected = examples[:n]
    formatted_examples = []
    for i, row in enumerate(selected, start = 1):
        old_text = get_text_field(row, ["old_version", "input", "original", "draft"])
        new_text = get_text_field(row, ["new_version", "output", "revised", "revision"])
        category = get_text_field(row, ["categorization_of_change", "revision_category"])

        formatted_examples.append(
            f"""Example {i}
    Revision focus: {category}
    Original: 
{old_text}
    Revised: 
{new_text}
    """
        )
    return "\n\n".join(formatted_examples)


def build_editing_prompt(user_passage, examples):
    few_short_text = build_few_short_examples(examples, n=3)

    prompt = f"""
 You are a personalized fiction revision editor.

 Your task is to revise the user's passage for grammar, clarity, flow, and readability while preserving the author's style.

 Editing priorities:
 - Fix grammar, spelling, punctuation, and awkward phrasing.
 - Preserve the author's voice, tone, rhythm, and emotional intent.
 - Do not flatten the prose into generic corporate or academic writing.
 - Keep the same point of view and tense unless grammar requires a small correction.
 - Preserve character voice and dialogue style.
 - Do not summarize.
 - Do not explain the edits.
 - Return only the revised passage.

 Below are examples of the author's revision style:

 {few_short_text}

 Now revise the following passage:

 Original:
 {user_passage}

 Revised:
 """.strip()

    return prompt

def run_model(prompt):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
    )

    return response.output_text

def save_prompt(prompt, filename="baseline_prompt.txt"):
    output_path = OUTPUT_DIR / filename

    with open(output_path, mode="w", encoding="utf-8") as file:
        file.write(prompt)

    print(f"Saved prompt to: {output_path}")

def main():
    print("Looking for file at:", DATA_PATH)
    print("File exists:", DATA_PATH.exists())

    examples = load_jsonl(DATA_PATH)

    test_passage = """
Paste your rough paragraph here.
""".strip()

    prompt = build_editing_prompt(test_passage, examples)

    save_prompt(prompt)

    edited_text = run_model(prompt)

    output_path = OUTPUT_DIR / "baseline_output.txt"

    with open(output_path, mode="w", encoding="utf-8") as file:
        file.write(edited_text)

    print("Saved edited output to:", output_path)
    print("\nEdited preview:\n")
    print(edited_text[:2000])


if __name__ == "__main__":
    main()
