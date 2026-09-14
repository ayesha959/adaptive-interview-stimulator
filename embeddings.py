from sklearn.feature_extraction.text import TfidfVectorizer


class EmbeddingStore:

    def __init__(self, documents):

        self.names = list(documents.keys())
        self.texts = list(documents.values())

        self.vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        self.vectors = self.vectorizer.fit_transform(self.texts)

    def search(self, query, top_k=2):

        query_vector = self.vectorizer.transform([query])

        scores = self.vectors @ query_vector.T

        scores = scores.toarray().flatten()

        indexes = scores.argsort()[::-1][:top_k]

        results = []

        for index in indexes:

            results.append({
                "document": self.names[index],
                "content": self.texts[index],
                "score": float(scores[index])
            })

        return results