from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain.agents import AgentExecutor
import streamlit as st
from langchain_service import setup_agent

def prepare_agent(msgs) -> AgentExecutor:
    return setup_agent(msgs,st.secrets.OPENAI_API_KEY,st.secrets.LANGCHAIN_API_KEY,st.secrets.OPENWEATHERMAP_API_KEY)


def init_streamlit():
    
    
    st.set_page_config(page_title="Ellie Explorer", page_icon="📖")
    st.title(" ✈️ Ellie Explorer ")

    """
    Ellie Explorer holiday assistant View
    """

    # Set up memory
    msgs = StreamlitChatMessageHistory()
    # Create our agent
    agent_executor: AgentExecutor = prepare_agent(msgs)

    welcome = """
    Hello! Ready to find your ideal hotel? I can help you search based on your unique preferences, whether you're seeking accommodations close to running trails, known for excellent service, or anything else that's important to you. 
    Just let me know what you're looking for, and I'll take care of the rest. How can I assist you today?
    """

    if len(msgs.messages) == 0:
        msgs.add_ai_message(welcome)

    view_messages = st.expander("View the message contents in session state")

    # Render current messages from StreamlitChatMessageHistory
    for msg in msgs.messages:
        st.chat_message(msg.type).write(msg.content) 

    # If user inputs a new prompt, generate and draw a new response
    if prompt := st.chat_input():
        st.chat_message("human").write(prompt)
        try:
            response = agent_executor.invoke({"input": prompt})
            if 'output' in response:
                st.chat_message("ai").write(response['output'])
            else:
                st.error("Received an unexpected response format from the agent.")
        except Exception as e:
            # Log the exception here if logging is set up
            st.error(f"An error occurred: {str(e)}. Please try again later.")


    # Draw the messages at the end, so newly generated ones show up immediately
    with view_messages:
        """
        Message History initialized with:
        ```python
        msgs = StreamlitChatMessageHistory(key="langchain_messages")
        ```

        Contents of `st.session_state.langchain_messages`:
        """
        view_messages.json(st.session_state.langchain_messages)

def prepare_agent(msgs) -> AgentExecutor:
    return setup_agent(msgs,st.secrets.OPENAI_API_KEY,st.secrets.LANGCHAIN_API_KEY,st.secrets.OPENWEATHERMAP_API_KEY)

if __name__ == "__main__":
    init_streamlit()


