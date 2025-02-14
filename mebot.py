
from google import genai
from google.genai import types
import pathlib
import httpx
import os

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

print("My files:")
for f in client.files.list():
    print("  ", f.name)


