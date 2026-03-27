import os
import json

from langchain.schema import Document

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


CHUNKS_PATH = "data/processed/chunks.json"
VECTORSTORE_PATH = "vectorstore"


def load_chunks():

    with open(CHUNKS_PATH, "r") as f:
        data = json.load(f)

    documents = []

    for item in data:

        doc = Document(
            page_content=item["text"],
            metadata=item["metadata"]
        )

        documents.append(doc)

    print("Loaded chunks:", len(documents))

    return documents


def create_embeddings():

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    print("Embeddings model loaded")

    return embeddings


def build_vector_store(documents, embeddings):

    vector_store = FAISS.from_documents(
        documents,
        embeddings
    )

    print("Vector store created")

    return vector_store


def save_vector_store(vector_store):

    os.makedirs(VECTORSTORE_PATH, exist_ok=True)

    vector_store.save_local(
        VECTORSTORE_PATH
    )

    print("Vector store saved")


def main():

    print("Starting vector database build")

    documents = load_chunks()

    embeddings = create_embeddings()

    vector_store = build_vector_store(
        documents,
        embeddings
    )

    save_vector_store(vector_store)

    print("Index build complete")


if __name__ == "__main__":
    main()