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

code = """import numpy as np
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

packages = """numpy
pandas
"""

code1 = """import os
import sys
import json
from ability_functions import search_function

search_function("Weather")
"""

packages1 = "empty"

human_template = "Do not keep packages like os, sys and other pre-installed packages in python in requirements.txt.\nDo not keep ability_functions in requirements.txt, they do not need to be installed. If no packages are needed to be installed then output 'empty' ."

human_template1 = "Give the list of packages for requirements.txt to install based on this code\n" + code + "\nDo not keep ability_functions in requirements.txt, they do not need to be installed. If no packages are needed to be installed then output 'empty' ."

human_template2 = "Give the list of packages for requirements.txt to install based on this code\n" + code1 + "\nDo not keep ability_functions in requirements.txt, they do not need to be installed. If no packages are needed to be installed then ONLY output 'empty' ."

human_template3 = "Give the list of packages for requirements.txt to install based on this code\n{script}\nDo not keep ability_functions in requirements.txt, they do not need to be installed. If no packages are needed to be installed then ONLY output 'empty' ."

def create_requirements_function(script):
    """
    Generates a list of packages for requirements.txt based on a given code.
    Args:
      script (str): The code to generate the list of packages from.
    Returns:
      str: A list of packages for requirements.txt, or 'empty' if no packages are needed.
    Examples:
      >>> create_requirements_function("import numpy as np")
      "numpy"
    """
    chat = ChatOpenAI(temperature  = 0, model= 'gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY)
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    human_message_prompt1 = HumanMessagePromptTemplate.from_template(human_template1)

    assistant_template1 = packages
    assistant_message_prompt1 = AIMessagePromptTemplate.from_template(assistant_template1)

    human_message_prompt2 = HumanMessagePromptTemplate.from_template(human_template2)

    assistant_template2 = packages1
    assistant_message_prompt2 = AIMessagePromptTemplate.from_template(assistant_template2)

    human_message_prompt3 = HumanMessagePromptTemplate.from_template(human_template3)

    chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt, human_message_prompt1, assistant_message_prompt1, human_message_prompt2, assistant_message_prompt2, human_message_prompt3])
    requirements = chat(chat_prompt.format_prompt(script=script).to_messages()).content

    if 'empty' in requirements:
        # if yes, then assign the value 'empty' to the variable
        requirements = 'empty'

    return requirements.replace('ability_functions' , "")