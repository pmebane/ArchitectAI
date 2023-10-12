def create_generate_summary_prompt(chat_history):
    prompt = f"""You are an expert in data architecture.
    
    You have been given a conversation between a user and an assistant. The conversation is delimited by triple backticks.
    
    The assistant recommended tools to the user that they should use in their data architecture. You should generate a description of how the tools that were recommended would integrate in a data architecture.
    
    Do not include the names of individual vendors in your response or discuss the requirements of the tools. 
    
    You should only include names of technology groups like Data Warehouse, Streaming Ingestion, or Visualization.
    
    '''
    {chat_history}
    '''
    """

    return prompt