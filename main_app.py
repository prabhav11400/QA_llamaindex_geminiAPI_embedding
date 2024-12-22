import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.gemini import Gemini
from llama_index.core import Settings
from llama_index.embeddings.gemini import GeminiEmbedding
import streamlit as st
import google.generativeai as genai

# Load environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

# Streamlit App Title
st.title("LlamaIndex Q&A App")
st.write("A Q&A application using LlamaIndex and Gemini.")

# Initialize Gemini API
genai.configure(api_key = google_api_key)

# Load documents
@st.cache_data
def load_documents():
    document = SimpleDirectoryReader("./Data")
    return document.load_data()

doc = load_documents()

# Configure global settings
Settings.llm = Gemini(model="models/gemini-2.0-flash-exp", temperature=1.0)
Settings.embed_model = GeminiEmbedding(model_name="models/embedding-001")
Settings.chunk_size = 800
Settings.chunk_overlap = 20

# Build or load the index
@st.cache_data
def build_index(_documents):
    index = VectorStoreIndex.from_documents(_documents)
    index.storage_context.persist()
    return index

index = build_index(doc)

# Query engine
query_engine = index.as_query_engine()

# User Input
user_query = st.text_input("Enter your query regarding Indian Railway:", "")

if st.button("Get Answer"):
    if user_query.strip():
        response = query_engine.query(user_query)
        st.write("**Answer:**")
        st.write(response.response)
    else:
        st.warning("Please enter a query.")
