import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def extract_entities(text: str):
    try:
       
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"Extract entities: {text}",
            config=types.GenerateContentConfig(
                system_instruction="You are a Named Entity Recognition expert. Extract all named entities from the text and respond ONLY in this exact JSON format: [{\"text\": \"entity name\", \"label\": \"PERSON or ORG or GPE or DATE or MONEY or PRODUCT\"}]. Nothing else. No explanation.",
                temperature=0.1,

                response_mime_type="application/json" 
            ),
        )
        

        result = json.loads(response.text)
        return result
    except Exception as e:
        return [{"text": "unavailable", "label": str(e)}]
