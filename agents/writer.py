
# Directory: agents/writer.py
from groq import Groq

def spin_chapter(text):
    client = Groq(api_key="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")
    response = client.chat.completions.create(
        model="llama3-70b-8192",  # Or use "llama3-8b-8192" if you want it faster
        messages=[
            {"role": "system", "content": "You are a creative writer who rewrites chapters with more vivid language."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()
