import  os
from dotenv import load_dotenv
load_dotenv()

from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

prompt=ChatPromptTemplate([
    ("system","you are a helpful assistant. Please respond to the question asked"),
    ("user","Question:{question}")
])

#streamlit framework

st.title("langchain demo with mistral")
input_text=st.text_input("What question you have in mind")

#ollama mistral model

llm=OllamaLLM(model="llama2:7b-chat")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))