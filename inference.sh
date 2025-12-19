#!/bin/bash

# Initialize vector database in ./faiss_index
python scripts/vector_store.py

# Run inference pipeline
python scripts/predict.py