import os
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.memory import ConversationBufferWindowMemory
from tools.weather_search import weather_search
from tools.wikipedia_search import wikipedia
from tools.hotel_search import hotel_search

def setup_agent(msgs: list ,openai_api_key: str, langchain_api_key: str, openweathermap_api_key: str) -> AgentExecutor:
    """
    Sets up the tools for our chain.
    We have here the following tools:
    - wikipedia
    - weather_search
    - hotel_search

    Args:
        msgs (lst): List of messages
        openai_api_key (str): The API key for OpenAI.
        langchain_api_key (str): The API key for LangChain.
        openweathermap_api_key (str): The API key for OpenWeatherMap.
    Returns:
        AgentExecutor: The configured agent executor.

    """

    os.environ["OPENAI_API_KEY"] = openai_api_key
    os.environ["OPENWEATHERMAP_API_KEY"] = openweathermap_api_key 
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
    os.environ['LANGCHAIN_TRACING_V2'] = "true"
    os.environ['LANGCHAIN_ENDPOINT'] = "https://api.smith.langchain.com"
    os.environ['LANGCHAIN_PROJECT'] = "ellie_chatbot" 
    
    llm = ChatOpenAI(temperature=0.0, model='gpt-4-1106-preview',verbose=True)

    tools = [hotel_search,weather_search,wikipedia]

    hub_prompt = hub.pull("hwchase17/openai-tools-agent")

    memory = ConversationBufferWindowMemory(k=20, memory_key="chat_history", chat_memory=msgs, return_messages=True)

    agent = create_openai_tools_agent(llm, tools, hub_prompt)

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        return_intermediate_steps=False,
    )

    return agent_executor