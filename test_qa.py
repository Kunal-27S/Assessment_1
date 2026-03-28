from retrieval.qa_system import build_qa_system


def main():

    qa = build_qa_system()

    while True:

        question = input("\nAsk a question: ")

        if question == "exit":
            break

        answer = qa.invoke(
            {"query": question}
        )

        print("\nAnswer:\n")

        print(answer["result"])


if __name__ == "__main__":
    main()