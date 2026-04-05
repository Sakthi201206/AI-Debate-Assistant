def build_prompt(topic, context):
    return f"""
    You are an AI Debate Assistant.

    Topic: {topic}

    Context:
    {context}

    Generate:
    1. Strong arguments FOR
    2. Strong arguments AGAINST
    3. Give structured bullet points
    """