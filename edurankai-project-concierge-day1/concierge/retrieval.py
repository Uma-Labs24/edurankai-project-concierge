import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TfidfRetriever:
    def __init__(self, chunks):
        self.chunks = list(chunks)
        if not self.chunks: raise ValueError("Cannot index an empty corpus")
        self.vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1,2))
        self.matrix = self.vectorizer.fit_transform([c.text for c in self.chunks])

    def search(self, query: str, top_k: int=3) -> list[dict]:
        if not query.strip(): return []
        qv = self.vectorizer.transform([query])
        scores = cosine_similarity(qv, self.matrix).ravel()
        indices = np.argsort(scores)[::-1][:max(1,top_k)]
        return [{"chunk_id":self.chunks[i].chunk_id,"source":self.chunks[i].source,
                 "text":self.chunks[i].text,"score":float(scores[i])} for i in indices]
