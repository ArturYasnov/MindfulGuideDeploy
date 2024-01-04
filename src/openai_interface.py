from openai import OpenAI
from src.utils import *


def log_conversation(question, response):
            with open(f"{BASE_PATH}/conversation_history.txt", "a") as file:
                file.write(f"Question: {question}\n")
                file.write(f"Response: {response}\n\n\n\n")
                file.write("\n")  # Adds a newline for readability between conversations


def get_openai_response_login(input_text, system_prompt, user_info, recommended_content):
    print("Request has been sent.")

    client = OpenAI()
    # user_info = read_user_info()
    # recommended_content = extract_recommended_to_user_content(read_user_history()) 

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",  # "gpt-3.5-turbo", "gpt-4-1106-preview"
        messages=[
            {"role": "system", "content": f"{system_prompt} Questions go in format User profile: ..., User question ... Previously recommended content to user ..."},
            {"role": "user", "content": f"User profile: {user_info}. User question: {input_text}. Previously recommended content: {recommended_content}."}
        ]
    )

    response_text = completion.choices[0].message.content

    # Log the conversation
    log_conversation(input_text, response_text)

    return response_text


def get_openai_response_logout(input_text, system_prompt, user_info):
    print("Request has been sent.")

    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",  # "gpt-3.5-turbo", "gpt-4-1106-preview"
        messages=[
            {"role": "system", "content": f"{system_prompt} Questions go in format User profile: ..., User question ..."},
            {"role": "user", "content": f"User profile: {user_info}. User question: {input_text}."}
        ]
    )

    response_text = completion.choices[0].message.content

    return response_text
