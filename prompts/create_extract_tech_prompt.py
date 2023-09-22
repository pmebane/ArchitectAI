def create_extract_tech_prompt(chat_history):
    prompt = f"""Look at the chat history delimited by triple backticks. 
    Extract which technologies and vendors were recommended by the assistant. Also extract why each technology and vendor was recommended.
    
    '''
    {chat_history}
    '''
    """

    return prompt