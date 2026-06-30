from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CustomerCreate(BaseModel):
    name: str
    email: str
    company: Optional[str] = None
    phone: Optional[str] = None


class CustomerResponse(CustomerCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True