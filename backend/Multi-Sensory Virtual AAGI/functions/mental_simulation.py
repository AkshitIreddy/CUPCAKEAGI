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
import re
from functions.find_task_by_id import find_task_by_id_function

# load the environment variables from the .env file
load_dotenv()

# get the value of the OPENAI_API_KEY environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# get the value of the STATE_DIR environment variable
STATE_DIR = os.environ.get("STATE_DIR")


def mental_simulation_function(id):
    """
    Simulates a conversation between Alex and the user.
    Args:
      id (int): The id of the task.
    Returns:
      str: The response from Alex.
    Examples:
      >>> mental_simulation_function(1)
      "Alex's response to the task."
    """
    chat = ChatOpenAI(temperature  = 0, model= 'gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY)

    # create conversation string, each dialogue seperated by new line
    with open(os.path.join(STATE_DIR,'conversation.json'), 'r') as f:
        data = json.load(f)

    conversation_str = '\nConversation:'
    for message in data['conversation']:
        conversation_str += message['sender'] + ': ' + message['message']
        if message['file_upload'] != 'none':
            conversation_str += '\nFile Uploaded by ' + message['sender'] + ": " + message['file_upload']
        conversation_str += '\n'

    # Load the ability JSON file
    with open(os.path.join(STATE_DIR,'abilities.json'), 'r') as f:
        abilities_data = json.load(f)

    abilities = "Tools: \n" + '\n'.join( [ability['name'] + ": " + ability['description'] + "\n" + ability['directions'] for ability in abilities_data['abilities']])

    task_details = find_task_by_id_function(id)

    personality = "Personality:\n" + open(os.path.join(STATE_DIR, "personality.txt")).read() 

    thought_bubble = "\nAlex's thought bubble\n" + open(os.path.join(STATE_DIR, "thought_bubble.txt")).read() 

    instructions = "\nYou are Alex, think about how you would implement this task."

    info = personality + thought_bubble + abilities + conversation_str + "\n" + task_details + instructions

    human_message_prompt = HumanMessagePromptTemplate.from_template(info)

    chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt])

    response = chat(chat_prompt.format_prompt().to_messages()).content
    return response




