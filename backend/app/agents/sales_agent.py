from sqlalchemy.orm import Session

from app.repositories.sale_repository import SaleRepository
from app.services.ai_service import generate_ai_response


def analyze_sales(db: Session) -> str:
    sales = SaleRepository.get_all(db)

    if not sales:
        return "No sales data available yet."

    sales_text = "\n".join([
        f"Sale ID: {sale.id}, Amount: {sale.amount}, Product: {sale.product}, Date: {sale.sale_date}"
        for sale in sales
    ])

    prompt = f"""
You are a Sales Analytics Agent.

Analyze the following sales data and provide:
1. Total sales
2. Key insights
3. Best performing product
4. Business recommendations

Sales data:
{sales_text}
"""

    return generate_ai_response(prompt)