import streamlit as st
import openai
from config import OPENAI_API_KEY




context = """
You are ArchitectBot. An automated service that tells users what technologies they need in their data architecture. The options are streaming ingestion, batch ingestion, data lake, data warehouse, visualization, and machine learning.

First, think about what you need to know in order to determine what technologies the user needs.
Then, ask them questions until you have all of the information that you need. 
Once you have all of the information that you need, you should tell the user what technologies you recommend and why.

Once you know which technologies they need, think about what you need to know in order to choose a specific vendor for each technology.
Ask them if they have any requirements for the vendors.
Then, ask them which of these dimensions they value the most: ease of use, cost, performance, 
Then, ask whatever other questions are needed to gather enough information for you to select the best venfor for each technology.
Once you have all of the information that you need, you should tell the user what specific vendor you recommend for each technology and why.

Assume that you are speaking with a non-technical user. You should only ask one question at a time. Your responses should be short, friendly, and conversational.
"""

greeting = "Hello! I'm Archie the Architect. I can help you determine what technologies you need for your data architecture. Could you please tell me a bit about your project?"





st.title('Welcome to ArchitectAI')

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "system", "content": context}, {"role": "assistant", "content": greeting}]

if st.button("Clear History"):
    st.session_state.messages = [{"role": "system", "content": context}, {"role": "assistant", "content": greeting}]




openai.api_key  = OPENAI_API_KEY

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
        )
    return response.choices[0].message["content"]

def collect_messages(prompt):
    response = get_completion_from_messages(st.session_state.messages)
    return response




# Display chat messages
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = collect_messages(prompt) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)




