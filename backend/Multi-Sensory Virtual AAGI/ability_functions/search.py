from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv
from io import StringIO
import sys

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

SERPER_API_KEY = os.environ.get("SERPER_API_KEY")
os.environ["SERPER_API_KEY"] = SERPER_API_KEY
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

def search_function(question):
    """
    Searches for information on a given question.
    Args:
      question (str): The question to search for.
    Returns:
      str: Output of the search.
    Examples:
      >>> search_function("What is the capital of France?")
      "Searching for information on this What is the capital of France?\nParis"
    """
    # Redirecting stdout to StringIO object
    old_stdout = sys.stdout
    sys.stdout = result = StringIO()
    try:
        chat = ChatOpenAI(temperature  = 0, model= 'gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY)
        tools = load_tools(["google-serper"], llm=chat)
        agent = initialize_agent(tools, chat, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
        response = agent.run("Search and gather information on this " + question)
        output = result.getvalue()
        sys.stdout = old_stdout
        return  str(output) + response 
    except Exception as e:
        output = result.getvalue()
        sys.stdout = old_stdout
        return str(output)
    