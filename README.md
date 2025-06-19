# KG Population via PDF

![License: Non-Commercial](https://img.shields.io/badge/license-non--commercial-orange)

## Project Overview

**KG Population via PDF** is a FastAPI-based backend service that ingests PDF documents, extracts structured knowledge (triples), and populates a knowledge graph (KG) using Neo4j. The system leverages LLMs (via Azure OpenAI), LangChain, LlamaIndex, and integrates with MongoDB, Redis, and Neo4j for storage and retrieval. It is designed for rapid ingestion and semantic structuring of unstructured PDF data.

---

## Installation & Dependencies

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AmrithNiyogi/kg-population-pdf.git
   cd kg-population-pdf
   ```
2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

**Main dependencies:**
- fastapi, uvicorn
- pymongo, motor
- langchain, langchain-community, langchain-openai
- llama-index, llama-index-core, llama-index-vector-stores-redis, llama-index-embeddings-azure-openai
- neo4j, redis
- pdfplumber, PyPDF2, pypdf, pymupdf
- nltk
- python-dotenv
- litellm, langfuse

---

## Usage Examples

### 1. **Start the API server:**
```bash
uvicorn app.main:app --reload
```

### 2. **Upload a PDF for KG population:**
- **Endpoint:** `POST /pdf/upload`
- **Form field:** `file` (PDF file)
- **Example (using curl):**
  ```bash
  curl -F "file=@yourfile.pdf" http://localhost:8000/pdf/upload
  ```
- **Response:**
  ```json
  { "status": "success", "detail": "KG populated. PDF stored with id: <id>" }
  ```

### 3. **Check service health:**
- **Endpoint:** `GET /pdf/`
- **Response:**
  ```json
  { "message": "KG Population API Running", "services": { "mongodb": "🟢 running", ... } }
  ```

---

## Code Structure & Module Descriptions

```
app/
├── main.py                # FastAPI app entrypoint, CORS, router registration
├── connectors/
│   └── pdf_connector.py   # API endpoints for PDF upload and health check
├── services/
│   └── kg_services.py     # Core pipeline: PDF text extraction, chunking, vector storage, triple extraction, KG population
├── models/
│   └── triple_model.py    # Triple extraction logic using LLMs (Azure OpenAI, Langfuse)
├── utils/
│   └── preprocessing.py   # PDF text extraction and preprocessing utilities
├── configs/
│   └── settings.py        # Environment variable management and settings
```

- **main.py**: Initializes FastAPI app, sets up CORS, and includes routers.
- **connectors/pdf_connector.py**: Handles PDF upload, stores PDF in MongoDB, triggers KG pipeline, and provides health checks for MongoDB, Redis, and Neo4j.
- **services/kg_services.py**: Implements the pipeline: extract text from PDF, chunk and embed, store in Redis, extract triples, and push to Neo4j.
- **models/triple_model.py**: Uses LLMs to extract subject-predicate-object triples from text.
- **utils/preprocessing.py**: Cleans and tokenizes text, extracts text from PDFs.
- **configs/settings.py**: Loads environment variables for all services.

---

## Configuration & Customization

All configuration is managed via environment variables. Create a `.env` file in the project root with the following keys (see `app/configs/settings.py`):

## Running the Project & Interpreting Results

1. **Start all required services:**
   - MongoDB, Redis, Neo4j (ensure credentials match your `.env`)
2. **Run the FastAPI server:**
   ```bash
   uvicorn app.main:app --reload
   ```
3. **Upload PDFs via the API.**
4. **Check Neo4j Browser** to see the populated knowledge graph. Each PDF's triples are labeled by filename.
5. **MongoDB** stores the original PDF and extracted text. **Redis** stores vectorized chunks for semantic search (if extended).

---

## Testing, Contributing, and License Info

### Testing
- No dedicated test suite is included yet. For manual testing, use the `/pdf/upload` endpoint with various PDFs and check the KG in Neo4j.
- To add tests, create a `tests/` directory and use `pytest` or FastAPI's `TestClient`.

### Contributing
- Pull requests and issues are welcome! Please open an issue to discuss major changes.
- Follow PEP8 and best practices for Python and FastAPI.

### License 


- This project is licensed under a **Non-Commercial Use License**.  
- Personal and academic usage is permitted.  
- **Commercial use is prohibited** unless prior written permission is granted.
- See [LICENSE](https://github.com/AmrithNiyogi/kg-population-pdf/blob/main/LICENSE) for details.


📩 To obtain a commercial license, contact: [amrithniyogi@gmail.com](mailto:amrithniyogi@gmail.com)