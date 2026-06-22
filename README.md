# My RAG Chatbot

## Student Information
- **Student Name:** SYEDA AKASHA NAVEED
- **Student ID:** F2023065289
- **Project Title:** Retrieval-Augmented Generation (RAG) Chatbot


---

## Project Description
My RAG Chatbot is a document-based question-answering system developed using Python, Streamlit, LangChain, FAISS, and Hugging Face embeddings.

The chatbot allows users to place PDF or TXT documents inside a data folder and ask questions about their contents. The system retrieves the most relevant text chunks from the documents using semantic search and displays answers based on the retrieved information.

The project demonstrates the concepts of:

- Natural Language Processing (NLP)
- Text Embeddings
- Semantic Search
- Vector Databases (FAISS)
- Retrieval-Augmented Generation (RAG)
- Interactive Web Applications using Streamlit

---

## Features
- Upload and use PDF and TXT documents
- Automatically split documents into text chunks
- Generate embeddings using Sentence Transformers
- Store document embeddings in FAISS vector database
- Retrieve relevant information based on user queries
- Interactive web-based chatbot interface
- Completely free and runs locally without paid APIs

---

## Technologies Used
- Python
- Streamlit
- LangChain
- FAISS
- Sentence Transformers
- Hugging Face Embeddings
- PyPDF
- Python Dotenv

---

## Project Structure

```
rag-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── data/
│   ├── cv.pdf
│   └── notes.txt
├── venv/
└── other project files
```

---

## Dataset
The dataset consists of user-provided documents stored inside the `data` folder.

Supported file formats:
- PDF (.pdf)
- Text (.txt)

Users can replace these files with their own documents.

---

## Installation Instructions

### Step 1: Clone or Download the Project
Extract the ZIP file into a folder.

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Add Documents

Create a folder named:

```text
data
```

Place your PDF and TXT files inside this folder.

### Step 6: Run the Application

```bash
streamlit run app.py
```

### Step 7: Open the Application

Open:

```text
http://localhost:8501
```

---

## How It Works

1. Documents are loaded from the `data` folder.
2. Documents are split into smaller chunks.
3. Text embeddings are generated using Sentence Transformers.
4. Embeddings are stored inside a FAISS vector database.
5. User enters a question.
6. The system retrieves the most relevant document chunks.
7. The chatbot displays answers based on the retrieved content.

---

## Deployment Link

Local Deployment:

```text
http://localhost:8501


