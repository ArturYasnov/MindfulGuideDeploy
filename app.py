import streamlit as st
from openai import OpenAI

from src.utils import *
from src.system_prompt import system_prompt
from src.openai_interface import get_openai_response

# source ~/.zshrc

BASE_PATH = "users_info"


# Set the page to wide mode
st.set_page_config(page_title="MindfulGuide", layout="wide")

st.title("Mindful Guide")
st.write("Explore, Learn, Grow: Your AI Assistant for Long-Term Fulfillment and Learning")
st.write("\n")


col1, spacer2, col2, spacer3 = st.columns([8, 1, 4, 1])

# Column 1: Chat Request
with col1:
    # Get input question
    input_text = st.text_input("Enter your question:")

    # Button for sending the question
    if st.button("Ask Question"):
        response_text = get_openai_response(input_text, system_prompt)
        st.text_area("Response:", value=response_text, height=300)

# Column 2: User Info
with col2:
    # Load and display current user info
    user_info = st.text_area("User Information:", value=read_user_info(), height=300)

    # Save button for user info
    if st.button("Save User Information"):
        save_user_info_to_file(user_info)
        st.success("User information saved!")

    # showing recommended content
    if st.button("Show User Recommended Content"):
        recommended_content = extract_recommended_to_user_content(read_user_history())  # Assuming user info contains the recommendations
        if recommended_content:
            st.text_area("Recommended Content:", value=recommended_content, height=300)
        else:
            st.write("No recommended content found.")
