import json


def save_chunks(chunks):

    data = []

    for chunk in chunks:

        item = {
            "text": chunk.page_content,
            "metadata": chunk.metadata
        }

        data.append(item)

    with open("data/processed/chunks.json", "w") as f:

        json.dump(data, f, indent=2)

    print("Chunks saved.")