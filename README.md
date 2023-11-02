<h1 align="center">News Research Tool</h1>

As we know, ChatGPT is one of the most powerful tools . However, we know it isn't up to date with current data. That is why I decided to 

![News App Screenshot](./News%20App%20Picture.png)

## Dependencies
To run this project, download the repository and run<br><br>
**Streamlit:** Handles the front-end web interface<br>
**Langchain** Extensive developer toolkit to develop LLM applications.<br>
**Unstructured** Provides open-source components for processing images and documents.<br>
**Dotenv:** Loads the API key<br>
**OpenAI:** The official client for interacting with the OpenAI API.<br>
**Tiktoken:** Counts tokens in a text string without making API calls.<br>
**Faiss-cpu** A library for efficient similarity search and clustering of dense vectors.<br>
**Libmagic:** Helps determine the type of files based on their content.<br>
**Python-magic:** A wrapper around the libmagic file type identification library.<br>
**Python-magic-bin:** Binary dependency for python-magic, enabling file type identification.<br><br>
To install all dependencies at once:

**pip install -r requirements.txt**

## Usage
1. Copy the repository to your local machine.
2. Open the main.py file.
3. Install all dependencies
4. Enter "streamlit run app.py"
5. Wait for the web app to compile.
6. Enter 3 related articles' urls you want to analyze.
7. Wait for the urls to be processed.
8. Prompt the program with any question you want answered based on the articles provided.

## Challenges Faced

When installing the dependencies, python-magic-bin would not install properly. I completed this step by installing it from the GitHub repository. If you are experiencing this, delete the python-magic-bin line from the requirements.txt and run:

pip install git+https://github.com/riad-azz/py-file-type.git
