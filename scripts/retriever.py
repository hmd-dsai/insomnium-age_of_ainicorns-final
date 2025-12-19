from config import (
    FAISS_INDEX_PATH,
    VNPTAIEmbedding
)
from data_loader import chunks
from langchain_community.vectorstores import FAISS
from langchain_community.retrievers import BM25Retriever
from langchain_core.documents import Document
from langchain_classic.retrievers.ensemble import EnsembleRetriever
from typing import List

# code here

# ----------

# Assuming loaded_vector_store_for_hybrid and chunks are available from previous cells
# Initialize the custom embedding function if not already done in the current session
vnpt_embedding_for_retriever = VNPTAIEmbedding()
loaded_vector_store_for_hybrid = FAISS.load_local(FAISS_INDEX_PATH, vnpt_embedding_for_retriever, allow_dangerous_deserialization=True)

# 2. Initialize FAISS retriever
faiss_retriever = loaded_vector_store_for_hybrid.as_retriever()
print("FAISS retriever initialized.")

# 3. Initialize BM25 retriever
bm25_retriever = BM25Retriever.from_documents(chunks)
print("BM25 retriever initialized.")

# 4. Initialize EnsembleRetriever
ensemble_retriever = EnsembleRetriever(retrievers=[faiss_retriever, bm25_retriever], weights=[0.5, 0.5])
print("EnsembleRetriever initialized with FAISS and BM25.")

# 5. Define the hybrid search function
def get_relevant_contexts_hybrid(question: str, k: int = 4) -> List[Document]:
    """
    Performs a hybrid search using EnsembleRetriever to combine FAISS and BM25.

    Args:
        question (str): The search query.
        k (int): The number of top relevant documents to return (EnsembleRetriever handles this internally based on its sub-retrievers).

    Returns:
        List[Document]: A list of unique relevant documents from the hybrid search.
    """
    # EnsembleRetriever's invoke method will handle combining and re-ranking
    # Note: EnsembleRetriever will call each sub-retriever with 'k' internally, then combine.
    # The 'k' here is mainly for consistency in signature, actual number returned might vary based on re-ranking.
    # For precise control over the final number of docs, post-processing might be needed if k is strict.
    docs = ensemble_retriever.invoke(question)
    return docs[:k] # Limit to top k after ensemble processing

print("Hybrid search function 'get_relevant_contexts_hybrid' defined.")

"""# ----------

question_hybrid_demo = "Năng lực pháp luật của mỗi cá nhân có khác nhau không?"
print(f"Performing EnsembleRetriever hybrid search for question: '{question_hybrid_demo}'...")
relevant_contexts_ensemble_hybrid = get_relevant_contexts_hybrid(question_hybrid_demo, k=2)

if relevant_contexts_ensemble_hybrid:
    print("\nRelevant Contexts (EnsembleRetriever Hybrid Search):")
    for i, doc in enumerate(relevant_contexts_ensemble_hybrid):
        print(f"--- Context {i+1} ---")
        print(doc.page_content)
        print(f"  Source: {doc.metadata.get('source')}")
else:
    print("No relevant contexts found using EnsembleRetriever hybrid search or an error occurred.")"""