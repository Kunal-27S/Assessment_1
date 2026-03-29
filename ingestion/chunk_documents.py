from langchain.schema import Document

def chunk_documents(docs):

    chunks = []

    for i, doc in enumerate(docs):

        text = doc["text"]

        # Split by course
        #courses = text.split("Course:")
        # Split by divider line
        courses = text.split(
            "--------------------------------------------------"
        )


        for j, course in enumerate(courses):

            course = course.strip()

            if not course:
                continue

            chunk = Document(
                page_content="Course: " + course,

                metadata={
                    "source": doc.get("source", "unknown"),
                    "section": "course",
                    "chunk_id": f"{i}_{j}"
                }
            )

            chunks.append(chunk)

    print("Total chunks:", len(chunks))

    return chunks