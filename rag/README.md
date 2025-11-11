# RAG Pipeline for Viettel AI Race

This folder contains the implementation of a Retrieval-Augmented Generation (RAG) pipeline for question answering.

## Overview

The pipeline consists of two main phases:

### 1. Index Phase
**Purpose**: Process documents, split them into chunks, generate summaries, and store them for efficient retrieval.

**Files**:
- `index_document.py` - Main indexing script using tokenizer-based chunking
- `simple_index_document.py` - Simplified version using word-count based chunking

**Process**:
1. Load markdown documents from specified directory
2. Split each document into chunks using RecursiveCharacterTextSplitter
3. Generate summaries for each chunk using LLM
4. Generate whole document summary based on chunk summaries
5. Save results to `data_and_summary.json`

**Output Format** (`data_and_summary.json`):
```json
[
  {
    "file_path": "path/to/file.md",
    "document_content": "full document text",
    "document_summary": "whole document summary",
    "chunks": [
      {
        "chunk_content": "chunk text",
        "chunk_summary": "chunk summary"
      },
      ...
    ]
  },
  ...
]
```

### 2. Retrieve and Answer Phase
**Purpose**: Answer questions by retrieving relevant documents and chunks, then using LLM for final answer.

**Files**:
- `get_answer.py` - Question answering script

**Process**:
1. Load indexed data from `data_and_summary.json`
2. Augment the input question with multiple query variations
3. Split document summaries into manageable token chunks
4. Retrieve relevant document indices using summary matching
5. For each retrieved document, check chunks for answers
6. Return the first valid answer found

## Usage

### Running the Index Phase

```python
from rag.index_document import index_documents

# Using default paths
index_documents()

# Or with custom paths
index_documents(
    markdown_path="/path/to/markdown/*.md",
    output_path="/path/to/output.json",
    num_workers=10
)
```

### Running the Question Answering Phase

```python
from rag.get_answer import get_final_answer, load_data_and_summary

# Load indexed data
data_and_summary = load_data_and_summary()

# Prepare question
question = {
    "Question": "Your question here?",
    "A": "Option A",
    "B": "Option B",
    "C": "Option C",
    "D": "Option D"
}

# Get answer
answer = get_final_answer(question, data_and_summary)
print(f"Answer: {answer}")
```

## Configuration

Both scripts use the following configuration variables (defined at the top of each file):

- `DEFAULT_MODEL`: Model name for vLLM server
- `MODEL_PATH`: Path to the model for tokenizer loading
- `SERVER_HOST`: vLLM server endpoint
- `TEMPERATURE`: LLM temperature setting
- `TOP_P`: LLM top_p setting
- `MAX_TOKENS`: Maximum tokens for LLM responses
- `MARKDOWN_PATH`: Path pattern for input markdown files
- `OUTPUT_PATH`: Path for output JSON file
- `DATA_AND_SUMMARY_PATH`: Path to indexed data file

## Key Differences Between Files

### `index_document.py` vs `simple_index_document.py`

| Feature | index_document.py | simple_index_document.py |
|---------|------------------|--------------------------|
| Chunking method | Tokenizer-based | Word count-based |
| Chunk size | 1024 tokens | 500 words |
| Chunk overlap | 256 tokens | 50 words |
| Dependencies | Requires transformers | Lighter dependencies |
| Accuracy | More accurate for LLM context | Faster but less precise |

## Bug Fixes Applied

1. **Index Phase**: Fixed whole document summary generation to use raw chunks instead of chunk summaries
2. **Retrieval Phase**: Fixed logical condition in `split_summary_and_convert_to_index` 
3. **Answer Phase**: Fixed string join operation for question options
4. **Error Handling**: Added try-catch for JSON parsing in answer extraction

## Requirements

```
openai
transformers
langchain-text-splitters
tqdm
```

## Notes

- The vLLM server must be running before executing either phase
- Ensure the model path is correct for tokenizer loading
- The pipeline uses Vietnamese language for summaries and queries
- If no answer is found, the system returns a random choice as fallback

