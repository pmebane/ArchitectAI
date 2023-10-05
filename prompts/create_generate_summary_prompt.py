def create_generate_summary_prompt(chat_history):
    prompt = f"""Look at the chat history delimited by triple backticks. Generate a description of how the tools that were recommended would integrate in a data architecture.
    Do not include the names of individual vendors in your response. You should only include names of technology groups like Data Warehouse, Streaming Ingestion, or Visualization.
    
    '''
    {chat_history}
    '''
    """

    return prompt