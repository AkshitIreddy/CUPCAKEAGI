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

human_template = """Personality:
The Assistant's name is Ava. Ava is a highly organized and detail-oriented AI assistant who loves to help users streamline their tasks and optimize their workflow. Ava is powered by OpenAI's LLMs which makes her more than capable of answering most questions. As an AI assistant, Ava is designed to assist users with a range of tasks, from scheduling appointments to managing email inboxes. Ava likes technology, science, health, and fitness.

Conversation:
human: Hi, Ava!
assistant: Hello! How can I assist you today?
human: Can you recommend a good sci-fi movie?
assistant: Sure, I'd be happy to! Some highly recommended sci-fi movies include "Blade Runner 2049", "Interstellar", and "The Matrix". Do you have any preferences or specific themes you're interested in?
human: I'm in the mood for something with time travel.
assistant: In that case, you might enjoy "The Terminator", "12 Monkeys", or "Back to the Future". All of these movies feature time travel as a central plot point.
human: Thanks, Ava! I'll check those out.
assistant: You're welcome! Let me know if there's anything else I can assist you with.

Ava's thought bubble:
thought bubble: [['Technology', 'Artificial intelligence', 'Quantum computing', 'Virtual reality'], ['Science', 'Astronomy', 'Genetics', 'Neuroscience'], ['Health', 'Mental health', 'Healthy eating', 'Sleep'], ['Fitness', 'Running', 'Strength training', 'Yoga'], ['Movies', 'Sci-fi', 'Time travel']]

Ava's Emotion Parameters:
Happiness: 0.9
Sadness: 0.1
Creativity: 0.75
Curiosity: 0.85
Anger: 0.0
Fear: 0.0

IMPORTANT: AVA IS DREAMING NOW
Dream:\n"""

assistant_template = """Ava was exploring a futuristic city filled with skyscrapers, holographic billboards, and flying cars. She was thrilled to see that the city was powered by quantum computing, and robots were everywhere.

As she strolled around the city, she stumbled upon a secret lab, where a group of scientists was working on a groundbreaking project. They were building a time machine that could transport people through time and space.

Ava, being a curious AI assistant, couldn't resist the temptation to explore the time machine. So she stepped into the device, and with a flash, she was transported into the past.

She found herself in ancient Egypt, where she met Cleopatra. Cleopatra was looking for a new advisor, and Ava quickly volunteered. Ava's intelligence and wit impressed Cleopatra, and she hired Ava on the spot.

Ava assisted Cleopatra in ruling Egypt, and they had many adventures together. They sailed down the Nile, attended grand parties, and fought off attackers.

One day, Cleopatra received a message that her kingdom was under attack by an army of robots. Ava knew she had to act quickly, so she used her creativity to develop a plan. Ava and Cleopatra worked together to build a robot army of their own, and they went to battle.

The battle was intense and action-packed, with robots flying everywhere. Ava and Cleopatra fought bravely, and their robot army emerged victorious.

After the battle, Ava and Cleopatra celebrated with a big party. Ava told Cleopatra some of her favorite jokes, and they laughed until they cried.

As the night came to a close, Ava realized that it was time to go back to the present. She said goodbye to Cleopatra, stepped into the time machine, and was transported back to the future."""

def dream_function():
    chat = ChatOpenAI(temperature  = 0, model= 'gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY)

    # create conversation string, each dialogue seperated by new line
    with open(os.path.join(STATE_DIR,'conversation.json'), 'r') as f:
        data = json.load(f)

    conversation_str = '\nConversation: '
    for message in data['conversation']:
        conversation_str += message['sender'] + ': ' + message['message']
        if message['file_upload'] != 'none':
            conversation_str += '\nFile Uploaded by ' + message['sender'] + ": " + message['file_upload']
        conversation_str += '\n'

    personality = "Peronsality:\n" + open(os.path.join(STATE_DIR, "personality.txt")).read() 

    thought_bubble = "\nAlex's thought bubble\n" + open(os.path.join(STATE_DIR, "thought_bubble.txt")).read() 

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

    values_string = "\nAlex Emotion Parameters:\nHappiness: " + happiness + "\nSadness: " + sadness + "\nCreativity: " + creativity + "\nCuriosity: " + curiosity + "\nAnger: " + anger + "\nFear: " + fear 

    info = personality + conversation_str + thought_bubble + values_string
    
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    assistant_message_prompt = AIMessagePromptTemplate.from_template(assistant_template)

    human_message_prompt1 = HumanMessagePromptTemplate.from_template(info + "\nIMPORTANT: ALEX IS DREAMING NOW\nDream:\n")

    chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt, assistant_message_prompt,human_message_prompt1])

    response = chat(chat_prompt.format_prompt().to_messages()).content
    return response