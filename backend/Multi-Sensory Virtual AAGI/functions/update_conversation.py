from dotenv import load_dotenv
import os
import json
import tiktoken
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# load the environment variables from the .env file
load_dotenv()

# get the value of the OPENAI_API_KEY environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# get the value of the STATE_DIR environment variable
STATE_DIR = os.environ.get("STATE_DIR")

def tiktoken_len(text):
    """
    Calculates the length of a text in tokens.
    Args:
      text (str): The text to calculate the length of.
    Returns:
      int: The length of the text in tokens.
    Examples:
      >>> tiktoken_len("Hello world")
      2
    """
    tokenizer = tiktoken.get_encoding('cl100k_base')
    tokens = tokenizer.encode(
        text,
        disallowed_special={}
    )
    return len(tokens)

def summarize(text):
    """
    Summarizes a text using OpenAI's GPT-3.5-Turbo model.
    Args:
      text (str): The text to summarize.
    Returns:
      str: The summarized text.
    Examples:
      >>> summarize("This is a long text.")
      "This is a short summary of the text."
    """
    chat = ChatOpenAI(temperature  = 0, model= 'gpt-3.5-turbo')
    human_template1 = "Your Job is to convert this text to clear, concise, readable summaries without missing any important details that could be important for someone to know to answer a question. Summarize this text without losing any important details. \n {text} ."
    human_message_prompt1 = HumanMessagePromptTemplate.from_template(human_template1)
    chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt1])
    response = chat(chat_prompt.format_prompt(text = text).to_messages())
    return response.content

def update_conversation_function(user_response, sender, file_path, file_description):
    """
    Updates the conversation with a new message.
    Args:
      user_response (str): The user's response.
      sender (str): The sender of the message.
      file_path (str): The path of the file uploaded by the user.
      file_description (str): The description of the file uploaded by the user.
    Returns:
      str: An empty string.
    Examples:
      >>> update_conversation_function("Hello!", "User", "", "")
      ""
    """
    with open(os.path.join(STATE_DIR, "num_memories.txt"), "r") as f:
        num_memories = int(f.read().strip())

    # create conversation string, each dialogue seperated by new line
    with open(os.path.join(STATE_DIR,'conversation.json'), 'r') as f:
        data = json.load(f)

    conversation_str = ''
    for message in data['conversation']:
        if message['sender'] == 'Summary':
            continue
        conversation_str += message['sender'] + ': ' + message['message']
        if message['file_upload'] != 'none':
            conversation_str += '\nFile Uploaded by ' + message['sender'] + ": " + message['file_upload']
        conversation_str += '\n'

    file_upload = 'none'
    if file_path != "":
        file_upload = "File has been uploaded by user, File path is\n" + file_path + ".\nFile Description is\n" + file_description
    
    persist_directory = 'memory'
    embeddings = OpenAIEmbeddings()
    
    print(tiktoken_len(conversation_str))
    if num_memories == 0:
        if tiktoken_len(conversation_str) < 600:
            print("Inside num memories 0 and less than 600  tokens")
            # Add a new message to the conversation
            new_message = {"sender": sender, "message": user_response, "file_upload": file_upload}
            data["conversation"].append(new_message)
            # Write the updated JSON data back to the file
            with open(os.path.join(STATE_DIR,'conversation.json'), 'w') as f:
                json.dump(data, f)
            
            return ""
    

    if tiktoken_len(conversation_str) > 600:
        print("inside of more than 600 tokens")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 200,
            chunk_overlap  = 0,
            length_function = tiktoken_len,
        )
        texts = text_splitter.split_text(conversation_str)

        print("Summarising texts")
        summarized_texts = []
        for text in texts:
            summarized_texts.append(summarize(text))

        if num_memories == 0:
            print("Creating first database")
            vectordb = Chroma.from_texts(summarized_texts, embeddings, persist_directory=persist_directory)
            vectordb.persist()
            num_memories += 1
            with open(os.path.join(STATE_DIR, "num_memories.txt"), 'w') as f:
                f.write(str(1))
            f.close()
        else:
            vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
            print("adding summarised texts")
            vectordb.add_texts(summarized_texts)

    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

    search_string = conversation_str + sender + user_response
    docs = vectordb.similarity_search(search_string, k = 3) 
    summarized_text = ""
    for i in docs:
        summarized_text = summarized_text + "\n" + i.page_content

    data['conversation'][0]['message'] = summarized_text

    if tiktoken_len(conversation_str) > 600:
        print("inside bottom check")
        summary = data['conversation'][0]
        data['conversation'] = [summary, {
        'sender': sender,
        'message': user_response,
        'file_upload': file_upload
        }]
    else:
        new_message = {"sender": sender, "message": user_response, "file_upload": file_upload}
        data["conversation"].append(new_message)   

    with open(os.path.join('state_of_mind','conversation.json'), 'w') as f:
        json.dump(data, f)
