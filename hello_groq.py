import os
from groq import Groq

MODEL = "openai/gpt-oss-20b"

key = os.environ.get("GROQ_API_KEY")
if not key:
    raise SystemExit("GROQ_API_KEY is not set in this terminal")

client = Groq(api_key=key)
try:
    r = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": "Reply with exactly one word: ready"}],
        temperature=0,
        reasoning_effort="low",
        max_completion_tokens=300,
    )
    print("model replied:", r.choices[0].message.content)
    print("tokens used:", r.usage.total_tokens)
except Exception as e:
    print("call failed:", type(e).__name__, e)