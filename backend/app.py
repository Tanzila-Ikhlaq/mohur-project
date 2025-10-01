from fastapi import FastAPI
from pydantic import BaseModel
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi.middleware.cors import CORSMiddleware
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("⚠️ GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

app = FastAPI(title="Knowledge Base Chatbot with Gemini Fallback")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

st_model = SentenceTransformer('all-MiniLM-L6-v2')

class Question(BaseModel):
    query: str

with open("knowledge_base.json", "r", encoding="utf-8") as f:
    knowledge_base = json.load(f)

def fallback_gemini(user_input: str):
    model = genai.GenerativeModel("gemini-2.0-flash-001")
    response = model.generate_content(
        f"Generate a short, clear, and direct answer to this question (no extra symbols, no formatting): {user_input}"
    )
    return response.text.strip()

def save_chat(q: str, a: str):
    chat_entry = {"question": q, "answer": a}
    try:
        with open("chat_history.json", "r+", encoding="utf-8") as f:
            history = json.load(f)
            history.append(chat_entry)
            f.seek(0)
            json.dump(history, f, indent=2)
    except FileNotFoundError:
        with open("chat_history.json", "w", encoding="utf-8") as f:
            json.dump([chat_entry], f, indent=2)

@app.post("/ask")
def ask_question(q: Question):
    user_q = q.query.strip()

    base_questions = [v["question"] for v in knowledge_base]
    base_embeddings = st_model.encode(base_questions)
    user_embedding = st_model.encode([user_q])

    simi = cosine_similarity(user_embedding, base_embeddings)[0]
    max_idx = simi.argmax()
    best_score = simi[max_idx]

    threshold = 0.6

    if best_score >= threshold:
        answer = knowledge_base[max_idx]["answer"]
    else:
        answer = fallback_gemini(user_q)

    save_chat(user_q, answer)

    return {
        "question": user_q,
        "answer": answer
    }

