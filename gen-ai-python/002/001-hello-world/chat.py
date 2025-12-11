from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input=[
      {'role': 'user', 'content': 'Hey my name is Raj'},
      {'role': 'assistant', 'content': 'Hi Raj! How can I assist you today?'},
      {'role': 'user', 'content': 'Whats my name'},
      {'role': 'assistant', 'content': 'Your name is Raj. How can I help you further?'},
      {'role': 'user', 'content': 'How are you'},
      {'role': 'assistant', 'content': "I'm doing great, thank you for asking, Raj! How are you doing today?"},
       {'role': 'user', 'content': 'can you give json response, if yes than give me some random json example'},
    ]
)

print(response.output_text)