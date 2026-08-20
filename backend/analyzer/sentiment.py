import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_sentiment(text: str):
    try:
      
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"Analyze sentiment: {text}",
            config=types.GenerateContentConfig(
                system_instruction="You are a sentiment analysis expert. Analyze the sentiment of the given text and respond ONLY in this exact JSON format: {\"label\": \"POSITIVE\" or \"NEGATIVE\" or \"NEUTRAL\", \"score\": 0.0 to 1.0}. Nothing else. No explanation.",
                temperature=0.1,
                response_mime_type="application/json" 
            ),
        )
        

        result = json.loads(response.text)
        return {"label": result["label"], "score": round(float(result["score"]), 3)}
        
    except Exception as e:
        return {"label": "unavailable", "score": 0.0, "error": str(e)}
