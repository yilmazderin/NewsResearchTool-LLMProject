#Import Dependencies
import os
import time
import pickle
import streamlit as st
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

#Load API key
from dotenv import load_dotenv
load_dotenv()

#Title
st.title("News Research Tool")

#Sidebar
st.sidebar.title("News Research URLs")

#Create array of urls
urls = []

#Create url inputs and append urls array with each url
for i in range (3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

#Url load button in sidebar
process_url_clicked = st.sidebar.button("Process URLs")

#Name for vectored database
file_path = "faiss_store_openai.pkl"

#Initialize empty placeholder and create OpenAI instance
main_placeholder = st.empty()
llm = OpenAI(temperature=0.9, max_tokens=500)

#When the button is clicked, split the texts of the articles into 1000 token chunks
if process_url_clicked:
    loader = UnstructuredURLLoader(urls = urls)
    #Wait message as program loads url articles
    main_placeholder.text("Data loading...")
    data = loader.load()
    #Conditions to split chunk and size of chunk
    text_splitter = RecursiveCharacterTextSplitter(
        separators = ['\n\n', '\n', '.', ','],
        chunk_size = 1000
    )

    #Wait message as program is splitting documents
    main_placeholder.text("Text splitter loading...")
    docs = text_splitter.split_documents(data)

    #Wait message as program is creating vectored database
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedded vector building...")
    time.sleep(2)
    
    #Serializes and saves object to a binary file
    with open(file_path, "wb") as f:
        pickle.dump(vectorstore_openai, f)

#Question prompt
query = main_placeholder.text_input("Question: ")

#If there is a question and a vectored database in record, proceed to answer the question
if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            #Load serialized vector from file, set up retrieval based QA chain
            vectorstore = pickle.load(f)
            chain = RetrievalQAWithSourcesChain.from_llm(llm = llm, retriever = vectorstore.as_retriever())
            #Process user's question
            result = chain({"question": query}, return_only_outputs=True)
            #Display answer
            st.header("Answer")
            st.write(result["answer"]) 

            #Create sources section if available
            sources = result.get("sources", "")
            if sources:
                st.subheader("Source(s):")
                sources_list = sources.split("\n")
                for source in sources_list:
                    st.write(source)