from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.api.customers import router as customer_router
from app.core.config import settings

from app.database.database import Base, engine
from app.models.customer import Customer
from app.models.sale import Sale
from app.api.sales import router as sales_router
from app.api.chat import router as chat_router
from app.api.analytics import router as analytics_router
from app.models.report import Report
from app.api.reports import router as reports_router
from app.api.email import router as email_router
from app.models.conversation import Conversation
from app.api.knowledge import router as knowledge_router
from app.api.supervisor import router as supervisor_router
from app.api.dashboard import router as dashboard_router
from app.models.user import User
from app.api.auth import router as auth_router
from app.models.document import Document
from app.api.documents import router as documents_router
from app.models.document import Document, DocumentChunk
from app.api.rag import router as rag_router

app = FastAPI(
    title=settings.APP_NAME,
    description="AI-powered Business Operations Assistant",
    version=settings.APP_VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(router)
app.include_router(customer_router)
app.include_router(sales_router)
app.include_router(chat_router)
app.include_router(analytics_router)
app.include_router(reports_router)
app.include_router(email_router)
app.include_router(knowledge_router)
app.include_router(supervisor_router)
app.include_router(dashboard_router)
app.include_router(auth_router)
app.include_router(documents_router)
app.include_router(rag_router)