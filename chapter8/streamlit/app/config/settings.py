from dotenv import load_dotenv
import os
import streamlit as st


# settings.py
import streamlit as st

def get_secret(secret_name):
    """Safely retrieve a secret from st.secrets or return None if not found."""
    return st.secrets[secret_name] if secret_name in st.secrets else None

# Example usage with environment variables
OPENAI_API_KEY = get_secret("OPENAI_API_KEY")
LANGCHAIN_API_KEY = get_secret("OPENWEATHERMAP_API_KEY")



os.environ['OPENAI_API_KEY'] = "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"
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_ENDPOINT'] = "https://api.smith.langchain.com"
os.environ['LANGCHAIN_API_KEY'] = 'ls__950b2ad6e3e34afea6c9ba3461c5369a'
os.environ['LANGCHAIN_PROJECT'] = "book-chapter-8" 
