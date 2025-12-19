from config import (
    TXT_FILE_PATH
)
import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# --------------
# I - LOAD FILES
# --------------

# Define the base directory path
base_dir = TXT_FILE_PATH

# List to store file paths
file_paths = []

# Recursively find .txt and .md files
for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith(('.txt', '.md')):
            file_paths.append(os.path.join(root, file))

documents = []
# Load each document using TextLoader
for p in file_paths:
    loader = TextLoader(p)
    documents.extend(loader.load())

# Print the number of loaded documents
print(f"Number of loaded documents: {len(documents)}")

# -------------
# II - CHUNKING
# -------------

# Initialize the text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)