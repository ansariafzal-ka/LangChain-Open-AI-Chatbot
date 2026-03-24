from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# loading env variables
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# custom prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpful assistant. Please provide response to the user queries.'),
        ('user', 'Ouestion:{question}')
    ]
)

# frontend
st.title('Langchain Demo with Open AI API')
input_text = st.text_input('Search the topic you want')

# Open AI API call
llm = ChatOpenAI(model='gpt-3.5-turbo')
output_parser = StrOutputParser()

# chain
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))