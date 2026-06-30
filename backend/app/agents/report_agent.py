from app.services.ai_service import generate_ai_response


def generate_business_report(prompt: str) -> str:
    final_prompt = f"""
You are a Business Report Generator Agent.

Create a clean, professional business report based on this request:

{prompt}

Format the report with:
- Title
- Executive Summary
- Key Insights
- Recommendations
- Next Steps
"""

    return generate_ai_response(final_prompt)