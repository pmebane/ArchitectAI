import streamlit as st
import openai

def get_completion(prompt, model="gpt-4", temperature=0):
    openai.api_key  = st.secrets["db_username"]
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message["content"]
