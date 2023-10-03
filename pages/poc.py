import streamlit as st
from prompts.create_generate_poc_plan_prompt import create_generate_poc_plan_prompt
from functions.get_completion import get_completion

# Conversation complete, now work on the poc plan

st.title("Testing Plan")

if st.session_state.status != "Summary Complete":
    st.write("This will populate after your summary is generated")

if st.session_state.status == "Summary Complete":
    st.header("Project Goals")
    with st.spinner("Generating..."):
        prompt = create_generate_poc_goals_prompt(st.session_state.messages[1:]) # create summary of the goals of the project
        project_goals = get_completion(prompt=prompt)
    st.write(project_goals)
    st.header("Project Requirements")
    with st.spinner("Generating..."):
        prompt = create_generate_poc_requirements_prompt(st.session_state.messages[1:]) # create list of the requirements of the project
        project_requirements = get_completion(prompt=prompt)
    st.write(project_requirements)
    st.header("Evaluation Plan")
    i = 0
    for tool in st.session_state.tech_recommendations:
        st.subheader(tool)
        with st.spinner("Generating..."):
            prompt = create_generate_poc_eval_prompt(st.session_state.vendor_recommendations[i], project_requirements) # create evaluation plan for each group of technologies
            evaluation_plan = get_completion(prompt=prompt)
        st.write(evaluation_plan)

    







