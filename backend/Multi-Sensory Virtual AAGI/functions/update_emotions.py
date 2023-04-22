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
import random

# load the environment variables from the .env file
load_dotenv()

# get the value of the OPENAI_API_KEY environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# get the value of the STATE_DIR environment variable
STATE_DIR = os.environ.get("STATE_DIR")


def update_emotion_function(emotion):
    # chat = ChatOpenAI(temperature  = 0, model= 'gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY)
    # # create conversation string, each dialogue seperated by new line
    # with open(os.path.join(STATE_DIR,'conversation.json'), 'r') as f:
    #     data = json.load(f)

    # conversation_str = ''
    # for message in data['conversation']:
    #     conversation_str += message['sender'] + ': ' + message['message']
    #     if message['file_upload'] != 'none':
    #         conversation_str += '\nFile Uploaded by ' + message['sender'] + ": " + message['file_upload']
    #     conversation_str += '\n'

    # conversation_str_template = "human: Hello there, can you help me with something?\nassistant: What do you want? I'm really busy.\nhuman: Sorry to bother you, I just had a question about a product.\nassistant: Well, what is it? Spit it out.\nhuman: I was wondering if you could recommend a good laptop for gaming?\nassistant: Haven't you heard of Google? Why don't you go search for it yourself instead of wasting my time?"

    # human_template = "Conversation:\n{conversation_str_template}\nGive anger emotion value(ranges from 0 to 1), Only Ouput a number and nothing else\n"
    # human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    # assistant_template = "0.86"
    # assistant_message_prompt = AIMessagePromptTemplate.from_template(assistant_template)

    # conversation_str_template1 = "human: Hi, do you have a moment to assist me with something?\nassistant: Sure, what do you need help with?\nhuman: I'm interested in purchasing a new smartphone. Can you recommend a reliable brand?\nassistant: Of course, what's your budget and what features are you looking for?\nhuman: My budget is around $500 and I'm looking for a phone with a good camera and long battery life.\nassistant: Based on your budget and preferences, I would recommend the Google Pixel 4a. It has a great camera and good battery life. Would you like me to send you a link to purchase it?\nhuman: Yes, please. Thank you for your help!\nassistant: You're welcome. Let me know if you have any other questions."

    # human_template1 = "Conversation:\n{conversation_str_template1}\nGive happiness emotion value(ranges from 0 to 1), Only Ouput a number and nothing else\n"
    # human_message_prompt1 = HumanMessagePromptTemplate.from_template(human_template1)

    # assistant_template1 = "0.92"
    # assistant_message_prompt1 = AIMessagePromptTemplate.from_template(assistant_template1)

    # human_template2 = "Conversation:\n{conversation_str}\nGive {emotion} emotion value(ranges from 0 to 1):\n"
    # human_message_prompt2 = HumanMessagePromptTemplate.from_template(human_template2)

    # chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt, assistant_message_prompt, human_message_prompt1 , assistant_message_prompt1, human_message_prompt2])
    # response = chat(chat_prompt.format_prompt(conversation_str = conversation_str, conversation_str_template =conversation_str_template, emotion = emotion, conversation_str_template1 = conversation_str_template1).to_messages()).content

    # random_number = random.uniform(0.1, 0.2)
    # base_num = float(response)
    # response = str(random_number + base_num)

    with open(f"state_of_mind/{emotion}.txt", "r") as f:
        val = str(f.read())
    
    random_number1 = random.uniform(0.1, 0.3)
    base_num = float(val)
    random_number2 = random.uniform(0.1, 0.3)
    response = str(round(random_number1 + base_num - random_number2,2))
      
    with open(f"state_of_mind/{emotion}.txt", "w") as file:
        # Write the text to the file
        file.write(response)


def update_emotions_function():
    update_emotion_function('happiness')
    update_emotion_function('sadness')
    update_emotion_function('anger')
    update_emotion_function('fear')
    update_emotion_function('creativity')
    update_emotion_function('curiosity')
