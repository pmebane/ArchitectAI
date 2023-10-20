# import libraries
import streamlit as st
from prompts.create_generate_summary_prompt import create_generate_summary_prompt
from prompts.create_extract_tech_prompt import create_extract_tech_prompt
from prompts.create_generate_diagram_prompt import create_generate_diagram_prompt
from prompts.create_vendor_comparison_prompt import create_vendor_comparison_prompt
from functions.get_completion import get_completion
from functions.get_completion_with_function import get_completion_with_function
from functions.get_arch_diagram import get_arch_diagram
from functions.get_completion_stream import get_completion_stream
from functions.format_stream_response import format_stream_response
from functions.recommendation_function_schema import function_schema
import json
from functions.get_s3_conn import upload_to_s3

# title the page
st.title("Solution Overview")

# if conversation is not complete, tell them to finish
if st.session_state.status == "Conversation in Progress":
    st.write("This will populate after you complete your conversation with Archie on the Chat page")

# Conversation complete, now generate assets
if st.session_state.status != "Conversation in Progress":
    st.subheader("Architecture Overview")
    res_box = st.empty()
    # if the summary already exists, display it
    if "summary" in st.session_state.keys():
        summary = st.session_state.summary
        res_box.markdown(f'*{summary}')
    # if the summary doesn't exist, generate a new one
    else:
        report = []
        # generate the prompt
        generate_summary_prompt = create_generate_summary_prompt(st.session_state.messages[1:])
        # stream the output back and write it
        for event in get_completion_stream(generate_summary_prompt):
            try:
                summary = format_stream_response(report,event)
                res_box.markdown(f'*{summary}')
            except:
                break
        # save the summary
        st.session_state.summary = summary

    st.subheader("Architecture diagram")
    # generate the url for the diagram
    with st.spinner("Generating..."):
        generate_diagram_prompt = create_generate_diagram_prompt(summary)
        mermaid_code = get_completion(generate_diagram_prompt)
        mermaid_code = mermaid_code.replace("`","").replace("mermaid","")
        url = get_arch_diagram(mermaid_code)
    # display the diagram
    st.image(image=url)
    #save the diagram
    st.session_state.arch_url = url

    st.subheader("Recommended Tools")
    # extract the recommendations that were given
    with st.spinner("Generating..."):
        # create the prompt
        prompt = create_extract_tech_prompt(st.session_state.messages[1:])
        # define how we want the output to look
        schema = function_schema()
        # extract the recommendations
        recommendations = get_completion_with_function(prompt=prompt,function_schema=schema)
        # clean them up
        cleaned_recommendations = json.loads(recommendations["choices"][0]["message"]["function_call"]["arguments"].replace("\n", ""))["recommendations"]
        # save the recommendations
        st.session_state.recommendations = cleaned_recommendations
    # create list of the different technologies that were recommended
    tech_list = [] 
    # create list of the different vendors that were recommended  
    vendor_list = [] 
    # if the comparison has not been made, instantiate a new one
    if "comparison" not in st.session_state.keys():
        st.session_state_comparison = {}
    else:
        pass
    # loop through the list of recommendations
    for tech in cleaned_recommendations:
        # take the name of the technology and append it to the technology list
        tech_name = tech["tech"]
        tech_list.append(tech_name)
        # create an expander for that technology
        with st.expander(tech_name):
            # write why that technology was chosen
            tech_reasoning = tech["reasoning"]
            st.write(tech_reasoning) 
            # create a list of the vendors for that technology
            vendor_list_2 = []
            # loop through the list of vendors for that technology
            for vendors in tech["vendors"]:
                # take the name of the vendor and add it to the list
                vendor = vendors["name"]
                vendor_list_2.append(vendor)
                # extract why that vendor was chosen
                vendor_reasoning = vendors["reasoning"]
                # write the vendor name and why it was chosen
                st.write(f"**{vendor}:** {vendor_reasoning}")
            # create a list of all of the lists of vendors
            vendor_list.append(vendor_list_2)
            # create the section where the vendors will be compared
            st.subheader("How You Choose")
            res_box = st.empty()
            # if comparison is not in session state, initialize it and generate response
            if "comparison" not in st.session_state.keys():
                st.session_state.comparison = {}
                report = []
                prompt = create_vendor_comparison_prompt(vendor_list_2)
                for event in get_completion_stream(prompt):
                    try:
                        comparison = format_stream_response(report,event)
                        res_box.markdown(f'*{comparison}')
                    except:
                        break
                # save the comparison
                st.session_state.comparison[tech_name] = comparison
            else:
                pass
            # if comparison is in session state
            if "comparison" in st.session_state.keys():
                # if the comparison for this tech is in session state, use it
                if f"{tech_name}" in st.session_state.comparison:
                    comparison = st.session_state.comparison[tech_name]
                    res_box.markdown(f'*{comparison}')
                # if not, generate it
                else:
                    report = []
                    prompt = create_vendor_comparison_prompt(vendor_list_2)
                    for event in get_completion_stream(prompt):
                        try:
                            comparison = format_stream_response(report,event)
                            res_box.markdown(f'*{comparison}')
                        except:
                            break
                    # save the comparison
                    st.session_state.comparison[tech_name] = comparison
            else:
                pass
    # save the list of recommended technologies
    st.session_state.tech_recommendations = tech_list
    # save the list of recommended vendors
    st.session_state.vendor_recommendations = vendor_list

    # change the status to "Summary Complete"
    if st.session_state.status == "Conversation Complete":
        st.session_state.status = "Summary Complete"

    # try to save all of the information to S3
    try:
        upload_to_s3('summary', {k: v for k, v in st.session_state.items()})
    except Exception as e:
        pass