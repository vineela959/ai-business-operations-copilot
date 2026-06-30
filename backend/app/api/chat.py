from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ai_service import generate_ai_response
from app.repositories.conversation_repository import ConversationRepository
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/chat", tags=["AI Chat"])


@router.post("/", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    recent_conversations = ConversationRepository.get_recent(db)

    memory_text = "\n".join([
        f"User: {c.user_message}\nAI: {c.ai_response}"
        for c in reversed(recent_conversations)
    ])

    prompt = f"""
Previous conversation memory:
{memory_text}

Current user message:
{request.message}
"""

    ai_response = generate_ai_response(prompt)

    ConversationRepository.create(
        db=db,
        user_message=request.message,
        ai_response=ai_response
    )

    return {
        "response": ai_response,
        "route": "chat"
    }