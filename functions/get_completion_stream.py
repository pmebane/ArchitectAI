import streamlit as st
import openai

def get_completion_stream(prompt, model="gpt-4", temperature=0):
    openai.api_key  = st.secrets["api_key"]
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        stream=True
    )
    return response
