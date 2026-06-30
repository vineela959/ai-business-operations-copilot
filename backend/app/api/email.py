from fastapi import APIRouter

from app.schemas.email import EmailDraftRequest, EmailDraftResponse
from app.agents.email_agent import generate_email_draft

router = APIRouter(prefix="/email", tags=["Email Agent"])


@router.post("/draft", response_model=EmailDraftResponse)
def draft_email(request: EmailDraftRequest):
    return generate_email_draft(
        recipient_name=request.recipient_name,
        purpose=request.purpose,
        tone=request.tone
    )