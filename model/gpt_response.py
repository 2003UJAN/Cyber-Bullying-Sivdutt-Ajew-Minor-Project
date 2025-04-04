import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(toxic_text):
    prompt = f"Rewrite the following toxic comment to be respectful and positive:\n\n'{toxic_text}'\n\nRewritten version:"
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=80,
        temperature=0.7
    )
    return response.choices[0].text.strip()
