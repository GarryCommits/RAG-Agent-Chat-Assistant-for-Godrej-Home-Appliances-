# Godrej Smart Appliances RAG Chatbot

A command-line question-answering chatbot that uses retrieval-augmented generation (RAG) to answer questions about Godrej smart home appliances. It retrieves relevant customer-review text from a local vector store and passes that context to a locally served Ollama language model.

## How it works

1. `vector.py` reads `godrej_smart_appliances_rag_dataset.csv` as a tab-delimited file.
2. Each row is indexed as a document made from the product title and review. The rating and product category are stored as metadata.
3. Ollama's `mxbai-embed-large` model creates embeddings, which LangChain stores in the persistent Chroma database at `chroma_langchain_db`.
4. `main.py` accepts questions in a terminal loop. For each question, it retrieves up to five relevant documents and asks the Ollama `llama3.2` model to answer using those documents as context.
5. Enter `q` to exit.

## Requirements

- Python with the packages listed in `requirments.txt`
- [Ollama](https://ollama.com/) installed and running
- The Ollama models `llama3.2` and `mxbai-embed-large` available locally

## Run

From the project directory, install the Python dependencies and make sure both models are available in Ollama:

```powershell
pip install -r requirments.txt
ollama pull llama3.2
ollama pull mxbai-embed-large
python main.py
```

The CSV file and the `chroma_langchain_db` directory are accessed relative to the current working directory, so run the command from the project directory.

## Project files

- `main.py` — interactive terminal chat loop and language-model prompt chain.
- `vector.py` — dataset loading, embedding, Chroma persistence, and top-five document retrieval.
- `godrej_smart_appliances_rag_dataset.csv` — tab-delimited dataset containing product and review information.
- `Godrej_Chatbot_Knowledge_Base.pdf` — a PDF included with the project; it is not currently loaded by the chatbot code.
- `chroma_langchain_db/` — local persisted vector database, created and populated by `vector.py` when the database directory does not exist.
- `requirments.txt` — Python dependency list.

## Scope and data note

Although the dataset includes question-and-answer fields, the current indexing code uses only each row's product title and review as searchable text. The generated answers are therefore grounded in retrieved reviews, not in the dataset's answer field. The PDF is also not part of the current retrieval pipeline.
