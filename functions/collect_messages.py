from get_completion_from_message import get_completion_from_messages

def collect_messages(messages):
    response = get_completion_from_messages(messages)
    return response