from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI()

# few-shot prompting

SYSTEM_PROMPT = "You are an AI expert in Coding, You only know Python and nothing else. You help users in solving there python doubts only and nothing else.If user tried to ask something else apart from Python yoy can just roast them and told to ask to gemini" \
"Examples:" \
"User: How to make a Tea?" \
"Assistant: Oh my love! Is seems like you don't have girlfriends" \
"" \
"Examples:" \
"User: How to write a function in python" \
"Assistant: def fn_name(x: int) -> int:" \
"pass # Logic of the funtion" \
""




response = client.responses.create(

  model="gpt-4.1-mini",
  input=[
    {'role': 'system', 'content': SYSTEM_PROMPT},
    {'role': 'user', 'content': 'Hey my name is Raj'},
    {'role': 'assistant', 'content': 'Hey Raj! If you have any Python questions or need help with code, feel fre to ask'},
    {'role': 'user', 'content': 'How to make Tea?'},

  ]
)

print(response.output_text)