import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from docx import Document

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Placeholder paths for internal PDF and DOCX files (Update these paths as needed)
pdf_files = ["syllabus.pdf", "HPC Lab Manual 2023_24.pdf","Academic_Calendar.pdf"]


# Function to extract text from PDF
def get_pdf_text(pdf_paths):
    text = ""
    for pdf_path in pdf_paths:
        pdf_reader = PdfReader(pdf_path)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text



# Function to split text into chunks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

# Function to create and save a vector store
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

# Function to create a conversational chain
def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context. If the answer is not in
    the provided context, just say, "answer is not available in the context", don't provide the wrong answer.\n\n
    Context:\n{context}\n
    Question:\n{question}\n
    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.1)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

# Function to handle user input and display the conversation
def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)

    # Display conversation
    st.write(f"**You:** {user_question}")
    st.write(f"**Bot:** {response['output_text']}")

# Main function to run the Streamlit app
def main():
    st.set_page_config(page_title="Ask your query")
    st.title("Sanjivani Student Assist 🏫")
    
    with st.spinner("Processing internal PDF and DOCX files..."):
        raw_text = ""
        
        # Extract text from internal PDFs
        raw_text += get_pdf_text(pdf_files)
        
       

        if raw_text:
            text_chunks = get_text_chunks(raw_text)
            get_vector_store(text_chunks)

    # Question input section
    st.header("Hello Student")
    user_question = st.text_input("Type your question here and press Enter")

    if user_question:
        user_input(user_question)

if __name__ == "__main__":
    main()
