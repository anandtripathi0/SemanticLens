import { useState } from "react"
import axios from "axios"
import "./App.css"

const API = import.meta.env.VITE_API_URL || "http://localhost:8000"

export default function App() {
  const [text, setText] = useState("")
  const [simText, setSimText] = useState("")
  const [keywords, setKeywords] = useState(5)
  const [summary, setSummary] = useState(true)
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")

  const analyze = async () => {
    if (text.trim().length < 5) {
      setError("Please enter at least 5 characters.")
      return
    }
    setError("")
    setLoading(true)
    setResult(null)
    try {
      const res = await axios.post(`${API}/analyze`, {
        text,
        top_keywords: keywords,
        include_summary: summary,
        similarity_text: simText || null,
      })
      setResult(res.data)
    } catch (e) {
      setError("API error. Make sure backend is running.")
    }
    setLoading(false)
  }

  const sentimentColor = (label) => {
    if (label === "POSITIVE") return "#16a34a"
    if (label === "NEGATIVE") return "#dc2626"
    return "#d97706"
  }

  return (
    <div className="app">
      <header>
        <h1>🧠 SemanticLens</h1>
        <p>Semantic Analysis Dashboard</p>
      </header>

      <div className="card">
        <label>Enter Text</label>
        <textarea
          rows={5}
          placeholder="Paste any text here to analyze..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />

        <label>Compare with (optional)</label>
        <textarea
          rows={2}
          placeholder="Enter a second text to check similarity..."
          value={simText}
          onChange={(e) => setSimText(e.target.value)}
        />

        <div className="options">
          <div className="option-item">
            <label>Keywords: {keywords}</label>
            <input type="range" min={1} max={20} value={keywords}
              onChange={(e) => setKeywords(Number(e.target.value))} />
          </div>
          <div className="option-item">
            <label>
              <input type="checkbox" checked={summary}
                onChange={(e) => setSummary(e.target.checked)} />
              Include Summary
            </label>
          </div>
        </div>

        {error && <p className="error">{error}</p>}

        <button onClick={analyze} disabled={loading}>
          {loading ? "Analyzing..." : "Analyze Text →"}
        </button>
      </div>

      {result && (
        <div className="results">

          <div className="card result-card">
            <h3>😊 Sentiment</h3>
            <div className="sentiment-badge"
              style={{ background: sentimentColor(result.sentiment.label) }}>
              {result.sentiment.label}
            </div>
            <p className="score">Confidence: {(result.sentiment.score * 100).toFixed(1)}%</p>
          </div>

          <div className="card result-card">
            <h3>🏷️ Named Entities</h3>
            {result.entities.length === 0
              ? <p className="muted">No entities found</p>
              : result.entities.map((e, i) => (
                <span key={i} className="entity-tag">
                  {e.text} <small>{e.label}</small>
                </span>
              ))}
          </div>

          <div className="card result-card">
            <h3>🔑 Keywords</h3>
            <div className="keywords">
              {result.keywords.map((k, i) => (
                <span key={i} className="keyword-tag">{k}</span>
              ))}
            </div>
          </div>

          {result.summary && (
            <div className="card result-card full">
              <h3>📄 Summary</h3>
              <p>{result.summary}</p>
            </div>
          )}

          {result.similarity !== null && (
            <div className="card result-card">
              <h3>🔍 Similarity Score</h3>
              <div className="sim-score">
                {(result.similarity * 100).toFixed(1)}%
              </div>
              <p className="muted">
                {result.similarity > 0.7 ? "Very similar" :
                 result.similarity > 0.4 ? "Somewhat similar" : "Not similar"}
              </p>
            </div>
          )}
        </div>
      )}
    </div>
  )
}