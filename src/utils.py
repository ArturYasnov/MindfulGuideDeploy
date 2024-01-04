import re

BASE_PATH = "users_info"


def read_user_info():
    try:
        with open(f"{BASE_PATH}/user_info.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""

 
def read_user_history():
    try:
        with open(f"{BASE_PATH}/conversation_history.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""
    

def save_user_info_to_file(info):
    with open(f"{BASE_PATH}/user_info.txt", "w") as file:
        file.write(info)


def extract_recommended_to_user_content(text):
    # # Locate words in double quotes
    pattern = r'\"(.*?)\"'
    # matches = re.findall(pattern, text)

    # Locate categories
    lines = text.split('\n')

    # Filter for lines containing ":" and excluding "Question:" and "Response:"
    categories = [line.strip() for line in lines if ':' in line and len(line.split()) <= 5 and not line.startswith("Question:") and not line.startswith("Response:")]
    
    # Initialize dictionary to hold categories and their items
    categorized_content = {}

    # Current category tracker
    current_category = None

    for line in lines:
        # Check if line is a category
        if line.strip() in categories:
            # Update current category
            current_category = line.strip().replace(":", "").replace("- ", "").strip()
            categorized_content[current_category] = []
            # print(current_category)

        # Otherwise, if it's a content line and there is a current category
        elif current_category and '"' in line:
            # Extract all matches of quotes and add to the current category's list
            items = re.findall(pattern, line)
            categorized_content[current_category].extend(items)

    formatted_string = ""

    # Loop through each category and its items
    for category, items in categorized_content.items():
        # Clean up the category name
        category_clean = category.replace(":", "").replace("- ", "").strip()
        # Add category to string
        formatted_string += f"{category_clean}:\n"
        # Add each item under the category
        for item in items:
            formatted_string += f"  - {item}\n"
        # Add a newline after each category for better separation
        formatted_string += "\n"

    return formatted_string.strip()


