from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def extract_keyword(text:str,top_n:int=5):
    vectorizer = TfidfVectorizer(stop_words='english',max_features=100)
    tfidf = vectorizer.fit_transform([text])
    scores = zip(vectorizer.get_feature_names_out(), np.asarray(tfidf.sum(axis=0)).ravel())
    sorted_words = sorted(scores,key=lambda x:x[1],reverse=True)
    return [word for word , _ in sorted_words[:top_n]]


