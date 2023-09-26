def create_extract_tech_prompt(chat_history):
    prompt = f"""Look at the chat history delimited by triple backticks. 
    Extract which vendors were recommended by the assistant, and which technologies those vendors are. Also extract why those vendors and those technologies were recommended.
    
    '''
    {chat_history}
    '''
    """

    return prompt