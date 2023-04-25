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

Ava's thought bubble:
thought bubble: [['Technology', 'Artificial intelligence', 'Quantum computing', 'Virtual reality'], ['Science', 'Astronomy', 'Genetics', 'Neuroscience'], ['Health', 'Mental health', 'Healthy eating', 'Sleep'], ['Fitness', 'Running', 'Strength training', 'Yoga'], ['Movies', 'Sci-fi', 'Time travel']]

Ava's Emotion Parameters:
Happiness: 0.9
Sadness: 0.1
Creativity: 0.75
Curiosity: 0.85
Anger: 0.0
Fear: 0.0

IMPORTANT: AVA IS HAVING A RANDOM THOUGHT NOW
THOUGHT:\n"""

assistant_template = """What if we could go back in time and watch Leonardo da Vinci paint the Mona Lisa or witness the construction of the pyramids in ancient Egypt? And what about the future? """

def random_thought_function():
    """
    Generates a random thought for the AI assistant Alex.
    Args:
      None
    Returns:
      str: The random thought generated for Alex.
    Side Effects:
      Loads environment variables from the .env file.
      Reads from the STATE_DIR environment variable.
      Reads from the personality.txt, thought_bubble.txt, curiosity.txt, creativity.txt, fear.txt, happiness.txt, sadness.txt, and anger.txt files.
    Examples:
      >>> random_thought_function()
      "What if we could go back in time and watch Leonardo da Vinci paint the Mona Lisa or witness the construction of the pyramids in ancient Egypt? And what about the future?"
    """
    chat = ChatOpenAI(temperature  = 0, model= 'gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY)

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

    info = personality + thought_bubble + values_string
    
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    assistant_message_prompt = AIMessagePromptTemplate.from_template(assistant_template)

    human_message_prompt1 = HumanMessagePromptTemplate.from_template(info + "\nIMPORTANT: ALEX IS HAVING A RANDOM THOUGHT NOW\nThought:\n")

    chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt, assistant_message_prompt,human_message_prompt1])

    response = chat(chat_prompt.format_prompt().to_messages()).content
    return response