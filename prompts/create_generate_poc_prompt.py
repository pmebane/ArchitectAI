def create_generate_poc_prompt(summary):
    prompt = f"""Look at the summary of tech vendors and Generate a testing plan to build a  simple, measurable, minimum viable product \
         Make sure to ask questions to clarify what is important to test in order to ensure these are the correct tools for the use case. \
         Tests should be concise to be tested in under a month.
    '''
    {summary}
    '''
    """

    return prompt