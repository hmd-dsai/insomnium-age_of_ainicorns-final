# --------------------
# I - DEFINE CONSTANTS
# --------------------

# API Keys
EMBEDDING_API_URL = 'https://api.idg.vnpt.vn/data-service/vnptai-hackathon-embedding'
EMBEDDING_AUTH = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFuc2FjdGlvbl9pZCI6IjdkOGE5ZTRkLTI4NDUtNDYwNi05MGY3LWRkMDQ0NzBmMjE0MCIsInN1YiI6IjI4MDhjNDhmLWQxMmEtMTFmMC1hMDI3LWRmMmU0MDU5YjgxMCIsImF1ZCI6WyJyZXN0c2VydmljZSJdLCJ1c2VyX25hbWUiOiJob2FuZ21pbmhkdWMuYWxzQGdtYWlsLmNvbSIsInNjb3BlIjpbInJlYWQiXSwiaXNzIjoiaHR0cHM6Ly9sb2NhbGhvc3QiLCJuYW1lIjoiaG9hbmdtaW5oZHVjLmFsc0BnbWFpbC5jb20iLCJ1dWlkX2FjY291bnQiOiIyODA4YzQ4Zi1kMTJhLTExZjAtYTAyNy1kZjJlNDA1OWI4MTAiLCJhdXRob3JpdGllcyI6WyJVU0VSIiwiVFJBQ0tfMiJdLCJqdGkiOiI3ZWNhYThlYy1kMTNmLTQ4MTUtODY5MS0xODE5MDg1ZDdjMDUiLCJjbGllbnRfaWQiOiJhZG1pbmFwcCJ9.k8CkVS6-IdvpCVenCq7_smoFYl0BBkounZGng-Z1z6rRJAC92k_9Q6Vrz5zhF0tjWgybCLr9gdoult3y9N1WbuT7AFmOm4iFIjl13NLxv_GIxDLSHawRZL9UhKAzggGWbeZXYJNK29Fog5YI_GLLbVEe7zOLmO5YwL28-bFcsjAaFzOR-2JVr3ZA2CXH0Qr9lvfa28kMN8BgkKu7TELg5kDMx9UFeEVkRJHpzccqYF90gE0tnL3tywIdotTfJt3xBH5CUKQF0ODnnk_bfH2dSC9ZXin1RFL6kIrpSqzOtQCVxl_3itXLOX5t-dLTwg7YPcLaVpfchnn7s1h7jWv6nw'
EMBEDDING_TOKEN_KEY = 'MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBANPleoIv4N2jbwQ5KoDM3XsU6Tz7iitWrnvBMAfGlAhhM/ReOU0US1ZUFb3D8jraSF0Kv63DuEEMlFe689u53AsCAwEAAQ=='
EMBEDDING_TOKEN_ID = '4525a88b-e74f-4f0c-e063-62199f0a3a11'

SMALL_LLM_API_URL = 'https://api.idg.vnpt.vn/data-service/v1/chat/completions/vnptai-hackathon-small'
SMALL_LLM_AUTH = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFuc2FjdGlvbl9pZCI6IjdkOGE5ZTRkLTI4NDUtNDYwNi05MGY3LWRkMDQ0NzBmMjE0MCIsInN1YiI6IjI4MDhjNDhmLWQxMmEtMTFmMC1hMDI3LWRmMmU0MDU5YjgxMCIsImF1ZCI6WyJyZXN0c2VydmljZSJdLCJ1c2VyX25hbWUiOiJob2FuZ21pbmhkdWMuYWxzQGdtYWlsLmNvbSIsInNjb3BlIjpbInJlYWQiXSwiaXNzIjoiaHR0cHM6Ly9sb2NhbGhvc3QiLCJuYW1lIjoiaG9hbmdtaW5oZHVjLmFsc0BnbWFpbC5jb20iLCJ1dWlkX2FjY291bnQiOiIyODA4YzQ4Zi1kMTJhLTExZjAtYTAyNy1kZjJlNDA1OWI4MTAiLCJhdXRob3JpdGllcyI6WyJVU0VSIiwiVFJBQ0tfMiJdLCJqdGkiOiI3ZWNhYThlYy1kMTNmLTQ4MTUtODY5MS0xODE5MDg1ZDdjMDUiLCJjbGllbnRfaWQiOiJhZG1pbmFwcCJ9.k8CkVS6-IdvpCVenCq7_smoFYl0BBkounZGng-Z1z6rRJAC92k_9Q6Vrz5zhF0tjWgybCLr9gdoult3y9N1WbuT7AFmOm4iFIjl13NLxv_GIxDLSHawRZL9UhKAzggGWbeZXYJNK29Fog5YI_GLLbVEe7zOLmO5YwL28-bFcsjAaFzOR-2JVr3ZA2CXH0Qr9lvfa28kMN8BgkKu7TELg5kDMx9UFeEVkRJHpzccqYF90gE0tnL3tywIdotTfJt3xBH5CUKQF0ODnnk_bfH2dSC9ZXin1RFL6kIrpSqzOtQCVxl_3itXLOX5t-dLTwg7YPcLaVpfchnn7s1h7jWv6nw'
SMALL_LLM_TOKEN_KEY = 'MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBALHflHyE6dEK0arIlpEEjVKIO7gawpP5shJQFYakTwtY6aqI4EsDX3XNnk4o7ljL9ifMlYdqqetofb2uwuC4rmECAwEAAQ=='
SMALL_LLM_TOKEN_ID = '4525a88b-e74e-4f0c-e063-62199f0a3a11'

