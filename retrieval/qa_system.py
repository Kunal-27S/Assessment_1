from langchain_ollama import ChatOllama
from langchain.chains import RetrievalQA

from retrieval.retriever import get_retriever


def build_qa_system():

    # Load retriever
    retriever = get_retriever()

    # Load local LLM
    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0,
        num_predict=64,
        keep_alive="10m"
    )

    # Build QA chain
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    print("QA system ready")

    return qa