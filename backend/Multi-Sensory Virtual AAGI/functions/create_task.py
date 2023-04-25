from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from dotenv import load_dotenv
import os
import json

# load the environment variables from the .env file
load_dotenv()

# get the value of the OPENAI_API_KEY environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# get the value of the STATE_DIR environment variable
STATE_DIR = os.environ.get("STATE_DIR")


def create_task_function():
    """
    Creates a task function for an AI assistant.
    Args:
      None
    Returns:
      str: A string containing the task description, goals, and start time.
    Examples:
      >>> create_task_function()
      "You are Alex an AI assistant that uses a very Large Language Model.
      The user is asking you to perform a task. Write a small description of the task along with the expected goals and any additional information that would be helpful for someone performing this task who has no knowledge of the prior conversation. Clearly mention the start time for the task at the end."
    """
    chat = ChatOpenAI(temperature  = 0, model= 'gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY)

    # Load the ability JSON file
    with open(os.path.join(STATE_DIR,'abilities.json'), 'r') as f:
        abilities_data = json.load(f)
    # Extract the names of all abilities and format them into a string separated by commas
    ability_names = "\nTools the assistant can access are " + ', '.join([ability['name'] for ability in abilities_data['abilities']])

    # create conversation string, each dialogue seperated by new line
    with open(os.path.join(STATE_DIR,'conversation.json'), 'r') as f:
        data = json.load(f)

    conversation_str = ''
    for message in data['conversation']:
        conversation_str += message['sender'] + ': ' + message['message']
        if message['file_upload'] != 'none':
            conversation_str += '\nFile Uploaded by ' + message['sender'] + ": " + message['file_upload']
        conversation_str += '\n'
    
    intro = "You are Alex an AI assistant that uses a very Large Language Model."

    instructions = "\nThe user is asking you to perform a task. Write a small description of the task along with the expected goals and any additional information that would be helpful for someone performing this task who has no knowledge of the prior conversation. Clearly mention the start time for the task at the end.\n"

    human_template = intro + conversation_str + ability_names + instructions 
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt])
    response = chat(chat_prompt.format_prompt().to_messages()).content
    
    return response