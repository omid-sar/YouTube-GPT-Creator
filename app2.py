# Import the necessary packages
import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper


# Load the OpenAI API key from  apikey.py file
from apikey import apikey

os.environ["OPENAI_API_KEY"] = apikey


# ------------------------ streamlit app ------------------------
# APP Framework
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
    Your expertise lies in creating content optimized for 5-minute long videos.""",
)

# Memory


# LLMS
llm = OpenAI(temperature=0.5)
title_chain = LLMChain(llm=llm, prompt=title_template, output_key="title", verbose=True)
script_chain = LLMChain(
    llm=llm, prompt=script_template, output_key="script", verbose=True
)
wiki = WikipediaAPIWrapper()


import streamlit as st

# ... (other imports and setup)

# Set up logging
import logging

logging.basicConfig(level=logging.INFO)

st.title("YouTube Context Explorer")

# Define a separate button for generating scripts
if "generate_script" not in st.session_state:
    st.session_state.generate_script = False

# Get user input
prompt = st.text_input("Plug in your YouTube topic here")

if prompt:
    # Fetch title suggestions and display radio button
    title_suggestions = title_chain.run(topic=prompt)
    titles = title_suggestions["title"].split("\n")[1:]
    selected_title = st.radio("Select a title:", titles)

    if selected_title:
        st.session_state.selected_title = selected_title
        logging.info(f"Selected title: {st.session_state.selected_title}")

    # Get user input for tags
    tags = st.text_input("Enter tags (comma separated):")
    if tags:
        st.session_state.tags = tags

    # Define a button for generating the script
    if st.button("Generate Script"):
        st.session_state.generate_script = True

# Check if the generate script button was pressed
if st.session_state.generate_script:
    logging.info("Generating script...")
    # Fetch Wikipedia research and generate script
    wiki_research = wiki.run(st.session_state.selected_title)
    script = script_chain.run(
        title=st.session_state.selected_title,
        wikipedia_research=wiki_research,
        tags=st.session_state.tags,
    )
    st.write(f"Generated Script:\n{script}")
    st.session_state.generate_script = False  # Reset the button state



script_template = PromptTemplate(input_variables=["title", "tags", "wikipedia_research"], output_parser=None, partial_variables={}, template='Given the topic {topic}, you are tasked with generating five engaging content suggestions for a YouTuber in less than 20 words. Use your expertise in content creation to propose ideas that are captivating and suitable for a wide audience, ensuring each suggestion is distinct and offers a unique perspective or approach to the topic.', template_format='f-string', validate_template=True)

script_template = PromptTemplate.from_template(
    """You are a specialist in crafting engaging scripts for YouTubers. Given the title {title} 
    and incorporating the keywords/tags {tags}, while leveraging this wikipedia reserch:{wikipedia_research}, 
    your focus is to initiate the script with the most captivating aspects while maintaining a friendly tone throughout.
    Your expertise lies in creating content optimized for 5-minute long videos."""
)


script_template = PromptTemplate.from_template(
    """You are a specialist in crafting engaging scripts for YouTubers. Given the title {title} 
    and incorporating the keywords/tags {tags}, while leveraging this wikipedia reserch:{wikipedia_research}, 
    your focus is to initiate the script with the most captivating aspects while maintaining a friendly tone throughout.
    Your expertise lies in creating content optimized for 5-minute long videos."""
)c
script_template.format(title=title,tags=tags,wikipedia_research=wiki_research)




"""print(script_chain)

# Title
titles = title_chain("dogs")
print(titles)
title = titles["title"].split("\n")[1:][0]
print(title)
# Wikipedia
wiki = WikipediaAPIWrapper()
wiki_research = wiki.run(title)
print(wiki_research)
# tags
tags = "dogs, pets, animals"
# Script


script_chain.run({"title": title, "tags": tags, "wikipedia_research": wiki_research})



prompt = PromptTemplate(
    input_variables=["company", "product"],
    template="What is a good name for {company} that makes {product}?",
)





chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run({
    'company': "ABC Startup",
    'product': "colorful socks"
    }))
"""



