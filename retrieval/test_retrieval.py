from retrieval.load_vector_store import load_vector_store


def test():

    vector_store = load_vector_store()

    query = "What are prerequisites for Machine Learning?"

    results = vector_store.similarity_search(
        query,
        k=5
    )

    print("\nTop Results:\n")

    for i, doc in enumerate(results):

        print("Result", i + 1)
        print(doc.page_content)
        print(doc.metadata)
        print("-" * 50)


if __name__ == "__main__":
    test()