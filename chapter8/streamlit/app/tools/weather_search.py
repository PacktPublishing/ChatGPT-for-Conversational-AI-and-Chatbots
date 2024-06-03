from langchain.tools import BaseTool, StructuredTool, tool
from langchain_community.utilities import OpenWeatherMapAPIWrapper


@tool
def weather_search(query: str) -> str:
    """A weather tool optimized for comprehensive up to date weather information. 
    Useful for when you need to answer questions about the weather, use this tool to answer questions about the weather for a specific location. 
    Look in context for the location to provide weather for"""
    weather = OpenWeatherMapAPIWrapper()
    weather_data = weather.run(query)
    return weather_data