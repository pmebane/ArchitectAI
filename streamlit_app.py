import streamlit as st
from prompts.system_message import system_message
from prompts.greeting import greeting
from prompts.create_is_chat_complete_prompt import create_is_chat_complete_prompt
from prompts.create_generate_summary_prompt import create_generate_summary_prompt
from prompts.create_extract_tech_prompt import create_extract_tech_prompt
from prompts.create_extract_vendor_prompt import create_extract_vendor_prompt
from prompts.create_is_chat_complete_prompt import create_is_chat_complete_prompt
from prompts.create_generate_diagram_prompt import create_generate_diagram_prompt
from functions.collect_messages import collect_messages
from functions.get_completion import get_completion

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

if "status" not in st.session_state.keys():
    # Check to see if the conversation is done
    is_chat_complete_prompt = create_is_chat_complete_prompt(st.session_state.messages[1:])
    is_chat_complete = get_completion(is_chat_complete_prompt)
    st.write("Is Chat Complete? = "+is_chat_complete)
    if  is_chat_complete == "Yes":
        st.session_state.status = "Conversation Complete"

if "status" in st.session_state.keys():
    # generate written description of architecture
    generate_summary_prompt = create_generate_summary_prompt(st.session_state.messages[1:])
    summary = get_completion(generate_summary_prompt)
    st.write("Summary = "+summary)
    # extract technologies and reasonings
    extract_tech_prompt = create_extract_tech_prompt(st.session_state.messages[1:])
    tech = get_completion(extract_tech_prompt)
    st.write("Tech = "+tech)
    # extract vendors and reasonings
    extract_vendor_prompt = create_extract_vendor_prompt(st.session_state.messages[1:])
    vendors = get_completion(extract_vendor_prompt)
    st.write("Vendors = "+vendors)
    # generate architecture diagram
    generate_diagram_prompt = create_generate_diagram_prompt(summary)
    mermaid_code = get_completion(generate_diagram_prompt)
    st.write("Code = "+mermaid_code)
        # call Lucidchart API
    st.session_state.status = "Summary Complete"





