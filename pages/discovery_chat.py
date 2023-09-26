from prompts.system_message import system_message
from prompts.greeting import greeting
from prompts.create_is_chat_complete_prompt import create_is_chat_complete_prompt
from functions.get_completion import get_completion
from functions.get_completion_from_message import get_completion_from_messages
import streamlit as st

st.title("Chat")
# initialize everything
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "system", "content": system_message}, {"role": "assistant", "content": greeting}]
if "status" not in st.session_state.keys():
    st.session_state.status = "Conversation in Progress"

if st.button("Clear History"):
    st.session_state.messages = [{"role": "system", "content": system_message}, {"role": "assistant", "content": greeting}]
    st.session_state.status = "Conversation in Progress"

# Display previous chat messages
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Add new  suser message
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