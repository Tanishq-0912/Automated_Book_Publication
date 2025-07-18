# Directory: agents/reviewer.py
from groq import Groq

def review_text(text):
    client = Groq(api_key="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")
    response = client.chat.completions.create(
        model="llama3-8b-8192",  # Faster model; can upgrade to 70b if needed
        messages=[
            {"role": "system", "content": "You are an editor. Improve grammar, structure, and clarity."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()
