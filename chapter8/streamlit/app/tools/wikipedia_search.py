from langchain.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
# Create the Wikipedia API wrapper
api_wrapper = WikipediaAPIWrapper(top_k_results=5, doc_content_chars_max=500)

# Create the WikipediaQueryRun tool
wikipedia = WikipediaQueryRun(api_wrapper=api_wrapper,description="look up tourist information for locations") 
