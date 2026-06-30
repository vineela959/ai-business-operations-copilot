from sqlalchemy.orm import Session

from app.repositories.customer_repository import CustomerRepository
from app.services.ai_service import generate_ai_response


def analyze_customers(db: Session) -> str:
    customers = CustomerRepository.get_all(db)

    if not customers:
        return "No customer data available yet."

    customer_text = "\n".join([
        f"ID: {c.id}, Name: {c.name}, Email: {c.email}, Company: {c.company}, Phone: {c.phone}"
        for c in customers
    ])

    prompt = f"""
You are a CRM Agent.

Analyze the following customer data and provide:
1. Customer overview
2. Important customer insights
3. Possible follow-up opportunities
4. Recommended CRM actions

Customer data:
{customer_text}
"""

    return generate_ai_response(prompt)