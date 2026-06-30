from app.services.ai_service import generate_ai_response


def generate_email_draft(recipient_name: str, purpose: str, tone: str):
    prompt = f"""
You are an Email Assistant Agent.

Write a business email with:

Recipient Name: {recipient_name}
Purpose: {purpose}
Tone: {tone}

Return the response in this exact format:

Subject: <email subject>

Body:
<email body>
"""

    response = generate_ai_response(prompt)

    subject = "Business Email"
    body = response

    if "Subject:" in response and "Body:" in response:
        subject_part = response.split("Body:")[0].replace("Subject:", "").strip()
        body_part = response.split("Body:")[1].strip()

        subject = subject_part
        body = body_part

    return {
        "subject": subject,
        "body": body
    }