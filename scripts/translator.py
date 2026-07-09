from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)

SYSTEM_PROMPT = """
You are a professional technical translator.

Translate the following HTML document from French to English.

Rules:

- Preserve ALL HTML tags.
- Preserve indentation.
- Preserve CSS.
- Preserve JavaScript.
- Preserve links.
- Preserve images.
- Preserve code blocks.
- Translate ONLY visible French text.
- Do NOT add explanations.
- Do NOT remove anything.
- Return ONLY the translated HTML.
"""


def translate_html(html: str) -> str:
    response = client.responses.create(
        model="gpt-5.5",
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": html,
            },
        ],
    )

    return response.output_text