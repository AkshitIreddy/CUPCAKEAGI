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

# load the environment variables from the .env file
load_dotenv()

# get the value of the OPENAI_API_KEY environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# get the value of the STATE_DIR environment variable
STATE_DIR = os.environ.get("STATE_DIR")

def check_success_function(python_script, information, task_details):
    """
    Checks if a given task was successful.
    Args:
      python_script (str): The Python script to be evaluated.
      information (str): The output of the Python script.
      task_details (str): The details of the task.
    Returns:
      tuple: A tuple containing a boolean value and a string. The boolean value indicates if the task was successful, and the string contains the reason for the choice.
    Examples:
      >>> check_success_function("from ability_functions.send_email import send_email_function\\ndef function(text, receiver):\\n    send_email_function(text, receiver)\\n    return \"success\"\\nresponse = function(\"Hi, i have sent the refund to you!\", \"Bell\")\\nwith open(\"tempfiles/output2792.txt\", \"w\") as f:\\n    f.write(\"Result \" + response)", "success", "Task details: Send an email to Bell telling him you have sent the refund.")
      (True, "The task was successfully completed, Bell has received an email stating that we have sent the refund to him.")
    """
    chat = ChatOpenAI(temperature  = 0, model= 'gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY)
    instruction1 = "If the task was succesful then output True, if not then False."
    instruction2 = "Give the reason for the choice"
    python_script_template = """from ability_functions.send_email import send_email_function
    def function(text, receiver):
        send_email_function(text, receiver)
        return "success"
    response = function("Hi, i have sent the refund to you!", "Bell")
    with open("tempfiles/output2792.txt", "w") as f:
        f.write("Result " + response)
    """
    information_template = "success"
    task_details_template = "Task details: Send an email to Bell telling him you have sent the refund."

    human_template = "Python Code\n" + python_script_template + "\nCode Output\n" + information_template + "\n" + task_details_template + "\n" + instruction1
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    assistant_template = "True"
    assistant_message_prompt = AIMessagePromptTemplate.from_template(assistant_template)

    human_message_prompt1 = HumanMessagePromptTemplate.from_template(instruction2)

    assistant_template1 = "The task was successfully completed, Bell has received an email stating that we have sent the refund to him."
    assistant_message_prompt1 = AIMessagePromptTemplate.from_template(assistant_template1)

    human_template2 = "Python Code\n" + python_script + "\nCode Output\n" + information + "\n" + task_details + "\n" + instruction1
    human_message_prompt2 = HumanMessagePromptTemplate.from_template(human_template2)

    chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt, assistant_message_prompt, human_message_prompt1, assistant_message_prompt1, human_message_prompt2])
    check = chat(chat_prompt.format_prompt().to_messages()).content

    if check == "False":
        return check, ""
    
    assistant_message_prompt2 = AIMessagePromptTemplate.from_template(check)
    human_message_prompt3 = HumanMessagePromptTemplate.from_template(instruction2)

    chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt, assistant_message_prompt, human_message_prompt1, assistant_message_prompt1, human_message_prompt2, assistant_message_prompt2, human_message_prompt3])
    response = chat(chat_prompt.format_prompt().to_messages()).content

    return check, response