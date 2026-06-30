from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {
        "message": "Welcome to AI Business Operations Copilot 🚀"
    }

@router.get("/health")
def health():
    return {
        "status": "healthy"
    }