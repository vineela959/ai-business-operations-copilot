from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.report import ReportCreate, ReportResponse
from app.repositories.report_repository import ReportRepository
from app.agents.report_agent import generate_business_report

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.post("/", response_model=ReportResponse, status_code=status.HTTP_201_CREATED)
def create_report(report: ReportCreate, db: Session = Depends(get_db)):
    content = generate_business_report(report.prompt)

    saved_report = ReportRepository.create(
        db=db,
        title=report.title or "AI Generated Business Report",
        content=content
    )

    return saved_report


@router.get("/", response_model=list[ReportResponse])
def get_reports(db: Session = Depends(get_db)):
    return ReportRepository.get_all(db)