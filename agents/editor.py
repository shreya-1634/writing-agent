from utils.llm import call_llm

def refine_content(content):
    messages = [
        {"role": "system", "content": "You are an expert editor."},
        {"role": "user", "content": f"Improve clarity, grammar, and engagement:\n{content}"}
    ]
    return call_llm(messages)
