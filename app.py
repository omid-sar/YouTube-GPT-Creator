import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper
from apikey import apikey

os.environ["OPENAI_API_KEY"] = apikey

st.title("YouTube Context Explorer")
prompt = st.text_input("Plug in your YouTube topic here")

# Prompt Templates [Title]
title_template = PromptTemplate(
    input_variables=["topic"],
    template="""Given the topic {topic}, you are tasked with generating five engaging content suggestions
    for a YouTuber in less than 20 words. Use your expertise in content creation to propose ideas that are captivating and 
    suitable for a wide audience, ensuring each suggestion is distinct and offers a unique perspective or 
    approach to the topic.
""",
)

# Prompt Templates [Script]
script_template = PromptTemplate(
    input_variables=["title", "tags", "wikipedia_research"],
    template="""You are a specialist in crafting engaging scripts for YouTubers. Given the title {title} 
    and incorporating the keywords/tags {tags}, while leveraging this wikipedia reserch:{wikipedia_research}, 
    your focus is to initiate the script with the most captivating aspects while maintaining a friendly tone throughout.
    Your expertise lies in creating content optimized for 5-minute or700 words long videos.""",
)

#
llm = OpenAI(temperature=0.5)
title_chain = LLMChain(llm=llm, prompt=title_template, output_key="title", verbose=True)
script_chain = LLMChain(
    llm=llm, prompt=script_template, output_key="script", verbose=True
)
wiki = WikipediaAPIWrapper()

# Initialize session state variables
if "selected_title" not in st.session_state:
    st.session_state.selected_title = None
if "wiki_research" not in st.session_state:
    st.session_state.wiki_research = None
if "tags" not in st.session_state:
    st.session_state.tags = None
if "titles" not in st.session_state:
    st.session_state.titles = []

if prompt:
    # Check if the titles need to be regenerated
    if not st.session_state.titles or (st.session_state.get("last_prompt") != prompt):
        title_suggestions = title_chain(prompt)
        st.session_state.titles = title_suggestions["title"].split("\n")[1:]
        st.session_state.last_prompt = prompt

    st.session_state.selected_title = st.radio(
        "Select a title:", st.session_state.titles
    )
    st.write(f"You selected: {st.session_state.selected_title}")
    tags = st.text_input("Enter tags (comma separated):") or "No tags provided."
    if st.button("Submit"):
        if st.session_state.selected_title:
            wiki_research = wiki.run(st.session_state.selected_title)
            tags = tags or "No tags provided."
            script = script_chain.run(
                {
                    "title": st.session_state.selected_title,
                    "tags": tags,
                    "wikipedia_research": wiki_research,
                }
            )
            st.write(script)


# the most popular breads of dogs in the USA
# German Shepherd, Poodle, Golden Retriver and Labrador Retriver