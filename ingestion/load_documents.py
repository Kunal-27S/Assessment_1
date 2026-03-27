import os

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredHTMLLoader
)

def load_documents(data_path="data/raw"):

    documents = []

    for filename in os.listdir(data_path):

        file_path = os.path.join(data_path, filename)

        if filename.endswith(".pdf"):
            loader = PyPDFLoader(file_path)

        elif filename.endswith(".html"):
            loader = UnstructuredHTMLLoader(file_path)

        elif filename.endswith(".txt"):
            loader = TextLoader(file_path)

        else:
            continue

        docs = loader.load()

        documents.extend(docs)

    print("Loaded documents:", len(documents))

    return documents


if __name__ == "__main__":

    docs = load_documents()
    print(docs[0])