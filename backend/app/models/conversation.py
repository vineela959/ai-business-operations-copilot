from sqlalchemy import Column, BigInteger, Text, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(BigInteger, primary_key=True, index=True)
    user_message = Column(Text, nullable=False)
    ai_response = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())