import streamlit as st
from prompts.system_message import system_message
from prompts.greeting import greeting
from functions.collect_messages import collect_messages

st.title('Welcome to ArchitectAI')

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "system", "content": system_message}, {"role": "assistant", "content": greeting}]

if st.button("Clear History"):
    st.session_state.messages = [{"role": "system", "content": system_message}, {"role": "assistant", "content": greeting}]

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
            response = collect_messages(st.session_state.messages) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)




