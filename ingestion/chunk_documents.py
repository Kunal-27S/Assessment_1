from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100


def chunk_documents(docs):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = []

    for i, doc in enumerate(docs):

        # Split text into chunks
        split_texts = splitter.split_text(doc["text"])

        for j, text in enumerate(split_texts):

            chunk = Document(
                page_content=text,

                metadata={
                    "source": doc.get("source", "unknown"),
                    "section": doc.get("section", "unknown"),
                    "chunk_id": f"{i}_{j}"
                }
            )

            chunks.append(chunk)

    # IMPORTANT: return outside the loop
    return chunks