def create_generate_diagram_prompt(summary):
    prompt = f"""You are an expert in Mermaid code.
    You have been given a summary of a data architecture. The summary is delimited by triple backticks.

    Generate the mermaid code that would display a diagram for this archicture. The mermaid code should depict how the tools interact with one another. It should not include the names of languages or cloud platforms.
    
    Only generate code, do not include anything else in your response. In the code, all lines after the first should be indented. 
    All node labels should be enclosed in square brackets and double quotes. For example, if you wanted node A to display `[Fe(CN)6]4-`, it should be written as `A["[Fe(CN)6]4-"]`
    
    '''
    {summary}
    '''
    """

    return prompt