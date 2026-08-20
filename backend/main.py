from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel,Field
from typing import Optional
from analyzer import (
    analyze_sentiment, extract_entities,
    extract_keyword, similarity, summarizer
)

app = FastAPI(title="semantic analysis")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",
        "http://localhost:5173",
        "https://semantic-lens-21ao.vercel.app"
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    text: str = Field(..., min_length=5, max_length=10000)
    top_keywords: int = Field(default=5, ge=1, le=20)
    include_summary: bool = True
    similarity_text: Optional[str] = None

@app.post('/analyze')
def analyze(req:AnalyzeRequest):
    result = {
        'sentiment':analyze_sentiment(req.text),
        "entities":   extract_entities(req.text),
        "keywords":   extract_keyword(req.text, req.top_keywords),
        "summary":    summarizer(req.text) if req.include_summary else None,
        'similarity': similarity(req.text,req.similarity_text)
                    if req.similarity_text else None,
    }

    return result