import ollama

from prompts import SUMMARY_PROMPT


MODEL_NAME = "qwen2.5:7b"


def generate_summary(transcript):

    full_text = "\n".join([
        item["text"]
        for item in transcript
    ])

    prompt = f"""
    {SUMMARY_PROMPT}

    TRANSCRIPCIÓN:

    {full_text}
    """

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]