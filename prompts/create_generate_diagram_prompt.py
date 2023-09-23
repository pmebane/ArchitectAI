def create_generate_diagram_prompt(summary):
    prompt = f"""Look at the data architecture delimited by triple backticks. Generate the Mermaid code needed to create a diagram for this architecture. \
    Only generate code, do not include anything else in your response. In the code, all lines after the first should be indented. \
    All node labels should be enclosed in square brackets and double quotes. For example, if you wanted node A to display `[Fe(CN)6]4-`, it should be written as `A["[Fe(CN)6]4-"]`
    
    '''
    {summary}
    '''
    """

    return prompt