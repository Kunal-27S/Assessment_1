from load_documents import load_documents
from clean_documents import clean_documents
from chunk_documents import chunk_documents
from save_chunks import save_chunks


def process_documents():

    documents = load_documents()

    documents = clean_documents(documents)

    chunks = chunk_documents(documents)

    save_chunks(chunks)

    print("Processing complete.")


if __name__ == "__main__":

    process_documents()