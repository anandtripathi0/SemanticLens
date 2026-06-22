import os, requests
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_sentiment(text: str):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a sentiment analysis expert. Analyze the sentiment of the given text and respond ONLY in this exact JSON format: {\"label\": \"POSITIVE\" or \"NEGATIVE\" or \"NEUTRAL\", \"score\": 0.0 to 1.0}. Nothing else."
                },
                {
                    "role": "user",
                    "content": f"Analyze sentiment: {text}"
                }
            ],
            temperature=0.1
        )
        import json
        result = json.loads(response.choices[0].message.content)
        return {"label": result["label"], "score": round(result["score"], 3)}
    except Exception as e:
        return {"label": "unavailable", "score": 0.0, "error": str(e)}
