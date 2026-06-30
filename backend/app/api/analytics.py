from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.agents.sales_agent import analyze_sales
from app.agents.crm_agent import analyze_customers
from app.models.sale import Sale
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/sales")
def sales_analytics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return {
        "analysis": analyze_sales(db)
    }


@router.get("/customers")
def customer_analytics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return {
        "analysis": analyze_customers(db)
    }


@router.get("/sales-chart")
def sales_chart(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    sales = db.query(Sale).all()

    return [
        {
            "label": sale.product or "Unknown",
            "amount": float(sale.amount)
        }
        for sale in sales
    ]


@router.get("/revenue-chart")
def revenue_chart(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    sales = db.query(Sale).all()

    product_totals = {}

    for sale in sales:
        product = sale.product or "Unknown"
        product_totals[product] = product_totals.get(product, 0) + float(sale.amount)

    return [
        {
            "product": product,
            "revenue": revenue
        }
        for product, revenue in product_totals.items()
    ]