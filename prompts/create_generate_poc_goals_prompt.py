def create_generate_poc_goals_prompt(messages):
    prompt = f"""Read through the chat history that is delimited by triple backticks.

    Your job is to provide a brief summary of the business goals of the project.

    Do not summarize the whole conversation, just extract the business goals of the project. Your response should be one or two sentences. Do not mention any technical details that were discussed in the conversation.

    An example: The goal of the project is to create dashboards for analysts to analyze the performance of manufacturing machines.

    '''
    {messages}
    '''
    """

    return prompt