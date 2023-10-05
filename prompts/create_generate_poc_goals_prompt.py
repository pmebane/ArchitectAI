def create_generate_poc_goals_prompt(messages):
    prompt = f"""You are a data architecture consultant who is an expert at helping companies evaluate software.
    
    Describe what success looks like in the project that is described in the chat history delimited by triple backticks.  

    Your output should be a short paragraph.

    '''
    {messages}
    '''
    """

    return prompt