from retrieval.qa_system import build_qa_system


def main():

    qa = build_qa_system()

    while True:

        question = input("\nAsk a question: ")

        if question == "exit":
            break

        for chunk in qa.stream({"query": question}):
            if "result" in chunk:
                print(chunk["result"], end="", flush=True)

        print()



if __name__ == "__main__":
    main()