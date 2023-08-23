# Import the necessary packages
import os
import streamlit as st

impo

# Load the OpenAI API key from  apikey.py file
from apikey import apikey

os.environ["OPENAI_API_KEY"] = apikey


# ------------------------ streamlit app ------------------------
# APP Framework
st.title("🦜🔗 YouTube GPT Creator")
prompt = st.text_input("Plug in your prompt here")
