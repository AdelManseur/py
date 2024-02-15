import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma

try:
    # Your import statements go here
    pass
except ModuleNotFoundError as e:
    print(f"Module not found error: {e}")

# Rest of your code
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def initialize_streamlit():
    st.set_page_config(
        initial_sidebar_state="auto",
    )

def process_query(url, prompt):
    ABS_PATH = os.path.dirname(os.path.abspath(__file__))
    DB_DIR = os.path.join(ABS_PATH, "db")

    loader = WebBaseLoader(url)
    data = loader.load()

    text_splitter = CharacterTextSplitter(separator='\n', chunk_size=500, chunk_overlap=40)
    docs = text_splitter.split_documents(data)

    openai_embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(documents=docs, embedding=openai_embeddings, persist_directory=DB_DIR)
    vectordb.persist()

    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    llm = ChatOpenAI(model_name='gpt-3.5-turbo')
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

    response = qa(prompt)
    return response
