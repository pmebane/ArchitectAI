import streamlit as st
import openai

@st.cache_data(show_spinner = False)
def get_completion_from_messages(messages, model="gpt-4", temperature=0):
    openai.api_key  = st.secrets["api_key"]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
        )
    return response.choices[0].message["content"]
