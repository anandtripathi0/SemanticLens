# 🔍 SemanticLens — AI Semantic Analysis Dashboard

SemanticLens is a full-stack AI-powered text analysis web app that performs deep semantic analysis using LLaMA 3.3 70B via Groq API. Built with React and FastAPI.

🌐 **Live Demo:** [semanticlens.vercel.app](https://semanticlens.vercel.app)  
⚡ **API Docs:** [semanticlens-api.onrender.com/docs](https://semanticlens-api.onrender.com/docs)

---

## ✨ Features

- 😊 **Sentiment Analysis** — Positive, Negative, Neutral detection with confidence score
- 🏷️ **Named Entity Recognition** — Extracts Person, Organization, Location, Date entities
- 🔑 **Keyword Extraction** — Top keywords using TF-IDF algorithm
- 📄 **Text Summarization** — Concise 2-3 sentence summary of long text
- 🔍 **Semantic Similarity** — Compare two texts with cosine similarity score

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React.js, Vite, Axios |
| Backend | FastAPI, Python |
| AI Model | LLaMA 3.3 70B via Groq API |
| ML/NLP | scikit-learn (TF-IDF, Cosine Similarity) |
| Frontend Deploy | Vercel |
| Backend Deploy | Render |

---

## 📁 Project Structure

```
semanticlens/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── analyzer/
│       ├── __init__.py
│       ├── sentiment.py
│       ├── ner.py
│       ├── keywords.py
│       ├── similarity.py
│       └── summarizer.py
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── App.css
│   ├── package.json
│   └── vite.config.js
├── .gitignore
└── README.md
```

---

## 🚀 Run Locally

### Prerequisites
- Python 3.10+
- Node.js 18+
- Groq API Key — [console.groq.com](https://console.groq.com)

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
pip install -r requirements.txt
```

Create `.env` file in `backend/` folder:
```
GROQ_API_KEY=your_groq_api_key_here
```

Run backend:
```bash
uvicorn main:app --reload
```

API runs at `http://localhost:8000`  
Swagger docs at `http://localhost:8000/docs`

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

App runs at `http://localhost:5173`

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/analyze` | Full semantic analysis |

### Request Body
```json
{
  "text": "Your text here",
  "top_keywords": 5,
  "include_summary": true,
  "similarity_text": null
}
```

### Response
```json
{
  "sentiment": { "label": "POSITIVE", "score": 0.95 },
  "entities": [{ "text": "Elon Musk", "label": "PERSON" }],
  "keywords": ["tesla", "ai", "technology"],
  "summary": "Short summary of the text.",
  "similarity": null
}
```

---

## 🌍 Deployment

| Service | Platform | URL |
|---|---|---|
| Frontend | Vercel | semanticlens.vercel.app |
| Backend | Render | semanticlens-api.onrender.com |

**Backend Environment Variables on Render:**
```
GROQ_API_KEY = your_groq_api_key_here
```

**Frontend Environment Variables on Vercel:**
```
VITE_API_URL = https://semanticlens-api.onrender.com
```

---

## 👨‍💻 Author

**Anand Tripathi**  
BCA Student — Dr. Virendra Swaroop Institute of Computer Studies, Kanpur  
[GitHub](https://github.com/anandtripathi0) • [LinkedIn](https://linkedin.com/in/anand-tripathi01)

---
