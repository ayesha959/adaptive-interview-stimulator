import os

KNOWLEDGE_PATH = "data/knowledge"


def load_documents():
    documents = {}

    for filename in os.listdir(KNOWLEDGE_PATH):

        if filename.endswith(".txt"):

            path = os.path.join(KNOWLEDGE_PATH, filename)

            with open(path, "r", encoding="utf-8") as file:
                documents[filename] = file.read()

    return documents