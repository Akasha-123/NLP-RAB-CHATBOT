import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np

# ---------------- UI ----------------
st.set_page_config(page_title="Akasha CV Bot")
st.title("🤖 Syeda Akasha CV Chatbot")

st.write("Ask anything about your CV or click examples below 👇")

# ---------------- YOUR CV DATA ----------------
documents = [
    "Skills: Object-Oriented Programming, Data Structures, MySQL, Python (basic)",
    "Education: BS Software Engineering (2023-2027), University of Management and Technology, Lahore",
    "Projects: Police Information System, Student Management System (Python), BST implementation in C++",
    "Interests: Programming, Artificial Intelligence, Problem Solving, Reading tech content",
    "Languages: Urdu, English",
    "Summary: Software Engineering student interested in AI, software development, and programming"
]

# ---------------- MODEL ----------------
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# ---------------- EMBEDDINGS ----------------
@st.cache_resource
def embed_docs():
    return model.encode(documents, normalize_embeddings=True)

doc_embeddings = embed_docs()

# ---------------- RETRIEVAL ----------------
def retrieve(query):
    query_embedding = model.encode(query, normalize_embeddings=True)

    scores = np.dot(doc_embeddings, query_embedding)

    best_index = np.argmax(scores)

    return documents[best_index]

# ---------------- ANSWER FUNCTION ----------------
def answer(query):
    context = retrieve(query)

    return f"""
📌 Based on Syeda Akasha’s CV:

👉 {context}

---

Short answer extracted from your CV data.
"""

# ---------------- SIDEBAR (WAQAR STYLE QUESTIONS) ----------------
st.sidebar.header("📌 Example Questions")

example_questions = [
    "What skills does she have?",
    "What is her education background?",
    "What are her interests and hobbies?",
    "What languages does she know?",
    "What is her summary?"
]

for q in example_questions:
    if st.sidebar.button(q):
        st.session_state["question"] = q

# ---------------- CHAT MEMORY ----------------
if "chat" not in st.session_state:
    st.session_state.chat = []

# Display chat history
for role, msg in st.session_state.chat:
    with st.chat_message(role):
        st.write(msg)

# ---------------- INPUT ----------------
if "question" not in st.session_state:
    st.session_state["question"] = ""

user_input = st.chat_input("Ask about Akasha CV...")

# if sidebar question clicked → auto use it
if st.session_state["question"]:
    user_input = st.session_state["question"]
    st.session_state["question"] = ""

if user_input:
    response = answer(user_input)

    st.session_state.chat.append(("user", user_input))
    st.session_state.chat.append(("assistant", response))

    st.rerun()