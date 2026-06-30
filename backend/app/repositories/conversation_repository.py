from sqlalchemy.orm import Session

from app.models.conversation import Conversation


class ConversationRepository:

    @staticmethod
    def create(db: Session, user_message: str, ai_response: str):
        conversation = Conversation(
            user_message=user_message,
            ai_response=ai_response
        )

        db.add(conversation)
        db.commit()
        db.refresh(conversation)

        return conversation

    @staticmethod
    def get_recent(db: Session, limit: int = 5):
        return (
            db.query(Conversation)
            .order_by(Conversation.id.desc())
            .limit(limit)
            .all()
        )