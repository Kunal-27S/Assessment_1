from retrieval.qa_system import build_qa_system, format_response

REQUIRED_FIELDS = [
    "major",
    "completed_courses",
    "term"
]


def check_missing(profile):

    missing = []

    for field in REQUIRED_FIELDS:
        if field not in profile:
            missing.append(field)

    return missing


def run_app():

    qa = build_qa_system()

    # Example empty student profile
    student_profile = {}

    missing = check_missing(student_profile)

    # Clarifying questions requirement
    if missing:

        print("\nClarifying questions:")

        for m in missing:
            print(f"- Please provide your {m}")

        print()

    while True:

        question = input("Ask a question: ")

        if question.lower() in ["exit", "quit"]:
            break

        result = qa.invoke({"query": question})

        formatted = format_response(result)

        print(formatted)


if __name__ == "__main__":
    run_app()