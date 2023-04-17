import os
import datetime
from fastapi import FastAPI, HTTPException, Request, Depends, File, UploadFile, Form, BackgroundTasks
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
from functions.file_describe import file_describe_function
from functions.update_conversation import update_conversation_function
from functions.update_thought_bubble import update_thought_bubble_function
from functions.update_emotions import update_emotions_function
from functions.perform_task import perform_task_function
from functions.dream import dream_function
from functions.random_thought import random_thought_function
from functions.mental_simulation import mental_simulation_function
from main import main_function
from dotenv import load_dotenv
import os
import time
import random
import json
import asyncio

# load the environment variables from the .env file
load_dotenv()

# get the value of the STATE_DIR environment variable
STATE_DIR = os.environ.get("STATE_DIR")

app = FastAPI()
security = HTTPBasic()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def task(id):
    while True:
        print("Checking...")
        check, timer, response = perform_task_function(id)
        print(check)
        print(response)
        if check == 'wait':
            print("waiting")
            time.sleep(int(timer/2))
            random_number = random.random()
            if random_number > 0.6:
                print("dreaming")
                response = dream_function()
            elif random_number > 0.2:
                print("random thoughts")
                response = random_thought_function()
            else:
                print("Mental simulation")
                response = mental_simulation_function(id)
            update_conversation_function(response, "assistant", "" , "")
            update_thought_bubble_function()
            update_emotions_function()
            continue
        update_conversation_function("Task Completed: " + response, "assistant", "" , "")
        update_thought_bubble_function()
        update_emotions_function()
        break
    print("Done with " + str(id))

@app.post("/chat")
async def chat(
    background_tasks: BackgroundTasks,
    request: Request,
    credentials: HTTPBasicCredentials = Depends(security),
    file: UploadFile = File(None),
    question: str = Form(...),
):
    if credentials.username != "myusername" or credentials.password != "mypassword":
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    if not question and not file:
        raise HTTPException(status_code=400, detail="Question or file must be provided")

    if question:
        print(question)
    else:
        print("question is null")

    file_contents = await file.read()
    timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    user_response =  question
    file_description = ""
    file_path = ""
    sender = "human"

    if file.filename != "empty-file.txt":
        print(file.filename)
        print(len(file_contents))

        filename, extension = os.path.splitext(file.filename)
        filename = filename.replace(" ", "")
        new_filename = f"{filename}_{timestamp}{extension}"
        file_path = os.path.join("tempfiles", new_filename)

        with open(file_path, "wb") as buffer:
            buffer.write(file_contents)

        file_description = file_describe_function(file_path)

    update_conversation_function(user_response, sender, file_path, file_description)
    action, response = main_function(timestamp)
    update_conversation_function(response, "assistant", "" , "")
    update_thought_bubble_function()
    update_emotions_function()
    print(file_description)
    print(response)

    # Load conversation from JSON file
    with open('state_of_mind/conversation.json', 'r') as f:
        conversation = json.load(f)['conversation']

    # Remove first and last message
    conversation = conversation[1:-1]

    # Check if second last message starts with "Task Completed:"
    if (len(conversation) > 1 ) and conversation[-2]['message'].startswith('Task Completed:'):
        # Swap last two messages
        conversation[-2], conversation[-1] = conversation[-1], conversation[-2]
        
    with open(os.path.join(STATE_DIR, "thought_bubble.txt"), "r") as f:
        thought_bubble = f.read()
    thought_bubble = "Thought bubble: " + thought_bubble
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

    emotion_values_string = "Happiness😊: " + happiness + " Sadness😭: " + sadness + " Creativity🤩: " + creativity + " Curiosity🤔: " + curiosity + " Anger😡: " + anger + " Fear😱: " + fear 

    sense_values_string = "Current Sensory Parameters: " + " Smell👃: " + smell + " Taste👅: " + taste + " Touch✋:" + touch

    result = {"text": response , "emotion_values" : emotion_values_string , "sense_values" : sense_values_string, "thought" : thought_bubble, "conversation": conversation}

    id = timestamp

    if action != 'Talk':
        background_tasks.add_task(task, id)
    return result
    