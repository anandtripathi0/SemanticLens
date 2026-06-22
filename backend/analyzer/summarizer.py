import os, json
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarizer(text: str):
    try:
        if len(text.split()) < 5:
            return "Text too short to summarize."
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a text summarization expert. Summarize the given text in 2-3 clear sentences. Respond with ONLY the summary, nothing else."
                },
                {
                    "role": "user",
                    "content": f"Summarize: {text}"
                }
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"