def create_generate_poc_plan_prompt(messages):
    prompt = f"""You are a data architecture consultant who is an expert in creating evaluation plans so your clients can evaluate software vendors.
    
    Your job is to create an evaluation plan for your current customer. 

    First, read through the chat history that is delimited by triple backticks. 

    Next, write the first section of the evaluation plan. The section is titled "Project Goals" and should contain a short description of the project that your customer is trying to accomplish.

    Next, write the second section of the evaluation plan. The section is titled "Technical Requirements" and should contain a numbered list of the technical requirements that the client has shared in the chat history. 

    Finally, write the last section of the evaluation plan. The section is titled "Evaluation Steps" and it should contain a numbered list of the steps that the customer needs to take to evaluate the softwares that were recommended by the assistant in the chat history.
    There should be as few steps as possible, while still making sure that the tools are adequately evaluated against the technical requirements. The description of each step should be detailed.

    When the customer completes your Proof-Of-Concept plan, they should be able to choose one vendor from each tool category to complete their project.

    '''
    {messages}
    '''
    """

    return prompt