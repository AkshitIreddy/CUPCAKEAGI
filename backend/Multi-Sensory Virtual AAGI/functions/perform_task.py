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
import subprocess
from functions.find_task_by_id import find_task_by_id_function
from functions.create_python_script_task import create_python_script_task_function
from functions.create_requirements import create_requirements_function
from functions.handle_error import handle_error_function
from functions.check_success import check_success_function
from functions.talk import talk_function
import datetime

# load the environment variables from the .env file
load_dotenv()

# get the value of the OPENAI_API_KEY environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# get the value of the STATE_DIR environment variable
STATE_DIR = os.environ.get("STATE_DIR")

def perform_task_function(id):
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

    task_details = find_task_by_id_function(id)
    timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    dt_obj = datetime.datetime.strptime(timestamp, '%Y_%m_%d_%H_%M_%S')
    # convert datetime object to desired format
    formatted_dt = dt_obj.strftime('%Y-%m-%d %H:%M:%S')

    instructions = "\nIf the task has a start time, and current time still hasn't reached that time then output the number of seconds to wait for. If the current time has crossed the start time given in the task then output True. ( 1 minute is 60, 5 minutes is 300, 10 minutes is 600 ) DO NOT OUTPUT True IF THE CURRENT TIME HAS NOT CROSSED THE START TIME. ONLY OUTPUT A NUMBER."

    human_template = """Task Details:
Task: The user is requesting to provide a guide in making chocolate chip cookies by 10am. The expected goal is to provide a clear and concise explanation of the steps involved in making chocolate chip cookies, including the ingredients and equipment needed. The additional information that would be helpful for someone performing this task who has no knowledge of the prior conversation is to provide any tips or tricks for making the perfect chocolate chip cookies, such as how to measure ingredients accurately and how to properly mix the dough.\nIMPORTANT TASK CREATION TIME: 2023-04-13 9:47:56\n\nCURRENT TIME: 2023-04-13 09:50:00\nIf current time has crossed start time output True, if it hasn't then output the number of seconds to wait for.""" 
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    assistant_template = "600"
    assistant_message_prompt = AIMessagePromptTemplate.from_template(assistant_template)

    human_template1 = """Task Details:
Task: The user has given a task to send an email to john at 9am. The expected goal is to send an email to John at 9.\nIMPORTANT TASK CREATION TIME: 2023-04-13 08:30:00\nCURRENT TIME: 2023-04-13 08:58:00\nIf current time has crossed start time output True, if it hasn't then output the number of seconds to wait for.""" 
    human_message_prompt1 = HumanMessagePromptTemplate.from_template(human_template1)

    assistant_template1 = "120"  
    assistant_message_prompt1 = AIMessagePromptTemplate.from_template(assistant_template1)

    human_template2 = """Task Details:
Task: The user has given a task to make a report about pandas after 6pm. The expected goal is to make a report after 6pm.\nIMPORTANT TASK CREATION TIME: 2023-04-13 17:46:10\nCURRENT TIME: 2023-04-13 18:18:00\nIf current time has crossed start time output True, if it hasn't then output the number of seconds to wait for.""" 
    human_message_prompt2 = HumanMessagePromptTemplate.from_template(human_template2)

    assistant_template2 = "True"  
    assistant_message_prompt2 = AIMessagePromptTemplate.from_template(assistant_template2)

    human_template3 = """Task Details:
Task: The user has given a task to send a joke after 7am. The expected goal is to send a joke to user after 7.\nIMPORTANT TASK CREATION TIME: 2023-04-13 06:34:20\nCURRENT TIME: 2023-04-13 06:57:00\nIf current time has crossed start time output True, if it hasn't then output the number of seconds to wait for."""
    human_message_prompt3 = HumanMessagePromptTemplate.from_template(human_template3)

    assistant_template3 = "180"  
    assistant_message_prompt3 = AIMessagePromptTemplate.from_template(assistant_template3)

    human_template4 = task_details + "\nCURRENT TIME: " + formatted_dt + instructions 
    human_message_prompt4 = HumanMessagePromptTemplate.from_template(human_template4)

    chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt, assistant_message_prompt, human_message_prompt1, assistant_message_prompt1, human_message_prompt2, assistant_message_prompt2, human_message_prompt3, assistant_message_prompt3, human_message_prompt4])
    response = chat(chat_prompt.format_prompt().to_messages()).content
    print(response)
    if response != "True":
        return 'wait', int(response), ""

    while True:
        script_flag = 0
        python_script = create_python_script_task_function(id)
        print("Python Script is\n" + python_script)

        if python_script == 'none':
            script_flag = 1
            print('script_flag set to 1')

        if script_flag == 0:
            requirements = create_requirements_function(python_script)
            print("Requirements is\n" + requirements)
            if requirements == "empty":
                requirements = ""

            # write python file
            with open(f"tempfiles/python_script{id}.py", "w") as file:
                # Write the text to the file
                file.write(python_script)

            # write requirements file
            with open(f"tempfiles/requirements{id}.txt", "w") as file:
                # Write the text to the file
                file.write(requirements)

        while script_flag == 0:
            # Run multiple commands in succession
            commands = f'conda activate aagi && pip install -r tempfiles/requirements{id}.txt && python tempfiles/python_script{id}.py'
            result = subprocess.run(commands, capture_output=True, shell=True, universal_newlines=True)
            print("Commands finished running")
            if result.returncode == 0:
                print("Shell output:", result.stdout)
                break
            else:
                print("Error executing the command:", result.stderr)
                handle_error_function(python_script , requirements, result.stderr, id)

        information = ""
        if script_flag == 0:
            # Open the file for reading
            with open(f'tempfiles/output{id}.txt', 'r') as file:
                # Read the entire contents of the file
                information = file.read()
                print("Extra Information is\n" + information)

            check , response = check_success_function(python_script, information, task_details)
            if check == 'False':
                continue
            return 'done', 0, response
        
        response = talk_function(id)
        return 'done', 0, response