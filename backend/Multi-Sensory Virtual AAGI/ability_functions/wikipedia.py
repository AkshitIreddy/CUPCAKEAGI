from langchain.utilities import WikipediaAPIWrapper

def wikipedia_function(topic):
    wikipedia = WikipediaAPIWrapper()
    result = wikipedia.run(topic)
    return result