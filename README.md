# Base of Knowledge (RAG) for AI Companion Jois

This project implements a local Retrieval-Augmented Generation (RAG) system for the personal assistant Jois. The system allows the Gemini model to answer user questions based strictly on loaded internal documents, mitigating hallucinations by grounding responses in the provided context.

## Project Structure

* `__pycache__/` — Directory containing compiled Python bytecode files (automatically generated).
* `.venv/` — Isolated Python virtual environment containing project-specific dependencies.
* `chroma_langchain_db/` — Local vector database storing embedded document chunks.
* `knowledge_base/` — Directory containing raw text knowledge documents (.txt) for the Jois companion.
* `.env` — Configuration file for private API keys and environment variables (excluded from Git).
* `.gitignore` — Specifies intentionally untracked files that Git should ignore.
* `api_key.py` — Script handling environment variable loading and Gemini model initialization.
* `emb_model.py` — Script configuring the text embedding model used for vectorization.
* `langsmith_settings.py` — Configuration for LangSmith tracing, logging, and evaluation metrics.
* `load_split_doc.py` — Module responsible for loading raw text files and splitting them into optimal chunks.
* `rag_agent.py` — Core logic assembling the context retrieval mechanism and the LangChain conversational agent.
* `storing_doc.py` — Execution script that invokes document chunking and populates the Chroma vector database.
* `test.py` — Automated testing suite executing the 10-question evaluation benchmark against the RAG system.
* `vector_store.py` — Interface script managing connections, searches, and configurations for the ChromaDB store.
---

## Installation and Setup

### 1. Navigate to the Project Directory
Open your terminal and ensure you are inside the root directory of the project:
```bash
cd RAG

```

### 2. Activate the Virtual Environment

Activate the isolated virtual environment using venv:

```bash
source .venv/bin/activate


```
### 3. Install Dependencies

Install all required libraries, including LangChain, ChromaDB, and python-dotenv, using the package manager:

```bash
pip install -r requirements.txt

```

### 4. Configure Environment Variables

Create a file named `.env` in the root directory. Add your secret access tokens without quotes or spaces around the assignment operators:

```env
GEMINI_API_KEY=your_actual_gemini_api_key
LANGSMITH_API_KEY=your_actual_langsmith_api_key
LANGSMITH_TRACING=true

```

---

## Application Usage

### How to Add or Update Documents

1. Place your new text files (.txt) or edit existing ones inside the `knowledge_base/` directory.
2. Run the ingestion script to update the local vector database:

```bash
   python storing_doc.py

```

Note: If the database is already populated and your source documents have not changed, you can skip this step.

### How to Launch the Chat / Test Suite

To execute the automated evaluation suite and verify the RAG system performance across the 10 benchmark questions, run the following command:

```bash
python test.py

```

