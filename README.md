
# YouTube Context Explorer

## Goal

The goal of this application is to facilitate the generation of engaging content suggestions and scripts for YouTube videos based on user-input topics. By leveraging OpenAI's language models and Wikipedia research, the application aims to provide captivating and unique content ideas and initiate scripts optimized for 5-minute videos, all while maintaining a friendly tone.

## Overview

The application is built using Streamlit and the langchain library, creating an interactive user interface where users can input YouTube video topics and tags. The application generates title suggestions based on the input topic, allows users to select a title, input tags, and then generates a script incorporating the selected title, tags, and Wikipedia research related to the title.

## Features

- **YouTube Topic Input**: Accepts user-input YouTube video topics to generate content suggestions.
- **Title Suggestions Generation**: Generates five engaging content suggestions using OpenAI's language models and displays them for user selection.
- **Tags Input**: Allows users to input tags for the script generation.
- **Script Generation**: Generates an engaging script incorporating the selected title, tags, and Wikipedia research.
- **Interactive User Interface**: Utilizes Streamlit for an interactive and user-friendly experience.

## Prerequisites

- Python 3.x
- Streamlit
- OpenAI API Key
- langchain library

## Setup and Installation

Clone the repository:

```bash
git clone <Your Repository URL>
cd <Your Repository Directory>
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Set up your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Open the app in your web browser, input the YouTube video topic and tags. Select a title from the generated suggestions and submit to generate and view the script based on the selected title, tags, and Wikipedia research.

## Testing on Hugging Face Spaces

You can also test the application on Hugging Face Spaces by visiting [YouTube Context Explorer](https://huggingface.co/spaces/Omid-sar/YouTube_GPT_Creator). Follow the same usage steps to generate YouTube video scripts.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

Please replace `<Your Repository URL>` and `<Your Repository Directory>` with the actual URL of your GitHub repository and the directory name. Also, ensure you have a `requirements.txt` file listing all the necessary packages and a `LICENSE` file in your repository.