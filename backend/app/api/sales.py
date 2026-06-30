from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repositories.sale_repository import SaleRepository
from app.schemas.sale import SaleCreate, SaleResponse
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)


@router.post(
    "/",
    response_model=SaleResponse,
    status_code=status.HTTP_201_CREATED
)
def create_sale(
    sale: SaleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return SaleRepository.create(db, sale)


@router.get(
    "/",
    response_model=list[SaleResponse]
)
def get_sales(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return SaleRepository.get_all(db)