from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunk_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    print("Total chunks:", len(chunks))

    return chunks

def add_metadata(chunks):

    for i, chunk in enumerate(chunks):

        chunk.metadata["chunk_id"] = i

    return chunks