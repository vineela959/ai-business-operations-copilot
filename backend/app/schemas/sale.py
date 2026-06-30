from pydantic import BaseModel
from typing import Optional
from datetime import date
from decimal import Decimal


class SaleCreate(BaseModel):
    customer_id: Optional[int] = None
    amount: Decimal
    product: Optional[str] = None


class SaleResponse(SaleCreate):
    id: int
    sale_date: date

    class Config:
        from_attributes = True