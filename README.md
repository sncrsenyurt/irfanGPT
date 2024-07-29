

# IrfanGPT Chatbot

IrfanGPT is an interactive web chat application powered by the Hugging Face Transformers library. It utilizes the Streamlit library to create a user-friendly interface for interacting with the chatbot.

## Features

Offers an interactive chat interface for user interaction
Leverages Hugging Face's BlenderBot model for generating responses
Maintains conversation history to provide a more engaging user experience
## Requirements

Python (version 3.7 or higher)
Streamlit library
Transformers library from Hugging Face
## Installation

Create and Activate a Virtual Environment:
Bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate


Install Required Libraries:
Bash
pip install   
 streamlit transformers


## Usage

Run the following command in your terminal to start the local Streamlit server and access IrfanGPT in your web browser:

Bash
streamlit run app.py


This will open http://localhost:8501 where you can interact with the chatbot through a text input box and a "Chat" button.

## Code Overview (app.py)

Imports necessary libraries
Loads the BlenderBot model from Hugging Face
Defines the render_ui function for:
Creating the Streamlit UI with chat input and button
Handling user interactions
Manages conversation history using st.session_state
Generates responses and handles errors
## Example Conversation

Upon starting the application, you'll see a text input box and a "Chat" button. Simply type your message and click "Chat" to start conversing with IrfanGPT. The conversation history and chatbot responses will be displayed on the page.


## Acknowledgements

Hugging Face for providing the Transformers library and BlenderBot model
Streamlit for the easy-to-use web application framework
