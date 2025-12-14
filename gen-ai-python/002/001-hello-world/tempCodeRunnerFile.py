from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input='can you give me circle cordinate for Iframe which paste on eraser and it make'
)

print(response.output_text)