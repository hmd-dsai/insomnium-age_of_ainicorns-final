# insomnium-age_of_ainicorns

## Brief description of scripts (in sequence)
1. `config.py`: Defines constants (API, paths...), function `get_vnpt_embedding()` and class `VNPTAIEmbedding`
2. `data_loader.py`: Loads cleaned TXT/MD files and splits them into chunks
files
3. `retriever.py`: Defines function `get_relevant_contexts_hybrid()` to perform RAG using hybrid search (vector + keyword search)
4. `llm_call_config.py`: Defines 2 functions to call 2 LLM APIs
5. `predict.py`: Call APIs to answer questions in `test.json`

## Methods of gathering and cleaning data
- Gathering: Manual download
- Cleaning: Convert PDFs to TXTs using pdfplumber, or PDFs to MDs using online tools? As each text file has unique problems, they are mostly cleaned independently using unique codes (remove excess linebreaks, replace corrupt characters,...)