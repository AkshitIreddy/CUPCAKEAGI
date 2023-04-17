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

instructions = "\nIs the user asking you to perform a task or are they just talking to you? If they are talking to you or asking questions or asking you to explain things then output Talk. A task is something where if the user gives you a start time or deadline.\nIF THE QUESTION DOES NOT HAVE A START TIME OR DEADLINE THEN IT IS NOT A TASK. IF THE USER IS ASKING A QUESTION OR ASKING TO EXPLAIN SOMETHING LIKE HOW OR WHAT OR EXPLAIN THEN IT IS Talk. If the question has the words what or explain or how then it is very likely that it is Talk."

human_template1 = """Conversation\nhuman: Hello there! I'm interested in learning about endangered species. Can you tell me something interesting?
assistant: Sure! Did you know that the pangolin is the most trafficked animal in the world? All eight species of pangolins are now endangered due to illegal poaching for their scales and meat.
human: That's really sad. What can we do to protect endangered species like the pangolin?"""
human_template2 = """Conversation\nhuman: Hi, Alex. I have been thinking about immortality lately. What are your thoughts on the topic?
assistant: Immortality is a fascinating subject that has been debated for centuries. Some people believe that achieving immortality is possible, while others think it is impossible.
human: Do you think that immortality will ever be possible?
assistant: Many scientists and researchers are working on ways to extend human lifespan and even potentially achieve immortality. Some studies have shown that certain treatments and lifestyle changes can increase lifespan and healthspan, but the idea of true immortality is still largely hypothetical and debated among experts.
human: Interesting. Give me comphrehensive report on whether immortality is possible by 6pm."""
human_template3 = """Conversation\nhuman: Hi, i like cycling!
assistant: That's nice!
human: can you explain how to fill a tire, the instructions should be written as a poem."""
human_template4 = """Conversation\n{conversation_str}\nIF THE QUESTION DOES NOT HAVE A START TIME OR DEADLINE THEN IT IS NOT A TASK. UNDER NO CIRCUMSTANCE SHOULD YOU OUTPUT Task WHEN START TIME OR DEADLINE IS NOT MENTIONED. YOU SHOULD OUTPUT Talk. Talk IS THE DEFAULT ANSWER ALWAYS. IF THE USER EXPLICITLY MENTION ITS A TASK THEN OUTPUT Task ."""
def determine_task_talk_function():
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

    Human_template = intro + ability_names + instructions 
    Human_message_prompt = HumanMessagePromptTemplate.from_template(Human_template)

    human_message_prompt1 = HumanMessagePromptTemplate.from_template(human_template1)

    assistant_template1 = "Talk"
    assistant_message_prompt1 = AIMessagePromptTemplate.from_template(assistant_template1)
    
    human_message_prompt2 = HumanMessagePromptTemplate.from_template(human_template2)

    assistant_template2 = "Task"
    assistant_message_prompt2 = AIMessagePromptTemplate.from_template(assistant_template2)

    human_message_prompt3 = HumanMessagePromptTemplate.from_template(human_template3)

    assistant_template3 = "Talk"
    assistant_message_prompt3 = AIMessagePromptTemplate.from_template(assistant_template3)

    human_message_prompt4 = HumanMessagePromptTemplate.from_template(human_template4)

    chat_prompt = ChatPromptTemplate.from_messages([Human_message_prompt, human_message_prompt2, assistant_message_prompt2, human_message_prompt1, assistant_message_prompt1, human_message_prompt3, assistant_message_prompt3, human_message_prompt4])
    response = chat(chat_prompt.format_prompt(conversation_str=conversation_str).to_messages()).content
    return response