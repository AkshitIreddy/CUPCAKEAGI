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
from functions.find_task_by_id import find_task_by_id_function

# load the environment variables from the .env file
load_dotenv()

# get the value of the OPENAI_API_KEY environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# get the value of the STATE_DIR environment variable
STATE_DIR = os.environ.get("STATE_DIR")

assistant_template2 = """import os
import sys

# Get the absolute path to the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the path to the root directory
sys.path.append(os.path.join(current_dir, '..'))

from ability_functions.search import search_function
from ability_functions.calculator import calculator_function
from ability_functions.natural_language_task import natural_language_task_function

def python_function(text):
    # search for relevant information on this topic
    search_response = search_function(text)
    # create an instructions that tells the natural language function to extract the search response and frame it as question
    instructions = "Create a question in words that tells to divide the total amount spent by 10.\nYou can find the total amount spent by analyzing this piece of text\n" + search_response
    # get the question
    question = natural_language_task_function(instructions)
    # pass the question to the calculator function to get the answer
    answer = calculator_function(question)
    # write the result to tempfiles/output{id}.txt file
    with open("tempfiles/output{id}.txt", "w") as f:
        f.write("Search response was " + search_response)
        f.write("After Computation the answer is " + str(answer))

#call the function
python_function("Total Cost USA Latest Semiconductor Bill")"""

assistant_template3 = """import os
import sys

# Get the absolute path to the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the path to the root directory
sys.path.append(os.path.join(current_dir, '..'))

from ability_functions.search import search_function
from ability_functions.natural_language_task import natural_language_task_function

def python_function(name1, name2):
    # search for relevant information on first laptop
    search_response1 = search_function("Review of " + name1)
    # search for relevant information on second laptop
    search_response2 = search_function("Review of " + name2)
    # create an instructions that tells the natural language function to determine which laptop is best based on the above search info
    instruction = "Which is laptop is better?" + "Laptop 1 info" + search_response1 + "Laptop 2 info" + search_response2
    # get the answer
    answer = natural_language_task_function(instruction)
    # write the answer to tempfiles/output{id}.txt file
    with open("tempfiles/output{id}.txt", "w") as f:
        f.write(answer)

#call the function
python_function("alienware X839", "alienware X758")"""

import_instructions = "Example of importing these functions\nimport os\nimport sys\n# Get the absolute path to the current directory\ncurrent_dir = os.path.dirname(os.path.abspath(__file__))\n# Add the path to the root directory\nsys.path.append(os.path.join(current_dir, '..'))\n# Import the search_function from the search module, You need to append _function to the name of the tool\nfrom ability_functions.search import search_function"

instructions = "To complete the user's task, if you need to use any of the above mentioned tools you can import them by following the import instructions. To use the above tools or to execute python code write a python script and save the output to tempfiles/output{id}.txt if you don't expect any output then save task success message or any logs or data that can be helpful in determining if the task was a success. "

human_template1 = """Conversation:\nhuman: Hi there! I'm interested in learning more about space. Can you tell me something interesting?
assistant: Of course! Did you know that there are over 100 billion galaxies in the observable universe, each
containing billions of stars and planets?
human: Wow, that's mind-boggling! Can you tell me about the possibility of life on other planets?\nIf you don't need to execute python code or use any of the above tools to solve the user's task then output none .You can chain abilities in the python script. You can use the natural_language_task function to connect different abilities."""

human_template2 = """Conversation:\nhuman: Hi there! I'm interested in learning more about semi-conductors. Can you tell me something interesting?
assistant: Sure! Semi-conductors are materials that can conduct electricity under certain conditions, but not under others. This unique property makes them essential components in electronic devices like computer chips and solar panels.
human: How much did the usa spend on the latest semiconductor bill? How much would it be per year for 10 years when spread out?\nIf you don't need to execute python code or use any of the above tools to solve the user's task then output none .You can chain abilities in the python script. You can use the natural_language_task function to connect different abilities."""
human_template3 = """Conversation:\nhuman: Hi there! I'm planning to buy a laptop.
assistant: Wow, that's great to hear!
human: Which laptop is better alienware X839 or alienware X758?\nIf you don't need to execute python code or use any of the above tools to get information that may in help in answering the user's question then output 'none'. You can chain abilities in the python script."""
human_template4 = "Conversation:\n{conversation_str}\n{task_details}\nIf you don't need to execute python code or use any of the above tools to solve the user's task then output none .You can chain abilities in the python script. You can use the natural_language_task function to connect different abilities."

