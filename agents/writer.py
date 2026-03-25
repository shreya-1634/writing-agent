from utils.llm import call_llm

def write_content(plan):
    messages = [
        {"role": "system", "content": "You are a professional writer."},
        {"role": "user", "content": f"Write a detailed article based on this outline:\n{plan}"}
    ]
    return call_llm(messages)
