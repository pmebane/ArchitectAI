import streamlit as st
from prompts.create_generate_summary_prompt import create_generate_summary_prompt
from prompts.create_generate_poc_prompt import create_generate_poc_prompt
from functions.get_completion import get_completion
from functions.get_completion_from_message import get_completion_from_messages
from prompts.poc_greeting import greeting
import json

# Conversation complete, now work on the poc plan

st.title("Testing Plan")
# retrieve architecure summary and past chat history
# use it to generate poc
generate_summary_prompt = create_generate_summary_prompt(st.session_state.messages[1:])
summary = get_completion(generate_summary_prompt)
    

# generate poc plan 
generate_poc_summary = create_generate_poc_prompt(summary)
poc = get_completion(create_generate_poc_prompt)

#init poc convo
st.session_state.messages = [{"role": "system", "content": poc}, {"role": "assistant", "content": greeting}]
st.session_state.status = "Conversation in Progress"

with st.chat_message("assistant"):
    with st.spinner("Generating POC Plan"):
        response = get_completion_from_messages(st.session_state.messages) 
        st.write(response) 
message = {"role": "assistant", "content": response}
st.session_state.messages.append(message)



# Display previous chat messages
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Add new user message
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_completion_from_messages(st.session_state.messages) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)

# Determine if conversation is over
is_chat_complete_prompt = create_is_chat_complete_prompt(st.session_state.messages[1:])
is_chat_complete = get_completion(is_chat_complete_prompt)
#st.write("Is Chat Complete? = "+is_chat_complete)
if  is_chat_complete == "Yes":
    st.session_state.status = "Conversation Complete"