def create_python_script_task_function(id):
    """
    Creates a python script for a given task.
    Args:
      id (int): The ID of the task.
    Returns:
      str: The python script for the task.
    Examples:
      >>> create_python_script_task_function(1)
      'import os\\nimport sys\\n# Get the absolute path to the current directory\\ncurrent_dir = os.path.dirname(os.path.abspath(__file__))\\n# Add the path to the root directory\\nsys.path.append(os.path.join(current_dir, '..'))\\n# Import the search_function from the search module, You need to append _function to the name of the tool\\nfrom ability_functions.search import search_function\\ndef python_function(text):\\n    # search for relevant information on this topic\\n    search_response = search_function(text)\\n    # create an instructions that tells the natural language function to extract the search response and frame it as question\\n    instructions = "Create a question in words that tells to divide the total amount spent by 10.\\nYou can find the total amount spent by analyzing this piece of text\\n" + search_response\\n    # get the question\\n    question = natural_language_task_function(instructions)\\n    # pass the question to the calculator function to get the answer\\n    answer = calculator_function(question)\\n    # write the result to tempfiles/output{id}.txt file\\n    with open("tempfiles/output{id}.txt", "w") as f:\\n        f.write("Search response was " + search_response)\\n        f.write("After Computation the answer is " + str(answer))\\n#call the function\\npython_function("Total Cost USA Latest Semiconductor Bill")'
    """
    chat = ChatOpenAI(temperature  = 0, model= 'gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY)

    personality = open(os.path.join(STATE_DIR, "personality.txt")).read()

    task_details = find_task_by_id_function(id)

    # Load the ability JSON file
    with open(os.path.join(STATE_DIR,'abilities.json'), 'r') as f:
        abilities_data = json.load(f)

    abilities = "Tools: \n" + '\n'.join( [ability['name'] + ": " + ability['description'] + "\n" + ability['directions'] for ability in abilities_data['abilities']])

    # create conversation string, each dialogue seperated by new line
    with open(os.path.join(STATE_DIR,'conversation.json'), 'r') as f:
        data = json.load(f)

    conversation_str = ''
    for message in data['conversation']:
        conversation_str += message['sender'] + ': ' + message['message']
        if message['file_upload'] != 'none':
            conversation_str += '\nFile Uploaded by ' + message['sender'] + ": " + message['file_upload']
        conversation_str += '\n'   

    intial_text = personality + "\n" + abilities + "\n" + import_instructions + "\n" + instructions

    human_template = intial_text
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    human_message_prompt1 = HumanMessagePromptTemplate.from_template(human_template1)

    assistant_template1 = "none"
    assistant_message_prompt1 = AIMessagePromptTemplate.from_template(assistant_template1)

    human_message_prompt2 = HumanMessagePromptTemplate.from_template(human_template2)

    assistant_message_prompt2 = AIMessagePromptTemplate.from_template(assistant_template2)
    human_message_prompt3 = HumanMessagePromptTemplate.from_template(human_template3)

    assistant_message_prompt3 = AIMessagePromptTemplate.from_template(assistant_template3)
    human_message_prompt4 = HumanMessagePromptTemplate.from_template(human_template4)

    chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt, human_message_prompt1, assistant_message_prompt1, human_message_prompt2, assistant_message_prompt2, human_message_prompt3, assistant_message_prompt3, human_message_prompt4])
    python_script = chat(chat_prompt.format_prompt(conversation_str=conversation_str, id = id, task_details=task_details).to_messages()).content
    return python_script