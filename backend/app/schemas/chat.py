from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str
    route: Optional[str] = None