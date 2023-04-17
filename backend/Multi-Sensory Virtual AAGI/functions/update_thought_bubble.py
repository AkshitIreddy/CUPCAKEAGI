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

def update_thought_bubble_function():
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

    with open(os.path.join(STATE_DIR, "thought_bubble.txt"), "r") as f:
        thought_bubble = f.read()

    thought_bubble_template = "[['Music', 'pop', 'rock', 'jazz'], ['Travel', 'beach', 'mountains', 'adventure'], ['Food', 'sushi', 'pasta', 'vegan']]"
    thought_bubble_modified_template = "[['TV Shows', 'Game of Thrones', 'Friends', 'The Office', 'Breaking Bad', 'Stranger Things'], ['Travel', 'beach', 'mountains', 'adventure'], ['Food', 'sushi', 'pasta', 'vegan']]"
    conversation_str_template = """human: Hi there!
assistant: Hello! How can I assist you today?
human: Can you tell me about some popular TV shows?
assistant: Of course! Some popular TV shows include Game of Thrones, Friends, The Office, Breaking Bad, and Stranger Things. Game of Thrones is known for its epic battles and fantasy world with dragons, while Friends is a classic sitcom about a group of friends in New York City. The Office is a mockumentary-style show about a group of employees working at a paper company, and Breaking Bad is a thrilling drama about a chemistry teacher who becomes a drug kingpin. Stranger Things is a sci-fi/horror series set in the 1980s that follows a group of kids as they uncover supernatural mysteries."""

    human_template = "Current thought bubble:\n{thought_bubble_template}\nConversation:\n{conversation_str_template}\nGive modified thought bubble:\n"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    assistant_template = "{thought_bubble_modified_template}"
    assistant_message_prompt = AIMessagePromptTemplate.from_template(assistant_template)

    human_template1 = "Current thought bubble:\n{thought_bubble}\nConversation:\n{conversation_str}\nGive modified thought bubble:\n"
    human_message_prompt1 = HumanMessagePromptTemplate.from_template(human_template1)

    chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt, assistant_message_prompt, human_message_prompt1])
    response = chat(chat_prompt.format_prompt(thought_bubble=thought_bubble, thought_bubble_template = thought_bubble_template, thought_bubble_modified_template=thought_bubble_modified_template, conversation_str = conversation_str, conversation_str_template =conversation_str_template).to_messages()).content

    with open(f"state_of_mind/thought_bubble.txt", "w") as file:
        # Write the text to the file
        file.write(response)