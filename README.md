# Mini AI Chatbot

A lightweight AI chatbot application built with **React** for the frontend and **FastAPI** for the backend.  
It uses **sentence embeddings** to find the most relevant answers from a local knowledge base and falls back to **Google Gemini AI** for questions outside the knowledge base.

---
## Demo
Check out the working demo of the chatbot:

![demo](https://github.com/user-attachments/assets/86238217-7c7e-4494-af8c-fe772bf25594)

---

## Features

- Semantic search using **Sentence Transformers** (`all-MiniLM-L6-v2`) and cosine similarity.
- Knowledge base stored in **JSON**.
- Fallback to **Google Gemini AI** for unanswered questions.
- Responsive and modern chat UI built with **React**.
- CORS enabled in FastAPI for smooth frontend-backend communication.
- Persistent chat history saved locally.

---

## Tech Stack

- **Frontend:** React
- **Backend:** FastAPI, Python
- **NLP & AI:**
  - Sentence Transformers (`all-MiniLM-L6-v2`)
  - scikit-learn (`cosine_similarity`)
  - Google Generative AI (Gemini)
- **Other Tools:** dotenv for environment variable

---

## Setup

### Backend

1. Navigate to the backend folder:
```bash
cd backend
````

2. Install dependencies:

```bash
pip install fastapi uvicorn sentence-transformers scikit-learn python-dotenv google-generativeai
```

3. Add your **Google Gemini API key** in a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

4. Run the FastAPI server:

```bash
uvicorn app:app --reload
```

Backend will run at `http://127.0.0.1:8000`.

---

### Frontend

1. Navigate to the frontend folder:

```bash
cd chatbot-frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the development server:

```bash
npm run dev
```

Frontend will run at `http://localhost:5173` (or the port shown in your terminal).

---

## Usage

1. Open the frontend URL in your browser.
2. Type a question in the chat input.
3. The chatbot will:

   * Search the **local knowledge base** for the most similar question using cosine similarity.
   * If no close match is found, query **Google Gemini AI** for an answer.

---

## Example

**Knowledge Base Entry:**

```json
{
  "question": "How do I reset my password?",
  "answer": "Go to settings and click reset password."
}
```

**User Input:** `I forgot my password.`
**Bot Response:** `Go to settings and click reset password.`

If no match is found, the bot provides an AI-generated answer.

---

## Notes

* Ensure the backend is running before starting the frontend.
* Customize the `knowledge_base.json` with your own Q&A pairs.
* You can adjust the **similarity threshold** in `main.py` for more or less strict matching.
* For Google Gemini fallback, you need a valid API key from the official site.

---

