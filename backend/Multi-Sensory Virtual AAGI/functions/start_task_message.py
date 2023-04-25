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

def start_task_message_function(well_defined_task):
    """
    Generates a response to a well-defined task.
    Args:
      well_defined_task (str): The task to respond to.
    Returns:
      str: The response to the task.
    Side Effects:
      Loads environment variables from the .env file.
    Examples:
      >>> start_task_message_function("Create a new user")
      "I have received your task to create a new user. My name is Alex. I will proceed to execute the task accordingly."
    """
    chat = ChatOpenAI(temperature  = 0, model= 'gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY)

    assistant_template = "{well_defined_task}\nI need to tell the user I have received their task, and will proceed to execute it accordingly. My name is Alex. I should mention few key details about the task. But it should not be long. I SHOULD NOT ASK THE USER ANY QUESTION."
    assistant_message_prompt = AIMessagePromptTemplate.from_template(assistant_template)

    chat_prompt = ChatPromptTemplate.from_messages([assistant_message_prompt])
    response = chat(chat_prompt.format_prompt(well_defined_task=well_defined_task).to_messages()).content
    
    return response
