from config import OPENAI_API_KEY
import openai

def get_completion(prompt, model="gpt-4"):
    openai.api_key  = OPENAI_API_KEY
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]