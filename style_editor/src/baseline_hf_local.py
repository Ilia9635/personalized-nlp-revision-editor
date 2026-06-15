from transformers import pipeline

editor = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    device=-1
)

prompt = """
<|system|>
You are a fiction revision editor. Revise text for grammar and clarity while preserving the author's style. Return only the revised passage.
</s>
<|user|>
Rewrite this sentence with better grammar:

She walk to the garden and seen the prince.
</s>
<|assistant|>
""".strip()

result = editor(
    prompt,
    max_new_tokens=100,
    do_sample=False,
    temperature=None,
    return_full_text=False
)

print(result[0]["generated_text"])