from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


VECTORSTORE_PATH = "vectorstore"


def load_vector_store():

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vector_store = FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    print("Vector store loaded")

    return vector_store


def get_retriever():

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 5}
    )

    return retriever