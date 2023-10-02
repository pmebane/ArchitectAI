import streamlit as st
import openai

@st.cache_data(show_spinner = False)
def get_completion_with_function(prompt, function_schema, model="gpt-4", temperature=0):
    openai.api_key  = st.secrets["api_key"]
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        functions=[{"name": "function_name", "parameters": function_schema}],
        function_call={"name": "function_name"}
    )
    return response
