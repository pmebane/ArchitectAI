def create_generate_poc_requirements_prompt(messages):
    prompt = f"""Read through the chat history that is delimited by triple backticks.

    Provide a numbered list of the technical requirements outlined by the user.

    '''
    {messages}
    '''
    """

    return prompt