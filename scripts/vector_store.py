from config import (
    FAISS_INDEX_PATH,
    VNPTAIEmbedding
)
from data_loader import chunks
from langchain_community.vectorstores import FAISS

# Initialize the custom embedding function
vnpt_embedding = VNPTAIEmbedding(batch_size=100)

# Create a FAISS vector store from the chunks and the custom embedding function
# This step will embed all chunks and build the index
print("Creating FAISS vector store...")
vector_store = FAISS.from_documents(chunks, vnpt_embedding)
print("FAISS vector store created successfully.")

# Save the FAISS index to disk
vector_store.save_local(FAISS_INDEX_PATH)
print(f"FAISS index saved to {FAISS_INDEX_PATH}/")