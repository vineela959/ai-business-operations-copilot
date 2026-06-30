from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.agents.knowledge_agent import knowledge_agent

router = APIRouter(
    prefix="/knowledge",
    tags=["Knowledge Agent"]
)


@router.post("/", response_model=ChatResponse)
def ask_knowledge(request: ChatRequest):
    return {
        "response": knowledge_agent(request.message)
    }