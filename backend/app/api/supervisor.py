from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.chat import ChatRequest, ChatResponse
from app.agents.supervisor_agent import supervisor_agent
from app.repositories.conversation_repository import ConversationRepository
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/supervisor", tags=["Supervisor Agent"])


@router.post("/", response_model=ChatResponse)
def run_supervisor(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = supervisor_agent(request.message, db)

    ConversationRepository.create(
        db=db,
        user_message=request.message,
        ai_response=result["response"]
    )

    return {
        "response": result["response"],
        "route": result["route"]
    }