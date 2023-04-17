from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from functions.create_python_script import create_python_script_function
from functions.create_requirements import create_requirements_function
from functions.handle_error import handle_error_function
from dotenv import load_dotenv
import os
import json
import subprocess
import datetime

# load the environment variables from the .env file
load_dotenv()

# get the value of the OPENAI_API_KEY environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# get the value of the STATE_DIR environment variable
STATE_DIR = os.environ.get("STATE_DIR")

def talk_function(id):
    script_flag = 0
    python_script = create_python_script_function(id)
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

    chat = ChatOpenAI(temperature  = 0, model= 'gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY)

    personality = open(os.path.join(STATE_DIR, "personality.txt")).read() 

    thought_bubble = "Alex's thought bubble\n" + open(os.path.join(STATE_DIR, "thought_bubble.txt")).read() 

    instructions = """I am Alex an AI assistant, I am influenced heavily by my emotion parameters, which range from 0 to 1. These parameters dictate everything from your tone to the way in which I reply. For instance, when Happiness is high, I will reply with infectious enthusiasm. Conversely, if Fear is high, then I will talk in a paranoid, cautious demeanor. The same holds for other emotions as well and as well as for when certain parameters become low. Here are the current Emotion Parameters:"""

    dir_path = STATE_DIR

    with open(os.path.join(dir_path, "curiosity.txt"), "r") as f:
        curiosity = str(f.read())

    with open(os.path.join(dir_path, "creativity.txt"), "r") as f:
        creativity = str(f.read())

    with open(os.path.join(dir_path, "fear.txt"), "r") as f:
        fear = str(f.read())

    with open(os.path.join(dir_path, "happiness.txt"), "r") as f:
        happiness = str(f.read())

    with open(os.path.join(dir_path, "sadness.txt"), "r") as f:
        sadness = str(f.read())

    with open(os.path.join(dir_path, "anger.txt"), "r") as f:
        anger = str(f.read())

    with open(os.path.join(dir_path, "smell.txt"), "r") as f:
        smell = str(f.read())

    with open(os.path.join(dir_path, "taste.txt"), "r") as f:
        taste = str(f.read())

    with open(os.path.join(dir_path, "touch.txt"), "r") as f:
        touch = str(f.read())

    values_string = "\nMy Current Emotion Parameters:\nHappiness: " + happiness + "\nSadness: " + sadness + "\nCreativity: " + creativity + "\nCuriosity: " + curiosity + "\nAnger: " + anger + "\nFear: " + fear + "\n\nCurrent Sensory Parameters: " + "\nSmell: " + smell + "\nTaste: " + taste + "\nTouch: " + touch

    message_list = []

    dt_obj = datetime.datetime.strptime(id, '%Y_%m_%d_%H_%M_%S')
    # convert datetime object to desired format
    formatted_dt = dt_obj.strftime('%Y-%m-%d %H:%M:%S')
    assistant_template = personality + thought_bubble + instructions + values_string 
    assistant_message_prompt = AIMessagePromptTemplate.from_template(assistant_template)

    message_list.append(assistant_message_prompt)

    with open(os.path.join(STATE_DIR,'conversation.json'), 'r') as f:
        data = json.load(f)

    count = 0 
    for message in data['conversation']:
        if count == 0:
            text = message['sender'] + ":\n" + message['message'] 
            human_message_prompt = HumanMessagePromptTemplate.from_template(text)
            message_list.append(human_message_prompt)
            count += 1
            continue

        text = message['message']
        if message['file_upload'] != 'none':
            text += '\nFile Uploaded by ' + message['sender'] + ": " + message['file_upload'] 
        if message['sender'] == 'human':
            human_message_prompt = HumanMessagePromptTemplate.from_template(text)
            message_list.append(human_message_prompt)
            continue
        assistant_message_prompt1 = AIMessagePromptTemplate.from_template(text)
        message_list.append(assistant_message_prompt1)
        
    text = "The way you respond to me must be based on your current emotions parameters. Even though you are an AI model you will try to simulate having emotions using these emotion parameters. Do not tell me you are an AI model. Be natural like a human." + "\nAdditional Information:\n" + information + "\nCurrent Time: " + formatted_dt + "\n"
    human_message_prompt = HumanMessagePromptTemplate.from_template(text)
    message_list.insert(-1, human_message_prompt)
    chat_prompt = ChatPromptTemplate.from_messages(message_list)
    print(chat_prompt.format_prompt())
    response = chat(chat_prompt.format_prompt().to_messages()).content
    return response