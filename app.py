# Import the necessary packages
import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory


# Load the OpenAI API key from  apikey.py file
from apikey import apikey

os.environ["OPENAI_API_KEY"] = apikey


# ------------------------ streamlit app ------------------------
# APP Framework
st.title("🦜🔗 YouTube GPT Creator")
prompt = st.text_input("Plug in your prompt here")


# Prompt Templates
title_template = PromptTemplate(
    input_variables=["topic"],
    template="write me a YouTube video title about {topic}",
)

script_template = PromptTemplate(
    input_variables=["title"],
    template="write me a YouTube video script based on this {title}",
)
# Memory
memory = ConversationBufferMemory(input_key="topic", memory_key="chat_history")

# LLMS
llm = OpenAI(temperature=0.0)
title_chain = LLMChain(
    llm=llm, prompt=title_template, output_key="title", memory=memory, verbose=True
)
script_chain = LLMChain(
    llm=llm, prompt=script_template, output_key="script", memory=memory, verbose=True
)
sequential_chain = SequentialChain(
    chains=[title_chain, script_chain],
    input_variables=["topic"],
    output_variables=["title", "script"],
    verbose=True,
)

# Screen Output
if prompt:
    response = sequential_chain({"topic": prompt})
    st.write(response["title"])
    st.write(response["script"])

    with st.expander(" Chat History"):
        st.info(memory.buffer)
