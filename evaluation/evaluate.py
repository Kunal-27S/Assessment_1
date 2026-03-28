import json

from retrieval.qa_system import build_qa_system, format_response


def compute_metrics(results):

    total = len(results)

    citation_count = 0
    abstain_count = 0

    for r in results:

        # Check real citations
        if "Citations:" in r and "None" not in r:
            citation_count += 1

        # Check abstention
        if "I don't have that information" in r:
            abstain_count += 1

    citation_rate = citation_count / total
    abstention_rate = abstain_count / total

    print("\nEvaluation Results")
    print("------------------")
    print("Total queries:", total)
    print("Citation coverage rate:", round(citation_rate, 2))
    print("Abstention rate:", round(abstention_rate, 2))


def run_evaluation():

    qa = build_qa_system()

    with open("evaluation/test_queries.json") as f:
        queries = json.load(f)

    results = []

    for q in queries:

        query = q["query"]

        print("\nRunning:", query)

        result = qa.invoke({
            "query": query
        })

        formatted = format_response(result)

        print(formatted)

        results.append(formatted)

    compute_metrics(results)


if __name__ == "__main__":
    run_evaluation()