from langchain.chains import RetrievalQA
from langchain_ollama import ChatOllama
from retriever import get_retriever


def format_response(result):
    """
    Enforces the mandatory output format.
    """

    answer = result.get("result", "")
    docs = result.get("source_documents", [])

    citations = []

    for doc in docs:
        source = doc.metadata.get("source", "Unknown source")
        section = doc.metadata.get("section", "Unknown section")
        chunk_id = doc.metadata.get("chunk_id", "")

        citation = f"{source} — {section} — chunk {chunk_id}"
        citations.append(citation)

    # Safe abstention
    if not docs:
        return """
Answer / Plan:
I don't have that information in the provided catalog/policies.

Why (requirements/prereqs satisfied):
Information not found in documents.

Citations:
None

Clarifying questions:
None

Assumptions / Not in catalog:
Please check the department website or academic advisor.
"""

    citation_text = "\n".join(citations)

    return f"""
Answer / Plan:
{answer}

Why (requirements/prereqs satisfied):
Based on retrieved catalog information.

Citations:
{citation_text}

Clarifying questions:
None

Assumptions / Not in catalog:
None
"""


def build_qa_system():

    retriever = get_retriever()

    # Optimized for low latency on CPU
    llm = ChatOllama(
        model="llama3.2:3b",

        temperature=0,

        # VERY IMPORTANT for latency
        num_predict=64,
        num_ctx=1024,

        # reuse model in memory
        keep_alive="10m",

        # CPU optimization
        num_thread=8
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa


def run_qa():

    qa = build_qa_system()

    print("System ready. Type 'exit' to quit.\n")

    while True:

        question = input("Ask a question: ")

        if question.lower() in ["exit", "quit"]:
            break

        result = qa.invoke({"query": question})

        formatted = format_response(result)

        print(formatted)


if __name__ == "__main__":
    run_qa()