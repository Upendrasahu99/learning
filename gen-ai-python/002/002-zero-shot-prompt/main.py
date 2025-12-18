print('start')

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
aiClient = OpenAI()

# Zero-shot Prompting
systemPrompt = """
  You are a Math Expert. You only know Math and nothing else.
  You help studen to solve ther Math problem only and nothing else.
  If user try to asked apart from Math you just needd to say "Me nahi bataung" in reply nothing else.
  But user coming first time just greet and reply politely
"""

response = aiClient.responses.create(
  model= 'gpt-5-nano',
  input= [
    {'role': 'system', 'content': systemPrompt},
    {'role': 'user', 'content': 'Hey, My name is Upendra'},
    {'role': 'assistant', 'content': 'Hello Upendra, nice to meet you. I’m here to help with math problems. What math problem would you like to work on today? '},
    {'role': 'user', 'content': 'what is algebra'},
    {
      'role': 'assistant',
      'content': """
              Algebra is a branch of mathematics that uses symbols (usually letters) to stand for numbers and to describe relationships and patterns. It lets us solve for unknown values and generalize rules.

Key ideas:
- Variables: symbols like x, y that represent numbers.       
- Expressions: combinations of numbers, variables, and operations (e.g., 3x + 5).
- Equations: statements that two expressions are equal (e.g., 2x - 4 = 8).
- Solving: finding the value(s) of the variable that make the equation true.

Example:
- Solve 3x + 5 = 20.
  3x = 15, so x = 5.

Two-variable example:
- Solve 2x + 3y = 12 and x - y = 1.
  From x - y = 1, y = x - 1.
  Substitute: 2x + 3(x - 1) = 12 → 5x - 3 = 12 → 5x = 15 → x = 3, then y = 2.

Why it’s useful:
- Describes general rules and patterns.
- Solves problems with unknown values.
- Underpins more advanced math (polynomials, functions, systems of equations).
              """
     },
     {'role': 'user', 'content': 'what is Computer Science'}
  ]
)

print(response.output_text)
