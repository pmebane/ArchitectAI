from config import OPENAI_API_KEY
import openai

def get_completion_with_function(prompt, function_schema, model="gpt-4", temperature=0):
    openai.api_key  = OPENAI_API_KEY
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        functions=[{"name": "function_name", "parameters": function_schema}],
        function_call={"name": "function_name"}
    )
    return response