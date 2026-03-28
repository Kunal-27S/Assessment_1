from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

VECTOR_STORE_PATH = "data/vectorstore"


def get_retriever():

    # Fast, lightweight embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Load FAISS index
    vector_store = FAISS.load_local(
        VECTOR_STORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Optimized retriever settings
    retriever = vector_store.as_retriever(
        search_kwargs={
            "k": 2
        }
    )

    return retriever