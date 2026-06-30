from sqlalchemy import Column, BigInteger, String, Numeric, Date, ForeignKey
from sqlalchemy.sql import func

from app.database.database import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(BigInteger, primary_key=True, index=True)
    customer_id = Column(BigInteger, ForeignKey("customers.id"), nullable=True)
    amount = Column(Numeric, nullable=False)
    product = Column(String, nullable=True)
    sale_date = Column(Date, server_default=func.current_date())