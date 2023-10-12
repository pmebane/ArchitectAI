import streamlit as st
from prompts.create_generate_summary_prompt import create_generate_summary_prompt
from prompts.create_extract_tech_prompt import create_extract_tech_prompt
from prompts.create_generate_diagram_prompt import create_generate_diagram_prompt
from prompts.create_vendor_comparison_prompt import create_vendor_comparison_prompt
from functions.get_completion import get_completion
from functions.get_completion_with_function import get_completion_with_function
from functions.get_arch_diagram import get_arch_diagram
import json
from functions.get_s3_conn import upload_to_s3

st.title("Solution Overview")

if st.session_state.status == "Conversation in Progress":
    st.write("This will populate after you complete your conversation with Archie on the Chat page")

# Conversation complete, now generate assets
if st.session_state.status != "Conversation in Progress":
    st.subheader("Architecture Overview")
    with st.spinner("Generating..."):
        generate_summary_prompt = create_generate_summary_prompt(st.session_state.messages[1:]) # generate written description of architecture
        summary = get_completion(generate_summary_prompt)
    st.write(summary)

    st.subheader("Architecture diagram")
    with st.spinner("Generating..."):
        generate_diagram_prompt = create_generate_diagram_prompt(summary) # generate architecture diagram
        mermaid_code = get_completion(generate_diagram_prompt)
        mermaid_code = mermaid_code.replace("`","").replace("mermaid","")
        url = get_arch_diagram(mermaid_code)
    st.image(image=url)

    # extract recommendations
    # define how we want the output to look
    function_schema = {
    "type": "object",
    "properties": {
        "recommendations": {
        "type": "array",
        "items": 
            {
            "type": "object",
            "properties": {
                "tech": {"type": "string", "description": "the technology that was recommended by the assistant, e.g. Data Warehouse"},
                "reasoning": {"type": "string", "description": "why the technology was recommended"},
                "vendors": {
                "type": "array",
                "items": 
                    {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "name of the vendor that was recommended"},
                        "reasoning": {"type": "string", "description": "why the vendor was recommended"}
                    },
                    "required": ["name","reasoning"]
                    }
                
                }
            },
            "required": ["tech","reasoning","vendors"]
            }
        
        }
    },
    "required": ["recommendations"]
    }

    # create section with information for each tool that was recommended
    st.subheader("Recommended Tools")
    with st.spinner("Generating..."):
        prompt = create_extract_tech_prompt(st.session_state.messages[1:])
        recommendations = get_completion_with_function(prompt=prompt,function_schema=function_schema)
        cleaned_recommendations = json.loads(recommendations["choices"][0]["message"]["function_call"]["arguments"].replace("\n", ""))["recommendations"]
    tech_list = [] # create list of the different technologies that were recommended
    vendor_list = [] # create list of the different vendors that were recommended   
    for tech in cleaned_recommendations:
        tech_name = tech["tech"]
        tech_list.append(tech_name) # add technology to the list
        with st.expander(tech_name):
            tech_reasoning = tech["reasoning"]
            st.write(tech_reasoning) 
            vendor_list_2 = [] # create a list of vendors for each technology
            for vendors in tech["vendors"]:
                vendor = vendors["name"]
                vendor_list_2.append(vendor) # add individual vendor to the vendor list
                vendor_reasoning = vendors["reasoning"]
                st.write(f"**{vendor}:** {vendor_reasoning}")
            vendor_list.append(vendor_list_2) # create list of vendor lists
            st.subheader("How You Choose")
            with st.spinner("Generating..."):
                prompt = create_vendor_comparison_prompt(vendor_list_2)
                comparison = get_completion(prompt=prompt)
            st.write(comparison) 

    st.session_state.summary = summary
    st.session_state.arch_url = url
    st.session_state.recommendations = cleaned_recommendations
    st.session_state.tech_recommendations = tech_list
    st.session_state.vendor_recommendations = vendor_list
    if st.session_state.status == "Conversation Complete":
        st.session_state.status = "Summary Complete"
    try:
        upload_to_s3('summary', {k: v for k, v in st.session_state.items()})
    except Exception as e:
        pass