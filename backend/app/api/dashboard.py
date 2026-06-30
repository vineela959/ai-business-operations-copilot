from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.database import get_db
from app.models.customer import Customer
from app.models.sale import Sale
from app.models.report import Report
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/stats")
def dashboard_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    total_customers = db.query(Customer).count()
    total_sales = db.query(Sale).count()
    total_reports = db.query(Report).count()
    total_revenue = db.query(func.sum(Sale.amount)).scalar() or 0

    return {
        "customers": total_customers,
        "sales": total_sales,
        "reports": total_reports,
        "revenue": float(total_revenue)
    }


@router.get("/activity")
def recent_activity(current_user: User = Depends(get_current_user)):
    return [
        {"title": "CRM Agent analyzed customers", "time": "Just now", "type": "crm"},
        {"title": "Sales Agent generated revenue analysis", "time": "2 min ago", "type": "sales"},
        {"title": "Report created successfully", "time": "10 min ago", "type": "report"},
        {"title": "Supervisor routed conversation", "time": "15 min ago", "type": "ai"},
    ]