LARGE_LLM_API_URL = 'https://api.idg.vnpt.vn/data-service/v1/chat/completions/vnptai-hackathon-large'
LARGE_LLM_AUTH = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFuc2FjdGlvbl9pZCI6IjdkOGE5ZTRkLTI4NDUtNDYwNi05MGY3LWRkMDQ0NzBmMjE0MCIsInN1YiI6IjI4MDhjNDhmLWQxMmEtMTFmMC1hMDI3LWRmMmU0MDU5YjgxMCIsImF1ZCI6WyJyZXN0c2VydmljZSJdLCJ1c2VyX25hbWUiOiJob2FuZ21pbmhkdWMuYWxzQGdtYWlsLmNvbSIsInNjb3BlIjpbInJlYWQiXSwiaXNzIjoiaHR0cHM6Ly9sb2NhbGhvc3QiLCJuYW1lIjoiaG9hbmdtaW5oZHVjLmFsc0BnbWFpbC5jb20iLCJ1dWlkX2FjY291bnQiOiIyODA4YzQ4Zi1kMTJhLTExZjAtYTAyNy1kZjJlNDA1OWI4MTAiLCJhdXRob3JpdGllcyI6WyJVU0VSIiwiVFJBQ0tfMiJdLCJqdGkiOiI3ZWNhYThlYy1kMTNmLTQ4MTUtODY5MS0xODE5MDg1ZDdjMDUiLCJjbGllbnRfaWQiOiJhZG1pbmFwcCJ9.k8CkVS6-IdvpCVenCq7_smoFYl0BBkounZGng-Z1z6rRJAC92k_9Q6Vrz5zhF0tjWgybCLr9gdoult3y9N1WbuT7AFmOm4iFIjl13NLxv_GIxDLSHawRZL9UhKAzggGWbeZXYJNK29Fog5YI_GLLbVEe7zOLmO5YwL28-bFcsjAaFzOR-2JVr3ZA2CXH0Qr9lvfa28kMN8BgkKu7TELg5kDMx9UFeEVkRJHpzccqYF90gE0tnL3tywIdotTfJt3xBH5CUKQF0ODnnk_bfH2dSC9ZXin1RFL6kIrpSqzOtQCVxl_3itXLOX5t-dLTwg7YPcLaVpfchnn7s1h7jWv6nw'
LARGE_LLM_TOKEN_KEY = 'MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAJefJNZFR6qaeTtMxFu9rGDeD7ptsWjF7uXBfJrTUcPN0lyonPkje8q0frOrxgoAA2E7KMRvI06M3o8ugwOGzC8CAwEAAQ=='
LARGE_LLM_TOKEN_ID = '4525a84a-fffd-2031-e063-62199f0af9db'

# File Paths
TXT_FILE_PATH = './raw_data'
FAISS_INDEX_PATH = './faiss_index'
JSON_TEST_PATH = './private_test.json'

# -------------------------------
# II - DEFINE EMBEDDING UTILITIES
# -------------------------------

import requests
from typing import List
from langchain_core.embeddings import Embeddings
from tqdm import tqdm 

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