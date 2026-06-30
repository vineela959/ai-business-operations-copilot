from pydantic import BaseModel


class EmailDraftRequest(BaseModel):
    recipient_name: str
    purpose: str
    tone: str = "professional"


class EmailDraftResponse(BaseModel):
    subject: str
    body: str