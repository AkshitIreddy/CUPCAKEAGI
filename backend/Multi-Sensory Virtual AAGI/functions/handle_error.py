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

python_script_template = """import numpy as np
import pandas as pd

# create a numpy array with random numbers
arr = np.random.randn(5, 3)

# create a pandas dataframe from the numpy array
df = pd.DataFrame(arr, columns=['A', 'B', 'C'])

# add a new column to the dataframe
df['D'] = pd.Series(['foo', 'bar', 'baz', 'qux', 'quux'])

# display the dataframe
print(df)
"""

requirements_template = """numpy
pnds
"""

modified_text = """requirements.txt
numpy
pandas
python_script.py
import numpy as np
import pandas as pd

# create a numpy array with random numbers
arr = np.random.randn(5, 3)

# create a pandas dataframe from the numpy array
df = pd.DataFrame(arr, columns=['A', 'B', 'C'])

# add a new column to the dataframe
df['D'] = pd.Series(['foo', 'bar', 'baz', 'qux', 'quux'])

# display the dataframe
print(df)
""" 

def handle_error_function(python_script, requirements, error, id):
    """
    Handles errors in python scripts and requirements files.
    Args:
      python_script (str): The python script to be modified.
      requirements (str): The requirements file to be modified.
      error (str): The error message.
      id (int): The id of the conversation.
    Returns:
      None: No return value.
    Side Effects:
      Writes modified python script and requirements files to the tempfiles directory.
    Examples:
      >>> handle_error_function(python_script_template, requirements_template, error_template, 1)
      None
    """
    chat = ChatOpenAI(temperature  = 0, model= 'gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY)

    # create conversation string, each dialogue seperated by new line
    with open(os.path.join(STATE_DIR,'conversation.json'), 'r') as f:
        data = json.load(f)

    conversation_str = ''
    for message in data['conversation']:
        conversation_str += message['sender'] + ': ' + message['message']
        if message['file_upload'] != 'none':
            conversation_str += '\nFile Uploaded by ' + message['sender'] + ": " + message['file_upload']
        conversation_str += '\n'

    error_template = """ERROR: Could not find a version that satisfies the requirement pnds (from versions: none\nERROR: No matching distribution found for pnds"""

    human_template1 = "Error has been caused after running either the python_script{id}.py or installing requirements{id}.txt.\n" + error_template + "\nThis is the code in python_script{id}.py:" + python_script_template + "\nThe goal of this python code is to get information that can help in answering the question from the user in this conversation\n" + conversation_str + "\nThis is the text in requirements{id}.txt:" + requirements_template + "Give the modified text for python_script.py and requirements.txt to get rid of this error. DO NOT SAY ANYTHING ELSE. ONLY GENERATE THE PYTHON SCRIPT AND REQUIREMENTS FILE IN THE SPECIFIED FORMAT."
    human_message_prompt1 = HumanMessagePromptTemplate.from_template(human_template1)

    assistant_template1 = modified_text
    assistant_message_prompt1 = AIMessagePromptTemplate.from_template(assistant_template1)

    human_template2 = "Error has been caused after running either the python_script{id}.py or installing requirements{id}.txt.\n" + error + "\nThis is the code in python_script{id}.py:" + python_script + "\nThis is the code in requirements{id}.txt:" + requirements + "Give the modified text for these files to get rid of this error.  DO NOT SAY ANYTHING ELSE. ONLY GENERATE THE PYTHON SCRIPT AND REQUIREMENTS FILE IN THE SPECIFIED FORMAT."
    human_message_prompt2 = HumanMessagePromptTemplate.from_template(human_template2)

    chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt1, assistant_message_prompt1, human_message_prompt2])
    response = chat(chat_prompt.format_prompt(id=id).to_messages()).content
    print(response)
    # extract the requirements
    requirements = re.findall(r'^\s*(\w+)', response, flags=re.MULTILINE)

    requirements_list = []
    for r in requirements:
        if r == 'python_script':
            break
        requirements_list.append(r)
    requirements_str = "\n".join(requirements_list[1:])  # ignore the first element which is 'requirements.txt'

    # extract the python script
    python_script = re.search(r'python_script(?:\d+)?\.py\s*\n(.+)', response, flags=re.DOTALL).group(1)

    # write python file
    with open(f"tempfiles/python_script{id}.py", "w") as file:
        # Write the text to the file
        file.write(python_script)

    # write requirements file
    with open(f"tempfiles/requirements{id}.txt", "w") as file:
        # Write the text to the file
        file.write(requirements_str)