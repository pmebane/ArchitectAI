import streamlit as st
from prompts.create_generate_summary_prompt import create_generate_summary_prompt
from prompts.create_extract_tech_prompt import create_extract_tech_prompt
from prompts.create_extract_vendor_prompt import create_extract_vendor_prompt
from prompts.create_generate_diagram_prompt import create_generate_diagram_prompt
from functions.get_completion import get_completion

if st.session_state.status == "Chat":
    st.write("Please complete the conversation on the Chat page")

# Conversation complete, now generate assets
if st.session_state.status == "Conversation Complete":
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