# insomnium-age_of_ainicorns

## Brief description of scripts (in sequence)
1. `config.py`: Defines 
- Constants (API, paths...)
- Function `get_vnpt_embedding()` and class `VNPTAIEmbedding`
2. `data_loader.py`: Loads cleaned TXT/MD files and splits them into chunks
3. `vector_store.py`: Embed chunks into vector database
4. `llm_call_config.py`:
- Defines function `get_relevant_contexts_hybrid()` to perform RAG using hybrid search (vector + keyword search)
- Defines 2 functions to call 2 LLM APIs
5. `predict.py`: Call APIs to answer questions in `test.json`

## Methods of gathering and cleaning data
- Gathering: Manual download
- Cleaning: Convert PDFs to TXTs using pdfplumber, or PDFs to MDs using marker. As each text file has unique problems, they are mostly cleaned independently using unique codes (remove excess linebreaks, replace corrupt characters,...)

# Resource initialization
- Make sure the raw text files (TXT and MD) are located in `WORKKDIR/raw_data/`.
- Run `vector_store.py`. This script will run `data_loader.py` to split texts into chunks, then call `vnpt_embedding_api` to vectorize them, then use FAISS to save the vector database.