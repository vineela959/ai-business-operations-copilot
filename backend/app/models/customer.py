from sqlalchemy import Column, BigInteger, String, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    company = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())