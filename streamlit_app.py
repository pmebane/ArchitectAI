import streamlit as st
from prompts.system_message import system_message
from prompts.greeting import greeting
from prompts.create_is_chat_complete_prompt import create_is_chat_complete_prompt
from prompts.create_is_chat_complete_prompt import create_is_chat_complete_prompt
from functions.collect_messages import collect_messages
from functions.get_completion import get_completion
from st_pages import Page, show_pages

# Specify what pages should be shown in the sidebar, and what their titles should be
show_pages(
    [
        Page("streamlit_app.py", "Chat"),
        Page("pages/summary.py", "Summary"),
    ]
)

# initialize everything
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "system", "content": system_message}, {"role": "assistant", "content": greeting}]
if "status" not in st.session_state.keys():
    st.session_state.status = "Chat"

# Heading
st.title('Welcome to ArchitectAI')

if st.button("Clear History"):
    st.session_state.messages = [{"role": "system", "content": system_message}, {"role": "assistant", "content": greeting}]
    st.session_state.status = "Chat"

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
            response = collect_messages(st.session_state.messages) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)

# Determine if conversation is over
is_chat_complete_prompt = create_is_chat_complete_prompt(st.session_state.messages[1:])
is_chat_complete = get_completion(is_chat_complete_prompt)
#st.write("Is Chat Complete? = "+is_chat_complete)
if  is_chat_complete == "Yes":
    st.session_state.status = "Conversation Complete"







