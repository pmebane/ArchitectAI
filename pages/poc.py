import streamlit as st
from prompts.create_generate_poc_plan_prompt import create_generate_poc_plan_prompt
from functions.get_completion import get_completion

# Conversation complete, now work on the poc plan

st.title("Testing Plan")

if st.session_state.status != "Summary Complete":
    st.write("This will populate after your summary is generated")

if st.session_state.status == "Summary Complete":
    prompt = create_generate_poc_plan_prompt(st.session_state.messages[1:])
    result = get_completion(prompt=prompt)
    st.write(result)
    #st.header("Project Goals")
    #create summary of the goals of the project
    #st.header("Project Requirements")
    # create list of the requirements of the project
    #st.header("Evaluation Plan")
    #for tool in tool_list:
        #   st.subheader(tool)
        #create matrix of tools and requirements
        #create plan for testing 

    







