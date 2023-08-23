# Bring in deps
import os
from apikey import apikey
import streamlit as st
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import textwrap


os.environ["OPENAI_API_KEY"] = apikey


# *** YOUR VIDEO URL ***
video_url = "https://www.youtube.com/watch?v=jGwO_UgTS7I"
persist_directory = "../../data/processed"
embeddings = OpenAIEmbeddings()


loader = YoutubeLoader.from_youtube_url(video_url)
transcript = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=150)
docs = text_splitter.split_documents(transcript)
# docs[0].page_content

vectordb = Chroma.from_documents(
    documents=docs, embedding=embeddings, persist_directory=persist_directory
)


# *** YOUR QUESTION ABUT THE VIDEO ***
question = "what did course instructor say about computer learning?"

docs = vectordb.similarity_search(query=question, k=3)
docs_page_content = " ".join([doc.page_content for doc in docs])
docs[0].page_content


template = """You can provide answers about YouTube videos using their transcripts.

For the question: {question}
Please refer to the video transcript: {docs_page_content}

Rely solely on the transcript's factual data to respond.

If the information isn't sufficient, simply state "I don't know".

Ensure your answers are comprehensive and in-depth.
"""

prompt = PromptTemplate(
    input_variables=["question", "docs_page_content"],
    template=template,
)

llm = OpenAI(temperature=0)
chain = LLMChain(llm=llm, prompt=prompt)
response = chain.run(question=question, docs_page_content=docs_page_content)
print(textwrap.fill(response, width=85))


# ------------------------ streamlit app ------------------------
import os
import streamlit as st

# APP Framework
st.title("🦜🔗 YouTube GPT Creator")
prompt = st.text_input("Plug in your prompt here")
