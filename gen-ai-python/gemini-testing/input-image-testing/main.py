from google import genai
from dotenv import load_dotenv
from google.genai import types
from pydantic import BaseModel, Field
from typing import List
import json


prompt = f"""दिए गए दस्तावेज़ की छवि का ध्यानपूर्वक विश्लेषण करें और ठीक 5 उच्च गुणवत्ता वाले बहुविकल्पीय प्रश्न बनाएं।

महत्वपूर्ण नियम:
1. सभी प्रश्न, विकल्प और व्याख्याएं केवल शुद्ध हिंदी में लिखें (देवनागरी लिपि में)
2. रोमन/अंग्रेजी शब्दों का बिल्कुल उपयोग न करें
3. प्रत्येक प्रश्न में ठीक 4 विकल्प होने चाहिए (A, B, C, D)
4. केवल एक विकल्प सही होना चाहिए
5. गलत विकल्प प्रशंसनीय लेकिन स्पष्ट रूप से गलत होने चाहिए
6. सही उत्तर के लिए स्पष्ट व्याख्या दें
7. दस्तावेज़ से विभिन्न विषयों को कवर करें
8. प्रश्न स्पष्ट और असंदिग्ध होने चाहिए
9. प्रश्नों की संख्या 1 से शुरू करें
10. समझ का परीक्षण करने वाले प्रश्न बनाएं, न कि केवल याद रखने के

प्रश्न के प्रकार:
- तथ्यात्मक प्रश्न (What/Who/When)
- अवधारणात्मक प्रश्न (Why/How)
- अनुप्रयोग आधारित प्रश्न (उदाहरण/स्थिति)
- विश्लेषणात्मक प्रश्न (तुलना/अंतर)

दस्तावेज़ में उपलब्ध सामग्री के आधार पर 5 प्रश्न बनाएं।"""

with open('test-text-image.jpeg', 'rb') as f:
  image_bytes = f.read()

load_dotenv()

class Question(BaseModel):
  question: str
  option_a: str
  option_b: str
  option_c: str
  option_d: str
  correct_answer: str
  explanation: str

class MCQResponse(BaseModel):
  total_question:int = Field(description='Total number of question')
  questios: List[Question]

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response =   response = client.models.generate_content(
    model='gemini-2.5-flash-lite',
    contents=[
      types.Part.from_bytes(
        data=image_bytes,
        mime_type='image/jpeg',
      ),
      prompt
    ],
    config={
      'response_mime_type': 'application/json',
      'response_json_schema': MCQResponse.model_json_schema()
    }
  )

response_text = response.text.strip()

response_dictonary = json.loads(response_text)

print(response_text)