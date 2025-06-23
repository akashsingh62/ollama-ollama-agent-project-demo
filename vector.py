from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

# Load and print column names
df = pd.read_csv("ai_job_dataset.csv")
print("Columns in CSV:", df.columns.tolist())

embeddings = OllamaEmbeddings(model="mxbai-embed-large")
db_location = "./chroma_ai_job_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        content = f"{row['job_title']} at {row['company_name']} — Skills: {row['required_skills']}, Industry: {row['industry']}"
        doc = Document(
            page_content=content,
            metadata={
                "salary": row.get("salary_usd", ""),
                "location": row.get("company_location", ""),
                "experience": row.get("experience_level", "")
            },
            id=str(i)
        )
        documents.append(doc)
        ids.append(str(i))

vector_store = Chroma(
    collection_name="ai_job_info",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

retriever = vector_store.as_retriever(search_kwargs={"k": 5})
