def create_generate_summary_prompt(chat_history):
    prompt = f"""Look at the chat history delimited by triple backticks. Generate a description of how the vendors that were recommended would integrate in a data architecture.
    
    '''
    {chat_history}
    '''
    """

    return prompt