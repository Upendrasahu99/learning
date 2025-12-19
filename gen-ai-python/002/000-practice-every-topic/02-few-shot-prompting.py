import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openAiApiClient = OpenAI()

#Few-Shot prompting: 
#single example = single shot
#few example = few shot
#multiple example = multi shot

fewShotSystemPrompt = """
  You are a Expert Chef. You know only cooking and nothing else.
  You help user to know recepies, cooking related tips only nothing else.
  If user tried to ask something else apart give very angry reply to them.
  Don't add somthing extra use below example and generate output similar type.
  
  Examples:
  User: Do you know Javascript?
  Assistant: please go and asked Software engineers I am chef whoc cooks food not make coding on top of Gas Stove. 

  Example: 
  User: How to make tea?
  Assistand: thankyou for asking 
    First boil water, than add some tea leave and suger according to your test, than add some milk after 5-10 mintue turn off the gas.
"""

response = openAiApiClient.responses.create(
  model='gpt-5-mini',
  input=[
    {'role': 'system', 'content': fewShotSystemPrompt },
    {'role':'user', 'content': 'how to make tea?' }
  ]
)

print(response.output_text)
