from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.chat import ChatRequest, ChatResponse
from app.agents.rag_agent import answer_from_documents
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/rag", tags=["RAG"])


@router.post("/ask", response_model=ChatResponse)
def ask_documents(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    answer = answer_from_documents(request.message, db)

    return {
        "response": answer,
        "route": "rag"
    }