#Vector Search is a database; it going to be hosted locally on our machine
#chromaDB

from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document


import os
import pandas as pd

df = pd.read_csv("godrej_smart_appliances_rag_dataset.csv", sep="\t")

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            page_content=row["title"] + " " + row["review"],
            metadata={"rating": row["rating"], "product_category": row["product category"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name="appliances_reviews",
    persist_directory=db_location, # so we dont need to load into database again n again, doing this to persist the database on our local machine
    embedding_function=embeddings
)
        
if add_documents:
    vector_store.add_documents(documents, ids=ids)

# now we will make our vector store usable for retrieval, so we can use it to retrieve relevant documents based on user queries

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
) # k is the number of documents to retrieve based on user query

