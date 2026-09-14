from rag.documents import load_documents
from rag.embeddings import EmbeddingStore


documents = load_documents()

store = EmbeddingStore(documents)


def retrieve_context(query):

    results = store.search(query)

    context = ""

    for result in results:

        context += f"""
SOURCE: {result['document']}

{result['content']}

"""

    return context