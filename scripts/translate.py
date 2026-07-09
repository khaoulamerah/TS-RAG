from file_utils import read_file, write_file
from translator import translate_html

SOURCE = "docs/Fr/chapitre-01-llm.html"
DESTINATION = "docs/En/chapitre-01-llm.html"

print(f"Reading {SOURCE}")

html = read_file(SOURCE)

print("Sending to GPT-5.5...")

translated = translate_html(html)

print("Saving translated file...")

write_file(DESTINATION, translated)

print("Translation completed successfully.")