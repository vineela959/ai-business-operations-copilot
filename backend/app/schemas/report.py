from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ReportCreate(BaseModel):
    title: Optional[str] = None
    prompt: str


class ReportResponse(BaseModel):
    id: int
    title: Optional[str] = None
    content: str
    created_at: datetime

    class Config:
        from_attributes = True