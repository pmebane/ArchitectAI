def create_generate_poc_eval_prompt(tools, requirements):
    prompt = f"""You are a data consultant who is an expert in evaluating data tools.

    Create an evaluation plan for the tools delimited by triple backticks. The plan should test each tool against the technical requirements delimited by %%%.

    '''
    {tools}
    '''
    %%%
    {requirements}
    %%%
    """

    return prompt