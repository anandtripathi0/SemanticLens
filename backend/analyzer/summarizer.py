import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def summarizer(text: str):
    try:
        if len(text.split()) < 5:
            return "Text too short to summarize."
            

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"Summarize: {text}",
            config=types.GenerateContentConfig(
                system_instruction="You are a text summarization expert. Summarize the given text in 2-3 clear sentences. Respond with ONLY the summary, nothing else.",
                temperature=0.3
            ),
        )
        

        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
