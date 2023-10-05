from prompts.system_message import system_message
from prompts.greeting import greeting
from prompts.create_is_chat_complete_prompt import create_is_chat_complete_prompt
from functions.get_completion import get_completion
from functions.get_completion_from_message import get_completion_from_messages
import streamlit as st

st.title("Chat")

if st.button("Clear History"):
    st.session_state.messages = [{"role": "system", "content": system_message}, {"role": "assistant", "content": greeting}]
    st.session_state.status = "Conversation in Progress"
    if "summary" in st.session_state.keys():
        del st.session_state["summary"]
    if "arch_url" in st.session_state.keys():
        del st.session_state["arch_url"]
    if "recommendations" in st.session_state.keys():
        del st.session_state["recommendations"]
    if "comparison" in st.session_state.keys():
        del st.session_state["comparison"]

if st.button("Testing Mode"):
    st.session_state.messages = [{'role': 'system','content': f'{system_message}'}, {'role': 'assistant', 'content': "Hello! I'm Archie the Architect. I can help you determine what technologies you need for your data architecture. Could you please tell me a bit about your project?"}, {'role': 'user', 'content': 'i want to visualize my marketing data'}, {'role': 'assistant', 'content': "Great! To help you better, I need to understand a few things about your data and requirements. Let's start with the type of data you're working with. Is it structured (like CSVs), semi-structured (like JSON or XML), or unstructured (like PDFs or MP4s)?"}, {'role': 'user', 'content': 'it is structured'}, {'role': 'assistant', 'content': 'Excellent! Structured data is easier to work with. Now, could you please tell me about your latency requirements? In other words, how quickly do you need to access your data?'}, {'role': 'user', 'content': 'it needs to be updated daily'}, {'role': 'assistant', 'content': 'Understood, daily updates it is. Now, are you planning on doing any predictive analytics or machine learning with your data?'}, {'role': 'user', 'content': 'no'}, {'role': 'assistant', 'content': "Alright, no predictive analytics. Could you please tell me how much data you're working with?"}, {'role': 'user', 'content': '100GB'}, {'role': 'assistant', 'content': 'Thanks for the information. Lastly, does your data need to be manipulated in any way, such as deduplication, transformation, etc?'}, {'role': 'user', 'content': 'no '}, {'role': 'assistant', 'content': "Great! Based on the information you've provided, here are my technology recommendations:\n\n1. **Batch Ingestion**: Since your data is updated daily and not in real-time, batch ingestion would be a suitable method to bring your data into the system.\n\n2. **Data Warehouse**: Given that you're working with structured data and you don't need to perform any transformations, a data warehouse would be a good fit. It will allow you to store your data in a structured format and perform efficient queries.\n\n3. **Visualization Tool**: Since you mentioned you want to visualize your marketing data, a visualization tool would be necessary. This will allow you to create charts, graphs, and other visual representations of your data.\n\nWould you like me to generate vendor recommendations for all of these technologies, or just a few of them? If it's just a few, please specify which ones."}, {'role': 'user', 'content': 'all of them'}, {'role': 'assistant', 'content': "Great! To provide the best vendor recommendations, I need to understand a bit more about your preferences and requirements. \n\nLet's start with this: Which two of these do you value the most: ease of use, cost, or scalability/performance?"}, {'role': 'user', 'content': 'ease of use and cost'}, {'role': 'assistant', 'content': 'Understood, you value ease of use and cost. Now, could you please tell me what other tools your vendor recommendations will have to integrate with? Examples include data sources, cloud vendors, etc.'}, {'role': 'user', 'content': 'The data will have to be extracted from Facebook Ads and Google Ads. We have other services on AWS'}, {'role': 'assistant', 'content': "Thanks for sharing that. It's important to ensure that the tools we choose can integrate well with Facebook Ads, Google Ads, and AWS. \n\nNext, do you prefer if the tools are cloud-native? If yes, is it important to have a tool that can support multi-cloud deployments?"}, {'role': 'user', 'content': 'Yes we prefer if they are cloud-native but it is not important that they support multi-cloud deployments'}, {'role': 'assistant', 'content': 'Got it, cloud-native but no need for multi-cloud support. Lastly, could you please tell me about the technical skills your team has? For example, any cloud vendors that they have expertise in, languages they know, etc.'}, {'role': 'user', 'content': 'They have knowledge of AWS. From a languages standpoint, they know SQL and python'}, {'role': 'assistant', 'content': "Thanks for providing all the necessary details. Based on your requirements, here are my vendor recommendations:\n\n**Batch Ingestion:**\n1. **AWS Glue**: It's a fully managed extract, transform, and load (ETL) service that makes it easy to prepare and load your data for analytics. It's cloud-native and integrates well with other AWS services.\n2. **Stitch**: It's a simple, powerful ETL service built for developers. Stitch connects to your first-party data sources – from databases like MongoDB and MySQL, to SaaS tools like Salesforce and Zendesk – and replicates that data to your warehouse.\n3. **Talend**: It's a robust data integration tool that offers a free version and is known for its ease of use.\n\n**Data Warehouse:**\n1. **Amazon Redshift**: It's a fast, scalable data warehouse that makes it simple and cost-effective to analyze all your data using standard SQL. Your team's knowledge of AWS and SQL will be beneficial here.\n2. **Google BigQuery**: It's a web service from Google that is used for handling and analyzing big data. It's easy to use and offers a generous free tier.\n3. **Snowflake**: It's a cloud-based data warehousing platform that is extremely scalable and easy to use.\n\n**Visualization Tool:**\n1. **Tableau**: It's a powerful data visualization tool that is widely used in the industry. It's easy to use and can connect to a wide variety of data sources.\n2. **PowerBI**: It's a business analytics tool by Microsoft. It provides interactive visualizations with self-service business intelligence capabilities.\n3. **Looker**: It's a modern platform for data that offers powerful visualization capabilities. It's easy to use and offers a wide range of integrations.\n\nPlease review these options and let me know if you have any questions or need further assistance!"}]

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
            response = get_completion_from_messages(st.session_state.messages) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)

if st.session_state.status == "Conversation in Progress":
    # Determine if conversation is over
    is_chat_complete_prompt = create_is_chat_complete_prompt(st.session_state.messages[1:])
    is_chat_complete = get_completion(is_chat_complete_prompt)
    if  is_chat_complete == "Yes":
        st.session_state.status = "Conversation Complete"