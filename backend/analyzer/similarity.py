from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def similarity(text1: str, text2: str):
    try:
        vectorizer = TfidfVectorizer()
        tfidf = vectorizer.fit_transform([text1, text2])
        score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
        return round(float(score), 3)
    except Exception as e:
        return None