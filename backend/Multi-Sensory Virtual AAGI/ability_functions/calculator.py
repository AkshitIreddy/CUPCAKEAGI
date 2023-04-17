from langchain import LLMMathChain
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
import re
load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def calculator_function(question):
    chat = ChatOpenAI(temperature  = 0, model= 'gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY)
    llm_math = LLMMathChain(llm=chat, verbose=True)
    response = llm_math.run(question)
    return response