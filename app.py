import streamlit as st
from openai import OpenAI

# Assume these are the modules where you've defined these functions.
from src.utils import *
from src.system_prompt import system_prompt
from src.openai_interface import get_openai_response_login, get_openai_response_logout

# Set the page to wide mode
st.set_page_config(page_title="MindfulGuide", layout="wide")

# Initialize session state for login
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Function to verify login credentials (Replace with your actual verification logic)
def verify_login(username, password):
    # Here you might check against a database or a file with user credentials.
    return True if username == "admin" and password == "password" else False

# Define a function to handle login
def login_user():
    user = st.sidebar.text_input("Username")
    pwd = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if verify_login(user, pwd):
            st.session_state['logged_in'] = True
            st.rerun()  # Rerun the app to update the layout
        else:
            st.sidebar.error("Incorrect username or password.")


# App main layout
def app_layout_logout():

    st.title("Mindful Guide")
    st.write("Explore, Learn, Grow: Your AI Assistant for Long-Term Fulfillment and Learning")
    st.write("\n")

    col1, spacer2, col2, spacer3 = st.columns([8, 1, 4, 1])

    # Column 2: User Info
    with col2:
        user_info = st.text_area("User Information:", height=300)

    # Column 1: Chat Request
    with col1:
        input_text = st.text_input("Enter your question:")
        if st.button("Ask Question"):
            response_text = get_openai_response_logout(input_text, system_prompt, user_info)
            # st.text_area("Response:", value=response_text, height=450)
            st.text_area("User info:", value=f"Input text:\n {input_text} \n\n\n User info: \n{user_info}\n\n\n{response_text}\n\n\n\n System prompt: {system_prompt}", height=450)



# App main layout
def app_layout_login():
    st.title("Mindful Guide")
    st.write("Explore, Learn, Grow: Your AI Assistant for Long-Term Fulfillment and Learning")
    st.write("\n")

    col1, spacer2, col2, spacer3 = st.columns([8, 1, 4, 1])

    # Column 1: Chat Request
    with col1:
        input_text = st.text_input("Enter your question:")
        if st.button("Ask Question"):
            user_info = read_user_info()
            recommended_content = extract_recommended_to_user_content(read_user_history()) 
            response_text = get_openai_response_login(input_text, system_prompt, user_info, recommended_content)
            # st.text_area("Response:", value=response_text, height=450)
            st.text_area("User info:", value=f"Input text:\n {input_text} \n\n\n User info: \n{user_info}\n\n\n{response_text}\n\n\n\n System prompt: {system_prompt}\n\n\n\n Recommended content:{recommended_content}", height=450)


    # Column 2: User Info
    with col2:
        user_info = st.text_area("User Information:", value=read_user_info(), height=300)
        if st.button("Save User Information"):
            save_user_info_to_file(user_info)
            st.success("User information saved!")

        if st.button("Show User Recommended Content"):
            recommended_content = extract_recommended_to_user_content(read_user_history())
            if recommended_content:
                st.text_area("Recommended Content:", value=recommended_content, height=300)
            else:
                st.write("No recommended content found.")

# Main
if not st.session_state['logged_in']:
    st.sidebar.warning("Login to use history")
    login_user()
    app_layout_logout()
else:
    app_layout_login()

    # Logout button in the sidebar for logged-in users
    if st.sidebar.button("Logout"):
        st.session_state['logged_in'] = False
        st.rerun()  # Rerun the app to update
