def create_extract_tech_prompt(chat_history):
    prompt = f"""Look at the chat history delimited by triple backticks. Which technologies were recommended by the assistant and why were they recommended?
    
    '''
    {chat_history}
    '''
    """

    return prompt