import json
from retrieval.qa_system import build_qa_system, format_response
def compute_metrics(results):
total = len(results)
citation_count = sum(
1 for r in results
if "Citations:" in r
)
abstain_count = sum(
1 for r in results
if "I don't have that information" in r
)
citation_rate = citation_count / total
abstention_rate = abstain_count / total
print("\nEvaluation Results")
print("------------------")
print("Total queries:", total)
print("Citation coverage rate:", citation_rate)
print("Abstention rate:", abstention_rate)
def run_evaluation():
qa = build_qa_system()
with open("evaluation/test_queries.json") as f:
queries = json.load(f)
results = []
for q in queries:
query = q["query"]
print("\nRunning:", query)
result = qa.invoke({"query": query})
formatted = format_response(result)
print(formatted)
results.append(formatted)
compute_metrics(results)
if __name__ == "__main__":
run_evaluation()