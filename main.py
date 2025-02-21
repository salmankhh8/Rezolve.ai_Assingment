from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import spacy
from textblob import TextBlob
import subprocess
from huggingface_hub import InferenceClient
from fastapi.middleware.cors import CORSMiddleware
import requests
from starlette.middleware.sessions import SessionMiddleware
from fastapi.requests import Request
import uuid
from fastapi.responses import JSONResponse


app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="AASDFGHJ@#$%^&*&^DFGH")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


model_name = "en_core_web_sm"
try:
    nlp = spacy.load(model_name)
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", model_name])
    nlp = spacy.load(model_name)

HF_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
HF_HEADERS = {"Authorization": "Bearer hrXXXXXXXXXXXX"} #removing my original huging face access token due to Security reasons

sessions = {}


def query_huggingface(payload):
    response = requests.post(HF_API_URL, headers=HF_HEADERS, json=payload)
    return response.json()

class TextRequest(BaseModel):
    text: str

class TextProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        
    def summarize_text(self, text: str) -> str:
        response = query_huggingface({"inputs": text})
        return response[0]["summary_text"] if isinstance(response, list) else "Summarization failed"

    def extract_keywords(self, text: str) -> List[str]:
        doc = self.nlp(text)
        return list(set([ent.text for ent in doc.ents]))

    def analyze_sentiment(self, text: str) -> str:
        analysis = TextBlob(text).sentiment.polarity
        return "positive" if analysis > 0 else "negative" if analysis < 0 else "neutral"

@app.post("/process")
def process_text(request: TextRequest, req: Request):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    session_id = req.cookies.get("session_id")
    if not session_id:
        session_id = str(uuid.uuid4())
    
    if session_id not in sessions:
        sessions[session_id] = []
    
    processor = TextProcessor()  # Create a new instance for each request
    summary = processor.summarize_text(request.text)
    keywords = processor.extract_keywords(request.text)
    sentiment = processor.analyze_sentiment(request.text)
    
    result = {"text": request.text, "summary": summary, "keywords": keywords, "sentiment": sentiment}
    sessions[session_id].append(result)
    
    response = JSONResponse(content=result)
    response.set_cookie(key="session_id", value=session_id)
    return response


@app.get("/history")
def get_history(req: Request) -> List[Dict]:
    session_id = req.cookies.get("session_id")
    if session_id and session_id in sessions:
        return sessions[session_id]
    return []
