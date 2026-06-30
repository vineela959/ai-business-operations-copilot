from app.services.ai_service import generate_ai_response


def knowledge_agent(question: str) -> str:
    prompt = f"""
You are the Knowledge Agent of an AI Business Operations Copilot.

Your responsibilities:
- Answer business questions
- Explain business concepts
- Suggest operational improvements
- Give concise and professional advice

User Question:
{question}
"""

    return generate_ai_response(prompt)