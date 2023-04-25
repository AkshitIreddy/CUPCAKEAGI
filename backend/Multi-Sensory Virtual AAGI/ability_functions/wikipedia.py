from langchain.utilities import WikipediaAPIWrapper

def wikipedia_function(topic):
    """
    Runs a query on the Wikipedia API.
    Args:
      topic (str): The topic to query.
    Returns:
      dict: The result of the query.
    Examples:
      >>> wikipedia_function('Python')
      {'title': 'Python', 'summary': 'Python is a programming language...'}
    """
    wikipedia = WikipediaAPIWrapper()
    result = wikipedia.run(topic)
    return result