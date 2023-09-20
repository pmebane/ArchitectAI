def create_generate_diagram_prompt(summary):
    prompt = f"""Look at the data architecture delimited by triple backticks. Generate the Mermaid code needed to create a diagram for this architecture.
    
    '''
    {summary}
    '''
    """

    return prompt