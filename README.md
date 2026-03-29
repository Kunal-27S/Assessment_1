# Retrieval-Augmented Generation (RAG) Question Answering System

## Overview

This project implements a **Retrieval-Augmented Generation (RAG) Question Answering system** using LangChain, FAISS, and local language models. The system retrieves relevant information from a custom dataset and generates grounded answers using citations from the retrieved documents.

The pipeline demonstrates a production-style architecture commonly used in modern AI systems and is designed to be reproducible, modular, and easy to evaluate.

---

## Key Features

* Document ingestion and preprocessing
* Structured document chunking
* Vector embeddings using HuggingFace models
* FAISS vector database for fast similarity search
* Retrieval-based question answering
* Local LLM integration via Ollama
* Evaluation metrics for system performance
* Modular and extensible codebase

---

## System Architecture

User Query
↓
Retriever (FAISS)
↓
Relevant Document Chunks
↓
Language Model (LLM)
↓
Final Answer with Citations

### Components

1. **Data Loader**

   * Loads raw documents from the dataset
   * Prepares text for processing

2. **Text Splitter**

   * Splits documents into smaller chunks
   * Ensures efficient retrieval

3. **Embeddings Generator**

   * Converts text into vector representations

4. **Vector Store (FAISS)**

   * Stores embeddings for fast similarity search

5. **Retriever**

   * Finds the most relevant document chunks

6. **LLM Response Generator**

   * Generates answers using retrieved context

7. **Evaluation Module**

   * Measures system performance

---

## Project Structure

```
project_root/
│
├── app.py
├── build_index.py
├── requirements.txt
│
├── data/
│   ├── raw/
│   │   └── courses.txt
│   │
│   └── vectorstore/
│       ├── index.faiss
│       └── index.pkl
│
├── retrieval/
│   ├── retriever.py
│   ├── qa_system.py
│   └── text_splitter.py
│
├── evaluation/
│   ├── test_queries.json
│   └── run_evaluation.py
│
└── README.md
```

---

## Installation

### Step 1 — Clone the Repository

```
git clone <repository-url>
cd project
```

---

### Step 2 — Create Virtual Environment

Linux / macOS:

```
python3 -m venv venv
source venv/bin/activate
```

Windows:

```
python -m venv venv
venv\Scripts\activate
```

---

### Step 3 — Install Dependencies

```
pip install -r requirements.txt
```

---

## Requirements

Example requirements file:

```
langchain
langchain-community
langchain-huggingface
langchain-ollama
faiss-cpu
sentence-transformers
numpy
pydantic
python-dotenv
```

---

## Building the Vector Index

Run the following command to create embeddings and build the FAISS index:

```
python build_index.py
```

Expected output:

```
Embeddings model loaded
Vector store created
Vector store saved
Index build complete
```

Generated files:

```
data/vectorstore/index.faiss

data/vectorstore/index.pkl
```

---

## Running the Application

```
python app.py
```

Example interaction:

```
Enter your question:
What are the prerequisites for Machine Learning?

Answer:
The prerequisites for Machine Learning are Linear Algebra and Probability.

Citations:
Course: CS401
```

---

## Running the Retriever Test

```
python test_retriever.py
```

This command verifies:

* Retrieval functionality
* Vector database integrity
* Chunking correctness

---

## Running Evaluation

```
python evaluation/run_evaluation.py
```

This script evaluates system performance using predefined test queries.

---

## Evaluation Metrics

The evaluation module computes:

### Citation Coverage Rate

Measures how often responses include citations.

Formula:

```
Citation Rate = Responses with Citations / Total Responses
```

---

### Abstention Rate

Measures how often the system correctly refuses to answer when information is unavailable.

Formula:

```
Abstention Rate = Abstained Responses / Total Responses
```

---

## Example Test Queries

```
[
    {"query": "What is the credit value of Machine Learning?"},
    {"query": "What are the prerequisites for Probability?"},
    {"query": "Does the system support distributed computing?"}
]
```

---

## Configuration

### Chunk Size

```
CHUNK_SIZE = 500
```

### Chunk Overlap

```
CHUNK_OVERLAP = 100
```

These parameters control:

* Retrieval accuracy
* Memory usage
* Latency

---

## Supported Models

Embeddings Model:

```
all-MiniLM-L6-v2
```

Language Model:

```
llama3.2
```

---

## Troubleshooting

### Error: index.faiss not found

Cause:

The vector index has not been created.

Solution:

```
python build_index.py
```

---

### Error: Vectorstore directory missing

Cause:

Incorrect file path.

Solution:

Verify directory structure:

```
ls data/vectorstore
```

---

### Error: Deprecated HuggingFaceEmbeddings

Cause:

Old import path.

Solution:

Install updated package:

```
pip install langchain-huggingface
```

Update import:

```
from langchain_huggingface import HuggingFaceEmbeddings
```

---

### Retrieval Returns Multiple Courses in One Result

Cause:

Large document chunks.

Solution:

Rebuild index after updating chunking logic:

```
rm -rf data/vectorstore
python build_index.py
```

---

## Performance Characteristics

Typical performance on CPU:

Latency:

```
1–3 seconds per query
```

Memory Usage:

```
~500 MB
```

Vector Search Time:

```
< 100 milliseconds
```

---

## Design Decisions

### Why FAISS?

* Fast similarity search
* Lightweight
* CPU-friendly
* Industry standard

### Why RAG?

* Reduces hallucinations
* Improves answer accuracy
* Enables citations
* Works with private data

---

## Future Improvements

Possible extensions:

* Hybrid search (BM25 + embeddings)
* Metadata filtering
* Streaming responses
* Web interface
* API deployment
* Batch query support
* GPU acceleration
* Distributed vector database

---

## Reproducibility

To reproduce results on a new machine:

```
git clone <repo>
cd project

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python build_index.py
python app.py
```

---


## License

This project is intended for educational and evaluation purposes.
