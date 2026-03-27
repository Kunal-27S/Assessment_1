from retrieval.retriever import get_retriever


def main():

    retriever = get_retriever()

    query = "What are prerequisites for Machine Learning?"

    results = retriever.invoke(query)

    print("\nTop Results:\n")

    for i, doc in enumerate(results):

        print("Result", i + 1)
        print(doc.page_content)
        print(doc.metadata)
        print("-" * 50)


if __name__ == "__main__":
    main()