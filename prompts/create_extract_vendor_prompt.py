def create_extract_vendor_prompt(chat_history):
    prompt = f"""Look at the chat history delimited by triple backticks. Which vendors were recommended by the assistant and why were they recommended?
    
    '''
    {chat_history}
    '''
    """

    return prompt