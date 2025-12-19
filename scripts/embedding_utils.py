from config import EMBEDDING_API_URL, EMBEDDING_AUTH, EMBEDDING_TOKEN_ID, EMBEDDING_TOKEN_KEY
import requests
from typing import List
from langchain_core.embeddings import Embeddings
from tqdm import tqdm # Import tqdm

def get_vnpt_embedding(text_chunks: List[str]) -> List[List[float]] | None:
    """Gửi one or more text chunks to the VNPT Embedding API."""
    headers = {
        'Authorization': EMBEDDING_AUTH,
        'Token-id': EMBEDDING_TOKEN_ID,
        'Token-key': EMBEDDING_TOKEN_KEY,
        'Content-Type': 'application/json',
    }

    # The API expects 'input' to be a string or a list of strings
    json_data = {
        'model': 'vnptai_hackathon_embedding',
        'input': text_chunks, # Now accepts a list of strings
        'encoding_format': 'float',
    }

    try:
        response = requests.post(EMBEDDING_API_URL, headers=headers, json=json_data, timeout=60) # Increased timeout for batches
        response.raise_for_status()

        data = response.json()
        # Return a list of embedding vectors
        return [item['embedding'] for item in data['data']]

    except requests.exceptions.RequestException as e:
        first_chunk_preview = text_chunks[0][:30] if text_chunks else ""
        print(f"Lỗi gọi API Embedding cho văn bản (batch starting with '{first_chunk_preview}')... Chi tiết lỗi: {e}")
        return [None] * len(text_chunks) # Return None for each failed embedding in the batch

class VNPTAIEmbedding(Embeddings):
    def __init__(self, batch_size: int = 32):
        self.batch_size = batch_size

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        embeddings = []
        for i in tqdm(range(0, len(texts), self.batch_size), desc="Embedding documents"): 
            batch = texts[i : i + self.batch_size]
            batch_embeddings = get_vnpt_embedding(batch)
            if batch_embeddings:
                for j, embed in enumerate(batch_embeddings):
                    if embed is not None:
                        embeddings.append(embed)
                    else:
                        # Handle cases where embedding fails for a document in the batch
                        print(f"Warning: Embedding failed for document in batch. Index: {i+j}, Content: {batch[j][:50]}...")
                        embeddings.append([0.0] * 1024) # Assuming 1024 is the dimension
            else:
                # If the entire batch fails to return anything, append placeholders
                print(f"Warning: Entire batch failed starting at index {i}. Appending placeholders.")
                for _ in batch:
                    embeddings.append([0.0] * 1024)

        return embeddings

    def embed_query(self, text: str) -> List[float]:
        # For a single query, we still call the (now batched) function, but with a list of one item
        embedding_result = get_vnpt_embedding([text])
        if embedding_result and embedding_result[0] is not None:
            return embedding_result[0]
        else:
            print(f"Warning: Embedding failed for query: {text[:50]}...")
            return [0.0] * 1024 # Assuming 1024 is the dimension

print("Custom VNPTAIEmbedding class defined with embedded get_vnpt_embedding function, tqdm progress bar, and batching capability.")