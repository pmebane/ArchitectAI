def create_is_chat_complete_prompt(chat_history):
    prompt = f"""Look at the chat history delimited by triple backticks. Has the assistant recommended specific vendors yet? Response with "Yes" or "No".
    
    '''
    {chat_history}
    '''
    """

    return prompt