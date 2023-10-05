def create_generate_poc_eval_prompt(tools, success_criteria):
    prompt = f"""YYou are a data architecture consultant who is an expert at helping companies evaluate software.

    Your customer is evaluating the tools delimited by triple backticks. They need you to explain how they can verify that the tools can satisfy the success criteria delimited by %%%.
    
    They have already identified their key requirements and researched the tools. Start by telling them how they can start using the tools.
    
    Your output should be a numbered list of the steps that the customer should take to evaluate the tools. They should be specific and detailed.
    '''
    {tools}
    '''
    %%%
    {success_criteria}
    %%%
    """

    return prompt