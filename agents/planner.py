from utils.llm import call_llm

def generate_plan(topic):
    messages = [
        {"role": "system", "content": "You are a content strategist."},
        {"role": "user", "content": f"Create a structured outline for: {topic}"}
    ]
    return call_llm(messages)
