import requests,os,json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# HEADERS = {'Authorization' : f"Bearer {os.getenv('HF_TOKEN')}"}
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_entities(text: str):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a Named Entity Recognition expert. Extract all named entities from the text and respond ONLY in this exact JSON format: [{\"text\": \"entity name\", \"label\": \"PERSON or ORG or GPE or DATE or MONEY or PRODUCT\"}]. Nothing else. No explanation."
                },
                {
                    "role": "user",
                    "content": f"Extract entities: {text}"
                }
            ],
            temperature=0.1
        )
        result = json.loads(response.choices[0].message.content)
        return result
    except Exception as e:
        return [{"text": "unavailable", "label": str(e)}]