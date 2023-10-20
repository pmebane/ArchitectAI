# import libraries
import streamlit as st
from prompts.create_generate_poc_goals_prompt import create_generate_poc_goals_prompt
from prompts.create_generate_poc_requirements_prompt import create_generate_poc_requirements_prompt
from prompts.create_generate_poc_eval_prompt import create_generate_poc_eval_prompt
from functions.get_completion_stream import get_completion_stream
from functions.format_stream_response import format_stream_response
from functions.get_s3_conn import upload_to_s3

# title the page
st.title("Testing Plan")

# tell them to finish the summary if it isn't complete
if st.session_state.status != "Summary Complete":
    st.write("This will populate after your summary is generated")

# if the summary is complete, create the poc plan
if st.session_state.status == "Summary Complete":
    # generate the goals of the project
    st.header("Project Goals")
    res_box = st.empty()
    if "project_goals" in st.session_state.keys():
         project_goals = st.session_state.project_goals
         st.write(project_goals)
    else:
        report = []
        # generate the prompt
        prompt = create_generate_poc_goals_prompt(st.session_state.messages[1:])
        # stream the output back and write it
        for event in get_completion_stream(prompt):
            try:
                project_goals = format_stream_response(report,event)
                res_box.markdown(f'*{project_goals}')
            except:
                break
        # save the project goals
        st.session_state.project_goals = project_goals
    # generate the success criteria
    st.header("Project Requirements and Success Criteria")
    res_box = st.empty()
    if "success" in st.session_state.keys():
         success = st.session_state.success
         st.write(success)
    else:
        report = []
        # generate the prompt
        prompt = create_generate_poc_requirements_prompt(st.session_state.messages[1:])
        # stream the output back and write it
        for event in get_completion_stream(prompt):
            try:
                success = format_stream_response(report,event)
                res_box.markdown(f'*{success}')
            except:
                break
        # save the success criteria
        st.session_state.success = success
    # generate the evaluation plan for each technology group
    st.header("Evaluation Plan")
    tools = []
    # create a library where each key is a tool and each value is a list of the vendors
    for index, tool in enumerate(st.session_state.tech_recommendations):
        data = {tool: st.session_state.vendor_recommendations[index]}
        tools.append(data)
    res_box = st.empty()
    if "eval_plan" in st.session_state.keys():
         eval_plan = st.session_state.eval_plan
         st.write(eval_plan)
    else:
        report = []
        # generate the prompt
        prompt = create_generate_poc_eval_prompt(tools, success)
        # stream the output back and write it
        for event in get_completion_stream(prompt):
            try:
                eval_plan = format_stream_response(report,event)
                res_box.markdown(f'*{eval_plan}')
            except:
                break
        # save the success criteria
        st.session_state.eval_plan = eval_plan

# try to upload everything to S3
try:
    upload_to_s3('poc', {k: v for k, v in st.session_state.items()})
except Exception as e:
     pass  






