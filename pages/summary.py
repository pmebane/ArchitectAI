import streamlit as st
from prompts.create_generate_summary_prompt import create_generate_summary_prompt
from prompts.create_extract_tech_prompt import create_extract_tech_prompt
from prompts.create_generate_diagram_prompt import create_generate_diagram_prompt
from functions.get_completion import get_completion
from functions.get_completion_with_function import get_completion_with_function
from functions.get_arch_diagram import get_arch_diagram
import json

if st.session_state.status == "Conversation in Progress":
    st.write("Please complete the conversation on the Chat page")

# Conversation complete, now generate assets
if st.session_state.status == "Conversation Complete":
    st.title("Solution Overview")
    # generate written description of architecture
    generate_summary_prompt = create_generate_summary_prompt(st.session_state.messages[1:])
    summary = get_completion(generate_summary_prompt)
    st.subheader("Architecture Overview")
    st.write(summary)
    # generate architecture diagram
    generate_diagram_prompt = create_generate_diagram_prompt(summary)
    mermaid_code = get_completion(generate_diagram_prompt)
    st.subheader("Architecture diagram")
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

    # call API and extract recommendations
    st.subheader("Recommended Tools")
    prompt = create_extract_tech_prompt(st.session_state.messages[1:])
    result = get_completion_with_function(prompt=prompt,function_schema=function_schema)
    res = json.loads(result["choices"][0]["message"]["function_call"]["arguments"].replace("\n", ""))["recommendations"]
    for tech in res:
        with st.expander(tech["tech"]):
            tech_reasoning = tech["reasoning"]
            st.write(tech_reasoning)
            vendor = tech["vendors"][0]["name"]
            vendor_reasoning = tech["vendors"][0]["reasoning"]
            st.write(f"**{vendor}:** {vendor_reasoning}")

    # Change status
    st.session_state.status = "Summary Complete"