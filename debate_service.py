from app.core.retriever import retrieve
from app.core.prompt_builder import build_prompt
from app.services.llm_service import generate_response

def generate_debate(topic):
    docs = retrieve(topic)
    context = "\n".join(docs)

    prompt = build_prompt(topic, context)

    response = generate_response(prompt)

    return {"result": response}