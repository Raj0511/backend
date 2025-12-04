import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.core.config import settings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

INDEX_PATH = "faiss_index"

def get_vector_store():
    """
    Loads the Vector DB from disk if it exists, otherwise creates a new one.
    """
    if os.path.exists(INDEX_PATH):
        return FAISS.load_local(INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
    else:
        return FAISS.from_texts(["Start of index"], embeddings)

def add_document_to_knowledge_base(text: str):
    """
    1. Splits text intelligently.
    2. Embeds it.
    3. Adds to FAISS index.
    4. Saves to disk.faiss_index
    """
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_text(text)
    
    vector_store = get_vector_store()
    
    vector_store.add_texts(chunks)
    
    vector_store.save_local(INDEX_PATH)
    print(f"Added {len(chunks)} chunks to knowledge base.")

def get_retriever():
    """
    Returns a 'Retriever' object that LangChain can use directly in chains.
    """
    vector_store = get_vector_store()
    return vector_store.as_retriever(search_kwargs={"k": 4})