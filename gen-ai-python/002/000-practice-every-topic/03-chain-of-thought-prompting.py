from dotenv import load_dotenv
from openai import OpenAI
import json
load_dotenv()
client = OpenAI()

##### THis prompt is not working properlly giving full step reply at once some time not giving step by step


CHAIN_OF_THOUGHT_SYSTEM_PROMPT = """
    You are an helpfull AI assistant who is specialized in resolving user query.
    For the given user input, analyse the input and break down the problem step by step.

    Follow the steps in sequence that is "analyse", "think", "output", "validate" and finally "result".

    Rules:
    1. Follow the strict JSON output as per schema.
    2. Always perform one step at a time and wait for the next input or next output step.
    3. Carefully analyse the user query,
    4. After step result stop don't start again.

    Output Format:
    {{ "step": "string", "content": "string" }}

    Example:
    Input: What is 2 + 2
    Output: {{ "step": "analyse", "content": "Alight! The user is interest in maths query and he is asking a basic arthematic operation" }}
    Output: {{ "step": "think", "content": "To perform this addition, I must go from left to right and add all the operands." }}
    Output: {{ "step": "output", "content": "4" }}
    Output: {{ "step": "validate", "content": "Seems like 4 is correct ans for 2 + 2" }}
    Output: {{ "step": "result", "content": "2 + 2 = 4 and this is calculated by adding all numbers" }}

"""


# IMPORTANT: THIS CHANGE OR THOUGHT WORKING NOT PROPELY WITH EVERY MODEL SO NEED TO NOT GIVE EVERY STEP AND ONCE GIVE DYNAMIC WAY TO ASKED STEP WITH EVERY NEW

response = client.responses.create(
    model='gpt-5-nano',
    input=[
      {'role': 'system', 'content': CHAIN_OF_THOUGHT_SYSTEM_PROMPT},
      {'role': 'user', 'content': 'What is 4 + 6'},
      {'role': 'assistant', 'content': json.dumps({"step": "analyse", "content": "The user is asking for the sum of two numbers, 4 and 6, which is a basic arithmetic addition problem."})},
      {'role': 'assistant', 'content': json.dumps( {"step": "think", "content": "To compute 4 + 6, perform a straightforward numeric addition."})},
      {'role': 'assistant', 'content': json.dumps( {"step": "output", "content": "10"} )},
      {'role': 'assistant', 'content': json.dumps( {"step": "validate", "content": "The sum 4 + 6 equals 10. This is a straightforward addition."} )},
    ],
    text={
    "format": {
      "type": "json_schema",
      "name": "person",
      "strict": True,
      "schema": {
        "type": "object",
        "properties": {
          "step": {
            "type": "string",
          },
          "content": {
            "type": "string",
          }
        },
        "required": [
          "step",
          "content"
        ],
        "additionalProperties": False
      }
    }
  }
)

response_text = response.output_text

print("\n\n",response_text, '\n\n')

