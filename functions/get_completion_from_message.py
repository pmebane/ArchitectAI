from config import OPENAI_API_KEY
import openai

def get_completion_from_messages(messages, model="gpt-4", temperature=0):
    openai.api_key  = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
        )
    return response.choices[0].message["content"]