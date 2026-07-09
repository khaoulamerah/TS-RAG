import os
from openai import OpenAI

print(" OpenAI SDK imported successfully")

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print(" OPENAI_API_KEY found")
else:
    print(" OPENAI_API_KEY not found")
    raise RuntimeError("OPENAI_API_KEY is missing")

client = OpenAI(api_key=api_key)

print("OpenAI client created successfully")