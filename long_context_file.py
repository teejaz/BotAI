from google import genai
from google.genai import types
import pathlib
import httpx
import os

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

#long_context_pdf_path = "https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf" # Replace with the actual URL of your large PDF

# Retrieve the PDF
file_path = pathlib.Path('WEF_Future_of_Jobs_Report_2025.pdf')
#file_path.write_bytes(httpx.get(long_context_pdf_path).content)

# Upload the PDF using the File API
sample_file = client.files.upload(
  file=open(file_path, "rb"),
  config=dict(
    # It will guess the mime type from the file extension, but if you pass
    # a file-like object, you need to set the
    mime_type='application/pdf')
)

prompt="Summarize this document"

response = client.models.generate_content(
  model="gemini-2.0-flash",
  contents=[sample_file, "Summarize this document"])
print(response.text)
